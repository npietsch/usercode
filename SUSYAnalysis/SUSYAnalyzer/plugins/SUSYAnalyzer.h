#ifndef SUSYAnalyzer_h  
#define SUSYAnalyzer_h

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

class SUSYAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit SUSYAnalyzer(const edm::ParameterSet&);
  ~SUSYAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
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
  int btagBin_;
  int inclusiveBtagBin_; 

  bool useEventWgt_;
  bool useBtagEventWgt_;
  bool useInclusiveBtagEventWgt_;

  edm::InputTag TriggerWeight_;
  bool useTriggerEvtWgt_;

  double HT0_, HT1_, HT2_;
  double Y0_,  Y1_,  Y2_;

  // dummy histogram
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // TH2F histograms
  TH2F* JetEt_nrBjets_;

  // TH1F histograms

  TH1F* nPV_;
  TH1F* nPV_noWgt_;
  TH1F* nPU_;
  TH1F* nPU_noWgt_;

  TH1F* btagWeights_noWgt_;
  TH1F* btagWeights_PUWgt_;
  TH1F* nBtags_noWgt_;
  TH1F* nBtags_PUWgt_;
  TH1F* nBjets_;
  TH1F* nBtags_;

  TH1F* TCHE_;
  TH1F* TCHP_;
  TH1F* SSVHE_;
  TH1F* SSVHP_;

  TH1F *MET_;
  TH1F *MET_SSDiLepReco_;
  TH1F *MET_OSDiLepReco_;
  TH1F *HT_;
  TH1F *SigMET_;
  TH1F *significance_;
  TH1F *nJets_;
  TH1F *nMuons_;
  TH1F *nElectrons_;
  TH1F *nLeptons_;
  TH1F *MT_;
  TH1F *invMuMuMass_;
  TH1F *RelIsoMu1_;
  TH1F *RelIsoMu2_;

  TH1F *Electron0_eta_;
  TH1F *Muon0_eta_;

  TH2F *HTidxMETidx_;
  TH2F *HT_SigMET_;
  TH2F *HT_SigMET2_;
  TH2F *HT_MET_;

  TH2F *HT_significance2_;
  TH2F *HT_significance_;
  TH2F *significance_SigMET_;

  TH2F *HT_SigPtl_;
  TH2F *HT_SigPtl_smeared_;
  TH1F *SigPtl_smearFactor_;
  TH2F *HT_SigMET_unweighted_;

  //HISTS FOR STUDYING THE MET AND PT DEPENDENCE OF KAPPA
  ///////////////////////////////////////////////////////
  TH2F * HT_SigMET_PT20_MET60;
  TH2F * HT_SigMET_PT40_MET60;       
  TH2F * HT_SigMET_PT60_MET60;       

  TH2F * HT_SigPtl_PT20_MET20       ;
  TH2F * HT_SigPtl_PT20_MET40       ;
  TH2F * HT_SigPtl_PT20_MET60       ;

  TH2F * HT_SigPtl_PT20_MET20_smeared;
  TH2F * HT_SigPtl_PT20_MET40_smeared;
  TH2F * HT_SigPtl_PT20_MET60_smeared;

  TH2F * HT_significance_PT20_MET20 ;
  TH2F * HT_significance_PT20_MET40 ;
  TH2F * HT_significance_PT20_MET60 ;
  TH2F * HT_significance_PT40_MET60 ;
  TH2F * HT_significance_PT60_MET60 ;
  ////////////////////////////

  TH2F *mW_SigMET_;
  TH2F *sigMET_nJets_;
  TH2F *HT_nJets_;

  std::vector<TH1F*> Jet_Et_;
  std::vector<TH1F*> Muon_pt_;
  std::vector<TH1F*> Elec_pt_;
  std::vector<TH1F*> Bjet_EtFrac_;
  std::vector<TH1F*> LightJet_EtFrac_;

  TH1F *Bjets_EtFrac_;
  TH1F *LightJets_EtFrac_;
  TH1F *mW_;
  TH1F *mW_posCharge_;
  TH1F *mW_negCharge_;
  TH1F *mW2_;
  TH1F *mTop_;

  TH2F *mW_MET_;
  TH2F *mW_nJets_;
  TH2F *mW_HT_;
  TH2F *mW_MT_;
  TH2F *mW_MTHad_;


};  

#endif  
