#include <memory>
#include <string>
#include <vector>
#include <map>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class SUSYEventProducer : public edm::EDProducer {

 public:

  explicit SUSYEventProducer(const edm::ParameterSet&);
  ~SUSYEventProducer();
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:

  int test_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag jets_;
  edm::InputTag mets_;
};
