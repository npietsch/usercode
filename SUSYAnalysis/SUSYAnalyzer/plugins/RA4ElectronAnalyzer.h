#ifndef RA4ElectronAnalyzer_h  
#define RA4ElectronAnalyzer_h

#include "TH1.h"
#include "TH2.h"
#include "TRandom3.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/angle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class RA4ElectronAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit RA4ElectronAnalyzer(const edm::ParameterSet&);
  ~RA4ElectronAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;

  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;
  edm::InputTag BtagEventWeights_;
  edm::InputTag BtagJetWeights_;
  int btagBin_;
  int inclusiveBtagBin_; 

  bool useEventWgt_;
  bool useBtagEventWgt_;
  bool useInclusiveBtagEventWgt_;

  edm::InputTag TriggerWeight_;
  bool useTriggerEvtWgt_;

  double HT0_, HT1_, HT2_;
  double Y0_,  Y1_,  Y2_;

  //-----------------------
  // Dummy histograms
  //-----------------------

  TH1F* Dummy_;
  TH2F* Dummy2_;

  //-----------------------
  // Event weighting
  //-----------------------

  TH1F* btagWeights_noWgt_;
  TH1F* btagWeights_PUWgt_;
  TH1F* nPU_noWgt_;
  TH1F* nPU_;
  TH1F* nPV_noWgt_;       
  TH1F* nPV_;
  
  TH1F* Weight_ ;
  TH1F* WeightPU_;
  TH1F* WeightRA2_;
  TH1F* WeightBtagEff_;
  TH1F* WeightTrigger_;

  //-----------------------
  // Muon variables
  //-----------------------

  // pt and eta
  TH1F* pt_;
  TH1F* eta_;

  TH1F* dB_;
  TH1F* dz_;

  TH1F* ID_;

  // nMuons
  TH1F* nElectrons_;
};  

#endif
