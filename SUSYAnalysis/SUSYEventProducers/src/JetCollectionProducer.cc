#include <algorithm>

#include "FWCore/Framework/interface/Event.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/JetCollectionProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

JetCollectionProducer::JetCollectionProducer(const edm::ParameterSet& cfg):
  inputJets_  (cfg.getParameter<edm::InputTag>("inputJets"))

{
  edm::Service<TFileService> fs;

  // register products
  produces<std::vector<pat::Jet> >("GluinoJets");
  produces<std::vector<pat::Jet> >("NoGluonJets");
}

void
JetCollectionProducer::beginJob()
{	
}

void
JetCollectionProducer::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // access jets
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(inputJets_, jets);
  
  // create new jet collections
  std::auto_ptr<std::vector<pat::Jet> > gluinoJets(new std::vector<pat::Jet>);
  std::auto_ptr<std::vector<pat::Jet> > noGluonJets(new std::vector<pat::Jet>);
  
  // loop over jets
  for(std::vector<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet)
    {
      pat::Jet selectedJet  = *jet;
      
      // if genParton is not from gluino three-body decay
      if(selectedJet.genParton())
	{
	  if(selectedJet.genParton()->mother()->pdgId()==1000021) gluinoJets->push_back(selectedJet);
	}
      
      // if matched parton is gluon
      if(selectedJet.genParton())
	{
	  if(selectedJet.partonFlavour()!=21) noGluonJets->push_back(selectedJet);
	}
    }

  event.put(gluinoJets,"GluinoJets");
  event.put(noGluonJets,"NoGluonJets");
}

DEFINE_FWK_MODULE(JetCollectionProducer);
