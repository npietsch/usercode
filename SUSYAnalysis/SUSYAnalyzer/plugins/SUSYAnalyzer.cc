#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"\

using namespace std;
 
SUSYAnalyzer::SUSYAnalyzer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("source")),
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons"))
{ 
  edm::Service<TFileService> fs;
  MET_ = fs->make<TH1F>("MET","MET", 40, 0., 1000.);
  HT_ = fs->make<TH1F>("HT","HT", 40, 0., 2000.);
  nJets_ = fs->make<TH1F>("nJets","njets",16 , -0.5, 15.5);
  nMuons_ = fs->make<TH1F>("nMuons","nMuons",7 , -0.5, 6.5);
  nElec_ = fs->make<TH1F>("nElectrons","nElectrons",7 , -0.5, 6.5);
  nLep_ = fs->make<TH1F>("nLeptons","nLeptons",13 , -0.5, 12.5);
  HTall_ = fs->make<TH1F>("HTall","HT all", 40, 0., 2000.);

  for(int idx=0; idx<6; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet_Et_%i",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 30, 0., 900.));
    }
  for(int idx=0; idx<3; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon_Et_%i",idx);
      Muon_pt_.push_back(fs->make<TH1F>(histname,histname, 20, 0., 600.));
    }
  for(int idx=0; idx<3; ++idx)
    {
      char histname[20];
      sprintf(histname,"Elec_Et_%i",idx);
      Elec_pt_.push_back(fs->make<TH1F>(histname,histname, 20, 0., 600.));
    }
}

SUSYAnalyzer::~SUSYAnalyzer()
{
}

void
SUSYAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{  
  //--------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<reco::GenParticleCollection> src;
  evt.getByLabel(src_, src);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  //-------------------------------------------------
  // Jet Et, MET, HT, nJets
  //-------------------------------------------------

  double HT=0;
  int njets=0;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      if(i<6) Jet_Et_[i]->Fill((*jets)[i].et());
      HT=HT+(*jets)[i].et();
      njets=njets+1;
    }

  MET_->Fill((*met)[0].et());
  HT_->Fill(HT);
  nJets_->Fill(njets);

  //-------------------------------------------------
  // Lepton pt, nMuons, nElectrons, nLeptons
  //-------------------------------------------------

  int nlep=0;
  int nmuons=0;
  int nelec=0;
  double HTlep=0;

  for(int i=0; i<(int)muons->size(); ++i)
    {
      if(i<3) Muon_pt_[i]->Fill((*muons)[i].pt());
      nmuons=nmuons+1;
      nlep=nlep+1;
      HTlep=HTlep+(*muons)[i].et();
    }
  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<3) Elec_pt_[i]->Fill((*electrons)[i].pt());
      nelec=nelec+1;
      nlep=nlep+1;
      HTlep=HTlep+(*electrons)[i].et();
    }
  nMuons_->Fill(nmuons);
  nElec_->Fill(nelec);
  nLep_->Fill(nlep);

  double MT=HTlep+HT+(*met)[0].et();

  HTall_->Fill(MT);
}


void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
