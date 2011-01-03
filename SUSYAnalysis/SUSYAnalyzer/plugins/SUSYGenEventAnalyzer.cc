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

using namespace std;

SUSYGenEventAnalyzer::SUSYGenEventAnalyzer(const edm::ParameterSet& cfg):
  inputGenEvent_(cfg.getParameter<edm::InputTag>("susyGenEvent")),
  initSubset_(cfg.getParameter<edm::InputTag>("initSubset")),
  jets_(cfg.getParameter<edm::InputTag>("jets"))
{ 
  edm::Service<TFileService> fs;

  nrBQuarks_gq_ = fs->make<TH1F>("nrBQuarks_gq",    "nr BQuarks gq",     9, -0.5, 8.5);
  nrBQuarks_gg_ = fs->make<TH1F>("nrBQuarks_gg",    "nr BQuarks gg",     9, -0.5, 8.5);
  nrBQuarks_qq_ = fs->make<TH1F>("nrBQuarks_qq",    "nr BQuarks qq",     9, -0.5, 8.5);
  nrBQuarks_other_ = fs->make<TH1F>("nrBQuarks_other",    "nr BQuarks other",     9, -0.5, 8.5);
  nrBQuarks_ = fs->make<TH1F>("nrBQuarks",    "nr BQuarks",     9, -0.5, 8.5);

  EtJet1_2BQuarks_gq_ = fs->make<TH1F>("EtJet1_2BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  EtJet1_2BQuarks_gg_ = fs->make<TH1F>("EtJet1_2BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  EtJet1_2BQuarks_qq_ = fs->make<TH1F>("EtJet1_2BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  EtJet1_2BQuarks_other_ = fs->make<TH1F>("EtJet1_2BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  EtJet1_2BQuarks_ = fs->make<TH1F>("EtJet1_2BQuarks_",    "Et Jet1",     30, 0, 900);

  EtJet1_012BQuarks_gq_ = fs->make<TH1F>("EtJet1_012BQuarks_gq",    "Et Jet1 gq",     30, 0, 900);
  EtJet1_012BQuarks_gg_ = fs->make<TH1F>("EtJet1_012BQuarks_gg",    "Et Jet1 gg",     30, 0, 900);
  EtJet1_012BQuarks_qq_ = fs->make<TH1F>("EtJet1_012BQuarks_qq",    "Et Jet1 qq",     30, 0, 900);
  EtJet1_012BQuarks_other_ = fs->make<TH1F>("EtJet1_012BQuarks_other",    "Et Jet1 other",     30, 0, 900);
  EtJet1_012BQuarks_ = fs->make<TH1F>("EtJet1_012BQuarks_",    "Et Jet1",     30, 0, 900);
}

SUSYGenEventAnalyzer::~SUSYGenEventAnalyzer()
{
}

void
SUSYGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<SUSYGenEvent> susyGenEvent;
  evt.getByLabel(inputGenEvent_, susyGenEvent);
  edm::Handle<reco::GenParticleCollection> initSubset;
  evt.getByLabel(initSubset_, initSubset);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);

  std::cout << "---------------------------------------------------------------------------------------------------"<< std::endl;
  std::cout << "| SUSGenEventAnalyzer: Decay cascade: " << susyGenEvent->decayCascadeA() << std::endl;
  std::cout << "---------------------------------------------------------------------------------------------------"<< std::endl;

  // number of bottom quarks for different processes of sparticle porduction
  if(susyGenEvent->GluinoSquarkDecay()) nrBQuarks_gq_->Fill(susyGenEvent->numberOfBQuarks());
  else if(susyGenEvent->GluinoGluinoDecay()) nrBQuarks_gg_->Fill(susyGenEvent->numberOfBQuarks());
  else if(susyGenEvent->SquarkSquarkDecay()) nrBQuarks_qq_->Fill(susyGenEvent->numberOfBQuarks());
  else nrBQuarks_other_->Fill(susyGenEvent->numberOfBQuarks());
  nrBQuarks_->Fill(susyGenEvent->numberOfBQuarks());
  
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
}

void SUSYGenEventAnalyzer::beginJob()
{  
}

void SUSYGenEventAnalyzer::endJob()
{
}
