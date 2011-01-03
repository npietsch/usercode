#ifndef SUSYObjects_SUSYGenEvent_h
#define SUSYObjects_SUSYGenEvent_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <string>
/* #include "FWCore/Framework/interface/Event.h" */
/* #include "FWCore/Framework/interface/EDFilter.h" */
/* #include "FWCore/Framework/interface/Frameworkfwd.h" */
/* #include "FWCore/ParameterSet/interface/ParameterSet.h" */


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
  SUSYGenEvent(int, reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& iniSubset, reco::GenParticleRefProd& iniSparticles);
  /// default destructor
  virtual ~SUSYGenEvent(){};

  /// return particles of decay chain
  const reco::GenParticleCollection& particles() const { return *parts_; }
  /// return particles of initial partons
  const reco::GenParticleCollection& initialPartons() const { return *initPartons_;}

  /// return radiated gluons from particle with pdgId
  std::vector<const reco::GenParticle*> radiatedGluons(int pdgId) const;

  // is muon or electron?
  bool isLepton(const reco::GenParticle&) const;
  /// return number of leptons in the decay chain
  int numberOfLeptons() const;
  // is di-lepton
  int isDiLepton() const;
  /// return number of leptons in the decay chain
  int numberOfLeptons(Wdecay::LepType type, bool fromWBoson=true) const;

  /// return number of b quarks in the decay chain
  int numberOfBQuarks() const;

  /// is gluino?
  bool isGluino(const reco::GenParticle & genParticle) const;
  /// is squark of first or second generation?
  bool isSquark(const reco::GenParticle & genParticle) const;
  /// is stop quark?
  bool isStop(const reco::GenParticle & genParticle) const;
  /// is sbottom quark?
  bool isSbottom(const reco::GenParticle & genParticle) const;
    /// is chargino?
  bool isChargino(const reco::GenParticle & genParticle) const;
  /// is neutralino?
  bool isNeutralino(const reco::GenParticle & genParticle) const;
  /// is neutral higgs?
  bool isNeutralHiggs(const reco::GenParticle & genParticle) const;
  /// is slepton?
  bool isSlepton(const reco::GenParticle & genParticle) const;

  /// is gluino decay?
  bool GluinoDecay() const;
  /// is squark decay?
  bool SquarkDecay() const;
  /// is gluino-gluino decay?
  bool GluinoGluinoDecay() const;
  /// is squark-squark decay?
  bool SquarkSquarkDecay() const;
  /// is same sign squark-squark decay?
  bool SSignSquarkSquarkDecay() const;
  /// is opposite sign squark-squark decay?
  bool OSignSquarkSquarkDecay() const;
  /// is gluino-squark decay?
  bool GluinoSquarkDecay() const;

  /// return pdgId of initial sparticle A
  int decayChainA() const;
  /// returns pdgId of initial sparticle B
  int decayChainB() const;

  /// creates daughter gen particle
  //reco::GenParticle* createDaughter(const reco::Candidate*, int) const;
  /// creates susy daughter of a gen particle
  const reco::Candidate* createSdaughter(const reco::Candidate*) const;
  /// returns sparticle name
  std::string sparticleName(const reco::Candidate*) const;
  /// returns decay cascade
  std::string decayCascade(int) const;
  /// returns decay cascadeA
  std::string decayCascadeA() const;
 /// returns decay cascadeB
  std::string decayCascadeB() const;

  /// get candidate with given pdg id if available; 0 else 
  const reco::GenParticle* candidate(int id, unsigned int parentId=0) const;

 protected:
  // reference to the top decay chain (has to be kept in the event!)
  reco::GenParticleRefProd parts_;       
  // reference to the list of initial partons (has to be kept in the event!)
  reco::GenParticleRefProd initPartons_;
   // reference to the list of initial sparticles (has to be kept in the event!)
  reco::GenParticleRefProd initSparticles_;
  int generation_;
};

#endif
