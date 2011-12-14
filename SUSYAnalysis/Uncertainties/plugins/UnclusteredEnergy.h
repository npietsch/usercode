#ifndef UnclusteredEnergy_h
#define UnclusteredEnergy_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDProducer.h"

class UnclusteredEnergy : public edm::EDProducer {

 public:
  /// default constructor
  explicit UnclusteredEnergy(const edm::ParameterSet&);
  /// default destructor
  ~UnclusteredEnergy(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// rescale jet energy and recalculated MET
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:
  /// jet input collection 
  edm::InputTag inputJets_;
  /// met input collection
  edm::InputTag inputMETs_;
  /// MET output collection 
  std::string outputMETs_;
  /// scale factor for the rescaling
  double scaleFactor_;
  /// jet pt threshold
  double jetPTThresholdForMET_;
  /// max jet eta
  double maxJetEtaForMET_;
};

#endif
