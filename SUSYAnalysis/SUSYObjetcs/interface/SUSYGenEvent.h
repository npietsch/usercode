#ifndef SUSYObjects_SUSYGenEvent_h
#define SUSYObjects_SUSYGenEvent_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"



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
  /// classification of leptons in the decay channel 
  /// of the W boson used in several places throughout 
  /// the package
  enum LepType {None, Elec, Muon, Tau};
}

class SUSYGenEvent {

 public:

  /// empty constructor
  SUSYGenEvent(){};
  /// default constructor
  SUSYGenEvent(reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& iniSubset);
  /// default destructor
  virtual ~SUSYGenEvent(){};

  /// return particles of decay chain
  const reco::GenParticleCollection& particles() const { return *parts_; }
  /// return particles of initial partons
  const reco::GenParticleCollection& initialPartons() const { return *initPartons_;}

  /// return radiated gluons from particle with pdgId
  std::vector<const reco::GenParticle*> radiatedGluons(int pdgId) const;

  /// return number of leptons in the decay chain
  int numberOfLeptons(bool fromWBoson=true) const;
  /// return number of leptons in the decay chain
  int numberOfLeptons(Wdecay::LepType type, bool fromWBoson=true) const;
  /// return number of b quarks in the decay chain
  int numberOfBQuarks(bool fromTopQuark=true) const;

  /// get candidate with given pdg id if available; 0 else 
  const reco::GenParticle* candidate(int id, unsigned int parentId=0) const;

 protected:

  // reference to the top decay chain (has to be kept in the event!)
  reco::GenParticleRefProd parts_;       
  // reference to the list of initial partons (has to be kept in the event!)
  reco::GenParticleRefProd initPartons_; 
};

#endif


