#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

using namespace std;
 
SUSYAnalyzer::SUSYAnalyzer(const edm::ParameterSet& cfg):
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  lightJets_    (cfg.getParameter<edm::InputTag>("lightJets")),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") ),
  weight_       (cfg.getParameter<edm::InputTag>("weight") ),
  PUSource_     (cfg.getParameter<edm::InputTag>("PUInfo") ),
  RA2weight_    (cfg.getParameter<edm::InputTag>("RA2weight") ),
  useEvtWgt_    (cfg.getParameter<bool>("useEventWeight") )

{ 
  edm::Service<TFileService> fs;

  Dummy_=fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_=fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);

  JetEt_nrBjets_ = fs->make<TH2F>("JetEt_nrBjets","JetEt nrBjets", 30,0.,300.,5,0.,5.);

  MET_ = fs->make<TH1F>("MET","MET", 40, 0., 1000.);
  MET_SSDiLepReco_ = fs->make<TH1F>("MET_SS_DiLepReco","MET", 40, 0., 1000.);
  MET_OSDiLepReco_ = fs->make<TH1F>("MET_OS_DiLepReco","MET", 40, 0., 1000.);
  HT_ = fs->make<TH1F>("HT","HT", 40, 0., 2000.);
  SigMET_ = fs->make<TH1F>("SigMET","SigMET", 20, 0., 20);

  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0., 50);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  MET1pv_ = fs->make<TH1F>("MET1pv","MET1pv ", 40, 0., 1000.);
  HT1pv_ = fs->make<TH1F>("HT1pv","HT 1pv", 40, 0., 2000.);
  nJets1pv_ = fs->make<TH1F>("nJets1pv","njets 1pv",16 , -0.5, 15.5);
  Jet0_Et1pv_=fs->make<TH1F>("Jet0_Et1pv","Jet1 Et 1pv", 90, 0., 900.);
  Jet1_Et1pv_=fs->make<TH1F>("Jet1_Et1pv","Jet2 Et 1pv", 90, 0., 900.);

  MET2pv_ = fs->make<TH1F>("MET2pv","MET2pv ", 40, 0., 1000.);
  HT2pv_ = fs->make<TH1F>("HT2pv","HT 2pv", 40, 0., 2000.);
  nJets2pv_ = fs->make<TH1F>("nJets2pv","njets 2pv",16 , -0.5, 15.5);
  Jet0_Et2pv_=fs->make<TH1F>("Jet0_Et2pv","Jet2 Et 2pv", 90, 0., 900.);
  Jet1_Et2pv_=fs->make<TH1F>("Jet1_Et2pv","Jet2 Et 2pv", 90, 0., 900.);

  MET3pv_ = fs->make<TH1F>("MET3pv","MET3pv ", 40, 0., 1000.);
  HT3pv_ = fs->make<TH1F>("HT3pv","HT 3pv", 40, 0., 2000.);
  nJets3pv_ = fs->make<TH1F>("nJets3pv","njets 3pv",16 , -0.5, 15.5);
  Jet0_Et3pv_=fs->make<TH1F>("Jet0_Et3pv","Jet1 Et 3pv", 90, 0., 900.);
  Jet1_Et3pv_=fs->make<TH1F>("Jet1_Et3pv","Jet2 Et 3pv", 90, 0., 900.);

  MET4pv_ = fs->make<TH1F>("MET4pv","MET4pv ", 40, 0., 1000.);
  HT4pv_ = fs->make<TH1F>("HT4pv","HT 4pv", 40, 0., 2000.);
  nJets4pv_ = fs->make<TH1F>("nJets4pv","njets 4pv",16 , -0.5, 15.5);
  Jet0_Et4pv_=fs->make<TH1F>("Jet0_Et4pv","Jet1 Et 4pv", 90, 0., 900.);
  Jet1_Et4pv_=fs->make<TH1F>("Jet1_Et4pv","Jet2 Et 4pv", 90, 0., 900.);
 
  MET5pv_ = fs->make<TH1F>("MET5pv","MET5pv ", 40, 0., 1000.);
  HT5pv_ = fs->make<TH1F>("HT5pv","HT 5pv", 40, 0., 2000.);
  nJets5pv_ = fs->make<TH1F>("nJets5pv","njets 5pv",16 , -0.5, 15.5);
  Jet0_Et5pv_=fs->make<TH1F>("Jet0_Et5pv","Jet1 Et 5pv", 90, 0., 900.);
  Jet1_Et5pv_=fs->make<TH1F>("Jet1_Et5pv","Jet2 Et 5pv", 90, 0., 900.);

  HT_MET_ = fs->make<TH2F>("HT_MET","HT vs. MET", 78, 220., 1000., 30, 0., 300. );
  HT_SigMET_ = fs->make<TH2F>("HT_SigMET","HT vs. SigMET", 36, 200., 2000., 40, 0., 20. );
  HT_SigMET2_ = fs->make<TH2F>("HT_SigMET2","HT vs. SigMET2", 40, 0., 2000., 40, 0., 20. );

  HTidxMETidx_= fs->make<TH2F>("HTidxMETidx","HTidx METidx", 38, 220., 600., 30, 0., 300. );

  nJets_ = fs->make<TH1F>("nJets","njets",16 , -0.5, 15.5);

  nJets_control_ = fs->make<TH1F>("nJets_control","nJets_control",16 , -0.5, 15.5);
  nJets_control_eta05_ = fs->make<TH1F>("nJets_control_eta05","nJets_control_eta05",16 , -0.5, 15.5);
  nJets_control_eta10_ = fs->make<TH1F>("nJets_control_eta10","nJets_control_eta10",16 , -0.5, 15.5);
  nJets_control_eta15_ = fs->make<TH1F>("nJets_control_eta15","nJets_control_eta15",16 , -0.5, 15.5);
  nJets_control_eta20_ = fs->make<TH1F>("nJets_control_eta20","nJets_control_eta20",16 , -0.5, 15.5);
  nJets_control_eta25_ = fs->make<TH1F>("nJets_control_eta25","nJets_control_eta25",16 , -0.5, 15.5);

  nJets_signal_ = fs->make<TH1F>("nJets_signal","nJets_signal",16 , -0.5, 15.5);
  nJets_signal_eta05_ = fs->make<TH1F>("nJets_signal_eta05","nJets_signal_eta05",16 , -0.5, 15.5);
  nJets_signal_eta10_ = fs->make<TH1F>("nJets_signal_eta10","nJets_signal_eta10",16 , -0.5, 15.5);
  nJets_signal_eta15_ = fs->make<TH1F>("nJets_signal_eta15","nJets_signal_eta15",16 , -0.5, 15.5);
  nJets_signal_eta20_ = fs->make<TH1F>("nJets_signal_eta20","nJets_signal_eta20",16 , -0.5, 15.5);
  nJets_signal_eta25_ = fs->make<TH1F>("nJets_signal_eta25","nJets_signal_eta25",16 , -0.5, 15.5);

  HT_control_ = fs->make<TH1F>("HT_control","HT_control",40, 0., 2000.);
  HT_control_eta05_ = fs->make<TH1F>("HT_control_eta05","HT_control_eta05",40, 0., 2000.);
  HT_control_eta10_ = fs->make<TH1F>("HT_control_eta10","HT_control_eta10",40, 0., 2000.);
  HT_control_eta15_ = fs->make<TH1F>("HT_control_eta15","HT_control_eta15",40, 0., 2000.);
  HT_control_eta20_ = fs->make<TH1F>("HT_control_eta20","HT_control_eta20",40, 0., 2000.);
  HT_control_eta25_ = fs->make<TH1F>("HT_control_eta25","HT_control_eta25",40, 0., 2000.);

  HT_signal_ = fs->make<TH1F>("HT_signal","HT_signal",40, 0., 2000.);
  HT_signal_eta05_ = fs->make<TH1F>("HT_signal_eta05","HT_signal_eta05",40, 0., 2000.);
  HT_signal_eta10_ = fs->make<TH1F>("HT_signal_eta10","HT_signal_eta10",40, 0., 2000.);
  HT_signal_eta15_ = fs->make<TH1F>("HT_signal_eta15","HT_signal_eta15",40, 0., 2000.);
  HT_signal_eta20_ = fs->make<TH1F>("HT_signal_eta20","HT_signal_eta20",40, 0., 2000.);
  HT_signal_eta25_ = fs->make<TH1F>("HT_signal_eta25","HT_signal_eta25",40, 0., 2000.);

  mW_eta05_ = fs->make<TH1F>("mW_eta05","mW_eta05",40, 0., 400.);
  mW_eta10_ = fs->make<TH1F>("mW_eta10","mW_eta10",40, 0., 400.);
  mW_eta15_ = fs->make<TH1F>("mW_eta15","mW_eta15",40, 0., 400.);
  mW_eta20_ = fs->make<TH1F>("mW_eta20","mW_eta20",40, 0., 400.);
  mW_eta25_ = fs->make<TH1F>("mW_eta25","mW_eta25",40, 0., 400.);

  mW_control_ = fs->make<TH1F>("mW_control","mW_control",40, 0., 400.);
  mW_control_eta05_ = fs->make<TH1F>("mW_control_eta05","mW_control_eta05",40, 0., 400.);
  mW_control_eta10_ = fs->make<TH1F>("mW_control_eta10","mW_control_eta10",40, 0., 400.);
  mW_control_eta15_ = fs->make<TH1F>("mW_control_eta15","mW_control_eta15",40, 0., 400.);
  mW_control_eta20_ = fs->make<TH1F>("mW_control_eta20","mW_control_eta20",40, 0., 400.);
  mW_control_eta25_ = fs->make<TH1F>("mW_control_eta25","mW_control_eta25",40, 0., 400.);

  mW_signal_ = fs->make<TH1F>("mW_signal","mW_signal",40, 0., 400.);
  mW_signal_eta05_ = fs->make<TH1F>("mW_signal_eta05","mW_signal_eta05",40, 0., 400.);
  mW_signal_eta10_ = fs->make<TH1F>("mW_signal_eta10","mW_signal_eta10",40, 0., 400.);
  mW_signal_eta15_ = fs->make<TH1F>("mW_signal_eta15","mW_signal_eta15",40, 0., 400.);
  mW_signal_eta20_ = fs->make<TH1F>("mW_signal_eta20","mW_signal_eta20",40, 0., 400.);
  mW_signal_eta25_ = fs->make<TH1F>("mW_signal_eta25","mW_signal_eta25",40, 0., 400.);

  nMuons_ = fs->make<TH1F>("nMuons","nMuons",7 , -0.5, 6.5);
  nElectrons_ = fs->make<TH1F>("nElectrons","nElectrons",7 , -0.5, 6.5);
  nLeptons_ = fs->make<TH1F>("nLeptons","nLeptons",13 , -0.5, 12.5);
  MT_ = fs->make<TH1F>("MT","MT", 40, 0., 2000.);
  invMuMuMass_= fs->make<TH1F>("invMuMuMass","invMuMuMass",200,0.,200);

  RelIsoMu1_= fs->make<TH1F>("RelIsoMu1","RelIso Muon 1",40,0.,1.0);
  RelIsoMu2_= fs->make<TH1F>("RelIsoMu2","RelIso Muon 2",100,0.,5.0);

  Electron0_eta_=fs-> make<TH1F>("Elec0_eta","Elec0 eta", 60, -3, 3);
  Muon0_eta_=fs-> make<TH1F>("Muon0_eta","Muon0 eta", 60, -3, 3);

  for(int idx=0; idx<6; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));
    }
  for(int idx=0; idx<4; ++idx)
    {
      char histname[20];
      sprintf(histname,"Bjet%i_EtFrac",idx);
      Bjet_EtFrac_.push_back(fs->make<TH1F>(histname,histname, 50, 0., 5.));
    }
  for(int idx=0; idx<4; ++idx)
    {
      char histname[20];
      sprintf(histname,"LightJet%i_EtFrac",idx);
      LightJet_EtFrac_.push_back(fs->make<TH1F>(histname,histname, 50, 0., 5.));
    }
  for(int idx=0; idx<3; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon%i_Et",idx);
      Muon_pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));
    }
  for(int idx=0; idx<3; ++idx)
    {
      char histname[20];
      sprintf(histname,"Elec%i_Et",idx);
      Elec_pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));
    }
  Bjets_EtFrac_=fs->make<TH1F>("Bjets_EtFrac","Bjets Et fraction", 50, 0., 5.);
  LightJets_EtFrac_=fs->make<TH1F>("LightJets_EtFrac","LightJets Et fraction", 50, 0., 5.);

  BjetsEt_LooseA_=fs->make<TH1F>("BjetsEt_LooseA","BjetsEt LooseA", 90, 0., 900.);
  BjetsEt_LooseB_=fs->make<TH1F>("BjetsEt_LooseB","BjetsEt LooseB", 90, 0., 900.);
  BjetsEt_LooseC_=fs->make<TH1F>("BjetsEt_LooseC","BjetsEt LooseC", 90, 0., 900.);
  BjetsEt_LooseD_=fs->make<TH1F>("BjetsEt_LooseD","BjetsEt LooseD", 90, 0., 900.);
  BjetsEt_TightA_=fs->make<TH1F>("BjetsEt_TightA","BjetsEt TightA", 90, 0., 900.);
  BjetsEt_TightB_=fs->make<TH1F>("BjetsEt_TightB","BjetsEt TightB", 90, 0., 900.);
  BjetsEt_TightC_=fs->make<TH1F>("BjetsEt_TightC","BjetsEt TightC", 90, 0., 900.);
  BjetsEt_TightD_=fs->make<TH1F>("BjetsEt_TightD","BjetsEt TightD", 90, 0., 900.);

  Bjet0Et_LooseA_=fs->make<TH1F>("Bjet0Et_LooseA","Bjet0Et LooseA", 90, 0., 900.);
  Bjet0Et_LooseB_=fs->make<TH1F>("Bjet0Et_LooseB","Bjet0Et LooseB", 90, 0., 900.);
  Bjet0Et_LooseC_=fs->make<TH1F>("Bjet0Et_LooseC","Bjet0Et LooseC", 90, 0., 900.);
  Bjet0Et_LooseD_=fs->make<TH1F>("Bjet0Et_LooseD","Bjet0Et LooseD", 90, 0., 900.);
  Bjet0Et_TightA_=fs->make<TH1F>("Bjet0Et_TightA","Bjet0Et TightA", 90, 0., 900.);
  Bjet0Et_TightB_=fs->make<TH1F>("Bjet0Et_TightB","Bjet0Et TightB", 90, 0., 900.);
  Bjet0Et_TightC_=fs->make<TH1F>("Bjet0Et_TightC","Bjet0Et TightC", 90, 0., 900.);
  Bjet0Et_TightD_=fs->make<TH1F>("Bjet0Et_TightD","Bjet0Et TightD", 90, 0., 900.);

  Bjet1Et_LooseA_=fs->make<TH1F>("Bjet1Et_LooseA","Bjet1Et LooseA", 90, 0., 900.);
  Bjet1Et_LooseB_=fs->make<TH1F>("Bjet1Et_LooseB","Bjet1Et LooseB", 90, 0., 900.);
  Bjet1Et_LooseC_=fs->make<TH1F>("Bjet1Et_LooseC","Bjet1Et LooseC", 90, 0., 900.);
  Bjet1Et_LooseD_=fs->make<TH1F>("Bjet1Et_LooseD","Bjet1Et LooseD", 90, 0., 900.);
  Bjet1Et_TightA_=fs->make<TH1F>("Bjet1Et_TightA","Bjet1Et TightA", 90, 0., 900.);
  Bjet1Et_TightB_=fs->make<TH1F>("Bjet1Et_TightB","Bjet1Et TightB", 90, 0., 900.);
  Bjet1Et_TightC_=fs->make<TH1F>("Bjet1Et_TightC","Bjet1Et TightC", 90, 0., 900.);
  Bjet1Et_TightD_=fs->make<TH1F>("Bjet1Et_TightD","Bjet1Et TightD", 90, 0., 900.);

  Bjet2Et_LooseA_=fs->make<TH1F>("Bjet2Et_LooseA","Bjet2Et LooseA", 90, 0., 900.);
  Bjet2Et_LooseB_=fs->make<TH1F>("Bjet2Et_LooseB","Bjet2Et LooseB", 90, 0., 900.);
  Bjet2Et_LooseC_=fs->make<TH1F>("Bjet2Et_LooseC","Bjet2Et LooseC", 90, 0., 900.);
  Bjet2Et_LooseD_=fs->make<TH1F>("Bjet2Et_LooseD","Bjet2Et LooseD", 90, 0., 900.);
  Bjet2Et_TightA_=fs->make<TH1F>("Bjet2Et_TightA","Bjet2Et TightA", 90, 0., 900.);
  Bjet2Et_TightB_=fs->make<TH1F>("Bjet2Et_TightB","Bjet2Et TightB", 90, 0., 900.);
  Bjet2Et_TightC_=fs->make<TH1F>("Bjet2Et_TightC","Bjet2Et TightC", 90, 0., 900.);
  Bjet2Et_TightD_=fs->make<TH1F>("Bjet2Et_TightD","Bjet2Et TightD", 90, 0., 900.);

  JetsEt_LooseA_=fs->make<TH1F>("JetsEt_LooseA","JetsEt LooseA", 90, 0., 900.);
  JetsEt_LooseB_=fs->make<TH1F>("JetsEt_LooseB","JetsEt LooseB", 90, 0., 900.);
  JetsEt_LooseC_=fs->make<TH1F>("JetsEt_LooseC","JetsEt LooseC", 90, 0., 900.);
  JetsEt_LooseD_=fs->make<TH1F>("JetsEt_LooseD","JetsEt LooseD", 90, 0., 900.);
  JetsEt_TightA_=fs->make<TH1F>("JetsEt_TightA","JetsEt TightA", 90, 0., 900.);
  JetsEt_TightB_=fs->make<TH1F>("JetsEt_TightB","JetsEt TightB", 90, 0., 900.);
  JetsEt_TightC_=fs->make<TH1F>("JetsEt_TightC","JetsEt TightC", 90, 0., 900.);
  JetsEt_TightD_=fs->make<TH1F>("JetsEt_TightD","JetsEt TightD", 90, 0., 900.);

  Jet0Et_LooseA_=fs->make<TH1F>("Jet0Et_LooseA","Jet0Et LooseA", 90, 0., 900.);
  Jet0Et_LooseB_=fs->make<TH1F>("Jet0Et_LooseB","Jet0Et LooseB", 90, 0., 900.);
  Jet0Et_LooseC_=fs->make<TH1F>("Jet0Et_LooseC","Jet0Et LooseC", 90, 0., 900.);
  Jet0Et_LooseD_=fs->make<TH1F>("Jet0Et_LooseD","Jet0Et LooseD", 90, 0., 900.);
  Jet0Et_TightA_=fs->make<TH1F>("Jet0Et_TightA","Jet0Et TightA", 90, 0., 900.);
  Jet0Et_TightB_=fs->make<TH1F>("Jet0Et_TightB","Jet0Et TightB", 90, 0., 900.);
  Jet0Et_TightC_=fs->make<TH1F>("Jet0Et_TightC","Jet0Et TightC", 90, 0., 900.);
  Jet0Et_TightD_=fs->make<TH1F>("Jet0Et_TightD","Jet0Et TightD", 90, 0., 900.);

  Jet1Et_LooseA_=fs->make<TH1F>("Jet1Et_LooseA","Jet1Et LooseA", 90, 0., 900.);
  Jet1Et_LooseB_=fs->make<TH1F>("Jet1Et_LooseB","Jet1Et LooseB", 90, 0., 900.);
  Jet1Et_LooseC_=fs->make<TH1F>("Jet1Et_LooseC","Jet1Et LooseC", 90, 0., 900.);
  Jet1Et_LooseD_=fs->make<TH1F>("Jet1Et_LooseD","Jet1Et LooseD", 90, 0., 900.);
  Jet1Et_TightA_=fs->make<TH1F>("Jet1Et_TightA","Jet1Et TightA", 90, 0., 900.);
  Jet1Et_TightB_=fs->make<TH1F>("Jet1Et_TightB","Jet1Et TightB", 90, 0., 900.);
  Jet1Et_TightC_=fs->make<TH1F>("Jet1Et_TightC","Jet1Et TightC", 90, 0., 900.);
  Jet1Et_TightD_=fs->make<TH1F>("Jet1Et_TightD","Jet1Et TightD", 90, 0., 900.);

  Jet2Et_LooseA_=fs->make<TH1F>("Jet2Et_LooseA","Jet2Et LooseA", 90, 0., 900.);
  Jet2Et_LooseB_=fs->make<TH1F>("Jet2Et_LooseB","Jet2Et LooseB", 90, 0., 900.);
  Jet2Et_LooseC_=fs->make<TH1F>("Jet2Et_LooseC","Jet2Et LooseC", 90, 0., 900.);
  Jet2Et_LooseD_=fs->make<TH1F>("Jet2Et_LooseD","Jet2Et LooseD", 90, 0., 900.);
  Jet2Et_TightA_=fs->make<TH1F>("Jet2Et_TightA","Jet2Et TightA", 90, 0., 900.);
  Jet2Et_TightB_=fs->make<TH1F>("Jet2Et_TightB","Jet2Et TightB", 90, 0., 900.);
  Jet2Et_TightC_=fs->make<TH1F>("Jet2Et_TightC","Jet2Et TightC", 90, 0., 900.);
  Jet2Et_TightD_=fs->make<TH1F>("Jet2Et_TightD","Jet2Et TightD", 90, 0., 900.);

  mW_=fs-> make<TH1F>("mW","mW", 40 , 0, 400);
  mW_posCharge_=fs-> make<TH1F>("mW_posCharge","mW_posCharge", 40 , 0, 400);
  mW_negCharge_=fs-> make<TH1F>("mW_negCharge","mW_negCharge", 40 , 0, 400);
  mW2_=fs-> make<TH1F>("mW2","mW2", 40 , 0, 600);
  mTop_=fs-> make<TH1F>("mTop","mTop", 50 , 0, 500);

  mW_MET0_=fs-> make<TH1F>("mW_MET0","mW_MET0", 40 , 0, 400);
  mW_MET50_=fs-> make<TH1F>("mW_MET50","mW_MET50", 40 , 0, 400);
  mW_MET100_=fs-> make<TH1F>("mW_MET100","mW MET100", 40 , 0, 400);
  mW_MET150_=fs-> make<TH1F>("mW_MET150","mW MET150", 40 , 0, 400);
  mW_MET200_=fs-> make<TH1F>("mW_MET200","mW MET200", 40 , 0, 400);
  mW_MET250_=fs-> make<TH1F>("mW_MET250","mW MET250", 40 , 0, 400);
  mW_MET300_=fs-> make<TH1F>("mW_MET300","mW MET300", 40 , 0, 400);

  mW_SigMET0_=fs-> make<TH1F>("mW_SigMET0","mW_SigMET0", 40 , 0, 400);
  mW_SigMET2_=fs-> make<TH1F>("mW_SigMET2","mW SigMET2", 40 , 0, 400);
  mW_SigMET4_=fs-> make<TH1F>("mW_SigMET4","mW SigMET4", 40 , 0, 400);
  mW_SigMET6_=fs-> make<TH1F>("mW_SigMET6","mW SigMET6", 40 , 0, 400);
  mW_SigMET9_=fs-> make<TH1F>("mW_SigMET9","mW SigMET9", 40 , 0, 400);
  mW_SigMET12_=fs-> make<TH1F>("mW_SigMET12","mW SigMET12", 40 , 0, 400);

  mW_4Jets_=fs-> make<TH1F>("mW_4Jets","mW 4Jets", 40 , 0, 400);
  mW_5Jets_=fs-> make<TH1F>("mW_5Jets","mW 5Jets", 40 , 0, 400);
  mW_6Jets_=fs-> make<TH1F>("mW_6Jets","mW 6Jets", 40 , 0, 400);
  mW_7Jets_=fs-> make<TH1F>("mW_7Jets","mW 7Jets", 40 , 0, 400);
  mW_8Jets_=fs-> make<TH1F>("mW_8Jets","mW 8Jets", 40 , 0, 400);
  mW_9Jets_=fs-> make<TH1F>("mW_9Jets","mW 9Jets", 40 , 0, 400);

  mW_HT300_=fs-> make<TH1F>("mW_HT300","mW HT300", 40 , 0, 400);
  mW_HT400_=fs-> make<TH1F>("mW_HT400","mW HT400", 40 , 0, 400);
  mW_HT500_=fs-> make<TH1F>("mW_HT500","mW HT500", 40 , 0, 400);
  mW_HT600_=fs-> make<TH1F>("mW_HT600","mW HT600", 40 , 0, 400);
  mW_HT700_=fs-> make<TH1F>("mW_HT700","mW HT700", 40 , 0, 400);
  mW_HT800_=fs-> make<TH1F>("mW_HT800","mW HT800", 40 , 0, 400);

  mW_MET_=fs-> make<TH2F>("mW_MET","MET vs. mW",  40, 0., 400., 25, 0., 500.);
  mW_nJets_=fs-> make<TH2F>("mW_nJets","nJets vs. mW", 40, 0., 400.,16 , -0.5, 15.5 );
  mW_HT_=fs-> make<TH2F>("mW_HT","HT vs. mW", 20, 0., 400., 40, 0., 2000.);
  mW_MT_=fs-> make<TH2F>("mW_MT","MT vs. mW", 20, 0., 400., 40, 0., 2000.);
  mW_MTHad_=fs-> make<TH2F>("mW_MTHad","MTHad vs. mW", 20, 0., 400., 40, 0., 2000.);

  mW_SigMET_=fs-> make<TH2F>("mW_SigMET","SigMET vs. mW",  40, 0., 400., 20, 0., 20.);
  sigMET_nJets_=fs-> make<TH2F>("sigMET_nJets","nJets vs. sigMET", 20, 0., 20.,16 , -0.5, 15.5 );
  HT_nJets_=fs-> make<TH2F>("HT_nJets","nJets vs. HT", 25, 0., 1000.,16 , -0.5, 15.5 );
}

