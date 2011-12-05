#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "SUSYAnalysis/SUSYObjects/interface/GenEvent.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/GenEventReco.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"

GenEventReco::GenEventReco(const edm::ParameterSet& cfg):
  genParticles_    ( cfg.getParameter<edm::InputTag>( "genParticles"     ) ),
  initialParticles_( cfg.getParameter<edm::InputTag>( "initialParticles" ) )
{
  produces<GenEvent>();
}

GenEventReco::~GenEventReco()
{
}

void
GenEventReco::produce(edm::Event& evt, const edm::EventSetup& setup)
{     
  edm::Handle<reco::GenParticleCollection> genParticles;
  evt.getByLabel(genParticles_,  genParticles);

  edm::Handle<reco::GenParticleCollection> initialParticles;
  evt.getByLabel(initialParticles_, initialParticles);

  //add SUSYDecayTree
  reco::GenParticleRefProd cands( genParticles );

  //add InitialStatePartons
  reco::GenParticleRefProd initParts( initialParticles );

  //add genEvt to the output stream
  GenEvent* genEvt = new GenEvent(cands, initParts);
  std::auto_ptr<GenEvent> gen (genEvt);
  evt.put( gen );
}
