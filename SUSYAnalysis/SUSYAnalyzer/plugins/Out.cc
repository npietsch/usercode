#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/Out.h"
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
 
Out::Out(const edm::ParameterSet& cfg):
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons"))
  
{ 
  edm::Service<TFileService> fs;

  JetsEt_ = fs->make<TH1F>("JetsEt" ,"JetsEt",  90, 0., 900.);
  JetsEta_= fs->make<TH1F>("JetsEta","JetsEta",    60, -3, 3);
  nJets_  = fs->make<TH1F>("nJets"  ,"nJets",   16, -0.5, 15);

  MuonsPt_ = fs->make<TH1F>("MuonsPt" ,"MuonsPt",  90, 0., 900.);
  MuonsEta_= fs->make<TH1F>("MuonsEta","MuonsEta",    60, -3, 3);
  nMuons_  = fs->make<TH1F>("nMuons"  ,"nMuons",   7, -0.5, 6.5);

  ElectronsPt_ = fs->make<TH1F>("ElectronsPt", "ElectronsPt",  90, 0., 900.);
  ElectronsEta_= fs->make<TH1F>("ElectronsEta","ElectronsEta",    60, -3, 3);
  nElectrons_  = fs->make<TH1F>("nElectrons"  ,"nElectrons",   7, -0.5, 6.5);

  nLeptons_= fs->make<TH1F>("nElectrons","nElectrons", 7, -0.5, 6.5);

  dRMuonJet_ = fs->make<TH1F>("dRMuonJet","dRMuonJet", 60, 0., 3.);
  dRElectronJet_ = fs->make<TH1F>("dRElectronJet","dRElectronJet", 60, 0., 3.);
  // Et
  for(int idx=0; idx<4; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon%i_pt",idx);
      Muon_pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Elecelectron%i_pt",idx);
      Electron_pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));
    }

  // eta
  for(int idx=0; idx<4; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Eta",idx);
      Jet_eta_.push_back(fs->make<TH1F>(histname,histname, 60, -3, 3));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon%i_eta",idx);
      Muon_eta_.push_back(fs->make<TH1F>(histname,histname, 60, -3, 3));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Elecelectron%i_eta",idx);
      Electron_eta_.push_back(fs->make<TH1F>(histname,histname, 60, -3, 3));
    }
}

Out::~Out()
{
}

void
Out::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //-------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);

  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);

  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);

  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  //-------------------------------------------------
  // event weight
  //-------------------------------------------------

  double weight=1;

  //-------------------------------------------------
  // Kinematics and dR
  //-------------------------------------------------

  // Jets
  int nJets=0;
  double dR=10;

  for(int idx=0; idx<(int)jets->size(); ++idx)
    {
      JetsEt_->Fill((*jets)[idx].et(),weight);
      if(idx<4) Jet_Et_[idx]->Fill((*jets)[idx].et(),weight);

      JetsEta_->Fill((*jets)[idx].eta(),weight);
      if(idx<4) Jet_eta_[idx]->Fill((*jets)[idx].eta(),weight);

      nJets=nJets+1;

      for(int mdx=0; mdx<(int)muons->size(); ++mdx)
	{
	  dR=abs(deltaR((*jets)[idx].eta(),(*jets)[idx].phi(),(*muons)[mdx].eta(),(*muons)[mdx].phi()));
	  dRMuonJet_->Fill(dR,weight);
	}
      for(int edx=0; edx<(int)electrons->size(); ++edx)
	{
	  dR=abs(deltaR((*jets)[idx].eta(),(*jets)[idx].phi(),(*electrons)[edx].eta(),(*electrons)[edx].phi()));
	  dRElectronJet_->Fill(dR,weight);
	}
    }
  nJets_->Fill(nJets,weight);

  // Muons
  int nMuons=0;

  for(int idx=0; idx<(int)muons->size(); ++idx)
    {
      MuonsPt_->Fill((*muons)[idx].et(),weight);
      if(idx<2) Muon_pt_[idx]->Fill((*muons)[idx].et(),weight);

      MuonsEta_->Fill((*muons)[idx].eta(),weight);
      if(idx<2) Muon_eta_[idx]->Fill((*muons)[idx].eta(),weight);

      nMuons=nMuons+1;
    }
  nMuons_->Fill(nMuons,weight);

  // Electrons
  int nElectrons=0;

  for(int idx=0; idx<(int)electrons->size(); ++idx)
    {
      ElectronsPt_->Fill((*electrons)[idx].et(),weight);
      if(idx<2) Electron_pt_[idx]->Fill((*electrons)[idx].et(),weight);

      ElectronsEta_->Fill((*electrons)[idx].eta(),weight);
      if(idx<2) Electron_eta_[idx]->Fill((*electrons)[idx].eta(),weight);

      nElectrons=nElectrons+1;
    }
  nElectrons_->Fill(nElectrons,weight);

  nLeptons_->Fill(nMuons+nElectrons, weight);

  std::cout << "-------------------------------------------------------------------------------------------" << std::endl;
  std::cout << "OUT MODULE. Pt Jets, Muon, MET: " << (*jets)[0].pt() << " " << (*jets)[1].pt() << " " << (*jets)[2].pt() << " " << (*jets)[3].pt() << " " << (*muons)[0].pt() << " " << (*met)[0].et() << std::endl;
  std::cout << "-------------------------------------------------------------------------------------------" << std::endl;
}

void Out::beginJob()
{  
} 

void Out::endJob()
{
}
