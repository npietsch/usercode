#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/HerwigGenEvent.h"


/// default contructor
HerwigGenEvent::HerwigGenEvent(reco::GenParticleRefProd& decaySubset)
{
  parts_ = decaySubset;
}

// is gluino?
bool HerwigGenEvent::isGluino(const reco::GenParticle & genParticle) const
{
  bool gluino=false;
  if(genParticle.pdgId()==1000021 && genParticle.status() == 2)
    {
      gluino=true;
    }
  
  return gluino;
}

// is gluino three-body decay?
bool HerwigGenEvent::isGluinoThreeBodyDecay() const
{
  bool gluinoThreeBodyDecay = false;
  const reco::GenParticleCollection & partsColl = *parts_;

  for(unsigned int i = 0; i < partsColl.size(); ++i)
    {
      if(partsColl[i].pdgId()== 1000021 && partsColl[i].status()==2 && partsColl[i].numberOfDaughters()==3 )
	{
	  gluinoThreeBodyDecay=true;
	}
    }
  return gluinoThreeBodyDecay;
}
