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
  double recoPt=0;
  double pfPt=0;
  
  // require exactly one reco muon
  if(muons->size()==1)
    {
      recoPt=(*muons)[0].pt();

      // loop over pf muons
      for(int idx=0; idx<(int)pfMuons->size(); ++idx)
	{
	  double dR=abs(deltaR((*muons)[0].eta(),(*muons)[0].phi(),(*pfMuons)[idx].eta(),(*pfMuons)[idx].phi()));
	  // if pf muon pt is larger than 10
	  if((*pfMuons)[idx].pt() > 10)
	    {
	      if(dR < dRmin)
		{
		  dRmin=dR;
		  pfPt=(*pfMuons)[idx].pt();
		}
	    }
	}
      if(fabs(recoPt - pfPt) < 5) return true;
      else return false;
    }
  else return false;
}
