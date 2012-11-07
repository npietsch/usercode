#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/PFMuonConsistency.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

/// default constructor 
PFMuonConsistency::PFMuonConsistency(const edm::ParameterSet& cfg):
  muons_    (cfg.getParameter<edm::InputTag>("muons")),
  pfMuons_  (cfg.getParameter<edm::InputTag>("pfMuons"))
{
}

PFMuonConsistency::~PFMuonConsistency()
{
}

void 
PFMuonConsistency::beginJob()
{ 
}

bool
PFMuonConsistency::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  edm::Handle<std::vector<pat::Muon> > muons;
  event.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Muon> > pfMuons;
  event.getByLabel(pfMuons_, pfMuons);

  double dRmin=10;
  double PtPF=0;
  
  if(muons->size()==1)
    {
      for(int jdx=0; jdx<(int)pfMuons->size(); ++jdx)
	{
	  double dR=abs(deltaR((*muons)[0].eta(),(*muons)[0].phi(),(*pfMuons)[jdx].eta(),(*pfMuons)[jdx].phi()));
	  if(dR < dRmin)
	    {
	      dRmin=dR;
	      PtPF=(*pfMuons)[jdx].pt();
	    }
	}
    }
  
  if(muons->size()==1 && PtPF>0 && (fabs((*muons)[0].pt() - PtPF))/(*muons)[0].pt() < 0.2 ) return true;
  else
    {
//       std::cout << "F=================================" << std::endl;
//       std::cout << "F (*muons)[0].pt(): " << (*muons)[0].pt() << std::endl;
//       std::cout << "F PtPF: " << PtPF << std::endl;
//       std::cout << "F=================================" << std::endl;
      return false;
    }
}

