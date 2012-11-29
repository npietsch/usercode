#ifndef CorrelationAnalyzer_h  
#define CorrelationAnalyzer_h

#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
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

class CorrelationAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit CorrelationAnalyzer(const edm::ParameterSet&);
  ~CorrelationAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           
  edm::InputTag SUSYEvent_;
  std::vector<int> nJetsCut_;
  std::vector<double> HTCut_;
  std::vector<double> METCut_;

  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag lightJets_;
  edm::InputTag bjets_;
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

  bool TTJets_;
  edm::InputTag TtGenEvent_;

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

  TH1F* NumEvents_;

  //-----------------------
  // Basic kinematics
  //-----------------------

  std::vector<TH1F*> Jet_Et_;
  std::vector<TH1F*> Jet_Eta_;

  TH1F* Jets_Et_;
  TH1F* Jets_Eta_;
  TH1F* DeltaRecoGenJetPt_;
  TH1F* MET_;
  TH1F* HT_; 
  TH1F* nJets_;
  TH1F* DeltaRecoGenJetPtSum_;
  TH1F* AbsDeltaRecoGenJetPtSum_;

  TH2F* DeltaRecoGenJetPtSum_MET_;
  TH2F* AbsDeltaRecoGenJetPtSum_MET_;
  TH2F* DeltaRecoGenJetPtSum_nJets_;
  TH2F* AbsDeltaRecoGenJetPtSum_nJets_;

  TH1F* smearedGenMET_;

  std::vector<TH1F*> Muon_Pt_;
  std::vector<TH1F*> Muon_Eta_;

  std::vector<TH1F*> Electron_Pt_;
  std::vector<TH1F*> Electron_Eta_;

  TH1F* nMuons_;
  TH1F* nElectrons_;
  TH1F* nLeptons_;
  TH1F* LeptonPt_;
  TH1F* LeptonEta_;

  TH1F* MT_;

  TH1F* mT_;
  TH1F* mlb_;
  TH1F* mLepTop_;

  TH1F* YMET_;
  TH1F* METSig_;
  TH1F* LepPt_;
  TH1F* LepPtSig_;

  //-----------------------
  // Btagging
  //-----------------------

  TH1F* TCHE_;
  TH1F* TCHP_;
  TH1F* SSVHE_;
  TH1F* SSVHP_;
  
  TH1F* nBjets_noWgt_;
  TH1F* nBjets_noWgt_2_;
  TH1F* nBjets_;
  TH1F* nBjets_2_;

  std::vector<TH1F*> Bjet_Et_;
  std::vector<TH1F*> Bjet_Eta_;

  TH1F* Bjets_Et_;
  TH1F* Bjets_Eta_;

  //-----------------------
  // MET, Lepton pt vs. HT
  //-----------------------

  TH2F* HT_MET_;
  TH2F* HT_LepPt_;

  //-------------------------------------------------------
  // YMET, MET significnace, Lepton pt significance vs HT
  //-------------------------------------------------------

  TH2F* HT_YMET_;
  TH2F* HT_YMET_noWgt_;

  TH2F* HT_METSig_;
  TH2F* HT_METSig_noWgt_;

  TH2F* METSig_YMET_;

  TH2F* HT_LepPtSig_;

  TH2F* HT_LepPtSig_smeared_;
  TH1F* LepPtSig_smearFactor_;
  TH2F* HT_METSig_unweighted_;

  TH2F* HT_METSig_PT20_MET20_;
  TH2F* HT_METSig_PT20_MET40_;
  TH2F* HT_METSig_PT20_MET60_;
  TH2F* HT_METSig_PT40_MET60_;      
  TH2F* HT_METSig_PT60_MET60_;
			     
  TH2F* HT_LepPtSig_PT20_MET20_;
  TH2F* HT_LepPtSig_PT20_MET40_;
  TH2F* HT_LepPtSig_PT20_MET60_;
		
  TH2F* HT_LepPtSig_PT20_MET20_smeared_;
  TH2F* HT_LepPtSig_PT20_MET40_smeared_;
  TH2F* HT_LepPtSig_PT20_MET60_smeared_;
	     
  TH2F* HT_significance_PT20_MET20_;
  TH2F* HT_significance_PT20_MET40_;
  TH2F* HT_significance_PT20_MET60_;
  TH2F* HT_significance_PT40_MET60_;
  TH2F* HT_significance_PT60_MET60_;

  //-----------------------
  // mjj variabels
  //-----------------------

  TH1F* minj3_;

  TH2F* minj3_nJets_;
  TH2F* HT_minj3_;

  //-----------------------
  // Others
  //-----------------------

  TH2F* HT_mT_;
  TH2F* mT_nJets_;
  TH2F* YMET_nJets_;
  TH2F* mlb_YMET_;
  TH2F* HT_mLepTop_;
  TH2F* HT_mlb_;
  TH2F* mLepTop_nJets_;
  TH2F* mlb_nJets_;

  TH3F* mlb_YMET_nJets_;

  TH2F* YMET_nJets_0_;
  TH2F* YMET_nJets_100_;
  TH2F* YMET_nJets_200_;

  TH2F* mlb_nJets_0_;
  TH2F* mlb_nJets_5_;
  TH2F* mlb_nJets_10_;
  TH2F* mlb_nJets_15_;
  TH2F* mlb_nJets_20_;

  TH1F* pv_;
  TH1F* smearedPv_;

  TH2F* pv_nJets_;
  TH2F* mlv_nJets_gen_;
  TH2F* mlv_nJets_reco_;
  
  TH2F* pv_MET_;
  TH2F* smearedPv_MET_;
  
  //-----------------------
  // ABCD method
  //-----------------------

  TH1F* MET_A_;
  TH1F* MET_B_;
  TH1F* MET_C_;
  TH1F* MET_D_;

  TH1F* Lep_Pt_A_;
  TH1F* Lep_Pt_B_;
  TH1F* Lep_Pt_C_;
  TH1F* Lep_Pt_D_;

  TH1F* Jets_Et_A_;
  TH1F* Jets_Et_B_;
  TH1F* Jets_Et_C_;
  TH1F* Jets_Et_D_;

  TH1F* Bjets_Et_A_;
  TH1F* Bjets_Et_B_;
  TH1F* Bjets_Et_C_;
  TH1F* Bjets_Et_D_;
  
  TH1F* Bjets_Et_Weights_A_;
  TH1F* Bjets_Et_Weights_B_;
  TH1F* Bjets_Et_Weights_C_;
  TH1F* Bjets_Et_Weights_D_;

  TH1F* Bjets_Et_Weights_A_670_;
  TH1F* Bjets_Et_Weights_B_670_;
  TH1F* Bjets_Et_Weights_C_670_;
  TH1F* Bjets_Et_Weights_D_670_;
  
  TH1F* Bjets_Eta_Weights_A_;
  TH1F* Bjets_Eta_Weights_B_;
  TH1F* Bjets_Eta_Weights_C_;
  TH1F* Bjets_Eta_Weights_D_;

  TH1F* Bjets_Eta_Weights_A_670_;
  TH1F* Bjets_Eta_Weights_B_670_;
  TH1F* Bjets_Eta_Weights_C_670_;
  TH1F* Bjets_Eta_Weights_D_670_;

  TH1F* nJets_A_;
  TH1F* nJets_B_;
  TH1F* nJets_C_;
  TH1F* nJets_D_;

  std::vector<TH1F*> Jet_Et_A_;
  std::vector<TH1F*> Jet_Et_B_;
  std::vector<TH1F*> Jet_Et_C_;
  std::vector<TH1F*> Jet_Et_D_;

  std::vector<TH1F*> Bjet_Et_A_;
  std::vector<TH1F*> Bjet_Et_B_;
  std::vector<TH1F*> Bjet_Et_C_;
  std::vector<TH1F*> Bjet_Et_D_;
};  

#endif  
