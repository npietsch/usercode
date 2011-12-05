#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/GenEvent.h"


/// default contructor
GenEvent::GenEvent(reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& initSubset)
{ 
  parts_ = decaySubset; 
  initPartons_= initSubset;
}
