#include <algorithm>

#include "FWCore/Framework/interface/Event.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/JetsProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

JetsProducer::JetsProducer(const edm::ParameterSet& cfg):
  inputJets_  (cfg.getParameter<edm::InputTag>("inputJets"))

{
  edm::Service<TFileService> fs;

  outputJets_ = inputJets_.label();

  // register products
  produces<std::vector<pat::Jet> >(outputJets_);
}

void
JetsProducer::beginJob()
{	
}

void
JetsProducer::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // access jets
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(inputJets_, jets);
  
  // create new jet collection 
  std::auto_ptr<std::vector<pat::Jet> > pJets(new std::vector<pat::Jet>);

  // loop and rescale jets
  for(std::vector<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet)
    {
      pat::Jet selectedJet = *jet;

      if(selectedJet.genParton())
	{
	  if(selectedJet.genParton()->mother()->pdgId()==1000021) pJets->push_back(selectedJet);
	}
    }

  event.put(pJets,outputJets_);
}

DEFINE_FWK_MODULE( JetsProducer );
