#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/PFMuonConsistency.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

/// default constructor 
PFMuonConsistency::PFMuonConsistency(const edm::ParameterSet& cfg):
  muons_         (cfg.getParameter<edm::InputTag>("muons")),
  pfCandidates_  (cfg.getParameter<edm::InputTag>("pfCandidates"))
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
  edm::Handle<std::vector<reco::PFCandidate> > pfCandidates;
  event.getByLabel(pfCandidates_, pfCandidates);

  double dRmin=10;
  double recoPt=0;
  double pfPt=0;
  
  // require exactly one reco muon
  if(muons->size()==1)
    {
      recoPt=(*muons)[0].pt();

      // loop over pf candidates
      for(int idx=0; idx<(int)pfCandidates->size(); ++idx)
	{

	  // if pf candidate is muon and pt is larger than 10
	  if((*pfCandidates)[idx].particleId() == reco::PFCandidate::mu && (*pfCandidates)[idx].pt() > 10.)
	    {
	      double dR=abs(deltaR((*muons)[0].eta(),(*muons)[0].phi(),(*pfCandidates)[idx].eta(),(*pfCandidates)[idx].phi()));

	      if(dR < dRmin)
		{
		  dRmin=dR;
		  pfPt=(*pfCandidates)[idx].pt();
		}
	    }
	}
      if(fabs(recoPt - pfPt) < 5) return true;
      else return false;
    }
  else return false;
}
