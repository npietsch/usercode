#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"

SUSYInitSubset::SUSYInitSubset(const edm::ParameterSet& cfg):
  src_ ( cfg.getParameter<edm::InputTag>( "src" ) )
{
  // use label of input to create label for output
  InitParticles_ = src_.label();
  //InitSparticles_ = src.label();  

  // register products
  produces<reco::GenParticleCollection>(InitParticles_);
  produces<reco::GenParticleCollection>(InitSparticles_); 
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
  std::auto_ptr<reco::GenParticleCollection> sparticles( new reco::GenParticleCollection );

  //fill output collection
  fillOutput( *src, *sel, *sparticles );

  evt.put( sel, InitParticles_ );
  evt.put( sparticles,InitSparticles_ );

}

void SUSYInitSubset::fillOutput(const reco::GenParticleCollection& src, reco::GenParticleCollection& sel, reco::GenParticleCollection& sparticles)
{
  for(reco::GenParticleCollection::const_iterator t=src.begin(); t!=src.end(); ++t)
    {
      if(t->numberOfMothers()==2)
	{
	  for(int idx=0; idx<(int)t->numberOfMothers(); ++idx)
	    {      
	      //std::cout << "mother pdgId: " << t->mother(idx)->pdgId() << std::endl;
	      //std::cout << "nr of mother's daughters: " << t->mother(idx)->numberOfDaughters() << std::endl;
	      	      
	      reco::GenParticle* cand = new reco::GenParticle( t->mother(idx)->threeCharge(), t->mother(idx)->p4(), 
							       t->mother(idx)->vertex(), t->mother(idx)->pdgId(), 
							       t->mother(idx)->status(), false );
	      std::auto_ptr<reco::GenParticle> ptr( cand );
	      sel.push_back( *ptr );
	    }
	  for(int idx=0; idx<(int)t->mother(0)->numberOfDaughters(); ++idx)
	    {
	      //std::cout << "mother pdgId: " << t->mother(0)->pdgId() << std::endl;
	      //std::cout << "mother's daughter: " << t->mother(0)->daughter(idx)->pdgId() << std::endl;
	      
	      reco::GenParticle* daughter = new reco::GenParticle( t->mother(0)->daughter(idx)->threeCharge(),
								   t->mother(0)->daughter(idx)->p4(), 
								   t->mother(0)->daughter(idx)->vertex(), 
								   t->mother(0)->daughter(idx)->pdgId(), 
								   t->mother(0)->daughter(idx)->status(), false );
	      std::auto_ptr<reco::GenParticle> dtr( daughter );
	      sparticles.push_back( *dtr ); 
	    }
	  break;
	}
    }
}
