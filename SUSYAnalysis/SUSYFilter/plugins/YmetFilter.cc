#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "SUSYAnalysis/SUSYFilter/plugins/YmetFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

/// default constructor 
YmetFilter::YmetFilter(const edm::ParameterSet& cfg):
  jets_ (cfg.getParameter<edm::InputTag>("jets")),
  mets_ (cfg.getParameter<edm::InputTag>("mets")),
  Cut_  (cfg.getParameter<double>("Cut"))
{
}

/// default destructor
YmetFilter::~YmetFilter()
{
}

/// sanity check
void 
YmetFilter::beginJob()
{ 
}

/// event veto
bool
YmetFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(jets_, jets);

  edm::Handle<std::vector<pat::MET> > mets;
  event.getByLabel(mets_, mets);
  
  double HT=0;
  double Ymet=0;

  // loop over all jets
  for(int i=0; i< (int)jets->size(); ++i)
    {
      HT=HT+(*jets)[i].pt();
    }
  
  Ymet=((*mets)[0].et())/sqrt(HT);

  if (Ymet > Cut_) return true;
  else return false;
}


