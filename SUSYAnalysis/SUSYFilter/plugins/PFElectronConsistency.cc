#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/PFElectronConsistency.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

/// default constructor 
PFElectronConsistency::PFElectronConsistency(const edm::ParameterSet& cfg):
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pfElectrons_  (cfg.getParameter<edm::InputTag>("pfElectrons"))
{
}

PFElectronConsistency::~PFElectronConsistency()
{
}

void 
PFElectronConsistency::beginJob()
{ 
}

bool
PFElectronConsistency::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  edm::Handle<std::vector<pat::Electron> > electrons;
  event.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::PFCandidate> > pfElectrons;
  event.getByLabel(pfElectrons_, pfElectrons);

  double dRmin=10;
  double reco_pt=0;
  double pf_pt=0;
  
  if(electrons->size()==1)
    {
      reco_pt=(*electrons)[0].pt();
      for(int jdx=0; jdx<(int)pfElectrons->size(); ++jdx)
	{
	  double dR=abs(deltaR((*electrons)[0].eta(),(*electrons)[0].phi(),(*pfElectrons)[jdx].eta(),(*pfElectrons)[jdx].phi()));
	  if(dR < dRmin && (*pfElectrons)[jdx].pt() > 10)
	    {
	      dRmin=dR;
	      pf_pt=(*pfElectrons)[jdx].pt();
	    }
	}
      
      if(fabs(reco_pt - pf_pt) < 10) return true;
      else return false;
    }
  else return false;
}
