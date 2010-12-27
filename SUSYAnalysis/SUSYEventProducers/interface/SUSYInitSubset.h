#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <string>

namespace SUSYInitID{
  static const int status = 3;
  static const int tID    = 6; 
}

class SUSYInitSubset : public edm::EDProducer {

 public:

  explicit SUSYInitSubset(const edm::ParameterSet&);
  ~SUSYInitSubset();
  
  virtual void produce(edm::Event&, const edm::EventSetup&);
  void fillOutput(const reco::GenParticleCollection&, reco::GenParticleCollection&, reco::GenParticleCollection&);

 private:

  edm::InputTag src_;  

  std::string InitParticles_;
  std::string InitSparticles_;


};
