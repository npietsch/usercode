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

  number_of_BQuarks_ = fs->make<TH1F>("nr_BQuarks",    "nr BQuarks",     9, -0.5, 8.5);
  number_of_BQuarks_sgsg_ = fs->make<TH1F>("nr_BQuarks_sgsg",    "nr BQuarks for sgsg",     9, -0.5, 8.5);
  number_of_BQuarks_sqsq_ = fs->make<TH1F>("nr_BQuarks_sqsq",    "nr BQuarks for sqsq",     9, -0.5, 8.5);
  number_of_BQuarks_sgsq_ = fs->make<TH1F>("nr_BQuarks_sgsq",    "nr BQuarks for sgsq",     9, -0.5, 8.5);

  number_of_BQuarks_jet1_et_ = fs->make<TH2F>("nr_BQuarks_jet1_et",    "nr BQuarks vs. jet1 et",     9, -0.5, 8.5, 30, 0, 900);
  jet1_et_0BQuarks_ = fs->make<TH1F>("jet1_et_0BQuarks",    "et jet1",     30, 0, 900);
  jet1_et_2BQuarks_ = fs->make<TH1F>("jet1_et_2BQuarks",    "et jet1",     30, 0, 900);
  jet1_et_4BQuarks_ = fs->make<TH1F>("jet1_et_4BQuarks",    "et jet1",     30, 0, 900);
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

  number_of_BQuarks_->Fill(susyGenEvent->numberOfBQuarks());
  
  reco::GenParticleCollection initSub=*initSubset;

  //for(reco::GenParticleCollection::const_iterator p=initSub.begin(); p!=initSub.end(); ++p){
  //  std::cout << "pdg-ID: " << p->pdgId() << std::endl;
  //}
  
  const std::vector<pat::Jet>& Jets=*jets;
  std::vector<pat::Jet>::const_iterator jet = Jets.begin();

  number_of_BQuarks_jet1_et_->Fill(susyGenEvent->numberOfBQuarks(),jet[0].et());

  if(susyGenEvent->numberOfBQuarks()==0)
    {
      jet1_et_0BQuarks_->Fill(jet[0].et());
    }
  if(susyGenEvent->numberOfBQuarks()==2)
    {
      jet1_et_2BQuarks_->Fill(jet[0].et());
    }
  if(susyGenEvent->numberOfBQuarks()==4)
    {
      jet1_et_4BQuarks_->Fill(jet[0].et());
    }

  //std::cout << "Test1" << std::cout << endl;

  if(susyGenEvent->GluinoGluinoDecay()==true)
    {
      //std::cout << "Test2" << std::cout << endl;
      number_of_BQuarks_sgsg_->Fill(susyGenEvent->numberOfBQuarks());
    }
  if(susyGenEvent->SquarkSquarkDecay()==true)
    {
      //std::cout << "Test3" << std::cout << endl;
      number_of_BQuarks_sqsq_->Fill(susyGenEvent->numberOfBQuarks());
    }
  if(susyGenEvent->GluinoSquarkDecay()==true)
    {
      //std::cout << "Test4" << std::cout << endl;
      number_of_BQuarks_sgsq_->Fill(susyGenEvent->numberOfBQuarks());
    }

}

void SUSYGenEventAnalyzer::beginJob()
{  
}

void SUSYGenEventAnalyzer::endJob()
{
}
