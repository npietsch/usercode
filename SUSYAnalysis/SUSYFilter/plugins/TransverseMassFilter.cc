#include "SUSYAnalysis/SUSYFilter/plugins/TransverseMassFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

/// default constructor 
TransverseMassFilter::TransverseMassFilter(const edm::ParameterSet& cfg):
  met_      (cfg.getParameter<edm::InputTag>("met"  )),
  muons_    (cfg.getParameter<edm::InputTag>("muons"  )),
  electrons_(cfg.getParameter<edm::InputTag>("electrons"  )),
  Cut_      (cfg.getParameter<std::vector<double> >("Cut"    ))
{
}

/// default destructor
TransverseMassFilter::~TransverseMassFilter()
{
}

/// sanity check
void 
TransverseMassFilter::beginJob()
{ 
}

/// event veto
bool
TransverseMassFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::MET> > met;
  event.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Muon> > muons;
  event.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  event.getByLabel(electrons_, electrons);

  //transverse W-mass
  double mW=0;
  double LeptonPt=0;

  if(muons->size()>=1)
    {
      LeptonPt = (*muons)[0].et();
      mW=sqrt(2*(((*met)[0].et())*((*muons)[0].et())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
    }
  if(electrons->size()>=1)
    {
      if((*electrons)[0].et()>LeptonPt)
	{
	  mW=sqrt(2*(((*met)[0].et())*((*electrons)[0].et())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
	}
    }
  
  if (Cut_[0] <= mW && mW < Cut_[1]) return false;
  else return true;
}


