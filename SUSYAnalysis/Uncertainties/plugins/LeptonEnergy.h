#ifndef LeptonEnergy_h
#define LeptonEnergy_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"

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

  /// scale factor for the rescaling of muon energy
  double scaleFactorMu_;
  /// scale factor for the rescaling of electron energy
  double scaleFactorEl_;
  /// threshold on lepton pt for MET corrections 
  double leptonPTThresholdForMET_;
 
};

#endif
