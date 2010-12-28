#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"


// SUSYEvent::SUSYEvent()
// {
//   muons_ = muons;
// }

int
SUSYEvent::leptons() const
{
  int lep=-1;
  
  return lep;
}
