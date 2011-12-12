#ifndef LeptonEnergy_h
#define LeptonEnergy_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class LeptonEnergy : public edm::EDProducer {

 public:
  /// default constructor
  explicit LeptonEnergy(const edm::ParameterSet&);
  /// default destructor
  ~LeptonEnergy(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// rescale jet energy and recalculated MET
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:
  /// muon input collection 
  edm::InputTag inputMuons_;
  /// electron input collection 
  edm::InputTag inputElectrons_;
  /// met input collection
  edm::InputTag inputMETs_;

  /// muon output collection 
  std::string outputMuons_;
  /// electron output collection 
  std::string outputElectrons_;
  /// MET output collection
  std::string outputMETs_;

  /// scale Type
  std::string scaleType_;
  /// scale factor for the rescaling of lepton energy
  double scaleFactor_;
  /// threshold on lepton pt for MET corrections 
  double leptonPTThresholdForMET_;
 
};

#endif
