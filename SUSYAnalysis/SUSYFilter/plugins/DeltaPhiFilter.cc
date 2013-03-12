#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "SUSYAnalysis/SUSYFilter/plugins/DeltaPhiFilter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

/// default constructor 
DeltaPhiFilter::DeltaPhiFilter(const edm::ParameterSet& cfg):
  jets_ (cfg.getParameter<edm::InputTag>("jets")),
  mets_ (cfg.getParameter<edm::InputTag>("mets")),
  Jet_  (cfg.getParameter<int>("Jet")),
  Cut_  (cfg.getParameter<double>("Cut"))
{
}

/// default destructor
DeltaPhiFilter::~DeltaPhiFilter()
{
}

/// sanity check
void 
DeltaPhiFilter::beginJob()
{ 
}

/// event veto
bool
DeltaPhiFilter::filter(edm::Event& event, const edm::EventSetup& setup)
{       
  // fetch the input collection from the event content  
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::MET> > mets;
  event.getByLabel(mets_, mets);
  
  //std::cout << "DeltaPhiFilter: nJets=" << jets->size() << std::endl;

  double dPhi=deltaPhi((*mets)[0].phi(),(*jets)[Jet_].phi());

  //std::cout << "--------------------------" << std::endl;
  //std::cout << "Jet_: " << Jet_ << std::endl;
  //std::cout << "Cut_: " << Cut_ << std::endl;
  //std::cout << "dPhi: " << dPhi << std::endl;
  //std::cout << "abs(dPhi): " << abs(dPhi) << std::endl;

  if (fabs(dPhi) < 0.5)
    {
      //std::cout << "false" << std::endl;
      return false;
    }
  else
    {
      //std::cout << "true" << std::endl;
      return true;
    }
}


