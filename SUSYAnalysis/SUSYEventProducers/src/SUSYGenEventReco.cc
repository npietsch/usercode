#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "AnalysisDataFormats/TopObjects/interface/SUSYGenEvent.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYGenEventReco.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"

SUSYGenEventReco::SUSYGenEventReco(const edm::ParameterSet& cfg):
  src_ ( cfg.getParameter<edm::InputTag>( "src"  ) ),
  init_( cfg.getParameter<edm::InputTag>( "init" ) )
{
  produces<SUSYGenEvent>();
}

SUSYGenEventReco::~SUSYGenEventReco()
{
}

void
SUSYGenEventReco::produce(edm::Event& evt, const edm::EventSetup& setup)
{     
  edm::Handle<reco::GenParticleCollection> parts;
  evt.getByLabel(src_,  parts);

  edm::Handle<reco::GenParticleCollection> inits;
  evt.getByLabel(init_, inits);

  //add SUSYDecayTree
  reco::GenParticleRefProd cands( parts );

  //add InitialStatePartons
  reco::GenParticleRefProd initParts( inits );

  //add genEvt to the output stream
  SUSYGenEvent* SgenEvt = new SUSYGenEvent( cands, initParts );
  std::auto_ptr<SUSYGenEvent> gen (SgenEvt);
  evt.put( gen );
}
