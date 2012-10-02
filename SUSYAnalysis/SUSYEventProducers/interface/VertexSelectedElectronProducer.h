#ifndef VertexSelectedElectronProducer_h
#define VertexSelectedElectronProducer_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


class VertexSelectedElectronProducer : public edm::EDProducer {

 public:
  explicit VertexSelectedElectronProducer(const edm::ParameterSet&);
  ~VertexSelectedElectronProducer() {};
  
 private:
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:
  edm::InputTag src_;
  edm::InputTag primaryVertex_;

};

#endif
