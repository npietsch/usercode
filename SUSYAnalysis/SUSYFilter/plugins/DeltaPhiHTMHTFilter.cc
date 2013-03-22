#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SUSYAnalysis/SUSYFilter/plugins/DeltaPhiHTMHTFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

/// default constructor 
DeltaPhiHTMHTFilter::DeltaPhiHTMHTFilter(const edm::ParameterSet& cfg):
  jets_    (cfg.getParameter<edm::InputTag>("jets")),
  Cut_     (cfg.getParameter<std::vector<double> > ("Cut") )
{
}

/// default destructor
DeltaPhiHTMHTFilter::~DeltaPhiHTMHTFilter()
{
}

/// sanity check
void 
DeltaPhiHTMHTFilter::beginJob()
{ 
}

/// event veto
bool
DeltaPhiHTMHTFilter::filter(edm::Event& event, const edm::EventSetup& setup)
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
      MHT=P4.pt();
    }
  //std::cout << "DeltaPhiHTMHTFilter: " << MHT << std::endl;
  
  if (MHT > 1.) return true;
  else return false;
}


