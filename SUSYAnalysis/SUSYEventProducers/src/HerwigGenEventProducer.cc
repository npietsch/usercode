#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "SUSYAnalysis/SUSYObjects/interface/HerwigGenEvent.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/HerwigGenEventProducer.h"

HerwigGenEventProducer::HerwigGenEventProducer(const edm::ParameterSet& cfg):
  src_ ( cfg.getParameter<edm::InputTag>( "src"  ) )
{
  produces<HerwigGenEvent>();
}

HerwigGenEventProducer::~HerwigGenEventProducer()
{
}

void
HerwigGenEventProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{     
  edm::Handle<reco::GenParticleCollection> parts;
  evt.getByLabel(src_,  parts);

  //add HerwigDecayTree
  reco::GenParticleRefProd cands( parts );

  //add genEvt to the output stream
  HerwigGenEvent* HgenEvt = new HerwigGenEvent(cands);
  std::auto_ptr<HerwigGenEvent> gen (HgenEvt);
  evt.put( gen );
}
