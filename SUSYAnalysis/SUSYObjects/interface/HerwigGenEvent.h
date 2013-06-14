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
  HerwigGenEvent(reco::GenParticleRefProd& genParticles);
  /// default destructor
  virtual ~HerwigGenEvent(){};

  /// return particles of decay chain
  const reco::GenParticleCollection& particles() const { return *particles_; }

  /// is gluino?
  bool isGluino(const reco::GenParticle & genParticle) const;
  /// is squark of first or second generation?
  bool isSquark(const reco::Candidate* candidate) const;
  /// gluinos
  std::vector<unsigned int> GluinoIndices() const;
  /// gluino1 decay
  std::string DecayA() const;
  /// gluino2 decay
  std::string DecayB() const;
  // isBinoBino ?
  bool BinoBino() const;
  // isBinoOther ?
  bool BinoOther() const;
  // isBinoWino ?
  bool BinoWino() const;
  // isWinoWino ?
  bool WinoWino() const;
  // isWinoOther ?
  bool WinoOther() const;
  // invariant dijet mass form Decay chain A
  double qqbarA() const;

 protected:
  
  reco::GenParticleRefProd particles_;
};

#endif
