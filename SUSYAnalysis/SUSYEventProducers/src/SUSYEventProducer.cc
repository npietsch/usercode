#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYEventProducer.h"

SUSYEventProducer::SUSYEventProducer(const edm::ParameterSet& cfg):
  test_      (cfg.getParameter<int> ("test")),
  muons_     (cfg.getParameter<edm::InputTag>("muons")),
  electrons_ (cfg.getParameter<edm::InputTag>("electrons")),
  jets_      (cfg.getParameter<edm::InputTag>("jets")),
  mets_      (cfg.getParameter<edm::InputTag>("mets"))
{
  produces<SUSYEvent>();
}

SUSYEventProducer::~SUSYEventProducer()
{
}

void
SUSYEventProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{     

  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::MET> > mets;
  evt.getByLabel(mets_, mets);


  SUSYEvent* SUSYEvt = new SUSYEvent(test_, *muons, *electrons, *jets, *mets);
  std::auto_ptr<SUSYEvent> susy (SUSYEvt);
  evt.put(susy);
}
