#include <memory>
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
#include <string>

class HerwigGenEventProducer : public edm::EDProducer {

 public:

  explicit HerwigGenEventProducer(const edm::ParameterSet&);
  ~HerwigGenEventProducer();
  virtual void produce(edm::Event&, const edm::EventSetup&);

  void fillOutput(const reco::GenParticleCollection&, reco::GenParticleCollection&);

 private:

  edm::InputTag src_;
};
