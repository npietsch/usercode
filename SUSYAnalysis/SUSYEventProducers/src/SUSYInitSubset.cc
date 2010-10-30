#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"

SUSYInitSubset::SUSYInitSubset(const edm::ParameterSet& cfg):
  src_ ( cfg.getParameter<edm::InputTag>( "src" ) )
{
  produces<reco::GenParticleCollection>();
}

SUSYInitSubset::~SUSYInitSubset()
{
}

void
SUSYInitSubset::produce(edm::Event& evt, const edm::EventSetup& setup)
{     
  edm::Handle<reco::GenParticleCollection> src;
  evt.getByLabel(src_, src);
  
  const reco::GenParticleRefProd ref = evt.getRefBeforePut<reco::GenParticleCollection>(); 
  std::auto_ptr<reco::GenParticleCollection> sel( new reco::GenParticleCollection );

  //fill output collection
  fillOutput( *src, *sel );

  evt.put( sel );
}

void SUSYInitSubset::fillOutput(const reco::GenParticleCollection& src, reco::GenParticleCollection& sel)
{
  for(reco::GenParticleCollection::const_iterator t=src.begin(); t!=src.end(); ++t){
    {
      if( t->status()==SUSYInitID::status && t->numberOfMothers()==2 )
	for(int idx=0; idx<(int)t->numberOfMothers(); ++idx){      
	  reco::GenParticle* cand = new reco::GenParticle( t->mother(idx)->threeCharge(), t->mother(idx)->p4(), 
							   t->mother(idx)->vertex(), t->mother(idx)->pdgId(), 
							   t->mother(idx)->status(), false );
	  std::auto_ptr<reco::GenParticle> ptr( cand );
	  sel.push_back( *ptr );
	}
      break;
    }
  }
}


