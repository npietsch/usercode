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

#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"

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
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag lightJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;

  // for event weighting
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;
  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;
  edm::InputTag BtagEventWeights_;
    
  // bool
  bool useEventWgt_;
  bool useBtagEventWgt_;
  //  bool doSusyGenEvent_;

  // int
  int btagBin_;


  //SUSY GenEvent
  edm::InputTag inputGenEvent_;

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
  TH1F* nJets_;

  TH1F* JetsPt_;
  TH1F* JetsEta_;

  std::vector<TH1F*> JetPt_;

  // histograms for ABCD method
  TH2F *HT_SigMET_;
  TH2F *HT_SigMET2_;

  //Histograms for SUSY sub-processes
  //------------------   
  TH2F *HT_SigMET_gg_;
  TH2F *HT_SigMET_gs_;
  TH2F *HT_SigMET_ss_;
  TH2F *HT_SigMET_sb_;
  TH2F *HT_SigMET_tb_;
  TH2F *HT_SigMET_bb_;
  TH2F *HT_SigMET_ll_;
  TH2F *HT_SigMET_nn_;
  TH2F *HT_SigMET_ng_;
  TH2F *HT_SigMET_ns_;
  TH2F *HT_SigMET_unknown_;

  TH2F *HT_SigMET_unweighted_gg_;
  TH2F *HT_SigMET_unweighted_gs_;
  TH2F *HT_SigMET_unweighted_ss_;
  TH2F *HT_SigMET_unweighted_sb_;
  TH2F *HT_SigMET_unweighted_tb_;
  TH2F *HT_SigMET_unweighted_bb_;
  TH2F *HT_SigMET_unweighted_ll_;
  TH2F *HT_SigMET_unweighted_nn_;
  TH2F *HT_SigMET_unweighted_ng_;
  TH2F *HT_SigMET_unweighted_ns_;
  TH2F *HT_SigMET_unweighted_unknown_;
  //--------//---------



};  

#endif
