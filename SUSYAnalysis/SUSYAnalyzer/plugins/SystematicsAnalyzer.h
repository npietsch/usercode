#ifndef SystematicsAnalyzer_h  
#define SystematicsAnalyzer_h

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

class SystematicsAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit SystematicsAnalyzer(const edm::ParameterSet&);
  ~SystematicsAnalyzer();

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
    
  // bool
  bool useEventWgt_;
  bool useBtagEventWgt_;

  // int
  int btagBin_;

  //--------------------------------
  // histograms      	
  //--------------------------------

  // dummy histogram
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // histogram for control quantities
  TH1F* nPV_;
  TH1F* nPV_noWgt_;
  TH1F* nPU_;
  TH1F* nPU_noWgt_;

  TH1F* btagWeights_noWgt_;
  TH1F* btagWeights_PUWgt_;
  TH1F* nBtags_noWgt_;
  TH1F* nBtags_PUWgt_;
  TH1F* nBtags_;
  TH1F* TCHE_;
  TH1F* TCHP_;
  TH1F* SSVHE_;
  TH1F* SSVHP_;

  TH1F* MET_;
  TH1F* HT_;
  TH1F* MHT_;

  // histograms for ABCD method
  TH2F *HT_SigMET_;
  TH2F *HT_SigMET2_;

};  

#endif
