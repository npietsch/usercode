#ifndef BtagSystematicsAnalyzer_h  
#define BtagSystematicsAnalyzer_h

#include "TH1.h"
#include "TH2.h"

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

class BtagSystematicsAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit BtagSystematicsAnalyzer(const edm::ParameterSet&);
  ~BtagSystematicsAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  //--------------------------------
  // input collections          	
  //--------------------------------

  // collections of RA4b objects
  edm::InputTag jets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag met_;

  // for event weighting
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;
  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;
  edm::InputTag BtagEventWeights_;
  edm::InputTag BtagJetWeights_;
  edm::InputTag BtagJetWeightsGrid_;
  edm::InputTag BtagEventWeightsGrid_;
  edm::InputTag MistagEventWeightsGrid_;

  // bool
  bool useEventWgt_;
  bool useBtagEventWgt_;

  // int
  int btagBin_;
	
  //--------------------------------
  // histograms      	
  //--------------------------------

  // Dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // ABCD histograms
  TH1F *BtagWeightsGridA_[4];
  TH1F *BtagWeightsGridB_[4];
  TH1F *BtagWeightsGridC_[4];
  TH1F *BtagWeightsGridD_[4];

  TH1F *MistagWeightsGridA_[4];
  TH1F *MistagWeightsGridB_[4];
  TH1F *MistagWeightsGridC_[4];
  TH1F *MistagWeightsGridD_[4];

  // Histograms for control quantities
  TH1F* nPV_;
  TH1F* nPV_noWgt_;
  TH1F* nPU_;
  TH1F* nPU_noWgt_;

  TH1F* btagWeights_noWgt_;
  TH1F* btagWeights_;
  TH1F* nBtags_noWgt_;
  TH1F* nBtags_;
  TH1F* TCHE_;
  TH1F* TCHP_;
  TH1F* SSVHE_;
  TH1F* SSVHP_;

  TH1F* MET_;
  TH1F* HT_;
  TH1F* MHT_;

};  

#endif
