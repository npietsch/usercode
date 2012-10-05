#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/PFElectronConsistency.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

/// default constructor 
PFElectronConsistency::PFElectronConsistency(const edm::ParameterSet& cfg):
  electrons_         (cfg.getParameter<edm::InputTag>("electrons")),
  pfCandidates_  (cfg.getParameter<edm::InputTag>("pfCandidates"))
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
  edm::Handle<std::vector<reco::PFCandidate> > pfCandidates;
  event.getByLabel(pfCandidates_, pfCandidates);

  double dRmin=10;
  double recoPt=0;
  double pfPt=0;
  
  // require exactly one reco electron
  if(electrons->size()==1)
    {
      recoPt=(*electrons)[0].pt();

      // loop over pf candidates
      for(int idx=0; idx<(int)pfCandidates->size(); ++idx)
	{

	  // if pf candidate is electron and pt is larger than 10
	  if((*pfCandidates)[idx].particleId() == reco::PFCandidate::e && (*pfCandidates)[idx].pt() > 10.)
	    {
	      double dR=abs(deltaR((*electrons)[0].eta(),(*electrons)[0].phi(),(*pfCandidates)[idx].eta(),(*pfCandidates)[idx].phi()));

	      if(dR < dRmin)
		{
		  dRmin=dR;
		  pfPt=(*pfCandidates)[idx].pt();
		}
	    }
	}
      if(fabs(recoPt - pfPt) < 10) return true;
      else return false;
    }
  else return false;
}
