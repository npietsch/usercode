#ifndef SUSYObjects_GenEvent_h
#define SUSYObjects_GenEvent_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

class GenEvent {

 public:

  /// empty constructor
  GenEvent(){};
  /// default constructor
  GenEvent(const reco::GenParticleCollection&);
  /// default destructor
  virtual ~GenEvent(){};

  std::vector<reco::GenParticle*> InitialParticles() const;

  double shat() const;

 protected:

  reco::GenParticleCollection genParticles_;
};

#endif
