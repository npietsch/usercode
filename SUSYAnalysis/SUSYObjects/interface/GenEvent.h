#ifndef SUSYObjects_GenEvent_h
#define SUSYObjects_GenEvent_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <string>

namespace SUSYDecayID{
  static const int stable = 2;
  static const int unfrag = 3;
  static const int tID    = 6;
  static const int bID    = 5;
  static const int glueID = 21;
  static const int photID = 22;
  static const int ZID    = 23;
  static const int WID    = 24;
  static const int elecID = 11;
  static const int muonID = 13;
  static const int tauID  = 15;
}

namespace Wdecay{
  enum LepType {None, Elec, Muon, Tau};
}

class GenEvent {

 public:

  /// empty constructor
  GenEvent(){};
  /// default constructor
  GenEvent(reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& iniSubset);
  /// default destructor
  virtual ~GenEvent(){};

 protected:

  // reference to the top decay chain (has to be kept in the event!)
  reco::GenParticleRefProd parts_;       
  // reference to the list of initial partons (has to be kept in the event!)
  reco::GenParticleRefProd initPartons_;
};

#endif
