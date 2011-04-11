#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYGenEventAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
#include "DataFormats/Math/interface/angle.h"

#include "PhysicsTools/CandUtils/interface/EventShapeVariables.h"
#include "TVector3.h"

using namespace std;

SUSYGenEventAnalyzer::SUSYGenEventAnalyzer(const edm::ParameterSet& cfg):
  inputGenEvent_(cfg.getParameter<edm::InputTag>("susyGenEvent")),
  initSubset_(cfg.getParameter<edm::InputTag>("initSubset")),
  jets_(cfg.getParameter<edm::InputTag>("jets")),
  bjets_(cfg.getParameter<edm::InputTag>("bjets")),
  matchedbjets_(cfg.getParameter<edm::InputTag>("matchedbjets")),
  matchedqjets_(cfg.getParameter<edm::InputTag>("matchedqjets")),
  matchedmuons_(cfg.getParameter<edm::InputTag>("matchedmuons")),
  matchedelectrons_(cfg.getParameter<edm::InputTag>("matchedelectrons")),
  met_(cfg.getParameter<edm::InputTag>("met"))

{
  edm::Service<TFileService> fs;

  nrBQuarks_gq_    = fs->make<TH1F>("nrBQuarks_gq",    "nr BQuarks gq",     9, -0.5, 8.5);
  nrBQuarks_gg_    = fs->make<TH1F>("nrBQuarks_gg",    "nr BQuarks gg",     9, -0.5, 8.5);
  nrBQuarks_qq_    = fs->make<TH1F>("nrBQuarks_qq",    "nr BQuarks qq",     9, -0.5, 8.5);
  nrBQuarks_other_ = fs->make<TH1F>("nrBQuarks_other", "nr BQuarks other",  9, -0.5, 8.5);
  nrBQuarks_       = fs->make<TH1F>("nrBQuarks",       "nr BQuarks",        9, -0.5, 8.5);
  nrBQuarks_ssqq_  = fs->make<TH1F>("nrBQuarks_ssqq",  "nr BQuarks ssqq",   9, -0.5, 8.5);
  nrBQuarks_osqq_  = fs->make<TH1F>("nrBQuarks_osqq",  "nr BQuarks osqq",   9, -0.5, 8.5);

  nrBQuarks_gq_ssDiLep_    = fs->make<TH1F>("nrBQuarks_gq_ssDiLep",    "nr BQuarks gq ss DiLep",     9, -0.5, 8.5);
  nrBQuarks_gg_ssDiLep_    = fs->make<TH1F>("nrBQuarks_gg_ssDiLep",    "nr BQuarks gg ss DiLep",     9, -0.5, 8.5);
  nrBQuarks_qq_ssDiLep_    = fs->make<TH1F>("nrBQuarks_qq_ssDiLep",    "nr BQuarks qq ss DiLep",     9, -0.5, 8.5);
  nrBQuarks_other_ssDiLep_ = fs->make<TH1F>("nrBQuarks_other_ssDiLep", "nr BQuarks other ss DiLep",  9, -0.5, 8.5);
  nrBQuarks_ssDiLep_       = fs->make<TH1F>("nrBQuarksssDiLep",        "nr BQuarksss DiLep",         9, -0.5, 8.5);
  nrBQuarks_ssqq_ssDiLep_  = fs->make<TH1F>("nrBQuarks_ssqq_ssDiLep",  "nr BQuarks ssqq ss DiLep",   9, -0.5, 8.5);
  nrBQuarks_osqq_ssDiLep_  = fs->make<TH1F>("nrBQuarks_osqq_ssDiLep",  "nr BQuarks osqq ss DiLep",   9, -0.5, 8.5);

  nrBQuarks_gq_osDiLep_    = fs->make<TH1F>("nrBQuarks_gq_osDiLep",    "nr BQuarks gq os DiLep",     9, -0.5, 8.5);
  nrBQuarks_gg_osDiLep_    = fs->make<TH1F>("nrBQuarks_gg_osDiLep",    "nr BQuarks gg os DiLep",     9, -0.5, 8.5);
  nrBQuarks_qq_osDiLep_    = fs->make<TH1F>("nrBQuarks_qq_osDiLep",    "nr BQuarks qq os DiLep",     9, -0.5, 8.5);
  nrBQuarks_other_osDiLep_ = fs->make<TH1F>("nrBQuarks_other_osDiLep", "nr BQuarks other os DiLep",  9, -0.5, 8.5);
  nrBQuarks_osDiLep_       = fs->make<TH1F>("nrBQuarkossDiLep",        "nr BQuarkoss DiLep",         9, -0.5, 8.5);
  nrBQuarks_ssqq_osDiLep_  = fs->make<TH1F>("nrBQuarks_ssqq_osDiLep",  "nr BQuarks ssqq os DiLep",   9, -0.5, 8.5);
  nrBQuarks_osqq_osDiLep_  = fs->make<TH1F>("nrBQuarks_osqq_osDiLep",  "nr BQuarks osqq os DiLep",   9, -0.5, 8.5);
 
  nrBJets_gq_ = fs->make<TH1F>("nrBJets_gq",    "nr BJets gq",     9, -0.5, 8.5);
  nrBJets_gg_ = fs->make<TH1F>("nrBJets_gg",    "nr BJets gg",     9, -0.5, 8.5);
  nrBJets_qq_ = fs->make<TH1F>("nrBJets_qq",    "nr BJets qq",     9, -0.5, 8.5);
  nrBJets_other_ = fs->make<TH1F>("nrBJets_other",    "nr BJets other",     9, -0.5, 8.5);
  nrBJets_ = fs->make<TH1F>("nrBJets",    "nr BJets",     9, -0.5, 8.5);
  nrBJets_ssqq_ = fs->make<TH1F>("nrBJets_ssqq",    "nr BJets ssqq",     9, -0.5, 8.5);
  nrBJets_osqq_ = fs->make<TH1F>("nrBJets_osqq",    "nr BJets osqq",     9, -0.5, 8.5);

  nrBTags_gq_ = fs->make<TH1F>("nrBTags_gq",    "nr BTags gq",     9, -0.5, 8.5);
  nrBTags_gg_ = fs->make<TH1F>("nrBTags_gg",    "nr BTags gg",     9, -0.5, 8.5);
  nrBTags_qq_ = fs->make<TH1F>("nrBTags_qq",    "nr BTags qq",     9, -0.5, 8.5);
  nrBTags_other_ = fs->make<TH1F>("nrBTags_other",    "nr BTags other",     9, -0.5, 8.5);
  nrBTags_ = fs->make<TH1F>("nrBTags",    "nr BTags",     9, -0.5, 8.5);
  nrBTags_ssqq_ = fs->make<TH1F>("nrBTags_ssqq",    "nr BTags ssqq",     9, -0.5, 8.5);
  nrBTags_osqq_ = fs->make<TH1F>("nrBTags_osqq",    "nr BTags osqq",     9, -0.5, 8.5);

  ratio_gq_=fs->make<TH1F>("ratio_gq_", "ratio gq", 60, -30., 30.);
  ratio_gg_=fs->make<TH1F>("ratio_gg_", "ratio gg", 60, -30., 30.);
  ratio_qq_=fs->make<TH1F>("ratio_qq_", "ratio qq", 60, -30., 30.);
  ratio_other_=fs->make<TH1F>("ratio_other_", "ratio other", 60, -30., 30.);
  ratio_=fs->make<TH1F>("ratio_", "ratio", 60, -30., 30.);
  ratio_ssqq_=fs->make<TH1F>("ratio_ssqq_", "ratio ssqq", 60, -30., 30.);
  ratio_osqq_=fs->make<TH1F>("ratio_osqq_", "ratio osqq", 60, -30., 30.);

  Jet1_Et_2BQuarks_gq_ = fs->make<TH1F>("Jet1_Et_2BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  Jet1_Et_2BQuarks_gg_ = fs->make<TH1F>("Jet1_Et_2BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  Jet1_Et_2BQuarks_qq_ = fs->make<TH1F>("Jet1_Et_2BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  Jet1_Et_2BQuarks_other_ = fs->make<TH1F>("Jet1_Et_2BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  Jet1_Et_2BQuarks_ = fs->make<TH1F>("Jet1_Et_2BQuarks",    "Et Jet1",     30, 0, 900);

  Jet1_Et_012BQuarks_gq_ = fs->make<TH1F>("Jet1_Et_012BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  Jet1_Et_012BQuarks_gg_ = fs->make<TH1F>("Jet1_Et_012BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  Jet1_Et_012BQuarks_qq_ = fs->make<TH1F>("Jet1_Et_012BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  Jet1_Et_012BQuarks_other_ = fs->make<TH1F>("Jet1_Et_012BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  Jet1_Et_012BQuarks_ = fs->make<TH1F>("Jet1_Et_012BQuarks",    "Et Jet1",     30, 0, 900);

  Jet1_Et_3456BQuarks_gq_ = fs->make<TH1F>("Jet1_Et_3456BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  Jet1_Et_3456BQuarks_gg_ = fs->make<TH1F>("Jet1_Et_3456BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  Jet1_Et_3456BQuarks_qq_ = fs->make<TH1F>("Jet1_Et_3456BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  Jet1_Et_3456BQuarks_other_ = fs->make<TH1F>("Jet1_Et_3456BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  Jet1_Et_3456BQuarks_ = fs->make<TH1F>("Jet1_Et_3456BQuarks",    "Et Jet1",     30, 0, 900);

  nrLeptons_ss_= fs->make<TH1F>("nrLeptons_ss",    "nr leptons same sign",     9, -0.5, 8.5);
  nrLeptons_os_= fs->make<TH1F>("nrLeptons_os",    "nr leptons opposite sign",     9, -0.5, 8.5);
  nrLeptons_= fs->make<TH1F>("nrLeptons",    "nr leptons",     9, -0.5, 8.5);

  angleb1b2_= fs->make<TH1F>("angleb1b2",    "angle (bjet1,bjet2)", 31, 0.,  3.1);
  mbb_= fs->make<TH1F>("mbb_",    "invariant bb mass", 30, 0.,  900);
  HTB_= fs->make<TH1F>("HTB_",    "HT (bjets)", 40, 0., 2000.);
  DeltaMT_min_ = fs->make<TH1F>("DeltaMT_min",    "Delta MT", 60, -300., 300.);

  deltaPhi_b1b2_= fs->make<TH1F>("DeltaPhib1b2","delta Phi(b,b)", 31 , 0., 3.1);
  deltaPhi_b1MET_= fs->make<TH1F>("DeltaPhib1MET","delta Phi(b1,MET)", 31 , 0., 3.1);
  deltaPhi_b2MET_= fs->make<TH1F>("DeltaPhib2MET","delta Phi(b2,MET)", 31 , 0., 3.1);
  deltaPhi_b12MET_= fs->make<TH1F>("DeltaPhib12MET","delta(delta Phi(b,MET))", 31 , 0., 3.1);

  deltaPhi_MuMET_= fs->make<TH1F>("DeltaPhiMuMET","delta Phi(Mu,MET)", 31 , 0., 3.1);
  deltaPhi_ElMET_= fs->make<TH1F>("DeltaPhiElMET","delta Phi(El,MET)", 31 , 0., 3.1);
  deltaPhi_LepMET_= fs->make<TH1F>("DeltaPhiLepMET","delta Phi(Lep,MET)", 31 , 0., 3.1);

  deltaPhi_Lep1Lep2_= fs->make<TH1F>("DeltaPhiLep1Lep2","delta Phi(Lep1,Lep2)", 31 , 0., 3.1);
  deltaPhi_Lep1MET_= fs->make<TH1F>("DeltaPhiLep1MET","delta Phi(Lep1,MET)", 31 , 0., 3.1);
  deltaPhi_Lep2MET_= fs->make<TH1F>("DeltaPhiLep2MET","delta Phi(Lep2,MET)", 31 , 0., 3.1);
  deltaPhi_Lep12MET_= fs->make<TH1F>("DeltaPhiLep12MET","delta(delta Phi(Lep,MET))", 31 , 0., 3.1);

  deltaPhi_Mu1Mu2_= fs->make<TH1F>("DeltaPhiMuMu","delta Phi(Mu,Mu)", 31 , 0., 3.1);
  deltaPhi_Mu1MET_= fs->make<TH1F>("DeltaPhiMu1MET","delta Phi(Mu1,MET)", 31 , 0., 3.1);
  deltaPhi_Mu2MET_= fs->make<TH1F>("DeltaPhiMu2MET","delta Phi(Mu2,MET)", 31 , 0., 3.1);
  deltaPhi_Mu12MET_= fs->make<TH1F>("DeltaPhiMu12MET","delta(delta Phi(Mu,MET))", 31 , 0., 3.1);

  deltaPhi_El1El2_= fs->make<TH1F>("DeltaPhiElEl","delta Phi(El,El)", 31 , 0., 3.1);
  deltaPhi_El1MET_= fs->make<TH1F>("DeltaPhiEl1MET","delta Phi(El1,MET)", 31 , 0., 3.1);
  deltaPhi_El2MET_= fs->make<TH1F>("DeltaPhiEl2MET","delta Phi(El2,MET)", 31 , 0., 3.1);
  deltaPhi_El12MET_= fs->make<TH1F>("DeltaPhiEl12MET","delta(delta Phi(El,MET))", 31 , 0., 3.1);

  deltaPhi_MuEl_= fs->make<TH1F>("DeltaPhiMuEl","delta Phi(Mu,El)", 31 , 0., 3.1);
  deltaPhi_MuElMET_= fs->make<TH1F>("DeltaPhiMuElMET","delta(delta Phi(Lep,MET))", 31 , 0., 3.1);
  
  sphericity_bjetsMET_ = fs->make<TH1F>("sphericity_bjetsMET","sphericity(bjets+MET)", 20 , 0., 1.);        
  aplanarity_bjetsMET_   = fs->make<TH1F>("aplanarity_bjetsMET","aplanarity(bjets+MET)", 20 , 0., 1.);
  circularity_bjetsMET_  = fs->make<TH1F>("circularity_bjetsMET","circularity(bjets+MET)", 20 , 0., 1.);      
  isotropy_bjetsMET_= fs->make<TH1F>("isotropy_bjetsMET","isotropy(bjets+MET)", 20 , 0., 1.);

  Jet1_Et_2Bjets_= fs->make<TH1F>("Jet1_Et_2Bjets","Et Jet1 2Bjets", 30 , 0, 900);
  Bjet1_Et_= fs->make<TH1F>("Bjet1_Et","Et Bjet1", 30 , 0, 900);
  Bjet2_Et_= fs->make<TH1F>("Bjet2_Et","Et Bjet2", 30 , 0, 900);
  HT_2Bjets_= fs->make<TH1F>("HT_2Bjets",    "HT (2bjets)", 40, 0., 2000.);
  HT_2Bjets_1LightJet_= fs->make<TH1F>("HT_2Bjets_1LightJet",    "HT (2bjets+1lightjet)", 40, 0., 2000.);

  MET_SSDiLep_ = fs->make<TH1F>("MET_SSDiLep",    "MET (SSDiLep)", 40, 0., 1000.);
  MET_OSDiLep_ = fs->make<TH1F>("MET_OSDiLep",    "MET (OSDiLep)", 40, 0., 1000.);

}

SUSYGenEventAnalyzer::~SUSYGenEventAnalyzer()
{
}

void
SUSYGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{

  //std::cout << "Test 1" << std::endl;

  // handles
  edm::Handle<SUSYGenEvent> susyGenEvent;
  evt.getByLabel(inputGenEvent_, susyGenEvent);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Jet> > matchedbjets;
  evt.getByLabel(matchedbjets_, matchedbjets);
  edm::Handle<std::vector<pat::Jet> > matchedqjets;
  evt.getByLabel(matchedqjets_, matchedqjets);
  edm::Handle<std::vector<pat::Muon> > matchedmuons;
  evt.getByLabel(matchedmuons_, matchedmuons);
  edm::Handle<std::vector<pat::Electron> > matchedelectrons;
  evt.getByLabel(matchedelectrons_, matchedelectrons);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);

  // number of matched bjets
  int nmatchedbjets=0;
  for(int idx=0; idx<(int)matchedbjets->size(); ++idx) ++nmatchedbjets;

  // number of bjets
  int nbtags=0;
  for(int jdx=0; jdx<(int)bjets->size(); ++jdx) ++nbtags;

  int nMatchedLeptons=matchedmuons->size()+matchedelectrons->size();

  //std::cout << "Test 2" << std::endl;

  //-----------------------------------------------------------------------------------------
  // number of b-quarks, bjets and btags for different processes of sparticle production
  //-----------------------------------------------------------------------------------------

  // gluino-squark
  if(susyGenEvent->GluinoSquarkDecay()==true)
    {
      nrBQuarks_gq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_gg_->Fill(nmatchedbjets);
      nrBTags_gg_->Fill(nbtags);
      //std::cout << "Test 21" << std::endl;
      ratio_gq_->Fill(susyGenEvent->ratio());
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_gq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_gq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  // gluino-gluino
  else if(susyGenEvent->GluinoGluinoDecay()==true)
    {
      nrBQuarks_gg_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_gq_->Fill(nmatchedbjets);
      nrBTags_gq_->Fill(nbtags);
      //std::cout << "Test 22" << std::endl;
      ratio_gg_->Fill(susyGenEvent->ratio());
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_gg_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_gg_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  // squark-squark
  else if(susyGenEvent->SquarkSquarkDecay()==true)
    {
      nrBQuarks_qq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_qq_->Fill(nmatchedbjets);
      nrBTags_qq_->Fill(nbtags);
      //std::cout << "Test 23" << std::endl;
      ratio_qq_->Fill(susyGenEvent->ratio());
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_qq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_qq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    } 
  // other
  else
    {
      nrBQuarks_other_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_other_->Fill(nmatchedbjets);
      nrBTags_other_->Fill(nbtags);
      //std::cout << "Test 24" << std::endl;
      //ratio_other_->Fill(susyGenEvent->ratio());

      //std::cout << "Test 242" << std::endl;
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      //std::cout << "Test 243" << std::endl;
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  //std::cout << "Test 244" << std::endl;
  // ss squark-squark
  if(susyGenEvent->SSignSquarkSquarkDecay())
    {
      nrBQuarks_ssqq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_ssqq_->Fill(nmatchedbjets);
      nrBTags_ssqq_->Fill(nbtags);
      //std::cout << "Test 5" << std::endl;
      ratio_ssqq_->Fill(susyGenEvent->ratio());
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_ssqq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_ssqq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  // os squark-squark
  if(susyGenEvent->OSignSquarkSquarkDecay())
    {
      nrBQuarks_osqq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_osqq_->Fill(nmatchedbjets);
      nrBTags_osqq_->Fill(nbtags);
      //std::cout << "Test 26" << std::endl;
      ratio_osqq_->Fill(susyGenEvent->ratio());
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_osqq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_osqq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  // all
   //std::cout << "Test 27" << std::endl;
  nrBQuarks_->Fill(susyGenEvent->numberOfBQuarks());
  nrBJets_->Fill(nmatchedbjets);
  nrBTags_->Fill(nbtags);
  //std::cout << "Test 28" << std::endl;
  //ratio_->Fill(susyGenEvent->ratio());
  //std::cout << "Test 3" << std::endl;

  //-------------------------------------------------------
  // correlation between number of b-quarks and jet1 et
  //-------------------------------------------------------

  //std::cout << "ratio: " << (susyGenEvent->ratio()) << std::endl;

  // 0,1 b-quarks
  if(susyGenEvent->numberOfBQuarks()<=2)
    {
      //std::cout << "Test 31" << std::endl;
      if(susyGenEvent->GluinoSquarkDecay()) Jet1_Et_012BQuarks_gq_->Fill((*jets)[0].et());
      else if(susyGenEvent->GluinoGluinoDecay()) Jet1_Et_012BQuarks_gg_->Fill((*jets)[0].et());
      else if(susyGenEvent->SquarkSquarkDecay()) Jet1_Et_012BQuarks_qq_->Fill((*jets)[0].et());
      else Jet1_Et_012BQuarks_other_->Fill((*jets)[0].et());
      Jet1_Et_012BQuarks_->Fill((*jets)[0].et()); 
    }
  //std::cout << "Test 32" << std::endl;
  // 2 b-quarks
  if(susyGenEvent->numberOfBQuarks()==2)
    {
    //std::cout << "Test 33" << std::endl;
      if(susyGenEvent->GluinoSquarkDecay()) Jet1_Et_2BQuarks_gq_->Fill((*jets)[0].et());
      else if(susyGenEvent->GluinoGluinoDecay()) Jet1_Et_2BQuarks_gg_->Fill((*jets)[0].et());
      else if(susyGenEvent->SquarkSquarkDecay()) Jet1_Et_2BQuarks_qq_->Fill((*jets)[0].et());
      else Jet1_Et_2BQuarks_other_->Fill((*jets)[0].et());
      Jet1_Et_2BQuarks_->Fill((*jets)[0].et()); 
    }

  //std::cout << "Test 34" << std::endl;
  // 3,4, ... b-quarks
  if(susyGenEvent->numberOfBQuarks()>=3)
    {
      //std::cout << "Test 35" << std::endl;
      if(susyGenEvent->GluinoSquarkDecay())

	{//std::cout << "Test 351" << std::endl;
	  Jet1_Et_3456BQuarks_gq_->Fill((*jets)[0].et());
	}
      else if(susyGenEvent->GluinoGluinoDecay())
	{
	  //std::cout << "Test 352" << std::endl;
	  //std::cout << "(*jets)[0].et()" << (*jets)[0].et() << std::endl;
	  Jet1_Et_3456BQuarks_gg_->Fill((*jets)[0].et());
	  //std::cout << "Test 3521" << std::endl;
	}
      else if(susyGenEvent->SquarkSquarkDecay())
	{
	  //std::cout << "Test 353" << std::endl;
	  Jet1_Et_3456BQuarks_qq_->Fill((*jets)[0].et());
	}
      else 
	{
	  //std::cout << "Test 354" << std::endl;
	  Jet1_Et_3456BQuarks_other_->Fill((*jets)[0].et());
	}
      Jet1_Et_3456BQuarks_->Fill((*jets)[0].et()); 
    }

  //std::cout << "Test 4" << std::endl;

  //---------------------------------------------------------------------------------------------
  // correlation between ss/os di-lepton and ss/os squark-squark production, MET
  //---------------------------------------------------------------------------------------------

  if(susyGenEvent->SSignDiLepton()==true && susyGenEvent->OSignDiLepton()==false)
    {
      nrLeptons_ss_->Fill(susyGenEvent->numberOfLeptons());
      MET_SSDiLep_->Fill((*met)[0].et());
    }
  if(susyGenEvent->OSignDiLepton()==true && susyGenEvent->SSignDiLepton()==false)
    {
      nrLeptons_os_->Fill(susyGenEvent->numberOfLeptons());
      MET_OSDiLep_->Fill((*met)[0].et());
    }

  //std::cout << "Test 5" << std::endl;

  //-------------------------
  // kinematics of leptons
  //-------------------------

  nrLeptons_->Fill(susyGenEvent->numberOfLeptons());

  //------------------------------
  // kinematics of matched bjets
  //------------------------------

  double HTB=0;
  for(int hdx=0; hdx<(int)matchedbjets->size(); ++hdx)
    {
      HTB=HTB+(*matchedbjets)[hdx].et();
    }
  HTB_->Fill(HTB);

  // for debugging only
  //std::cout << susyGenEvent->decayCascadeA() << std::endl;

  //------------------------------------------------------
  // kinematics, topology of events with 2 matched bjets
  //------------------------------------------------------

  //std::cout << "Test 6" << std::endl;


  if(matchedbjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*matchedbjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*matchedbjets)[1].p4();
      reco::Particle::LorentzVector MET=(*met)[0].p4();

      double mbb=sqrt(bjet1.Dot(bjet2));
      double dPhi=abs(deltaPhi((*matchedbjets)[0].phi(),(*matchedbjets)[1].phi()));
      double dPhi1=abs(deltaPhi((*matchedbjets)[0].phi(),(*met)[0].phi()));
      double dPhi2=abs(deltaPhi((*matchedbjets)[1].phi(),(*met)[0].phi()));

      mbb_->Fill(mbb);
      angleb1b2_->Fill(abs(angle(bjet1,bjet2)));
      deltaPhi_b1b2_->Fill(dPhi);
      deltaPhi_b1MET_->Fill(dPhi1);
      deltaPhi_b2MET_->Fill(dPhi1);
      deltaPhi_b12MET_->Fill(abs(dPhi1-dPhi2));

      Bjet1_Et_->Fill((*matchedbjets)[0].et());
      Bjet2_Et_->Fill((*matchedbjets)[1].et());
      HT_2Bjets_->Fill((*matchedbjets)[0].et()+(*matchedbjets)[1].et());

      if(matchedqjets->size()>=1)
	{
	  Jet1_Et_2Bjets_->Fill((*matchedqjets)[0].et());
	  HT_2Bjets_1LightJet_->Fill((*matchedbjets)[0].et()+(*matchedbjets)[1].et()+(*matchedqjets)[0].et());
	}
    }

  //--------------------------------------------------------------
  // kinematics, topology of events with 2,3, ... matched bjets
  //--------------------------------------------------------------

  //std::cout << "Test 7" << std::endl;

  if(matchedbjets->size()>=2 && matchedqjets->size()>=2 && met->size()>0)
    {
      const pat::Jet& b1 = (*matchedbjets)[0];
      const pat::Jet& b2 = (*matchedbjets)[1];
      const pat::Jet& j1 = (*matchedqjets)[0];
      const pat::Jet& j2 = (*matchedqjets)[1];
      const pat::MET& met1 = (*met)[0];
 
      double DeltaMT_min1=0;
      double DeltaMT_min2=0;
      
      if(matchedmuons->size()>0 || matchedelectrons->size()>0 )
	{
	  if(matchedmuons->size()>0)
	    {
	      const pat::Particle& lep1=(*matchedmuons)[0];
	      std::vector<double> hypothesis1=SemiLepHypo(b1,b2,j1,j2,lep1,met1);
	      std::vector<double> hypothesis2=SemiLepHypo(b1,b2,j1,j2,lep1,met1);
	      DeltaMT_min1=hypothesis1[3];
	      DeltaMT_min2=hypothesis2[3];
	    }
	  else if (matchedelectrons->size()>0)
	    {
	      const pat::Particle& lep1=(*matchedelectrons)[0];
	      std::vector<double> hypothesis1=SemiLepHypo(b1,b2,j1,j2,lep1,met1);
	      std::vector<double> hypothesis2=SemiLepHypo(b1,b2,j1,j2,lep1,met1);
	      DeltaMT_min1=hypothesis1[3];
	      DeltaMT_min2=hypothesis2[3];
	    }
	  if(DeltaMT_min1>DeltaMT_min2) DeltaMT_min_->Fill(DeltaMT_min2);
	  else DeltaMT_min_->Fill(DeltaMT_min1);
	}
    }

  //std::cout << "Test 8" << std::endl;

  if(matchedbjets->size()==4)
    {
      //std::vector<TVector3> bjetsMET;
      std::vector<math::XYZVector> bjetsMET;

      for(int idx=0; idx<(int)matchedbjets->size(); ++idx)
	{
	  math::XYZVector bjetsp3;
	  
	  bjetsp3.SetX((*matchedbjets)[idx].px());
	  bjetsp3.SetY((*matchedbjets)[idx].py());
	  bjetsp3.SetZ((*matchedbjets)[idx].pz());
	  bjetsMET.push_back(bjetsp3);
	}

      math::XYZVector metp3;
      metp3.SetX((*met)[0].px());
      metp3.SetY((*met)[0].py());
      metp3.SetZ((*met)[0].pz());
      bjetsMET.push_back(metp3);

      EventShapeVariables evtshape(bjetsMET);

      double sphericity_bjetsMET = evtshape.sphericity();
      double aplanarity_bjetsMET = evtshape.aplanarity();
      double circularity_bjetsMET = evtshape.circularity();
      double isotropy_bjetsMET = evtshape.isotropy();
      
      sphericity_bjetsMET_->Fill(sphericity_bjetsMET);          
      aplanarity_bjetsMET_->Fill(aplanarity_bjetsMET);   
      circularity_bjetsMET_->Fill(circularity_bjetsMET);        
      isotropy_bjetsMET_->Fill(isotropy_bjetsMET);          
      
    }

  //std::cout << "Test 9" << std::endl;

  //--------------------------------------------------------------
  // kinematics, topology of events with 1 matched lepton
  //--------------------------------------------------------------

  //std::cout << "matchedmuons->size(): "      << matchedmuons->size() << std::endl;
  //std::cout << "matchedelectrons->size(): "  << matchedelectrons->size() << std::endl;

  if(nMatchedLeptons==1)
    {
      if(matchedmuons->size()==1)
	{
	  if((*matchedmuons)[0].pdgId())
	    {
	      double dPhiMu=abs(deltaPhi((*matchedmuons)[0].phi(),(*met)[0].phi()));
	      deltaPhi_MuMET_->Fill(dPhiMu);
	      deltaPhi_LepMET_->Fill(dPhiMu);
	    }
	}
      else if(matchedelectrons->size()==1)
	{
	  if((*matchedelectrons)[0].pdgId())
	    {
	      double dPhiEl=abs(deltaPhi((*matchedelectrons)[0].phi(),(*met)[0].phi()));
	      deltaPhi_ElMET_->Fill(dPhiEl);
	      deltaPhi_LepMET_->Fill(dPhiEl);
	    }
	}
    }

  //std::cout << "Test 10" << std::endl;

  //--------------------------------------------------------------
  // kinematics, topology of events with 2 matched lepton
  //--------------------------------------------------------------

  if(nMatchedLeptons==2)
    {
      if(matchedmuons->size()==2)
	{
	  if((*matchedmuons)[0].pdgId() && (*matchedmuons)[1].pdgId())
	    {
	      double dPhiMuMu=abs(deltaPhi((*matchedmuons)[0].phi(),(*matchedmuons)[1].phi()));
	      double dPhiMu1MET=abs(deltaPhi((*matchedmuons)[0].phi(),(*met)[0].phi()));
	      double dPhiMu2MET=abs(deltaPhi((*matchedmuons)[1].phi(),(*met)[0].phi()));
	      
	      deltaPhi_Mu1Mu2_->Fill(dPhiMuMu);
	      deltaPhi_Mu1MET_->Fill(dPhiMu1MET);
	      deltaPhi_Mu2MET_->Fill(dPhiMu2MET);
	      deltaPhi_Mu12MET_->Fill(abs(dPhiMu1MET-dPhiMu2MET));
	      
	      deltaPhi_Lep1Lep2_->Fill(dPhiMuMu);
	      deltaPhi_Lep1MET_->Fill(dPhiMu1MET);
	      deltaPhi_Lep2MET_->Fill(dPhiMu2MET);
	      deltaPhi_Lep12MET_->Fill(abs(dPhiMu1MET-dPhiMu2MET));
	    }
	}
      if(matchedelectrons->size()==2)
	{
	  if((*matchedelectrons)[0].pdgId() && (*matchedelectrons)[1].pdgId())
	    {
	      double dPhiElEl=abs(deltaPhi((*matchedelectrons)[0].phi(),(*matchedelectrons)[1].phi()));
	      double dPhiEl1MET=abs(deltaPhi((*matchedelectrons)[0].phi(),(*met)[0].phi()));
	      double dPhiEl2MET=abs(deltaPhi((*matchedelectrons)[1].phi(),(*met)[0].phi()));
	      deltaPhi_El1El2_->Fill(dPhiElEl);
	      deltaPhi_El1MET_->Fill(dPhiEl1MET);
	      deltaPhi_El2MET_->Fill(dPhiEl2MET);
	      deltaPhi_El12MET_->Fill(abs(dPhiEl1MET-dPhiEl2MET));
	      deltaPhi_Lep1Lep2_->Fill(dPhiElEl);
	      deltaPhi_Lep1MET_->Fill(dPhiEl1MET);
	      deltaPhi_Lep2MET_->Fill(dPhiEl2MET);
	      deltaPhi_Lep12MET_->Fill(abs(dPhiEl1MET-dPhiEl2MET));
	    }
	}
      if(matchedmuons->size()==1 && matchedelectrons->size()==1)
	{
	  if((*matchedmuons)[0].pdgId() && (*matchedelectrons)[0].pdgId())
	    {
	      double dPhiMuEl=abs(deltaPhi((*matchedmuons)[0].phi(),(*matchedelectrons)[0].phi()));
	      double dPhiLep1MET=abs(deltaPhi((*matchedmuons)[0].phi(),(*met)[0].phi()));
	      double dPhiLep2MET=abs(deltaPhi((*matchedelectrons)[0].phi(),(*met)[0].phi()));
	      deltaPhi_MuEl_->Fill(dPhiMuEl);
	      deltaPhi_MuElMET_->Fill(abs(dPhiLep1MET-dPhiLep2MET));
	      deltaPhi_Lep1Lep2_->Fill(dPhiMuEl);
	      deltaPhi_Lep1MET_->Fill(dPhiLep1MET);
	      deltaPhi_Lep2MET_->Fill(dPhiLep2MET);
	      deltaPhi_Lep12MET_->Fill(abs(dPhiLep1MET-dPhiLep2MET));
	    }
	}
    } 
}

// function to calculate invariant and transverse masses in the semileptonic dacay-channel
std::vector<double> SUSYGenEventAnalyzer::SemiLepHypo(const pat::Jet& bjet1,const pat::Jet& bjet2,const pat::Jet& jet3,const pat::Jet& jet4,const pat::Particle& lep0, const pat::MET& met1) 
{
  std::vector<double> solution;

  // 0,1 invariant masses
  reco::Particle::LorentzVector Lep4Jet_p4 = lep0.p4()+bjet1.p4()+bjet2.p4()+jet3.p4()+jet4.p4();
  double Lep4Jet_mass = sqrt((Lep4Jet_p4).Dot(Lep4Jet_p4));
  solution.push_back(Lep4Jet_mass); 

  reco::Particle::LorentzVector Lep4JetMet_p4 = Lep4Jet_p4+met1.p4();
  double Lep4JetMet_mass = sqrt((Lep4JetMet_p4).Dot(Lep4JetMet_p4));
  solution.push_back(Lep4JetMet_mass); 

  // 2 transverse mass
  double LepJetMet_px = (lep0.px()+met1.px()+bjet1.px()+bjet2.px()+jet3.px()+jet4.px());
  double LepJetMet_py = (lep0.py()+met1.py()+bjet1.py()+bjet2.py()+jet3.py()+jet4.py());
  double LepJetMet_px_square = (LepJetMet_px)*(LepJetMet_px);
  double LepJetMet_py_square = (LepJetMet_py)*(LepJetMet_py);
  
  double Lep4JetMet_mt = sqrt(Lep4JetMet_mass+ LepJetMet_px_square+LepJetMet_py_square);
  solution.push_back(Lep4JetMet_mt);

  reco::Particle::LorentzVector LepBjet1Met_p4 = lep0.p4()+met1.p4()+bjet1.p4();
  reco::Particle::LorentzVector Jets234_p4  = bjet2.p4()+jet3.p4()+jet4.p4();

  double LepBjet1Met_mass_square = LepBjet1Met_p4.Dot(LepBjet1Met_p4);
  double Jets234_mass_square  = Jets234_p4.Dot(Jets234_p4);

  double LepBjet1Met_px = (lep0.px() + met1.px() + bjet1.px());
  double LepBjet1Met_py = (lep0.py()+met1.py() + bjet1.py());

  double Jets234_px = (bjet2.px() + jet3.px() + jet4.px());
  double Jets234_py = (bjet2.py() + jet3.py() + jet4.py());

  double LepBjet1Met_px_square = (LepBjet1Met_px)*(LepBjet1Met_px); 
  double LepBjet1Met_py_square = (LepBjet1Met_py)*(LepBjet1Met_py);

  double Jets234_px_square = (Jets234_px)*(Jets234_px); 
  double Jets234_py_square = (Jets234_py)*(Jets234_py);

  double LepBjet1Met_mt = sqrt(LepBjet1Met_mass_square + LepBjet1Met_px_square + LepBjet1Met_py_square);
  double Jets234_mt = sqrt(Jets234_mass_square + Jets234_px_square + Jets234_py_square);
  
  // 3 delta mt
  double Delta_mt = LepBjet1Met_mt - Jets234_mt;
  solution.push_back(Delta_mt);

  // 4 delta ET
  double DeltaEt = LepBjet1Met_p4.Et() - Jets234_p4.Et();
  solution.push_back(DeltaEt);

  // 5 HT
  double Lep4JetMet_HT = lep0.et()+met1.et()+bjet1.et()+bjet2.et()+jet3.et()+jet4.et();
  solution.push_back(Lep4JetMet_HT);

  // 6 delta HT
//   double Lep4JetMet_DeltaHT = lep0.et()+met1.et()+bjet1.et()-bjet2.et()-jet3.et()-jet4.et();
//   solution.push_back(Lep4JetMet_DeltaHT);

  return solution;
}


void SUSYGenEventAnalyzer::beginJob()
{  
}

void SUSYGenEventAnalyzer::endJob()
{
}
