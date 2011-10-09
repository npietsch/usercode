#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/HTFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

/// default constructor 
HTFilter::HTFilter(const edm::ParameterSet& cfg):
  jets_    (cfg.getParameter<edm::InputTag>(       "jets"  )),
  Cut_      (cfg.getParameter<double>("Cut"    ))
{
}

/// default destructor
HTFilter::~HTFilter()
{
}

/// sanity check
void 
HTFilter::beginJob()
{ 
}

/// event veto
bool
HTFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(jets_, jets);
  
  double HT=0;
  // loop over all jets
  for(int i=0; i< (int)jets->size(); ++i)
    {
      HT=HT+(*jets)[i].pt();
    }
  
  if (HT > Cut_) return true;
  else return false;
}


