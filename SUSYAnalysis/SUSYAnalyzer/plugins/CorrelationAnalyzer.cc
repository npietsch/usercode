#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/CorrelationAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include <math.h>

using namespace std;
 
CorrelationAnalyzer::CorrelationAnalyzer(const edm::ParameterSet& cfg):
  SUSYEvent_         (cfg.getParameter<edm::InputTag>("SUSYEvent")),
  nJetsCut_          (cfg.getParameter<std::vector<int> >("nJetsCut")),
  HTCut_             (cfg.getParameter<std::vector<double> >("HTCut")),
  METCut_            (cfg.getParameter<std::vector<double> >("METCut")),
  YMETCut_           (cfg.getParameter<std::vector<double> >("YMETCut")),

  met_               (cfg.getParameter<edm::InputTag>("met") ),
  jets_              (cfg.getParameter<edm::InputTag>("jets") ),
  lightJets_         (cfg.getParameter<edm::InputTag>("lightJets") ),
  bjets_             (cfg.getParameter<edm::InputTag>("bjets") ),
  muons_             (cfg.getParameter<edm::InputTag>("muons") ),
  electrons_         (cfg.getParameter<edm::InputTag>("electrons") ),
  vetoMuons_         (cfg.getParameter<edm::InputTag>("vetoMuons") ),
  vetoElectrons_     (cfg.getParameter<edm::InputTag>("vetoElectrons") ),
  PVSrc_             (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_            (cfg.getParameter<edm::InputTag>("PUInfo") ),

  PUWeight_          (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_         (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEventWeights_  (cfg.getParameter<edm::InputTag>("BtagEventWeights") ),
  BtagJetWeights_    (cfg.getParameter<edm::InputTag>("BtagJetWeights") ),
  btagBin_           (cfg.getParameter<int>("btagBin") ),
  inclusiveBtagBin_  (cfg.getParameter<int>("inclusiveBtagBin") ),

  useEventWgt_       (cfg.getParameter<bool>("useEventWeight") ),
  useBtagEventWgt_   (cfg.getParameter<bool>("useBtagEventWeight") ),
  useInclusiveBtagEventWgt_  (cfg.getParameter<bool>("useInclusiveBtagEventWeight") ),

  TriggerWeight_     (cfg.getParameter<edm::InputTag>("TriggerWeight") ),
  useTriggerEvtWgt_  (cfg.getParameter<bool>("useTriggerEventWeight") ),

  HT0_               (cfg.getParameter<double>("HT0") ),
  HT1_               (cfg.getParameter<double>("HT1") ),
  HT2_               (cfg.getParameter<double>("HT2") ),
  Y0_                (cfg.getParameter<double>("Y0") ),
  Y1_                (cfg.getParameter<double>("Y1") ),
  Y2_                (cfg.getParameter<double>("Y2") ),

  TTJets_            (cfg.getParameter<bool>("TTJets") ),
  TtGenEvent_        (cfg.getParameter<edm::InputTag>("TtGenEvent")),

  TTJetsHyp_         (cfg.getParameter<bool>("TTJetsHyp") ),
  TtSemiLepEvent_    (cfg.getParameter<edm::InputTag>("TtSemiLepEvent")),
  hypoKey_           (cfg.getParameter<std::string>("hypoKey"))

{ 
  edm::Service<TFileService> fs;

  //-------------------------------------------------
  // Dummy histograms
  //-------------------------------------------------

  Dummy_ =fs->make<TH1F>();
  Dummy2_=fs->make<TH2F>();

  Dummy_->SetDefaultSumw2(true);
  Dummy2_->SetDefaultSumw2(true);

  //-------------------------------------------------
  // Event weighting
  //-------------------------------------------------

  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt", "btagWeights_noWgt",  4, 0.,   4. );
  btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt", "btagWeights_PUWgt",  4, 0.,   4. );
  nPU_noWgt_         = fs->make<TH1F>("nPU_noWgt",         "nPU_noWgt",         71, -0.5, 70.5);
  nPU_               = fs->make<TH1F>("nPU",               "nPU",               71, -0.5, 70.5);
  nPV_noWgt_         = fs->make<TH1F>("nPV_noWgt",         "nPV_noWgt",         71, -0.5, 70.5);
  nPV_               = fs->make<TH1F>("nPV",               "nPV",               71, -0.5, 70.5);

  Weight_        = fs->make<TH1F>("Weight",        "Weight",        50 , 0.,   10. );
  WeightPU_      = fs->make<TH1F>("WeightPU",      "WeightPU",      50 , 0.,   10. );
  WeightRA2_     = fs->make<TH1F>("WeightRA2",     "WeightRA2",     50 , 0.,   10. );
  WeightBtagEff_ = fs->make<TH1F>("WeightBtagEff", "WeightBtagEff", 50 , 0.,   10. );
  WeightTrigger_ = fs->make<TH1F>("WeightTrigger", "WeightTrigger", 50 , 0.,   10. );

  NumEvents_     = fs->make<TH1F>("NumEvents",     "NumEvents",      1 , 0.,    1. );

  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------

  for(int idx=0; idx<8; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));

      char histname2[20];
      sprintf(histname2,"Jet%i_Eta",idx);
      Jet_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }

  Jets_Et_           = fs->make<TH1F>("Jets_Et",           "Jets_Et",           90,   0.,  900.);
  Jets_Eta_          = fs->make<TH1F>("Jets_Eta",          "Jets_Eta",          60,  -3.,    3.);
  DeltaRecoGenJetPt_ = fs->make<TH1F>("DeltaRecoGenJetPt", "DeltaRecoGenJetPt", 60, -30.,   30.);

  MET_                     = fs->make<TH1F>("MET",                      "MET",                     50,   0.,  1000.);
  HT_                      = fs->make<TH1F>("HT",                       "HT",                      60,   0.,  3000.);
  nJets_                   = fs->make<TH1F>("nJets",                    "nJets",                   16 , -0.5,  15.5);
  nJets50_                 = fs->make<TH1F>("nJets50",                  "nJets50",                 16 , -0.5,  15.5);
  DeltaRecoGenJetPtSum_    = fs->make<TH1F>("DeltaRecoGenJetPtSum_",    "DeltaRecoGenJetPtSum",    40,  -100.,  100);
  AbsDeltaRecoGenJetPtSum_ = fs->make<TH1F>("AbsDeltaRecoGenJetPtSum_", "AbsDeltaRecoGenJetPtSum", 40,     0.,  200);

  DeltaRecoGenJetPtSum_MET_ = fs->make<TH2F>("DeltaRecoGenJetPtSum_MET", "MET vs .DeltaRecoGenJetPtSum", 40, -100., 100., 50, 0., 1000.);
  AbsDeltaRecoGenJetPtSum_MET_ = fs->make<TH2F>("AbsDeltaRecoGenJetPtSum_MET", "MET vs. AbsDeltaRecoGenJetPtSum", 40, 0., 200., 50, 0., 1000.);
  DeltaRecoGenJetPtSum_nJets_ = fs->make<TH2F>("DeltaRecoGenJetPtSum_nJets", "nJets vs .DeltaRecoGenJetPtSum", 40, -100., 100., 16, -0.5, 15.5);
  AbsDeltaRecoGenJetPtSum_nJets_ = fs->make<TH2F>("AbsDeltaRecoGenJetPtSum_nJets", "nJets vs. AbsDeltaRecoGenJetPtSum", 40, 0., 200., 16, 0.5, 0.5);

  smearedGenMET_ = fs->make<TH1F>("smearedGenMET", "smearedGenMET", 50,   0.,  1000.);

  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon%i_Pt",idx);
      Muon_Pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));

      char histname2[20];
      sprintf(histname2,"Muon%i_Eta",idx);
      Muon_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Electron%i_Pt",idx);
      Electron_Pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));

      char histname2[20];
      sprintf(histname2,"Electron%i_Eta",idx);
      Electron_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }

  nMuons_        = fs->make<TH1F>("nMuons",       "nMuons",         7, -0.5,   6.5);
  nElectrons_    = fs->make<TH1F>("nElectrons",   "nElectrons",     7, -0.5,   6.5);
  nLeptons_      = fs->make<TH1F>("nLeptons",     "nLeptons",      13, -0.5,  12.5);
  LeptonPt_      = fs->make<TH1F>("LeptonPt",     "Lepton Pt",     60,   0.,  600.);
  LeptonEta_     = fs->make<TH1F>("LeptonEta",    "Lepton Eta",    60,   -3,    3.);
  nVetoLeptons_  = fs->make<TH1F>("nVetoLeptons", "nVetoLeptons",  13, -0.5,  12.5);

  MT_          = fs->make<TH1F>("MT",      "MT",            40, 0., 2000.);
  METfrac_     = fs->make<TH1F>("METfrac", "MET fraction",  40, 0.,    1.);

  mT_       = fs->make<TH1F>("mT",      "mT",      40, 0., 400.);
  mlb_      = fs->make<TH1F>("mlb",     "mlb",     40, 0., 400.);
  mLepTop_  = fs->make<TH1F>("mLepTop", "mLepTop", 40, 0., 400.);

  YMET_     = fs->make<TH1F>("YMET", "YMET", 50, 0., 25);
  METSig_   = fs->make<TH1F>("METSig", "METSig", 50, 0., 25);
  LepPt_    = fs->make<TH1F>("LepPt",      "Lepton Pt",  50,   0., 1000.);
  LepPtSig_ = fs->make<TH1F>("LepPtSig", "LepPtSig", 50, 0., 25);

  //-------------------------------------------------
  // Btagging
  //-------------------------------------------------

  TCHE_  = fs->make<TH1F>("TCHE",  "TCHE",   80, -20, 20);
  TCHP_  = fs->make<TH1F>("TCHP",  "TCHP",   80, -20, 20);
  SSVHE_ = fs->make<TH1F>("SSVHE", "SSVHE", 120,  -2, 10);
  SSVHP_ = fs->make<TH1F>("SSVHP", "SSVHP", 120,  -2, 10);

  nBjets_noWgt_    = fs->make<TH1F>("nBjets_noWgt",   "nBjets_noWgt",   4, -0.5, 3.5);
  nBjets_noWgt_2_  = fs->make<TH1F>("nBjets_noWgt_2", "nBjets_noWgt_2", 8, -0.5, 7.5);
  nBjets_          = fs->make<TH1F>("nBjets",          "nBjets",        4, -0.5, 3.5);
  nBjets_2_        = fs->make<TH1F>("nBjets_2",       "nBjets_2",       8, -0.5, 7.5);

  for(int idx=0; idx<4; ++idx)
    {
      char histname[20];
      sprintf(histname,"Bjet%i_Et",idx);
      Bjet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));

      char histname2[20];
      sprintf(histname2,"Bjet%i_Eta",idx);
      Bjet_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }

  Bjets_Et_  = fs->make<TH1F>("Bjets_Et",  "Bjets_Et",  90,   0.,   900.);
  Bjets_Eta_ = fs->make<TH1F>("Bjets_Eta", "Bjets_Eta", 60,  -3.,     3.);

  //-------------------------------------------------
  // MET, Lepton pt vs. HT
  //-------------------------------------------------

  HT_MET_   = fs->make<TH2F>("HT_MET",   "HT vs. MET",   40, 0., 2000., 50, 0., 1000.);
  HT_LepPt_ = fs->make<TH2F>("HT_LepPt", "HT vs. LepPt", 40, 0., 2000., 25, 0.,   50.);

  //-------------------------------------------------------
  // YMET, MET significnace, Lepton pt significance vs HT
  //-------------------------------------------------------

  // NP: Original binning for HT_YMET: 0-2000 80 bins, 0-20 80

  HT_YMET_         = fs->make<TH2F>("HT_YMET",         "HT vs. YMET",     40, 0., 2000., 50,   0.,   25.);
  HT_YMET_noWgt_   = fs->make<TH2F>("HT_YMET_noWgt",   "HT vs. YMET",     40, 0., 2000., 50,   0.,   25.);

  HT_METSig_       = fs->make<TH2F>("HT_METSig",       "HT vs. METSig",   40, 0., 2000., 50,   0.,   25.);
  HT_METSig_noWgt_ = fs->make<TH2F>("HT_METSig_noWgt", "HT vs. METSig",   40, 0., 2000., 50,   0.,   25.);
  
  METSig_YMET_     = fs->make<TH2F>("METSig_YMET",     "METSig_YMET",     40, 0.,   25., 50,   0.,   25.);

  HT_LepPtSig_     = fs->make<TH2F>("HT_LepPtSig",     "HT vs. LepPtSig", 40, 0., 2000., 50,   0.,   25.);

  HT_LepPtSig_smeared_ = fs->make<TH2F>("HT_LepPtSig_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  LepPtSig_smearFactor_ = fs->make<TH1F>("LepPtSig_smearFactor","LepPtSig_smearFactor", 100, 0., 10. );
  HT_METSig_unweighted_ = fs->make<TH2F>("HT_METSig_unweighted","HT vs. METSig unweighted", 80, 0., 2000., 80, 0., 20. );

  HT_METSig_PT20_MET20_      = fs->make<TH2F>("HT_METSig_PT20_MET20","HT vs. METSig", 80, 0., 2000., 80, 0., 20.);
  HT_METSig_PT20_MET40_       = fs->make<TH2F>("HT_METSig_PT20_MET40","HT vs. METSig", 80, 0., 2000., 80, 0., 20.);

  HT_METSig_PT20_MET60_      = fs->make<TH2F>("HT_METSig_PT20_MET60","HT vs. METSig", 80, 0., 2000., 80, 0., 20.);
  HT_METSig_PT40_MET60_       = fs->make<TH2F>("HT_METSig_PT40_MET60","HT vs. METSig", 80, 0., 2000., 80, 0., 20.);
  HT_METSig_PT60_MET60_       = fs->make<TH2F>("HT_METSig_PT60_MET60","HT vs. METSig", 80, 0., 2000., 80, 0., 20.);
			     
  HT_LepPtSig_PT20_MET20_       = fs->make<TH2F>("HT_LepPtSig_PT20_MET20","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET40_       = fs->make<TH2F>("HT_LepPtSig_PT20_MET40","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET60_       = fs->make<TH2F>("HT_LepPtSig_PT20_MET60","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
		
  HT_LepPtSig_PT20_MET20_smeared_ = fs->make<TH2F>("HT_LepPtSig_PT20_MET20_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET40_smeared_ = fs->make<TH2F>("HT_LepPtSig_PT20_MET40_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET60_smeared_ = fs->make<TH2F>("HT_LepPtSig_PT20_MET60_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
	     
  HT_significance_PT20_MET20_ = fs->make<TH2F>("HT_significance_PT20_MET20","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT20_MET40_ = fs->make<TH2F>("HT_significance_PT20_MET40","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT20_MET60_ = fs->make<TH2F>("HT_significance_PT20_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT40_MET60_ = fs->make<TH2F>("HT_significance_PT40_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT60_MET60_ = fs->make<TH2F>("HT_significance_PT60_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);

  //-------------------------------------------------
  // mjj variables
  //-------------------------------------------------

  minj3_ = fs->make<TH1F>("minj3", "minj3", 100, 0., 1000.);

  minj3_nJets_ = fs->make<TH2F>("minj3_nJets", "minj3 vs. nJets", 100, 0., 1000.,   16, -0.5,  15.5);
  HT_minj3_    = fs->make<TH2F>("HT_minj3",    "HT vs. minj3",     50, 0., 2000., 100.,   0., 1000.);

  //-------------------------------------------------
  // Others
  //-------------------------------------------------

  HT_mT_           = fs->make<TH2F>("HT_mT",          "HT vs. mT",      50, 0., 2000., 60,    0.,   600.);
  HT_nJets_        = fs->make<TH2F>("HT_nJets",       "HT vs. nJets",   50, 0., 2000., 16,  -0.5,   15.5);
  mT_nJets_        = fs->make<TH2F>("mT_nJets" ,      "mT vs. nJets",   60, 0.,  600., 16,  -0.5,   15.5);
  MET_nJets_       = fs->make<TH2F>("MET_nJets",      "MET vs. nJets",  50, 0., 1000., 16,  -0.5,   15.5);
  YMET_nJets_      = fs->make<TH2F>("YMET_nJets",     "YMET vs. nJets", 25, 0.,   25., 16,  -0.5,   15.5);
 
  mlb_YMET_        = fs->make<TH2F>("mlb_YMET",       "YMET vs. mlb",   60, 0., 600.,  50,    0,      25);
 
  HT_mLepTop_      = fs->make<TH2F>("HT_mLepTop",     "mLepTop vs. HT", 50, 0., 2000., 60,    0.,   600.);
  HT_mlb_          = fs->make<TH2F>("HT_mlb",         "mlb vs. HT",     50, 0., 2000., 60,    0.,   600.);
  
  mLepTop_nJets_   = fs->make<TH2F>("mLepTop_nJets",  "mLepTop vs. nJets", 60, 0., 600.,  16,  -0.5,   15.5);
  mlb_nJets_       = fs->make<TH2F>("mlb_nJets",      "mlb vs. nJets",     60, 0., 600.,  16,  -0.5,   15.5);

  mlb_YMET_nJets_  = fs->make<TH3F>("mlb_YMET_nJets", "mlb_YMET_nJets", 60, 0., 600.,  50,     0,     25,  16, -0.5,  15.5);
  
  YMET_nJets_0_    = fs->make<TH2F>("YMET_nJets_0",   "YMET vs. nJets", 50, 0.,  25.,  16,  -0.5,   15.5);
  YMET_nJets_100_  = fs->make<TH2F>("YMET_nJets_100", "YMET vs. nJets", 50, 0.,  25.,  16,  -0.5,   15.5);
  YMET_nJets_200_  = fs->make<TH2F>("YMET_nJets_200", "YMET vs. nJets", 50, 0.,  25.,  16,  -0.5,   15.5);

  mlb_nJets_0_     = fs->make<TH2F>("mlb_nJets_0",    "mlb vs. HT_0",   60, 0., 600.,  16,  -0.5,   15.5);
  mlb_nJets_5_     = fs->make<TH2F>("mlb_nJets_5",    "mlb vs. HT_5",   60, 0., 600.,  16,  -0.5,   15.5);
  mlb_nJets_10_    = fs->make<TH2F>("mlb_nJets_10",   "mlb vs. HT_10",  60, 0., 600.,  16,  -0.5,   15.5);
  mlb_nJets_15_    = fs->make<TH2F>("mlb_nJets_15",   "mlb vs. HT_15",  60, 0., 600.,  16,  -0.5,   15.5);
  mlb_nJets_20_    = fs->make<TH2F>("mlb_nJets_20",   "mlb vs. HT_20",  60, 0., 600.,  16,  -0.5,   15.5);

  //-------------------------------------------------
  // Only when TTJets is set to true in cfg file
  //-------------------------------------------------
  
  pv_             = fs->make<TH1F>("pv",             "pv",                  50, 0., 1000);
  smearedPv_      = fs->make<TH1F>("smearedPv",      "smearedPv",           50, 0., 1000);

  pv_nJets_       = fs->make<TH2F>("pv_nJets",       "nJets vs. pv",        50, 0., 1000,   16,  -0.5, 15.5);
  mlv_nJets_gen_  = fs->make<TH2F>("mlv_nJets_gen",  "mlv vs. nJets",       60, 0., 600.,   16,  -0.5, 15.5);
  mlv_nJets_reco_ = fs->make<TH2F>("mlv_nJets_reco", "mlv vs. nJets",       60, 0., 600.,   16,  -0.5, 15.5);

  pv_MET_         = fs->make<TH2F>("pv_MET",         "MET vs.pv",           50, 0., 1000,   50,   0., 1000);
  smearedPv_MET_  = fs->make<TH2F>("smearedPv_MET",  "MET vs. smeared pv",  50, 0., 1000,   50,   0., 1000);

  NuPt_nJets_     = fs->make<TH2F>("NuPt_nJets",     "nJets vs.NuPt",       50, 0., 1000,   16, -0.5, 1000);
  fakeMET_nJets_  = fs->make<TH2F>("fakeMET_nJets",  "nJets vs.fakeMET",    50, 0., 1000,   16, -0.5, 1000);

  HT_HadMET_         = fs->make<TH2F>("HT_HadMET",         "hadronic MET vs. HT",   40., 0.,2000,   50, -250, 250);
  HT_HadMET_2_       = fs->make<TH2F>("HT_HadMET_2",       "hadronic MET vs. HT",   40., 0.,2000,   50, -250, 250);
 
  HT_fakeMET_        = fs->make<TH2F>("HT_fakeMET",        "fake MET vs. HT",   40., 0.,2000,   50, -250, 250);
  HT_fakeMET_2_      = fs->make<TH2F>("HT_fakeMET_2",      "fake MET vs. HT",   40., 0.,2000,   50, -250, 250);

  HT_fakeMET_        = fs->make<TH2F>("HT_fakeMET",        "fake MET vs. HT",   40., 0.,2000,   50, -250, 250);
  HT_fakeMET_2_      = fs->make<TH2F>("HT_fakeMET_2",      "fake MET vs. HT",   40., 0.,2000,   50, -250, 250);

  HT_NuPt_           = fs->make<TH2F>("HT_NuPt",           "NuPt vs. HT",       40., 0.,2000,   50,   0., 1000);

  HT_NuPtSig_        = fs->make<TH2F>("HT_NuPtSig",        "HT vs. NuPtSig",    40, 0., 2000., 50,   0.,   25.);
  HT_fakeMETSig_     = fs->make<TH2F>("HT_fakeMETSig",     "HT vs. fakeMETSig", 40, 0., 2000., 50,   0.,   25.);

  NuPt_fakeMET_0HT125_   = fs->make<TH2F>("NuPt_fakeMET_0HT125",   "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_fakeMET_125HT250_ = fs->make<TH2F>("NuPt_fakeMET_125HT250", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_fakeMET_250HT375_ = fs->make<TH2F>("NuPt_fakeMET_250HT375", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_fakeMET_375HT500_ = fs->make<TH2F>("NuPt_fakeMET_375HT500", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_fakeMET_500HT650_ = fs->make<TH2F>("NuPt_fakeMET_500HT650", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_fakeMET_650HT800_ = fs->make<TH2F>("NuPt_fakeMET_650HT800", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_fakeMET_800HT950_ = fs->make<TH2F>("NuPt_fakeMET_800HT950", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);

  NuPt_fakeMET_ = fs->make<TH2F>("NuPt_fakeMET", "fakeMET vs. NuPt", 50, 0., 1000, 50, 0., 1000.);
  NuPt_MET_     = fs->make<TH2F>("NuPt_MET",     "MET vs. NuPt",     50, 0., 1000, 50, 0., 1000.);
  fakeMET_MET_  = fs->make<TH2F>("fakeMET_MET",  "fakeMET vs. MET",  50, 0., 1000, 50, 0., 1000.);

  HT_METNuPtRatio_      = fs->make<TH2F>("HT_METNuPtRatio",      "METNuPtRatio vs. HT",   40., 0.,2000,   80,   0.,   4); 
  HT_METHadMETRatio_    = fs->make<TH2F>("HT_METHadMETRatio",    "METHadMETRatio vs. HT", 40., 0.,2000,   80,   0.,   4);
  HT_METfakeMETRatio_   = fs->make<TH2F>("HT_METfakeMETRatio",   "METfakeRatio vs. HT",   40., 0.,2000,   80,   0.,   4);
  HT_NuPtfakeMETRatio_  = fs->make<TH2F>("HT_NuPtfakeMETRatio",  "NuPtfakeRatio vs. HT",  40., 0.,2000,   20,   0.,  10);
  HT_NuPtfakeMETRatio2_ = fs->make<TH2F>("HT_NuPtfakeMETRatio2", "NuPtfakeRatio vs. HT",  40., 0.,2000,   40,   0.,  10);
  HT_NuPtfakeMETRatio3_ = fs->make<TH2F>("HT_NuPtfakeMETRatio3", "NuPtfakeRatio vs. HT",  40., 0.,2000,   40,   0.,  10); 
  
  HadMET_400HT500_  = fs->make<TH1F>("HadMET_400HT500_",  "hadronic MET", 50, -250, 250);
  HadMET_500HT600_  = fs->make<TH1F>("HadMET_500HT600_",  "hadronic MET", 50, -250, 250);
  HadMET_600HT700_  = fs->make<TH1F>("HadMET_600HT700_",  "hadronic MET", 50, -250, 250);
  HadMET_700HT800_  = fs->make<TH1F>("HadMET_700HT800_",  "hadronic MET", 50, -250, 250);
  HadMET_800HT900_  = fs->make<TH1F>("HadMET_800HT900_",  "hadronic MET", 50, -250, 250);
  HadMET_900HT1000_ = fs->make<TH1F>("HadMET_900HT1000_", "hadronic MET", 50, -250, 250);
  HadMET_1000HTInf_ = fs->make<TH1F>("HadMET_1000HTInf_", "hadronic MET", 50, -250, 250);

  HadMET_400HT500_2_  = fs->make<TH1F>("HadMET_400HT500_2_",  "hadronic MET", 50, -250, 250);
  HadMET_500HT600_2_  = fs->make<TH1F>("HadMET_500HT600_2_",  "hadronic MET", 50, -250, 250);
  HadMET_600HT700_2_  = fs->make<TH1F>("HadMET_600HT700_2_",  "hadronic MET", 50, -250, 250);
  HadMET_700HT800_2_  = fs->make<TH1F>("HadMET_700HT800_2_",  "hadronic MET", 50, -250, 250);
  HadMET_800HT900_2_  = fs->make<TH1F>("HadMET_800HT900_2_",  "hadronic MET", 50, -250, 250);
  HadMET_900HT1000_2_ = fs->make<TH1F>("HadMET_900HT1000_2_", "hadronic MET", 50, -250, 250);
  HadMET_1000HTInf_2_ = fs->make<TH1F>("HadMET_1000HTInf_2_", "hadronic MET", 50, -250, 250);

  NuPt_400HT500_  = fs->make<TH1F>("NuPt_400HT500_",  "pT nu", 50, -250, 250);
  NuPt_500HT600_  = fs->make<TH1F>("NuPt_500HT600_",  "pT nu", 50, -250, 250);
  NuPt_600HT700_  = fs->make<TH1F>("NuPt_600HT700_",  "pT nu", 50, -250, 250);
  NuPt_700HT800_  = fs->make<TH1F>("NuPt_700HT800_",  "pT nu", 50, -250, 250);
  NuPt_800HT900_  = fs->make<TH1F>("NuPt_800HT900_",  "pT nu", 50, -250, 250);
  NuPt_900HT1000_ = fs->make<TH1F>("NuPt_900HT1000_", "pT nu", 50, -250, 250);
  NuPt_1000HTInf_ = fs->make<TH1F>("NuPt_1000HTInf_", "pT nu", 50, -250, 250);

  //-------------------------------------------------
  // Only when TTJetsHyp is set to true in cfg file
  //-------------------------------------------------

  hadWMass_      = fs->make<TH1F>("hadWMass",        "hadWMass",     400,  60., 100);
  hadTopMass_    = fs->make<TH1F>("hadTopMass",      "hadTopMass",   400, 100., 300);
  chi2_          = fs->make<TH1F>("chi2",            "chi2",         100,   0.,  1.);

  //-------------------------------------------------
  // ABCD method
  //-------------------------------------------------
  
  MET_A_ = fs->make<TH1F>("MET_A",   "MET_A",   50,   0.,  1000.);
  MET_B_ = fs->make<TH1F>("MET_B",   "MET_B",   50,   0.,  1000.);
  MET_C_ = fs->make<TH1F>("MET_C",   "MET_C",   50,   0.,  1000.);
  MET_D_ = fs->make<TH1F>("MET_D",   "MET_D",   50,   0.,  1000.);

  Lep_Pt_A_ = fs->make<TH1F>("Lep_Pt_A", "Lep_Pt_A", 60, 0., 600);
  Lep_Pt_B_ = fs->make<TH1F>("Lep_Pt_B", "Lep_Pt_B", 60, 0., 600);
  Lep_Pt_C_ = fs->make<TH1F>("Lep_Pt_C", "Lep_Pt_C", 60, 0., 600);
  Lep_Pt_D_ = fs->make<TH1F>("Lep_Pt_D", "Lep_Pt_D", 60, 0., 600);

  Jets_Et_A_ = fs->make<TH1F>("Jets_Et_A", "Jets_Et_A", 90, 0., 900);
  Jets_Et_B_ = fs->make<TH1F>("Jets_Et_B", "Jets_Et_B", 90, 0., 900);
  Jets_Et_C_ = fs->make<TH1F>("Jets_Et_C", "Jets_Et_C", 90, 0., 900);
  Jets_Et_D_ = fs->make<TH1F>("Jets_Et_D", "Jets_Et_D", 90, 0., 900);

  Bjets_Et_A_ = fs->make<TH1F>("Bjets_Et_A", "Bjets_Et_A", 90, 0., 900);
  Bjets_Et_B_ = fs->make<TH1F>("Bjets_Et_B", "Bjets_Et_B", 90, 0., 900);
  Bjets_Et_C_ = fs->make<TH1F>("Bjets_Et_C", "Bjets_Et_C", 90, 0., 900);
  Bjets_Et_D_ = fs->make<TH1F>("Bjets_Et_D", "Bjets_Et_D", 90, 0., 900);

  Bjets_Et_Weights_A_ = fs->make<TH1F>("Bjets_Et_Weights_A", "Bjets_Et_Weights_A", 90, 0., 900);
  Bjets_Et_Weights_B_ = fs->make<TH1F>("Bjets_Et_Weights_B", "Bjets_Et_Weights_B", 90, 0., 900);
  Bjets_Et_Weights_C_ = fs->make<TH1F>("Bjets_Et_Weights_C", "Bjets_Et_Weights_C", 90, 0., 900);
  Bjets_Et_Weights_D_ = fs->make<TH1F>("Bjets_Et_Weights_D", "Bjets_Et_Weights_D", 90, 0., 900);

  Bjets_Et_Weights_A_670_ = fs->make<TH1F>("Bjets_Et_Weights_A_670", "Bjets_Et_Weights_A_670", 90, 0., 900);
  Bjets_Et_Weights_B_670_ = fs->make<TH1F>("Bjets_Et_Weights_B_670", "Bjets_Et_Weights_B_670", 90, 0., 900);
  Bjets_Et_Weights_C_670_ = fs->make<TH1F>("Bjets_Et_Weights_C_670", "Bjets_Et_Weights_C_670", 90, 0., 900);
  Bjets_Et_Weights_D_670_ = fs->make<TH1F>("Bjets_Et_Weights_D_670", "Bjets_Et_Weights_D_670", 90, 0., 900);

  Bjets_Eta_Weights_A_ = fs->make<TH1F>("Bjets_Eta_Weights_A", "Bjets_Eta_Weights_A", 60, -3., 3);
  Bjets_Eta_Weights_B_ = fs->make<TH1F>("Bjets_Eta_Weights_B", "Bjets_Eta_Weights_B", 60, -3., 3);
  Bjets_Eta_Weights_C_ = fs->make<TH1F>("Bjets_Eta_Weights_C", "Bjets_Eta_Weights_C", 60, -3., 3);
  Bjets_Eta_Weights_D_ = fs->make<TH1F>("Bjets_Eta_Weights_D", "Bjets_Eta_Weights_D", 60, -3., 3);

  Bjets_Eta_Weights_A_670_ = fs->make<TH1F>("Bjets_Eta_Weights_A_670", "Bjets_Eta_Weights_A_670", 90, 0., 900);
  Bjets_Eta_Weights_B_670_ = fs->make<TH1F>("Bjets_Eta_Weights_B_670", "Bjets_Eta_Weights_B_670", 90, 0., 900);
  Bjets_Eta_Weights_C_670_ = fs->make<TH1F>("Bjets_Eta_Weights_C_670", "Bjets_Eta_Weights_C_670", 90, 0., 900);
  Bjets_Eta_Weights_D_670_ = fs->make<TH1F>("Bjets_Eta_Weights_D_670", "Bjets_Eta_Weights_D_670", 90, 0., 900);

  nJets_A_ = fs->make<TH1F>("nJets_A",    "nJets_A",    16 , -0.5,  15.5);
  nJets_B_ = fs->make<TH1F>("nJets_B",    "nJets_B",    16 , -0.5,  15.5);
  nJets_C_ = fs->make<TH1F>("nJets_C",    "nJets_C",    16 , -0.5,  15.5);
  nJets_D_ = fs->make<TH1F>("nJets_D",    "nJets_D",    16 , -0.5,  15.5);

  for(int idx=0; idx<8; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et_A",idx);
      Jet_Et_A_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));

      char histname2[20];
      sprintf(histname2,"Jet%i_Et_B",idx);
      Jet_Et_B_.push_back(fs->make<TH1F>(histname2,histname2, 90, 0., 900.));

      char histname3[20];
      sprintf(histname3,"Jet%i_Et_C",idx);
      Jet_Et_C_.push_back(fs->make<TH1F>(histname3,histname3, 90, 0., 900.));

      char histname4[20];
      sprintf(histname4,"Jet%i_Et_D",idx);
      Jet_Et_D_.push_back(fs->make<TH1F>(histname4,histname4, 90, 0., 900.));
    }

  for(int bdx=0; bdx<4; ++bdx)
    {
      char histname[20];
      sprintf(histname,"Bjet%i_Et_A",bdx);
      Bjet_Et_A_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));

      char histname2[20];
      sprintf(histname2,"Bjet%i_Et_B",bdx);
      Bjet_Et_B_.push_back(fs->make<TH1F>(histname2,histname2, 90, 0., 900.));

      char histname3[20];
      sprintf(histname3,"Bjet%i_Et_C",bdx);
      Bjet_Et_C_.push_back(fs->make<TH1F>(histname3,histname3, 90, 0., 900.));

      char histname4[20];
      sprintf(histname4,"Bjet%i_Et_D",bdx);
      Bjet_Et_D_.push_back(fs->make<TH1F>(histname4,histname4, 90, 0., 900.));
    }

}

CorrelationAnalyzer::~CorrelationAnalyzer()
{
}

void
CorrelationAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  edm::Handle<SUSYEvent> SUSYEvt;
  evt.getByLabel(SUSYEvent_, SUSYEvt);

  if(SUSYEvt->nJets() < nJetsCut_[0]  || SUSYEvt->nJets() > nJetsCut_[1]) return;
  if(SUSYEvt->HT()    < HTCut_[0]     || SUSYEvt->HT()    >  HTCut_[1]   ) return;
  if(SUSYEvt->MET()   < METCut_[0]    || SUSYEvt->MET()   >  METCut_[1]  ) return;
  if(SUSYEvt->YMET()  < YMETCut_[0]   || SUSYEvt->YMET()  >  YMETCut_[1] ) return;

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
  edm::Handle<std::vector<pat::Muon> > vetoMuons;
  evt.getByLabel(vetoMuons_, vetoMuons);
  edm::Handle<std::vector<pat::Electron> > vetoElectrons;
  evt.getByLabel(vetoElectrons_, vetoElectrons);
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);

  //-------------------------------------------------
  // Event weighting
  //----------------------f--------------------------

  //int run   = evt.id().run();
  //int lumi  = evt.id().luminosityBlock();
  //int event = evt.id().event();

  // declare and initialize different weights
  double weight=1;
  double weightPU=1;
  double weightRA2=1;
  double weightBtagEff=1;
  double weightTrigger=1;

  if(useEventWgt_)
    {
      // RA2 weight
      edm::Handle<double> RA2WeightHandle;
      evt.getByLabel(RA2Weight_, RA2WeightHandle);
      weightRA2=*RA2WeightHandle;
      
      // PU weight
      edm::Handle<double> PUWeightHandle;
      evt.getByLabel(PUWeight_, PUWeightHandle);
      weightPU=(*PUWeightHandle);
      
      // Btag efficiency weights
      if(useBtagEventWgt_ ||useInclusiveBtagEventWgt_)
	{
	  // Btag weights
	  edm::Handle<std::vector<double> > BtagEventWeightsHandle;
	  evt.getByLabel(BtagEventWeights_, BtagEventWeightsHandle);
	  
	  btagWeights_noWgt_->Fill(0.,(*BtagEventWeightsHandle)[0]);
	  btagWeights_noWgt_->Fill(1, (*BtagEventWeightsHandle)[1]);
	  btagWeights_noWgt_->Fill(2, (*BtagEventWeightsHandle)[2]);
	  btagWeights_noWgt_->Fill(3, (*BtagEventWeightsHandle)[3]);
	  
	  btagWeights_PUWgt_->Fill(0.,(*BtagEventWeightsHandle)[0]*weight);
	  btagWeights_PUWgt_->Fill(1, (*BtagEventWeightsHandle)[1]*weight);
	  btagWeights_PUWgt_->Fill(2, (*BtagEventWeightsHandle)[2]*weight);
	  btagWeights_PUWgt_->Fill(3, (*BtagEventWeightsHandle)[3]*weight); 

	  if(useBtagEventWgt_)
	    {
	      weightBtagEff=(*BtagEventWeightsHandle)[btagBin_];
	      
	      //std::cout << "SUSAnalyzer.cc (*BtagEventWeightsHandle)[0]): " << (*BtagEventWeightsHandle)[0] <<std::endl;
	      //std::cout << "SUSAnalyzer.cc (*BtagEventWeightsHandle)[1]): " << (*BtagEventWeightsHandle)[1] <<std::endl;
	      //std::cout << "SUSAnalyzer.cc (*BtagEventWeightsHandle)[2]): " << (*BtagEventWeightsHandle)[2] <<std::endl;
	      //std::cout << "SUSAnalyzer.cc (*BtagEventWeightsHandle)[3]): " << (*BtagEventWeightsHandle)[3] <<std::endl;
	    }
         
	  if(useInclusiveBtagEventWgt_)
	    {
	      weightBtagEff=0;
	      //for(int bwx=inclusiveBtagBin_; bwx<4; ++bwx)
	      //{
	      //  weightBtagEff=weightBtagEff+(*BtagEventWeightsHandle)[bwx];
	      //}
	      weightBtagEff=(*BtagEventWeightsHandle)[1]+(*BtagEventWeightsHandle)[2];
	    }
	}

      weight=weightRA2*weightPU*weightBtagEff;

      // number of PU interactions only in MC available, therefore filled in this loop
      edm::Handle<edm::View<PileupSummaryInfo> > PUInfoHandle;
      evt.getByLabel(PUInfo_, PUInfoHandle);

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)
	{ 
	  if (iterPU->getBunchCrossing()==0)
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	}

      nPU_noWgt_->Fill(nvtx);
      nPU_->Fill(nvtx,weightPU);
    }

  if(useTriggerEvtWgt_)
    {
      edm::Handle<double> TriggerWeightHandle;
      evt.getByLabel(TriggerWeight_, TriggerWeightHandle);
      weightTrigger=(*TriggerWeightHandle);
      weight=weight*weightTrigger;
    }

  Weight_->Fill(weight);
  WeightPU_->Fill(weightPU);
  WeightRA2_->Fill(weightRA2);
  WeightBtagEff_->Fill(weightBtagEff);
  WeightTrigger_->Fill(weightTrigger);

  // number of primary vertices
  nPV_noWgt_->Fill(PVSrc->size());
  nPV_->Fill(PVSrc->size(),weightPU);

  NumEvents_->Fill(0.5, weight);

  //-------------------------------------------------
  // Basic variables
  //-------------------------------------------------

  //std::cout << "Test2" << std::endl;

  if(met->size()==0) return;

  double HT=0;
  int nJets50 =0;
  double DeltaRecoGenJetPxSum=0;
  double DeltaRecoGenJetPySum=0;
  double AbsDeltaRecoGenJetPtSum=0;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      if(i<8)
	{
	  Jet_Et_[i] ->Fill((*jets)[i].et(),  weight);
	}
      Jets_Et_  ->Fill((*jets)[i].et(),  weight);
      Jets_Eta_ ->Fill((*jets)[i].eta(), weight);
      HT=HT+(*jets)[i].et();
      if((*jets)[i].pt()>50) nJets50=nJets50+1; 

	      if((*jets)[i].genJet())
		{
		  DeltaRecoGenJetPt_ ->Fill((*jets)[i].pt()-(*jets)[i].genJet()->pt(), weight);

		  DeltaRecoGenJetPxSum=DeltaRecoGenJetPxSum+((*jets)[i].px()-(*jets)[i].genJet()->px());
		  DeltaRecoGenJetPySum=DeltaRecoGenJetPySum+((*jets)[i].py()-(*jets)[i].genJet()->py());

		  AbsDeltaRecoGenJetPtSum=AbsDeltaRecoGenJetPtSum+abs((*jets)[i].pt()-(*jets)[i].genJet()->pt());
		}
    }
  double DeltaRecoGenJetPtSum = sqrt(pow(DeltaRecoGenJetPxSum,2) + pow(DeltaRecoGenJetPySum,2));
  
  MET_                     ->Fill((*met)[0].et(),          weight);
  HT_                      ->Fill(HT,                      weight);
  nJets_                   ->Fill(jets->size(),            weight);
  nJets50_                 ->Fill(nJets50,                weight);
  DeltaRecoGenJetPtSum_    ->Fill(DeltaRecoGenJetPtSum,    weight);
  AbsDeltaRecoGenJetPtSum_ ->Fill(AbsDeltaRecoGenJetPtSum, weight);

  DeltaRecoGenJetPtSum_MET_      ->Fill(DeltaRecoGenJetPtSum,    (*met)[0].et(), weight);
  AbsDeltaRecoGenJetPtSum_MET_   ->Fill(AbsDeltaRecoGenJetPtSum, (*met)[0].et(), weight);
  DeltaRecoGenJetPtSum_nJets_    ->Fill(DeltaRecoGenJetPtSum,    jets->size(),   weight);
  AbsDeltaRecoGenJetPtSum_nJets_ ->Fill(AbsDeltaRecoGenJetPtSum, jets->size(),   weight);

  if((*met)[0].genMET())
    {
      std::cout << (*met)[0].genMET()->et() << std::endl;
      double smearedGenMET = sqrt(pow((*met)[0].genMET()->px()+DeltaRecoGenJetPxSum,2)+pow((*met)[0].genMET()->py()+DeltaRecoGenJetPxSum,2));
      smearedGenMET_ ->Fill(smearedGenMET, weight);
    }

  int nLeptons=0;
  int nMuons=0;
  int nElectrons=0;
  double LepHT=0;

  //std::cout << "Test3" << std::endl;

  // loop over muons
  for(int i=0; i<(int)muons->size(); ++i)
    {
      if(i<2)
	{
	  Muon_Pt_[i] ->Fill((*muons)[i].pt(),  weight);
	  Muon_Eta_[i]->Fill((*muons)[i].eta(), weight);
	}
      nMuons=nMuons+1;
      nLeptons=nLeptons+1;
      LepHT=LepHT+(*muons)[i].pt();
      LeptonPt_->Fill((*muons)[i].pt());
      LeptonPt_->Fill((*muons)[i].eta());
    }

  //std::cout << "Test4" << std::endl;

  // loop over electrons
  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<2)
	{
	  Electron_Pt_[i] ->Fill((*electrons)[i].pt(),  weight);
	  Electron_Eta_[i]->Fill((*electrons)[i].eta(), weight);
	}
      nElectrons=nElectrons+1;
      nLeptons=nLeptons+1;
      LepHT=LepHT+(*electrons)[i].pt();
      LeptonPt_->Fill((*electrons)[i].pt());
      LeptonPt_->Fill((*electrons)[i].eta());
    }

  nMuons_       ->Fill(nMuons,     weight);
  nElectrons_   ->Fill(nElectrons, weight);
  nLeptons_     ->Fill(nLeptons,   weight);
  nVetoLeptons_ ->Fill(vetoMuons->size()+vetoElectrons->size(), weight);

  //std::cout << "Test5" << std::endl;

  // MT
  double MT=LepHT+HT+(*met)[0].et();
  MT_      ->Fill(MT, weight);
  METfrac_ ->Fill((*met)[0].et()/MT, weight);
  
  const reco::LeafCandidate * singleLepton = 0;

  // mT
  double LeptonPt = 0;
  double mT=0;
  double mLepTop=0;
  double mlb=0;
  if(muons->size()>=1)
    {
      LeptonPt = (*muons)[0].et();
      singleLepton = &(*muons)[0];
      
      mT=sqrt(2*(((*met)[0].et())*((*muons)[0].et())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
      reco::Particle::LorentzVector LepP4=(*muons)[0].p4();
      reco::Particle::LorentzVector METP4=(*met)[0].p4();
      double dRLepBjetMin=9;
      
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	  double dRLepBjet=abs(deltaR((*bjets)[bdx].eta(),(*bjets)[bdx].phi(),(*muons)[0].eta(),(*muons)[0].phi()));
	  reco::Particle::LorentzVector BjetP4=(*bjets)[bdx].p4();
	  if(dRLepBjet < dRLepBjetMin)
	   {
	     dRLepBjetMin=dRLepBjet;
	     mlb=sqrt((LepP4+BjetP4).Dot(LepP4+BjetP4));
	     mLepTop=sqrt((METP4+LepP4+BjetP4).Dot(METP4+LepP4+BjetP4));
	   }
	  mlb_    ->Fill(mlb,     weight);
	  mLepTop_->Fill(mLepTop, weight);
	}
      
      mT_ ->Fill(mT, weight); 
    }  
  if(electrons->size()==1)
    {
      if((*electrons)[0].et()<LeptonPt)
	{
	  singleLepton = &(*electrons)[0];
	  
	  mT=sqrt(2*(((*met)[0].et())*((*electrons)[0].et())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
	  reco::Particle::LorentzVector LepP4=(*electrons)[0].p4();
	  reco::Particle::LorentzVector METP4=(*met)[0].p4();
	  double dRLepBjetMin=9;
	  
	  for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	    {
	      double dRLepBjet=abs(deltaR((*bjets)[bdx].eta(),(*bjets)[bdx].phi(),(*electrons)[0].eta(),(*electrons)[0].phi()));
	      reco::Particle::LorentzVector BjetP4=(*bjets)[bdx].p4();
	      if(dRLepBjet < dRLepBjetMin)
		{
		  dRLepBjetMin=dRLepBjet;
		  mlb=sqrt((LepP4+BjetP4).Dot(LepP4+BjetP4));
		  mLepTop=sqrt((METP4+LepP4+BjetP4).Dot(METP4+LepP4+BjetP4));
		}
	      mlb_    ->Fill(mlb,     weight);
	      mLepTop_->Fill(mLepTop, weight);
	    }
	  
	  mT_ ->Fill(mT, weight);
	}
    }
  
  // YMET
  double YMET=((*met)[0].et())/(sqrt(HT));  
  YMET_->Fill(YMET, weight);

  // MET significance
  double sigmaX2 = (*met)[0].getSignificanceMatrix()(0,0);
  double sigmaY2 = (*met)[0].getSignificanceMatrix()(1,1);
  double METSig  = 0;
  if(sigmaX2<1.e10 && sigmaY2<1.e10) METSig = (*met)[0].significance();
  // Use the sqrt of the significance
  if (METSig > 0.) METSig = sqrt(METSig);
  METSig_->Fill(METSig, weight);

  // Lepton pt significance
  if(singleLepton != 0)
    {
      LepPt_   ->Fill(singleLepton->et());
      LepPtSig_->Fill(singleLepton->et()/sqrt(HT), weight);
    }

  //-------------------------------------------------
  // Btagging
  //-------------------------------------------------

  //std::cout << "Test6" << std::endl;

  for(int i=0; i<(int)jets->size();++i)
    {
      TCHE_  ->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
      TCHP_  ->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
      SSVHE_ ->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight);
      SSVHP_ ->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight);
    }

  int nBjets=bjets->size();
  if(bjets->size()>3) nBjets=3;

  nBjets_noWgt_   ->Fill(nBjets);
  nBjets_noWgt_2_ ->Fill(bjets->size());
  nBjets_         ->Fill(nBjets, weight);
  nBjets_2_       ->Fill(bjets->size(),weight);

  //std::cout << "Test7" << std::endl;

  for(int bdx=0; bdx<(int)bjets->size();++bdx)
    {
      if(bdx<4)
	{
	  Bjet_Et_[bdx] ->Fill((*bjets)[bdx].et(),  weight);
	  Bjet_Eta_[bdx]->Fill((*bjets)[bdx].eta(), weight);
	}
      Bjets_Et_  ->Fill((*bjets)[bdx].et(),  weight);
      Bjets_Eta_ ->Fill((*bjets)[bdx].eta(), weight);
    }
    
//   if(BtagEventWeightsHandle.isValid())
//     {
//       std::cout << "BtagEventWeightsHandle is valid()" << std::endl;
     
//       nJets_,(*BtagEventWeightsHandle)[0]*weight
//     }
//   else
//     {
//       std::cout << "BtagEventWeightsHandle is not valid" << std::endl;
//     }

  //-------------------------------------------------
  // MET, Lepton pt vs. HT
  //-------------------------------------------------

  //std::cout << "Test8" << std::endl;

  HT_MET_ ->Fill(HT, (*met)[0].et(), weight);
  if(singleLepton != 0)
    {
      //std::cout << "Single lepton" << std::endl;
      
      HT_LepPt_->Fill(HT, singleLepton->et(), weight);
    } 

  //-------------------------------------------------------
  // YMET, MET significnace, Lepton pt significance vs HT
  //-------------------------------------------------------

  //std::cout << "Test9" << std::endl;

  HT_YMET_       ->Fill(HT,   YMET,  weight);
  HT_YMET_noWgt_ ->Fill(HT,   YMET,      1.);

  HT_METSig_      ->Fill(HT, METSig, weight);
  HT_METSig_noWgt_->Fill(HT, METSig,     1.);

  METSig_YMET_ ->Fill(METSig, YMET,  weight);

  //std::cout << "Test10" << std::endl;

  if(singleLepton != 0 && HT > 0. && jets->size()>=4)
    {
      double LepPtSig = singleLepton->et() / sqrt(HT); 
      HT_LepPtSig_->Fill(HT, LepPtSig, weight);
      
      double MET=(*met)[0].et();
      
      //Smear the lepton pT. Do this using the MET signficance
      double MET_resolution = 0.;
      if (METSig > 0.) MET_resolution = 1. / METSig ;  
      TRandom3 rNum(0);
      double smearFactor = pow ( (1.+ MET_resolution) , rNum.Gaus() );
      LepPtSig_smearFactor_->Fill(smearFactor, weight);
      HT_LepPtSig_smeared_->Fill(HT, LepPtSig * smearFactor, weight);
      
      //Fill histograms
      if (singleLepton->et() >= 60.) {
	if (MET >= 60.) {
	  HT_METSig_PT60_MET60_->Fill(HT, YMET, weight);
	  HT_METSig_PT60_MET60_->Fill(HT, METSig, weight);
	}
      }
      if (singleLepton->et() >= 40.) {
	if (MET >= 60.) {
	  HT_METSig_PT40_MET60_->Fill(HT, YMET, weight);
	  HT_METSig_PT40_MET60_->Fill(HT, METSig, weight);
	}
      }
      if (singleLepton->et() >= 20.) {
	if (MET >= 60.) {
	  HT_METSig_PT20_MET60_->Fill(HT, YMET, weight);
	  HT_METSig_PT20_MET60_->Fill(HT, METSig, weight);
	  HT_LepPtSig_PT20_MET60_->Fill(HT, LepPtSig, weight);
	  HT_LepPtSig_PT20_MET60_smeared_->Fill(HT, LepPtSig * smearFactor, weight);
	}
	if (MET >= 40.) {
	  HT_METSig_PT20_MET40_->Fill(HT, METSig, weight);
	  HT_LepPtSig_PT20_MET40_->Fill(HT, LepPtSig, weight);
	  HT_LepPtSig_PT20_MET40_smeared_->Fill(HT, LepPtSig * smearFactor, weight);
	}
	if (MET >= 20.) {
	  HT_METSig_PT20_MET20_->Fill(HT, METSig, weight);
	  HT_LepPtSig_PT20_MET20_->Fill(HT, LepPtSig, weight);
	  HT_LepPtSig_PT20_MET20_smeared_->Fill(HT, LepPtSig * smearFactor, weight);
	}  
      }    
    } 
  
  //std::cout << "Test11" << std::endl;

  //-------------------------------------------------
  // mjj variables
  //-------------------------------------------------
  
  // Example how to use member function of SUSYGenEvent
  //if(susyGenEvent->decayCascadeA()=="gluino->neutralino1" && susyGenEvent->decayCascadeB()=="gluino->neutralino1")
  
  double minj3 =0 ;
  if(jets->size() >= 3)
    {
      // define four-vectors
      reco::Particle::LorentzVector Jet1 = (*jets)[0].p4();
      reco::Particle::LorentzVector Jet2 = (*jets)[1].p4();
      reco::Particle::LorentzVector Jet3 = (*jets)[2].p4();
      
      // define invariant dijet masses   
      double m13=sqrt((Jet1+Jet3).Dot(Jet1+Jet3));
      double m23=sqrt((Jet2+Jet3).Dot(Jet2+Jet3));
     
      minj3 = min(m13,m23);
      minj3_->Fill(minj3, weight);

      minj3_nJets_ -> Fill(minj3, jets->size(), weight);
      HT_minj3_    -> Fill(HT,    minj3,        weight);
    }

  //std::cout << "Test12" << std::endl;

  //-------------------------------------------------
  // Others
  //-------------------------------------------------

  if(mT > 0)
    {
      HT_mT_    ->Fill(HT, mT,           weight);
      mT_nJets_ ->Fill(mT, jets->size(), weight);
    }

  HT_nJets_   ->Fill(HT,              jets->size(), weight);
  MET_nJets_  ->Fill((*met)[0].et(),  jets->size(), weight);
  YMET_nJets_ ->Fill(YMET, jets->size(), weight);

  if(mlb > 0)
    {
      HT_mLepTop_   ->Fill(HT, mLepTop, weight);
      HT_mlb_       ->Fill(HT, mlb,     weight);

      mLepTop_nJets_->Fill(mLepTop, jets->size(), weight);
      mlb_nJets_    ->Fill(mlb,     jets->size(), weight);
      mlb_YMET_     ->Fill(mlb,     YMET        , weight);

      mlb_YMET_nJets_->Fill(mlb, YMET, jets->size(), weight);

      if(mlb < 100)       YMET_nJets_0_   ->Fill(YMET, jets->size(), weight);
      else if (mlb < 200) YMET_nJets_100_ ->Fill(YMET, jets->size(), weight);
      else                YMET_nJets_200_ ->Fill(YMET, jets->size(), weight);

      if(YMET < 5)       mlb_nJets_0_  ->Fill(mlb, jets->size(), weight);
      else if(YMET < 10) mlb_nJets_5_  ->Fill(mlb, jets->size(), weight);
      else if(YMET < 15) mlb_nJets_10_ ->Fill(mlb, jets->size(), weight);
      else if(YMET < 20) mlb_nJets_15_ ->Fill(mlb, jets->size(), weight);
      else               mlb_nJets_20_ ->Fill(mlb, jets->size(), weight);
    }
  
  //-------------------------------------------------
  // Only when TTJets is set to true in cfg file
  //-------------------------------------------------

  if(TTJets_ == true)
    {
      edm::Handle<TtGenEvent> genEvent;
      evt.getByLabel(TtGenEvent_, genEvent);
      
      //std::cout << "Test 0" << std::endl;

      if(genEvent.isValid())
	{	  
	  //std::cout << "Test 1" << std::endl; 

	  if(genEvent->isSemiLeptonic(WDecay::kMuon) ||  genEvent->isSemiLeptonic(WDecay::kElec))
	    {      
	      //std::cout << "Test 2" << std::endl; 
	      
	      double NuPt = genEvent->singleNeutrino()->pt();
	      double NuPx = genEvent->singleNeutrino()->px();
	      double NuPy = genEvent->singleNeutrino()->py();
	      
	      double LepPt = genEvent->singleLepton()->pt();
	      double LepPx = genEvent->singleLepton()->px();
	      double LepPy = genEvent->singleLepton()->py();
	      
	      double LepBQuarkPt = genEvent->leptonicDecayB()->pt();
	      double LepBQuarkPx = genEvent->leptonicDecayB()->px();
	      double LepBQuarkPy = genEvent->leptonicDecayB()->py();
	      
	      double mlb_gen = sqrt(2*(LepPt*LepBQuarkPt-LepPx*LepBQuarkPx-LepPy*LepBQuarkPy));
	      double mlv_gen = sqrt(2*(NuPt*LepPt-NuPx*LepPx-NuPy*LepPy));
	      
	      double mlv_reco = 0;
	      
	      double HadMET = (*met)[0].et()-NuPt;
	      double fakeMET = sqrt(pow((*met)[0].px()-NuPx,2)+pow((*met)[0].py()-NuPy,2));
	      
	      double MET_NuPt_Ratio = ((*met)[0].et())/NuPt;
	      double MET_HadMET_Ratio = ((*met)[0].et())/HadMET;
	      double MET_fakeMET_Ratio = ((*met)[0].et())/fakeMET;
	      double NuPt_fakeMET_Ratio = NuPt/fakeMET;

	      if(singleLepton != 0) mlv_reco = sqrt(2*(NuPt*singleLepton->pt()-NuPx*singleLepton->px()-NuPy*singleLepton->py()));

	      //std::cout << "Test 3" << std::endl;

	      double smearedPv = sqrt(pow(NuPx+DeltaRecoGenJetPySum,2)+pow(NuPx+DeltaRecoGenJetPySum,2));

	      pv_             -> Fill(NuPt,      weight);
	      smearedPv_      -> Fill(smearedPv, weight);
	      
	      pv_nJets_       -> Fill(NuPt,     jets->size(), weight);
	      mlv_nJets_gen_  -> Fill(mlv_gen,  jets->size(), weight);
	      mlv_nJets_reco_ -> Fill(mlv_reco, jets->size(), weight);

	      pv_MET_         -> Fill(NuPt,      (*met)[0].et(), weight);
	      smearedPv_MET_  -> Fill(smearedPv, (*met)[0].et(), weight);

	      NuPt_nJets_    -> Fill(NuPt,           jets->size(), weight);
	      fakeMET_nJets_ -> Fill(fakeMET,        jets->size(), weight);

	      NuPt_fakeMET_ ->Fill(NuPt,    fakeMET,        weight);
	      NuPt_MET_     ->Fill(NuPt,    (*met)[0].et(), weight);
	      fakeMET_MET_  ->Fill(fakeMET, (*met)[0].et(), weight);

	      if (HT < 125)                  NuPt_fakeMET_0HT125_   ->Fill(NuPt, fakeMET, weight);
	      else if (125 < HT && HT < 250) NuPt_fakeMET_125HT250_ ->Fill(NuPt, fakeMET, weight);
	      else if (250 < HT && HT < 375) NuPt_fakeMET_250HT375_ ->Fill(NuPt, fakeMET, weight);
	      else if (375 < HT && HT < 500) NuPt_fakeMET_375HT500_ ->Fill(NuPt, fakeMET, weight);
	      else if (500 < HT && HT < 650) NuPt_fakeMET_500HT650_ ->Fill(NuPt, fakeMET, weight);
	      else if (650 < HT && HT < 800) NuPt_fakeMET_650HT800_ ->Fill(NuPt, fakeMET, weight);
	      else if (800 < HT && HT < 950) NuPt_fakeMET_800HT950_ ->Fill(NuPt, fakeMET, weight);

	      //std::cout << "Test 4" << std::endl;

	      HT_HadMET_   -> Fill(HT, HadMET,  weight);
	      HT_fakeMET_  -> Fill(HT, fakeMET, weight);
	      HT_NuPt_     -> Fill(HT, NuPt,    weight);

	      HT_NuPtSig_    -> Fill(HT, NuPt/sqrt(HT),    weight);
	      HT_fakeMETSig_ -> Fill(HT, fakeMET/sqrt(HT), weight);

	      //std::cout << "Test 5" << std::endl;

	      HT_METNuPtRatio_      -> Fill(HT, MET_NuPt_Ratio,     weight);
	      HT_METHadMETRatio_    -> Fill(HT, MET_HadMET_Ratio,   weight);
	      HT_METfakeMETRatio_   -> Fill(HT, MET_fakeMET_Ratio,  weight);
	      HT_NuPtfakeMETRatio_  -> Fill(HT, NuPt_fakeMET_Ratio, weight);
	      HT_NuPtfakeMETRatio2_ -> Fill(HT, NuPt_fakeMET_Ratio, weight);
	      if(NuPt > 100) HT_NuPtfakeMETRatio3_ -> Fill(HT, NuPt_fakeMET_Ratio, weight);

	      //std::cout << "Test 6" << std::endl;

	      if(NuPt > HadMET)  HT_HadMET_2_  -> Fill(HT, HadMET,  weight);
	      if(NuPt > fakeMET) HT_fakeMET_2_ -> Fill(HT, fakeMET, weight);

	      //std::cout << "Test 7" << std::endl; 
	  
	      if(400 < HT && HT < 500)
		{
		  HadMET_400HT500_ -> Fill(HadMET, weight);
		  NuPt_400HT500_   -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_400HT500_2_ -> Fill(HadMET, weight);
		}
	      else if(500 < HT && HT < 600) 
		{
		  HadMET_500HT600_ -> Fill(HadMET, weight);
		  NuPt_500HT600_   -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_500HT600_2_ -> Fill(HadMET, weight);
		}
	      
	      else if(600 < HT && HT < 700) 
		{
		  HadMET_600HT700_  -> Fill(HadMET, weight);
		  NuPt_600HT700_    -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_600HT700_2_ -> Fill(HadMET, weight);
		}
	      else if(700 < HT && HT < 800)
		{
		  HadMET_700HT800_  -> Fill(HadMET, weight);
		  NuPt_700HT800_    -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_700HT800_2_ -> Fill(HadMET, weight);
		}
	      
	      else if(800 < HT && HT < 900)
		{
		  HadMET_800HT900_  -> Fill(HadMET, weight);
		  NuPt_800HT900_    -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_800HT900_2_ -> Fill(HadMET, weight);
		}
	      
	      else if(900 < HT && HT < 1000)
		{
		  HadMET_900HT1000_ -> Fill(HadMET, weight);
		  NuPt_900HT1000_   -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_900HT1000_2_ -> Fill(HadMET, weight);
		}
	      
	      else if(HT > 1000)
		{
		  HadMET_1000HTInf_ -> Fill(HadMET, weight);
		  NuPt_1000HTInf_   -> Fill(NuPt, weight);
		  if(NuPt > HadMET) HadMET_1000HTInf_2_ -> Fill(HadMET, weight);
		}
	
	      //std::cout << "Test 8" << std::endl;		
	      
	    }
	}
    }
  
  //-------------------------------------------------
  // Only when TTJetsHyp is set to true in cfg file
  //-------------------------------------------------

  if(TTJetsHyp_ == true)
    {
      edm::Handle<TtSemiLeptonicEvent> semiLepEvent;
      evt.getByLabel(TtSemiLepEvent_, semiLepEvent);

      if(semiLepEvent->isHypoValid(hypoKey_))
	{
	  if(semiLepEvent->hadronicDecayW(hypoKey_))
	    {
	      hadWMass_  ->Fill(semiLepEvent->hadronicDecayW(hypoKey_)  ->mass(),  weight);
	      hadTopMass_->Fill(semiLepEvent->hadronicDecayTop(hypoKey_)->mass(),  weight);
	      if(hypoKey_ == "kKinFit")
		{
		  chi2_ ->Fill(semiLepEvent->fitChi2(), weight);
		}
	    }
	}
    }
  //std::cout << "Test13" << std::endl;

  //-------------------------------------------------
  // ABCD method
  //-------------------------------------------------

  bool ATight = HT >= HT0_ && HT < HT1_ && YMET >= Y0_ && YMET < Y1_;
  bool BTight = HT >= HT2_ && YMET >= Y0_ && YMET < Y1_;
  bool CTight = HT >= HT0_ && HT < HT1_ && YMET >= Y2_;
  bool DTight = HT >= HT2_ && YMET >= Y2_;

  // A region
  if(ATight)
    {
      MET_A_  ->Fill((*met)[0].et(),weight);
      nJets_A_->Fill(jets->size(),  weight);    
      if(singleLepton != 0)
	{
	  Lep_Pt_A_->Fill(singleLepton->pt(),weight);
	}
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{
	  if(jdx<8) Jet_Et_A_[jdx]->Fill((*jets)[jdx].et(),weight);
	  Jets_Et_A_->Fill((*jets)[jdx].et(),weight);
	}
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	  if(bdx<4) Bjet_Et_A_[bdx]->Fill((*bjets)[bdx].et(),weight);
	  Bjets_Et_A_->Fill((*bjets)[bdx].et(),weight);
	}
      // Enter loop only when b-tag weights are applied
      if(useBtagEventWgt_ || useInclusiveBtagEventWgt_)
	{
	  // Get jet weights
	  edm::Handle<std::vector<double> > BtagJetWeightsHandle;
	  evt.getByLabel(BtagJetWeights_, BtagJetWeightsHandle);
	  
	  //std::cout << "\n" << std::endl;
	  for(int idx=0; idx < (int)jets->size(); ++idx)
	    {
	      //std::cout << "(*BtagJetWeightsHandle)[idx]" << (*BtagJetWeightsHandle)[idx] << std::endl;
	      double combinedWeight=weightRA2*weightPU*(*BtagJetWeightsHandle)[idx];

	      Bjets_Et_Weights_A_ ->Fill((*jets)[idx].et(), combinedWeight);
	      Bjets_Eta_Weights_A_->Fill((*jets)[idx].eta(),combinedWeight);

	      if((*jets)[idx].et()<670)
		{
		  Bjets_Et_Weights_A_670_ ->Fill((*jets)[idx].et(), combinedWeight);
		  Bjets_Eta_Weights_A_670_->Fill((*jets)[idx].eta(),combinedWeight);
		}  
	    }
	  //std::cout << "\n" << std::endl;
	}
    }

  // B region
  if(BTight)
    {
      MET_B_->Fill((*met)[0].et(),weight);
      nJets_B_->Fill(jets->size(),  weight);
      if(singleLepton != 0)
	{
	  Lep_Pt_B_->Fill(singleLepton->pt(),weight);
	}
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{
	  if(jdx<8) Jet_Et_B_[jdx]->Fill((*jets)[jdx].et(),weight);
	  Jets_Et_B_->Fill((*jets)[jdx].et(),weight);
	}
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	  if(bdx<4) Bjet_Et_B_[bdx]->Fill((*bjets)[bdx].et(),weight);
	  Bjets_Et_B_->Fill((*bjets)[bdx].et(),weight);
	}
      // Enter loop only when b-tag weights are applied
      if(useBtagEventWgt_ || useInclusiveBtagEventWgt_)
	{
	  // Get jet weights
	  edm::Handle<std::vector<double> > BtagJetWeightsHandle;
	  evt.getByLabel(BtagJetWeights_, BtagJetWeightsHandle);
	  
	  //std::cout << "\n" << std::endl;
	  for(int idx=0; idx < (int)jets->size(); ++idx)
	    {
	      //std::cout << "(*BtagJetWeightsHandle)[idx]" << (*BtagJetWeightsHandle)[idx] << std::endl;
	      double combinedWeight=weightRA2*weightPU*(*BtagJetWeightsHandle)[idx];

	      Bjets_Et_Weights_B_ ->Fill((*jets)[idx].et(), combinedWeight);
	      Bjets_Eta_Weights_B_->Fill((*jets)[idx].eta(),combinedWeight);

	      if((*jets)[idx].et()<670)
		{
		  Bjets_Et_Weights_B_670_ ->Fill((*jets)[idx].et(), combinedWeight);
		  Bjets_Eta_Weights_B_670_->Fill((*jets)[idx].eta(),combinedWeight);
		}  
	    }
	  //std::cout << "\n" << std::endl;
	}
    }

  // C region
  if(CTight)
    {
      MET_C_->Fill((*met)[0].et(),weight);
      nJets_B_->Fill(jets->size(),  weight);
      if(singleLepton != 0)
	{
	  Lep_Pt_C_->Fill(singleLepton->pt(),weight);
	}
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{
	  if(jdx<8) Jet_Et_C_[jdx]->Fill((*jets)[jdx].et(),weight);
	  Jets_Et_C_->Fill((*jets)[jdx].et(),weight);
	}
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	  if(bdx<4) Bjet_Et_C_[bdx]->Fill((*bjets)[bdx].et(),weight);
	  Bjets_Et_C_->Fill((*bjets)[bdx].et(),weight);
	}
      // Enter loop only when b-tag weights are applied
      if(useBtagEventWgt_ || useInclusiveBtagEventWgt_)
	{
	  // Get jet weights
	  edm::Handle<std::vector<double> > BtagJetWeightsHandle;
	  evt.getByLabel(BtagJetWeights_, BtagJetWeightsHandle);
	  
	  //std::cout << "\n" << std::endl;
	  for(int idx=0; idx < (int)jets->size(); ++idx)
	    {
	      //std::cout << "(*BtagJetWeightsHandle)[idx]" << (*BtagJetWeightsHandle)[idx] << std::endl;
	      double combinedWeight=weightRA2*weightPU*(*BtagJetWeightsHandle)[idx];

	      Bjets_Et_Weights_C_ ->Fill((*jets)[idx].et(), combinedWeight);
	      Bjets_Eta_Weights_C_->Fill((*jets)[idx].eta(),combinedWeight);

	      if((*jets)[idx].et()<670)
		{
		  Bjets_Et_Weights_C_670_ ->Fill((*jets)[idx].et(), combinedWeight);
		  Bjets_Eta_Weights_C_670_->Fill((*jets)[idx].eta(),combinedWeight);
		}  
	    }
	  //std::cout << "\n" << std::endl;
	}
    }

  // D region
  if(DTight)
    {
      MET_D_->Fill((*met)[0].et(),weight);
      nJets_D_->Fill(jets->size(),  weight);
      if(singleLepton != 0)
	{
	  Lep_Pt_D_->Fill(singleLepton->pt(),weight);
	}
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{
	  if(jdx<8) Jet_Et_D_[jdx]->Fill((*jets)[jdx].et(),weight);
	  Jets_Et_D_->Fill((*jets)[jdx].et(),weight);
	}
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	  if(bdx<4) Bjet_Et_D_[bdx]->Fill((*bjets)[bdx].et(),weight);
	  Bjets_Et_D_->Fill((*bjets)[bdx].et(),weight);
	}
      // Enter loop only when b-tag weights are applied
      if(useBtagEventWgt_ || useInclusiveBtagEventWgt_)
	{
	  // Get jet weights
	  edm::Handle<std::vector<double> > BtagJetWeightsHandle;
	  evt.getByLabel(BtagJetWeights_, BtagJetWeightsHandle);
	  
	  //std::cout << "\n" << std::endl;
	  for(int idx=0; idx < (int)jets->size(); ++idx)
	    {
	      //std::cout << "(*BtagJetWeightsHandle)[idx]" << (*BtagJetWeightsHandle)[idx] << std::endl;
	      double combinedWeight=weightRA2*weightPU*(*BtagJetWeightsHandle)[idx];

	      Bjets_Et_Weights_D_ ->Fill((*jets)[idx].et(), combinedWeight);
	      Bjets_Eta_Weights_D_->Fill((*jets)[idx].eta(),combinedWeight);

	      if((*jets)[idx].et()<670)
		{
		  Bjets_Et_Weights_D_670_ ->Fill((*jets)[idx].et(), combinedWeight);
		  Bjets_Eta_Weights_D_670_->Fill((*jets)[idx].eta(),combinedWeight);
		}  
	    }
	  //std::cout << "\n" << std::endl;
	}

    }

  //std::cout << "Test12" << std::endl;

}

void CorrelationAnalyzer::beginJob()
{  
} 

void CorrelationAnalyzer::endJob()
{
}