SUSYAnalyzer::~SUSYAnalyzer()
{
}

void
SUSYAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //--------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > lightJets;
  evt.getByLabel(lightJets_, lightJets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);

  double weight=1;
  double weightPU=1;
  double weightRA2=1;

  if(useEvtWgt_)
    {
      //std::cout << "use event weight" << std::endl;
      edm::Handle<double> weightHandle;
      evt.getByLabel(weight_, weightHandle);
      weightPU=*weightHandle;

      edm::Handle<edm::View<PileupSummaryInfo> > PUInfo;
      evt.getByLabel(PUSource_, PUInfo);

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      
      for(iterPU = PUInfo->begin(); iterPU != PUInfo->end(); ++iterPU)  // vector size is 3
	{ 
	  if (iterPU->getBunchCrossing()==0) // -1: previous BX, 0: current BX,  1: next BX
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	}

      edm::Handle<double> RA2weightHandle;
      evt.getByLabel(RA2weight_, RA2weightHandle);
      weightRA2=*RA2weightHandle;

      weight=weightPU*weightRA2;

      //std::cout << "-------------------------------------" << std::endl;
      //std::cout << "weightPU: " << weightPU << std::endl;
      //std::cout << "weightRA2: " << weightRA2 << std::endl;
      //std::cout << "weight: " << weight << std::endl;
      //std::cout << "-------------------------------------" << std::endl;

      nPU_->Fill(nvtx,weight);
    }

  weight=1;

  //-------------------------------------------------
  // Jet Et, MET, HT, nJets
  //-------------------------------------------------

  double HT=0;
  int njets=0;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      if(i<6) Jet_Et_[i]->Fill((*jets)[i].et(), weight);
      HT=HT+(*jets)[i].et();
      njets=njets+1;
    }
  
  MET_->Fill((*met)[0].et(), weight);
  HT_->Fill(HT, weight);
  nJets_->Fill(njets, weight);

  double HTBjets=0;
  double HTLightJets=0;

  if(bjets->size()>0 && lightJets->size()>0 && jets->size()>0)
    {
      for(int i=0; i<(int)bjets->size(); ++i)
	{
	  double frac=((*bjets)[i].et())*(jets->size())/HT;
	  if(i<4) Bjet_EtFrac_[i]->Fill(frac, weight);
	  HTBjets=HTBjets+(*bjets)[i].et();
	}
      for(int i=0; i<(int)lightJets->size(); ++i)
	{
	  double frac=((*lightJets)[i].et())*(lightJets->size())/HT;
	  if(i<4) LightJet_EtFrac_[i]->Fill(frac, weight);
	  HTLightJets=HTLightJets+(*lightJets)[i].et();
	}
      double BjetsFrac=(HTBjets/(bjets->size()))/(HT/(jets->size()));
      double LightJetsFrac=(HTLightJets/(lightJets->size()))/(HT/(jets->size()));

      Bjets_EtFrac_->Fill(BjetsFrac, weight);
      LightJets_EtFrac_->Fill(LightJetsFrac, weight);
    }

  if(jets->size()>0)
    {
      JetEt_nrBjets_->Fill(HT/(jets->size()),bjets->size(), weight);
    }

  double sigMET=((*met)[0].et())/(sqrt(HT));
  
  SigMET_->Fill(sigMET, weight);
  HT_SigMET_->Fill(HT,sigMET, weight);
  HT_SigMET2_->Fill(HT,sigMET, weight);
  HT_MET_->Fill(HT,(*met)[0].et(), weight);

  for(int bdx=0; bdx<(int) bjets->size(); ++bdx)
    {
      if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) BjetsEt_LooseA_->Fill((*bjets)[bdx].et(),weight);
      else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) BjetsEt_LooseB_->Fill((*bjets)[bdx].et(),weight);
      else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) BjetsEt_LooseC_->Fill((*bjets)[bdx].et(),weight);
      else if(HT >= 400 && sigMET >= 4.5 )  BjetsEt_LooseD_->Fill((*bjets)[bdx].et(),weight);

      if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) BjetsEt_TightA_->Fill((*bjets)[bdx].et(),weight);
      else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) BjetsEt_TightB_->Fill((*bjets)[bdx].et(),weight);
      else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) BjetsEt_TightC_->Fill((*bjets)[bdx].et(),weight);
      else if(HT >= 650 && sigMET >= 5.5 ) BjetsEt_TightD_->Fill((*bjets)[bdx].et(),weight);

      if(bdx==0)
	{
	  if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) Bjet0Et_LooseA_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) Bjet0Et_LooseB_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) Bjet0Et_LooseC_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 4.5 )  Bjet0Et_LooseD_->Fill((*bjets)[bdx].et(),weight);
	  
	  if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) Bjet0Et_TightA_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) Bjet0Et_TightB_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) Bjet0Et_TightC_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 5.5 ) Bjet0Et_TightD_->Fill((*bjets)[bdx].et(),weight);
	}
      if(bdx==1)
	{
	  if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) Bjet1Et_LooseA_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) Bjet1Et_LooseB_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) Bjet1Et_LooseC_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 4.5 )  Bjet1Et_LooseD_->Fill((*bjets)[bdx].et(),weight);
	  
	  if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) Bjet1Et_TightA_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) Bjet1Et_TightB_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) Bjet1Et_TightC_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 5.5 ) Bjet1Et_TightD_->Fill((*bjets)[bdx].et(),weight);
	}
      if(bdx==2)
	{
	  if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) Bjet2Et_LooseA_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) Bjet2Et_LooseB_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) Bjet2Et_LooseC_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 4.5 )  Bjet2Et_LooseD_->Fill((*bjets)[bdx].et(),weight);
	  
	  if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) Bjet2Et_TightA_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) Bjet2Et_TightB_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) Bjet2Et_TightC_->Fill((*bjets)[bdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 5.5 ) Bjet2Et_TightD_->Fill((*bjets)[bdx].et(),weight);
	}
    }

  for(int jjdx=0; jjdx<(int) jets->size(); ++jjdx)
    {
      if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) JetsEt_LooseA_->Fill((*jets)[jjdx].et(),weight);
      else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) JetsEt_LooseB_->Fill((*jets)[jjdx].et(),weight);
      else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) JetsEt_LooseC_->Fill((*jets)[jjdx].et(),weight);
      else if(HT >= 400 && sigMET >= 4.5 )  JetsEt_LooseD_->Fill((*jets)[jjdx].et(),weight);

      if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) JetsEt_TightA_->Fill((*jets)[jjdx].et(),weight);
      else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) JetsEt_TightB_->Fill((*jets)[jjdx].et(),weight);
      else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) JetsEt_TightC_->Fill((*jets)[jjdx].et(),weight);
      else if(HT >= 650 && sigMET >= 5.5 ) JetsEt_TightD_->Fill((*jets)[jjdx].et(),weight);

      if(jjdx==0)
	{
	  if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) Jet0Et_LooseA_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) Jet0Et_LooseB_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) Jet0Et_LooseC_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 4.5 )  Jet0Et_LooseD_->Fill((*jets)[jjdx].et(),weight);
	  
	  if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) Jet0Et_TightA_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) Jet0Et_TightB_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) Jet0Et_TightC_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 5.5 ) Jet0Et_TightD_->Fill((*jets)[jjdx].et(),weight);
	}
      if(jjdx==1)
	{
	  if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) Jet1Et_LooseA_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) Jet1Et_LooseB_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) Jet1Et_LooseC_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 4.5 )  Jet1Et_LooseD_->Fill((*jets)[jjdx].et(),weight);
	  
	  if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) Jet1Et_TightA_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) Jet1Et_TightB_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) Jet1Et_TightC_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 5.5 ) Jet1Et_TightD_->Fill((*jets)[jjdx].et(),weight);
	}
      if(jjdx==2)
	{
	  if(HT >= 300 && HT < 350 && sigMET >= 2.5 && sigMET < 4.) Jet2Et_LooseA_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 2.5 && sigMET < 4.) Jet2Et_LooseB_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 300 && HT < 350 && sigMET >= 4.5 ) Jet2Et_LooseC_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 400 && sigMET >= 4.5 )  Jet2Et_LooseD_->Fill((*jets)[jjdx].et(),weight);
	  
	  if(HT >= 300 && HT < 650 && sigMET >= 2.5 && sigMET < 5.5) Jet2Et_TightA_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 2.5 && sigMET < 5.5) Jet2Et_TightB_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 300 && HT < 650 && sigMET >= 5.5 ) Jet2Et_TightC_->Fill((*jets)[jjdx].et(),weight);
	  else if(HT >= 650 && sigMET >= 5.5 ) Jet2Et_TightD_->Fill((*jets)[jjdx].et(),weight);
	}
    }

  nPV_->Fill(pvSrc->size(), weight);

  if(pvSrc->size()==1)
    {
      MET1pv_->Fill((*met)[0].et(), weight);
      HT1pv_->Fill(HT, weight);
      nJets1pv_->Fill(njets, weight);
      if(jets->size()>0)
	{
	  Jet0_Et1pv_->Fill((*jets)[0].et(), weight);
	}
      if(jets->size()>1)
	{
	  Jet0_Et1pv_->Fill((*jets)[1].et(), weight);
	} 
    }

  if(pvSrc->size()==2 || pvSrc->size()==3)
    {
      MET2pv_->Fill((*met)[0].et(), weight);
      HT2pv_->Fill(HT, weight);
      nJets2pv_->Fill(njets, weight);
      if(jets->size()>0)
	{
	  Jet0_Et2pv_->Fill((*jets)[0].et(), weight);
	}
      if(jets->size()>1)
	{
	  Jet0_Et2pv_->Fill((*jets)[1].et(), weight);
	} 
    }

  if(pvSrc->size()==4 || pvSrc->size()==5 || pvSrc->size()==6)
    {
      MET3pv_->Fill((*met)[0].et(), weight);
      HT3pv_->Fill(HT, weight);
      nJets3pv_->Fill(njets, weight);
      if(jets->size()>0)
	{
	  Jet0_Et3pv_->Fill((*jets)[0].et(), weight);
	}
      if(jets->size()>1)
	{
	  Jet0_Et3pv_->Fill((*jets)[1].et(), weight);
	} 
    }
  
  if(pvSrc->size()==7 || pvSrc->size()==8 || pvSrc->size()==9)
    {  
      MET4pv_->Fill((*met)[0].et(), weight);
      HT4pv_->Fill(HT, weight);
      nJets4pv_->Fill(njets, weight);
      if(jets->size()>0)
	{
	  Jet0_Et4pv_->Fill((*jets)[0].et(), weight);
	}
      if(jets->size()>1)
	{
	  Jet0_Et4pv_->Fill((*jets)[1].et(), weight);
	} 
    }
  
  if(pvSrc->size()>=10)
    {
      MET5pv_->Fill((*met)[0].et(), weight);
      HT5pv_->Fill(HT, weight);
      nJets5pv_->Fill(njets, weight);
      if(jets->size()>0)
	{
	  Jet0_Et5pv_->Fill((*jets)[0].et(), weight);
	}
      if(jets->size()>1)
	{
	  Jet0_Et5pv_->Fill((*jets)[1].et(), weight);
	} 
    }

  //std::cout << "===========================================" << std::endl;
  //std::cout << "==================MET: " << (*met)[0].et() << std::endl;
  //std::cout << "==================HT:  " << HT << std::endl;
  //std::cout << "===========================================" << std::endl;

  for(int METidx=0; METidx<300; METidx+=10 )
    {
      //std::cout << "-----------------" << std::endl;
      //std::cout << "METidx: " << METidx <<std::endl;
      //std::cout << "-----------------" << std::endl;

      for(int HTidx=200; HTidx<600; HTidx+=10)
	{
	  //std::cout << "-----------------" << std::endl;
	  //std::cout << "HTidx: " << HTidx <<std::endl;
	  //std::cout << "-----------------" << std::endl;

	  if( (*met)[0].et() > METidx && HT > HTidx) HTidxMETidx_->Fill(HTidx,METidx, weight);
	}
    }

  //-------------------------------------------------
  // Lepton pt, nMuons, nElectrons, nLeptons
  //-------------------------------------------------

  if(muons->size()>0) Muon0_eta_->Fill((*muons)[0].eta(), weight);
  if(electrons->size()>0) Electron0_eta_->Fill((*electrons)[0].eta(), weight);

  int nleptons=0;
  int nmuons=0;
  int nelectrons=0;
  double lepHT=0;
  std::vector<int> charge;
  
  double RelIso=100;
  double RelIso1=100;
  double RelIso2=100;

  for(int i=0; i<(int)muons->size(); ++i)
    {
      if(i<3) Muon_pt_[i]->Fill((*muons)[i].pt(), weight);
      nmuons=nmuons+1;
      nleptons=nleptons+1;
      lepHT=lepHT+(*muons)[i].et();
      //std::cout << "muon charge: " << (*muons)[i].charge() << std::endl;
      charge.push_back((*muons)[i].charge());
      //if((*muons)[i].genLepton()) std::cout << (*muons)[i].genLepton()->pdgId() << std::endl;

      RelIso=((*muons)[i].trackIso()+(*muons)[i].caloIso())/((*muons)[i].pt());

      if(RelIso < RelIso1)
	{
	  RelIso2=RelIso1;
	  RelIso1=RelIso;
	}
      else if(RelIso < RelIso2)
	{
	  RelIso2=RelIso;
	}
    }

  if(RelIso1 >= 1 && RelIso1 < 100) RelIso1=0.9999;
  if(RelIso1 >= 5 && RelIso2 < 100) RelIso2=0.4999;

  RelIsoMu1_->Fill(RelIso1, weight);
  RelIsoMu2_->Fill(RelIso2, weight);

  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<3) Elec_pt_[i]->Fill((*electrons)[i].pt(), weight);
      nelectrons=nelectrons+1;
      nleptons=nleptons+1;
      lepHT=lepHT+(*electrons)[i].et();
      //std::cout << "electron charge: " << (*electrons)[i].charge() << std::endl;
      charge.push_back((*electrons)[i].charge());
      //if((*electrons)[i].genLepton()) std::cout << (*electrons)[i].genLepton()->pdgId() << std::endl;
    }
  nMuons_->Fill(nmuons, weight);
  nElectrons_->Fill(nelectrons, weight);
  nLeptons_->Fill(nleptons, weight);

  double MT=lepHT+HT+(*met)[0].et();
  double MTHad=HT+(*met)[0].et();
  MT_->Fill(MT, weight);
  
  if(nleptons==2)
    {
      int chargeSign=1;

      for(int cdx=0; cdx < (int)charge.size(); ++cdx)
	{
	  chargeSign=chargeSign*charge[cdx];  
	}
      if(chargeSign>0)MET_SSDiLepReco_->Fill((*met)[0].et(), weight);
      else if(chargeSign < 0) MET_OSDiLepReco_->Fill((*met)[0].et(), weight);
    }

  if(muons->size() >= 2)
    {
      double MuMu_p4_square = ((*muons)[0].p4()+(*muons)[1].p4()).Dot((*muons)[0].p4()+(*muons)[1].p4());
      invMuMuMass_->Fill(sqrt(MuMu_p4_square), weight);
    }

  //transverse W-mass
  double mW=0;
  double mTop=0;
  double eta=3.0;
  double lepCharge=0;
  double mW2=0;
  double dRLepBjetMin=10;
  reco::Particle::LorentzVector METP4=(*met)[0].p4();
	 
  if(muons->size()==1)
    {
      mW=sqrt(2*(((*met)[0].et())*((*muons)[0].et())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
      eta=(*muons)[0].eta();
      mW2=sqrt(2*(((*met)[0].et())*((*muons)[0].energy())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
      eta=(*muons)[0].eta();
      lepCharge=(*muons)[0].charge();

      reco::Particle::LorentzVector LepP4=(*muons)[0].p4();
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	 double dRLepBjet=abs(deltaR((*bjets)[bdx].eta(),(*bjets)[bdx].phi(),(*muons)[0].eta(),(*muons)[0].phi()));
	 reco::Particle::LorentzVector BjetP4=(*bjets)[bdx].p4();
	 if(dRLepBjet < dRLepBjetMin)
	   {
	     dRLepBjetMin=dRLepBjet;
	     mTop=sqrt((METP4+LepP4+BjetP4).Dot(METP4+LepP4+BjetP4));
	   }
	}
    }
  else if(electrons->size()==1)
    {
      mW=sqrt(2*(((*met)[0].et())*((*electrons)[0].et())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
      mW2=sqrt(2*(((*met)[0].et())*((*electrons)[0].energy())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
      eta=(*electrons)[0].eta();
      lepCharge=(*electrons)[0].charge();

      reco::Particle::LorentzVector LepP4=(*electrons)[0].p4();
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	 double dRLepBjet=abs(deltaR((*bjets)[bdx].eta(),(*bjets)[bdx].phi(),(*electrons)[0].eta(),(*electrons)[0].phi()));
	 reco::Particle::LorentzVector BjetP4=(*bjets)[bdx].p4();
	 if(dRLepBjet < dRLepBjetMin)
	   {
	     dRLepBjetMin=dRLepBjet;
	     mTop=sqrt((METP4+LepP4+BjetP4).Dot(METP4+LepP4+BjetP4));
	   }
	}
    }

  if(mW2 > 0)
    {
      mW2_->Fill(mW2, weight);
    }

  if(70 < mW2 && 90 < mW2  && mTop > 0)
    {
      mTop_->Fill(mTop, weight);
    }

  if(mW > 0)
    {
      mW_->Fill(mW, weight);
      if(lepCharge > 0) mW_posCharge_->Fill(mW, weight);
      if(lepCharge < 0) mW_negCharge_->Fill(mW, weight);

      if(abs(eta)<= 0.5) mW_eta05_->Fill(mW, weight);
      else if(0.5 <= abs(eta) && abs(eta)< 1.0) mW_eta10_->Fill(mW, weight);
      else if(1.0 <= abs(eta) && abs(eta)< 1.5) mW_eta15_->Fill(mW, weight);
      else if(1.5 <= abs(eta) && abs(eta)< 2.0) mW_eta20_->Fill(mW, weight);
      else if(2.0 <= abs(eta) && abs(eta)< 2.5) mW_eta25_->Fill(mW, weight);

      if(mW >= 60 && mW < 90)
	{
	  nJets_control_->Fill(jets->size(), weight);
	  if(abs(eta)<= 0.5) nJets_control_eta05_->Fill(jets->size(), weight);
	  else if(0.5 <= abs(eta) && abs(eta)< 1.0) nJets_control_eta10_->Fill(jets->size(), weight);
	  else if(1.0 <= abs(eta) && abs(eta)< 1.5) nJets_control_eta15_->Fill(jets->size(), weight);
	  else if(1.5 <= abs(eta) && abs(eta)< 2.0) nJets_control_eta20_->Fill(jets->size(), weight);
	  else if(2.0 <= abs(eta) && abs(eta)< 2.5) nJets_control_eta25_->Fill(jets->size(), weight);

	  HT_control_->Fill(HT, weight);
	  if(abs(eta)<= 0.5) HT_control_eta05_->Fill(HT, weight);
	  else if(0.5 <= abs(eta) && abs(eta)< 1.0) HT_control_eta10_->Fill(HT, weight);
	  else if(1.0 <= abs(eta) && abs(eta)< 1.5) HT_control_eta15_->Fill(HT, weight);
	  else if(1.5 <= abs(eta) && abs(eta)< 2.0) HT_control_eta20_->Fill(HT, weight);
	  else if(2.0 <= abs(eta) && abs(eta)< 2.5) HT_control_eta25_->Fill(HT, weight);

	  mW_control_->Fill(mW, weight);
	  if(abs(eta)<= 0.5) mW_control_eta05_->Fill(mW, weight);
	  else if(0.5 <= abs(eta) && abs(eta) && abs(eta)< 1.0) mW_control_eta10_->Fill(mW, weight);
	  else if(1.0 <= abs(eta) && abs(eta) && abs(eta)< 1.5) mW_control_eta15_->Fill(mW, weight);
	  else if(1.5 <= abs(eta) && abs(eta) && abs(eta)< 2.0) mW_control_eta20_->Fill(mW, weight);
	  else if(2.0 <= abs(eta) && abs(eta) && abs(eta)< 2.5) mW_control_eta25_->Fill(mW, weight);
	}
      else
	{
	  nJets_signal_->Fill(jets->size(), weight);
	  if(eta<= 0.5) nJets_signal_eta05_->Fill(jets->size(), weight);
	  else if(0.5 <= abs(eta) && eta< 1.0) nJets_signal_eta10_->Fill(jets->size(), weight);
	  else if(1.0 <= abs(eta) && eta< 1.5) nJets_signal_eta15_->Fill(jets->size(), weight);
	  else if(1.5 <= abs(eta) && eta< 2.0) nJets_signal_eta20_->Fill(jets->size(), weight);
	  else if(2.0 <= abs(eta) && eta< 2.5) nJets_signal_eta25_->Fill(jets->size(), weight);

	  HT_signal_->Fill(HT, weight);
	  if(eta<= 0.5) HT_signal_eta05_->Fill(HT, weight);
	  else if(0.5 <= abs(eta) && eta< 1.0) HT_signal_eta10_->Fill(HT, weight);
	  else if(1.0 <= abs(eta) && eta< 1.5) HT_signal_eta15_->Fill(HT, weight);
	  else if(1.5 <= abs(eta) && eta< 2.0) HT_signal_eta20_->Fill(HT, weight);
	  else if(2.0 <= abs(eta) && eta< 2.5) HT_signal_eta25_->Fill(HT, weight);

	  mW_signal_->Fill(mW, weight);
	  if(eta< 0.5) mW_signal_eta05_->Fill(mW, weight);
	  else if(0.5 <= abs(eta) && eta< 1.0) mW_signal_eta10_->Fill(mW, weight);
	  else if(1.0 <= abs(eta) && eta< 1.5) mW_signal_eta15_->Fill(mW, weight);
	  else if(1.5 <= abs(eta) && eta< 2.0) mW_signal_eta20_->Fill(mW, weight);
	  else if(2.0 <= abs(eta) && eta< 2.5) mW_signal_eta25_->Fill(mW, weight);
	}

      mW_MET_->Fill(mW,(*met)[0].et(), weight);
      mW_nJets_->Fill(mW,jets->size(), weight);
      mW_HT_->Fill(mW,HT, weight);
      mW_SigMET_->Fill(mW,sigMET, weight);
      sigMET_nJets_->Fill(sigMET,jets->size(), weight);
      HT_nJets_->Fill(HT,jets->size(), weight);
      mW_MT_->Fill(mW,MT, weight);
      mW_MTHad_->Fill(mW,MTHad, weight);

      if((*met)[0].et()<50) mW_MET0_->Fill(mW, weight);
      else if((*met)[0].et()>= 50  &&(*met)[0].et()<100) mW_MET50_->Fill(mW, weight);
      else if((*met)[0].et()>= 100 &&(*met)[0].et()<150) mW_MET100_->Fill(mW, weight);
      else if((*met)[0].et()>= 150 &&(*met)[0].et()<200) mW_MET150_->Fill(mW, weight);
      else if((*met)[0].et()>= 200 &&(*met)[0].et()<250) mW_MET200_->Fill(mW, weight);
      else if((*met)[0].et()>= 250 &&(*met)[0].et()<300) mW_MET250_->Fill(mW, weight);
      else if((*met)[0].et()>= 300) mW_MET300_->Fill(mW, weight);
      
      if(sigMET<2) mW_SigMET0_->Fill(mW, weight);
      else if(sigMET>= 2 &&sigMET<4) mW_SigMET2_->Fill(mW, weight);
      else if(sigMET>= 4 &&sigMET<6) mW_SigMET4_->Fill(mW, weight);
      else if(sigMET>= 6 &&sigMET<9) mW_SigMET6_->Fill(mW, weight);
      else if(sigMET>= 9 &&sigMET<12) mW_SigMET9_->Fill(mW, weight);
      else if(sigMET>= 12) mW_SigMET12_->Fill(mW, weight);

      if(jets->size()==4) mW_4Jets_->Fill(mW, weight);
      else if(jets->size()==5) mW_5Jets_->Fill(mW, weight);
      else if(jets->size()==6) mW_6Jets_->Fill(mW, weight);
      else if(jets->size()==7) mW_7Jets_->Fill(mW, weight);
      else if(jets->size()==8) mW_8Jets_->Fill(mW, weight);
      else if(jets->size()>=9) mW_9Jets_->Fill(mW, weight);

      if(HT >= 300 && HT < 400) mW_HT300_->Fill(mW, weight);
      else if(HT >= 400 && HT < 500) mW_HT400_->Fill(mW, weight);
      else if(HT >= 500 && HT < 600) mW_HT500_->Fill(mW, weight);
      else if(HT >= 600 && HT < 700) mW_HT600_->Fill(mW, weight);
      else if(HT >= 700 && HT < 800) mW_HT700_->Fill(mW, weight);
      else if(HT >= 800) mW_HT800_->Fill(mW, weight);
    }
}

void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
