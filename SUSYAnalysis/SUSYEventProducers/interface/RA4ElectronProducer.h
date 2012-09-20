#ifndef RA4ElectronProducer_h
#define RA4ElectronProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include <string>

// Conversion variables
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

// ID computation
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "EGamma/EGammaAnalysisTools/interface/EGammaCutBasedEleId.h"

class RA4ElectronProducer : public edm::EDProducer {

 public:
  /// default constructor
  explicit RA4ElectronProducer(const edm::ParameterSet&);
  /// default destructor
  ~RA4ElectronProducer(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// create new jet collection
  virtual void produce(edm::Event&, const edm::EventSetup&);
  

 private:
  /// jet input collection 
  edm::InputTag inputElectrons_;
  edm::InputTag conversionsInputTag_;
  edm::InputTag beamSpotInputTag_;
  edm::InputTag rhoIsoInputTag_;
  edm::InputTag primaryVertexInputTag_;
/*   std::vector<edm::InputTag> isoValInputTags_; */

  // histograms
  //...
};

#endif
