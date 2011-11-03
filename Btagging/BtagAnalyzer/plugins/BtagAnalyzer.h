#ifndef BtagAnalyzer_h  
#define BtagAnalyzer_h

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

class BtagAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit BtagAnalyzer(const edm::ParameterSet&);
  ~BtagAnalyzer();

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

  // collections matched objects
  edm::InputTag matchedLightJets_;
  edm::InputTag matchedBjets_;

  // for event weighting
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;
  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;
  edm::InputTag BtagEventWeights_;
  edm::InputTag BtagJetWeights_;
  edm::InputTag BtagJetWeightsGrid_;
  edm::InputTag BtagEventWeightsGrid_;
  edm::InputTag BtagEffGrid_;

  // bool
  bool useEventWgt_;
  bool useBtagEventWgt_;

  // int
  int btagBin_;
	
  //--------------------------------
  // histograms      	
  //--------------------------------

  // dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

    // histogram for control quantities
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

  // Jets
  TH1F* JetsPt_;
  TH1F* JetsEta_;
  TH1F* JetsBdisc_;
  TH1F* NrJets_;
  TH1F* HighPtJetsEta_;
  TH1F* HighPtJetsBdisc_;
  TH1F* NrHighPtJets_;
  TH1F* LowPtJetsEta_;
  TH1F* LowPtJetsBdisc_;
  TH1F* NrLowPtJets_;
  TH1F* dPhiJetMET_;

  // Bjets
  TH1F* BjetsPt_;
  TH1F* BjetsEta_;
  TH1F* BjetsBdisc_;
  TH1F* NrBjets_;
  TH1F* HighPtBjetsEta_;
  TH1F* HighPtBjetsBdisc_;
  TH1F* NrHighPtBjets_;
  TH1F* NrHighPtBjets_2;
  TH1F* LowPtBjetsEta_;
  TH1F* LowPtBjetsBdisc_;
  TH1F* NrLowPtBjets_;
  TH1F* dPhiBjetMET_;

  // Btags
  TH1F* BtagsPt_;
  TH1F* BtagsEta_;
  TH1F* NrBtags_;
  TH1F* HighPtBtagsEta_;
  TH1F* NrHighPtBtags_;
  TH1F* LowPtBtagsEta_;
  TH1F* NrLowPtBtags_;
  TH1F* dPhiBtagMET_;

  // Btags for >= 1 btag
  TH1F* BtagsPt_1b_;
  TH1F* BtagsEta_1b_;
  TH1F* HighPtBtagsEta_1b_; 
  TH1F* LowPtBtagsEta_1b_;
  TH1F* dPhiBtagMET_1b_;

  // Btags for >= 2 btags
  TH1F* BtagsPt_2b_;
  TH1F* BtagsEta_2b_;  
  TH1F* HighPtBtagsEta_2b_;
  TH1F* LowPtBtagsEta_2b_;  
  TH1F* dPhiBtagMET_2b_;

  // Btags for >= 3 btags
  TH1F* BtagsPt_3b_;
  TH1F* BtagsEta_3b_;  
  TH1F* HighPtBtagsEta_3b_; 
  TH1F* LowPtBtagsEta_3b_; 
  TH1F* dPhiBtagMET_3b_;

  // combined jet and event weighting applied
  TH1F* BtagsPt_btagWeight_;
  TH1F* BtagsEta_btagWeight_;
  TH1F* BtagsPt_1b_btagWeight_;
  TH1F* BtagsEta_1b_btagWeight_;
  TH1F* BtagsPt_2b_btagWeight_;
  TH1F* BtagsEta_2b_btagWeight_;
  TH1F* BtagsPt_3b_btagWeight_;
  TH1F* BtagsEta_3b_btagWeight_;

  TH1F *BtagsPt_1b_btagWeightGrid_[21];
  TH1F *BtagsPt_2b_btagWeightGrid_[21];

  TH1F *BtagWeightsGrid_[4];
  TH1F *BtagWeightsGrid_excl_[4];
};  

#endif  
