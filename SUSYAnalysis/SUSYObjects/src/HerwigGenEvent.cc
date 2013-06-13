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
  if(genParticle.pdgId()==1000021)
    {
      gluino=true;
    }
  
  return gluino;
}
