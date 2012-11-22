#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/GenEvent.h"


/// default contructor
GenEvent::GenEvent(const reco::GenParticleCollection& genParticles)
{ 
  genParticles_ = genParticles;
}

std::vector<reco::GenParticle*> GenEvent::InitialParticles() const
{
  std::vector<reco::GenParticle*> particles;
  
  for(reco::GenParticleCollection::const_iterator t=genParticles_.begin(); t!=genParticles_.end(); ++t)
    {
      if(t->numberOfMothers()==2)
	{
	  for(int idx=0; idx<(int)t->mother(0)->numberOfDaughters(); ++idx)
	    {      
	      reco::GenParticle* particle = new reco::GenParticle( t->mother(0)->daughter(idx)->threeCharge(),
								   t->mother(0)->daughter(idx)->p4(), 
								   t->mother(0)->daughter(idx)->vertex(), 
								   t->mother(0)->daughter(idx)->pdgId(), 
								   t->mother(0)->daughter(idx)->status(), false );
	      particles.push_back(particle);
	    }
	}
    }
  return particles;
}

double GenEvent::shat() const
{
  double shat=0;
  if(InitialParticles().size()==2)
    {
      shat=InitialParticles()[0]->pt();
    }
  return shat;

}
