#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "SUSYAnalysis/SUSYFilter/plugins/DeltaPhiHTMETFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Math/interface/deltaPhi.h"

/// default constructor 
DeltaPhiHTMETFilter::DeltaPhiHTMETFilter(const edm::ParameterSet& cfg):
  jets_    (cfg.getParameter<edm::InputTag>("jets")),
  mets_    (cfg.getParameter<edm::InputTag>("mets")),
  Cut_     (cfg.getParameter<std::vector<double> > ("Cut") )
{
}

/// default destructor
DeltaPhiHTMETFilter::~DeltaPhiHTMETFilter()
{
}

/// sanity check
void 
DeltaPhiHTMETFilter::beginJob()
{ 
}

/// event veto
bool
DeltaPhiHTMETFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::MET> > mets;
  event.getByLabel(mets_, mets);
  
  double dPhi=10;

  if(jets->size()>0)
    {
      reco::Particle::LorentzVector P4=-(*jets)[0].p4();
      
      // loop over all jets
      for(int i=1; i< (int)jets->size(); ++i)
	{
	  P4=P4-(*jets)[i].p4();
  	}
      dPhi=deltaPhi(P4.phi(),(*mets)[0].phi());
    }
  
  //std::cout << "DeltaPhiHTMETFilter: " << dPhi << std::endl;
  //std::cout << "DeltaPhiHTMETFilter: " << fabs(dPhi) << std::endl;
  
  if(dPhi != 10 && fabs(dPhi) >= Cut_[0] && fabs(dPhi) < Cut_[1]) return true;
  else return false;
}
