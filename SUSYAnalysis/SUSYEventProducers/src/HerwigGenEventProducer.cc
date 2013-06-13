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

  std::auto_ptr<reco::GenParticleCollection> sel( new reco::GenParticleCollection );

  fillOutput(*parts, *sel);

  //add HerwigDecayTree
  reco::GenParticleRefProd cands( parts );

  //add genEvt to the output stream
  HerwigGenEvent* HgenEvt = new HerwigGenEvent(cands);
  std::auto_ptr<HerwigGenEvent> gen (HgenEvt);
  evt.put( gen );
}


void HerwigGenEventProducer::fillOutput(const reco::GenParticleCollection& parts, reco::GenParticleCollection& sel)
{
  //loop over genParticles
  for(reco::GenParticleCollection::const_iterator t=parts.begin(); t!=parts.end(); ++t)
    {
      if(t->pdgId()== 1000021 && t->status()==3 && t->numberOfDaughters() == 3)
	{
	  reco::GenParticle* cand = new reco::GenParticle(t->threeCharge(), t->p4(), t->vertex(), t->pdgId(), t->status(), false);
	  std::auto_ptr<reco::GenParticle> ptr( cand );
	  sel.push_back(*ptr);
	}
    }
}

