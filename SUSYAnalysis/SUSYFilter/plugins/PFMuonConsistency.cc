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
  edm::Handle<std::vector<reco::PFCandidate> > pfMuons;
  event.getByLabel(pfMuons_, pfMuons);

  double dRmin=10;
  double reco_pt=0;
  double pf_pt=0;
  
  if(muons->size()==1)
    {
      reco_pt=(*muons)[0].pt();
      for(int jdx=0; jdx<(int)pfMuons->size(); ++jdx)
	{
	  double dR=abs(deltaR((*muons)[0].eta(),(*muons)[0].phi(),(*pfMuons)[jdx].eta(),(*pfMuons)[jdx].phi()));
	  if(dR < dRmin && (*pfMuons)[jdx].pt() > 10)
	    {
	      dRmin=dR;
	      pf_pt=(*pfMuons)[jdx].pt();
	    }
	}
    }
  
  if(reco_pt > 0 && pf_pt > 0) 
    {
      if(fabs(reco_pt - pf_pt) > 5) return false;
      else return true;
    }
  else return false;
}


