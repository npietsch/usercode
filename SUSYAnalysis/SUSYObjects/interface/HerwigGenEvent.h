#ifndef SUSYObjects_HerwigGenEvent_h
#define SUSYObjects_HerwigGenEvent_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <string>

class HerwigGenEvent {

 public:

  /// empty constructor
  HerwigGenEvent(){};
  /// default constructor
  HerwigGenEvent(reco::GenParticleRefProd& decaySubset);
  /// default destructor
  virtual ~HerwigGenEvent(){};

  /// return particles of decay chain
  const reco::GenParticleCollection& particles() const { return *parts_; }

  /// is gluino?
  bool isGluino(const reco::GenParticle & genParticle) const;
  /// is gluino three-body decay?
  bool isGluinoThreeBodyDecay() const;


 protected:
  
  reco::GenParticleRefProd parts_;

};

#endif
