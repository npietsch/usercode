#ifndef SUSYObjects_SUSYEvent_h
#define SUSYObjects_SUSYEvent_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class SUSYEvent {

 public:

  /// empty constructor
  SUSYEvent(){};
  /// default constructor
  SUSYEvent(int, std::vector<pat::Muon>&, std::vector<pat::Electron>&, std::vector<pat::Jet>&, std::vector<pat::MET>&);
  /// default destructor
  virtual ~SUSYEvent(){};

  /// return number of objects
  int nMuons() const;
  int nElectrons() const;
  int nJets() const;

  /// return HT, MHT, MET, mT, YMET
  double HT() const;
  //double MHT() const;
  double MET() const;
  //double mT() const;
  double YMET() const;

 protected:

  int test_;
  std::vector<pat::Muon> muons_;
  std::vector<pat::Electron> electrons_;
  std::vector<pat::Jet> jets_;
  std::vector<pat::MET> mets_;

};

#endif
