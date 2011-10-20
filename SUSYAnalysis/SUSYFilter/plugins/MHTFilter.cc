#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/MHTFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

/// default constructor 
MHTFilter::MHTFilter(const edm::ParameterSet& cfg):
  jets_    (cfg.getParameter<edm::InputTag>(       "jets"  )),
  Cut_      (cfg.getParameter<double>("Cut"    ))
{
}

/// default destructor
MHTFilter::~MHTFilter()
{
}

/// sanity check
void 
MHTFilter::beginJob()
{ 
}

/// event veto
bool
MHTFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(jets_, jets);
  
  double MHT=0;
  
  if(jets->size()>0)
    {
      reco::Particle::LorentzVector P4=(*jets)[0].p4();
      
      // loop over all jets
      for(int i=1; i< (int)jets->size(); ++i)
	{
	  P4=P4+(*jets)[i].p4();
  	}   
      MHT=P4.Et();
    }
  
  if (MHT > Cut_) return true;
  else return false;
}


