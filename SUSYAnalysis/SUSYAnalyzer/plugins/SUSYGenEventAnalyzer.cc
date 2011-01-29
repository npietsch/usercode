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

  EtJet1_2BQuarks_gq_ = fs->make<TH1F>("EtJet1_2BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  EtJet1_2BQuarks_gg_ = fs->make<TH1F>("EtJet1_2BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  EtJet1_2BQuarks_qq_ = fs->make<TH1F>("EtJet1_2BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  EtJet1_2BQuarks_other_ = fs->make<TH1F>("EtJet1_2BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  EtJet1_2BQuarks_ = fs->make<TH1F>("EtJet1_2BQuarks",    "Et Jet1",     30, 0, 900);

  EtJet1_012BQuarks_gq_ = fs->make<TH1F>("EtJet1_012BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  EtJet1_012BQuarks_gg_ = fs->make<TH1F>("EtJet1_012BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  EtJet1_012BQuarks_qq_ = fs->make<TH1F>("EtJet1_012BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  EtJet1_012BQuarks_other_ = fs->make<TH1F>("EtJet1_012BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  EtJet1_012BQuarks_ = fs->make<TH1F>("EtJet1_012BQuarks",    "Et Jet1",     30, 0, 900);

  EtJet1_3456BQuarks_gq_ = fs->make<TH1F>("EtJet1_3456BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  EtJet1_3456BQuarks_gg_ = fs->make<TH1F>("EtJet1_3456BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  EtJet1_3456BQuarks_qq_ = fs->make<TH1F>("EtJet1_3456BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  EtJet1_3456BQuarks_other_ = fs->make<TH1F>("EtJet1_3456BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  EtJet1_3456BQuarks_ = fs->make<TH1F>("EtJet1_3456BQuarks",    "Et Jet1",     30, 0, 900);

  nrLep_ss_= fs->make<TH1F>("nrLep_ss",    "nr leptons same sign",     9, -0.5, 8.5);
  nrLep_os_= fs->make<TH1F>("nrLep_os",    "nr leptons opposite sign",     9, -0.5, 8.5);
  nrLep_= fs->make<TH1F>("nrLep",    "nr leptons",     9, -0.5, 8.5);

  angleb1b2_= fs->make<TH1F>("angleb1b2",    "angle (bjet1,bjet2)", 35, 0.,  3.5);
  mbb_= fs->make<TH1F>("mbb_",    "invariant bb mass", 30, 0.,  900);
  HTB_= fs->make<TH1F>("HTB_",    "HT (bjets)", 40, 0., 2000.);
  DeltaMT_min_ = fs->make<TH1F>("DeltaMT_min",    "Delta MT", 60, -300., 300.);

}

SUSYGenEventAnalyzer::~SUSYGenEventAnalyzer()
{
}

void
SUSYGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{
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

  int nmatchedbjets=0;
  for(int idx=0; idx<(int)matchedbjets->size(); ++idx) ++nmatchedbjets;

  int nbtags=0;
  for(int jdx=0; jdx<(int)bjets->size(); ++jdx) ++nbtags;

  // number of bottom quarks for different processes of sparticle porduction
  if(susyGenEvent->GluinoSquarkDecay()==true)
    {
      nrBQuarks_gq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_gg_->Fill(nmatchedbjets);
      nrBTags_gg_->Fill(nbtags);
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_gq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_gq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  else if(susyGenEvent->GluinoGluinoDecay()==true)
    {
      nrBQuarks_gg_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_gq_->Fill(nmatchedbjets);
      nrBTags_gq_->Fill(nbtags);
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_gg_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_gg_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  else if(susyGenEvent->SquarkSquarkDecay()==true)
    {
      nrBQuarks_qq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_qq_->Fill(nmatchedbjets);
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_qq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_qq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    } 
  else
    {
      nrBQuarks_other_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_other_->Fill(nmatchedbjets);
      nrBTags_other_->Fill(nbtags);
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  if(susyGenEvent->SSignSquarkSquarkDecay())
    {
      nrBQuarks_ssqq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_ssqq_->Fill(nmatchedbjets);
      nrBTags_ssqq_->Fill(nbtags);
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_ssqq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_ssqq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  
  if(susyGenEvent->OSignSquarkSquarkDecay())
    {
      nrBQuarks_osqq_->Fill(susyGenEvent->numberOfBQuarks());
      nrBJets_osqq_->Fill(nmatchedbjets);
      nrBTags_osqq_->Fill(nbtags);
      if(susyGenEvent->SSignDiLepton()==true) nrBQuarks_osqq_ssDiLep_->Fill(susyGenEvent->numberOfBQuarks());
      if(susyGenEvent->OSignDiLepton()==true) nrBQuarks_osqq_osDiLep_->Fill(susyGenEvent->numberOfBQuarks());
    }
  
  nrBQuarks_->Fill(susyGenEvent->numberOfBQuarks());
  nrBJets_->Fill(nmatchedbjets);
  nrBTags_->Fill(nbtags);
   
  // correlation betweem #BQuarks and et(jet1)
  if(susyGenEvent->numberOfBQuarks()==2)
    {
      if(susyGenEvent->GluinoSquarkDecay()) EtJet1_2BQuarks_gq_->Fill((*jets)[0].et());
      else if(susyGenEvent->GluinoGluinoDecay()) EtJet1_2BQuarks_gg_->Fill((*jets)[0].et());
      else if(susyGenEvent->SquarkSquarkDecay()) EtJet1_2BQuarks_qq_->Fill((*jets)[0].et());
      else EtJet1_2BQuarks_other_->Fill((*jets)[0].et());
      EtJet1_2BQuarks_->Fill((*jets)[0].et()); 
    }

  // correlation betweem #BQuarks and et(jet1)
  if(susyGenEvent->numberOfBQuarks()<=2)
    {
      if(susyGenEvent->GluinoSquarkDecay()) EtJet1_012BQuarks_gq_->Fill((*jets)[0].et());
      else if(susyGenEvent->GluinoGluinoDecay()) EtJet1_012BQuarks_gg_->Fill((*jets)[0].et());
      else if(susyGenEvent->SquarkSquarkDecay()) EtJet1_012BQuarks_qq_->Fill((*jets)[0].et());
      else EtJet1_012BQuarks_other_->Fill((*jets)[0].et());
      EtJet1_012BQuarks_->Fill((*jets)[0].et()); 
    }
  
  // correlation betweem #BQuarks and et(jet1)
  if(susyGenEvent->numberOfBQuarks()>=3)
    {
      if(susyGenEvent->GluinoSquarkDecay()) EtJet1_3456BQuarks_gq_->Fill((*jets)[0].et());
      else if(susyGenEvent->GluinoGluinoDecay()) EtJet1_3456BQuarks_gg_->Fill((*jets)[0].et());
      else if(susyGenEvent->SquarkSquarkDecay()) EtJet1_3456BQuarks_qq_->Fill((*jets)[0].et());
      else EtJet1_3456BQuarks_other_->Fill((*jets)[0].et());
      EtJet1_3456BQuarks_->Fill((*jets)[0].et()); 
    }

  //add histograms for correlation between same sign/ opposite sign lepton and same sign/ opposite sign squarks, GluinoGluino
  if(susyGenEvent->SSignDiLepton()==true) nrLep_ss_->Fill(susyGenEvent->numberOfLeptons());
  if(susyGenEvent->OSignDiLepton()==true) nrLep_os_->Fill(susyGenEvent->numberOfLeptons());
  nrLep_->Fill(susyGenEvent->numberOfLeptons());

  double HTB=0;
  for(int hdx=0; hdx<(int)matchedbjets->size(); ++hdx)
    {
      HTB=HTB+(*matchedbjets)[hdx].et();
    }
  HTB_->Fill(HTB);

  //std::cout << susyGenEvent->decayCascadeA() << std::endl;

  if(susyGenEvent->GluinoSquarkDecay()==true && matchedbjets->size()>=2 )
    {
      reco::Particle::LorentzVector bjet1=(*matchedbjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*matchedbjets)[1].p4();
      double mbb=0;
      mbb=sqrt(bjet1.Dot(bjet2));
      
      angleb1b2_->Fill(angle(bjet1,bjet2));
      mbb_->Fill(mbb);
    }
  
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

//   // 6 delta HT
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
