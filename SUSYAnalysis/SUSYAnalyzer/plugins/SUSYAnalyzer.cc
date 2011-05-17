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
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") )
{ 
  edm::Service<TFileService> fs;

  MET_ = fs->make<TH1F>("MET","MET", 40, 0., 1000.);
  MET_SSDiLepReco_ = fs->make<TH1F>("MET_SS_DiLepReco","MET", 40, 0., 1000.);
  MET_OSDiLepReco_ = fs->make<TH1F>("MET_OS_DiLepReco","MET", 40, 0., 1000.);
  HT_ = fs->make<TH1F>("HT","HT", 40, 0., 2000.);
  SigMET_ = fs->make<TH1F>("SigMET","SigMET", 20, 0., 20);

  nPV_ = fs->make<TH1F>("nPV","nPV", 20, 0., 20);

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
  HT_SigMET_ = fs->make<TH2F>("HT_SigMET","HT vs. SigMET", 40, 200., 2000., 40, 0., 20. );
  HTidxMETidx_= fs->make<TH2F>("HTidxMETidx","HTidx METidx", 38, 220., 600., 30, 0., 300. );

  nJets_ = fs->make<TH1F>("nJets","njets",16 , -0.5, 15.5);
  nMuons_ = fs->make<TH1F>("nMuons","nMuons",7 , -0.5, 6.5);
  nElectrons_ = fs->make<TH1F>("nElectrons","nElectrons",7 , -0.5, 6.5);
  nLeptons_ = fs->make<TH1F>("nLeptons","nLeptons",13 , -0.5, 12.5);
  MT_ = fs->make<TH1F>("MT","MT", 40, 0., 2000.);
  invMuMuMass_= fs->make<TH1F>("invMuMuMass","invMuMuMass",200,0.,200);

  RelIsoMu1_= fs->make<TH1F>("RelIsoMu1","RelIso Muon 1",40,0.,1.0);
  RelIsoMu2_= fs->make<TH1F>("RelIsoMu2","RelIso Muon 2",100,0.,5.0);

  for(int idx=0; idx<6; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));
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
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);

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

  double sigMET=((*met)[0].et())/(sqrt(HT));
  
  SigMET_->Fill(sigMET);
  HT_SigMET_->Fill(HT,sigMET);
  HT_MET_->Fill(HT,(*met)[0].et());

  nPV_->Fill(pvSrc->size());

  if(pvSrc->size()==1)
    {
      MET1pv_->Fill((*met)[0].et());
      HT1pv_->Fill(HT);
      nJets1pv_->Fill(njets);
      if(jets->size()>0)
	{
	  Jet0_Et1pv_->Fill((*jets)[0].et());
	}
      if(jets->size()>1)
	{
	  Jet0_Et1pv_->Fill((*jets)[1].et());
	} 
    }

  if(pvSrc->size()==2 && pvSrc->size()==3)
    {
      MET2pv_->Fill((*met)[0].et());
      HT2pv_->Fill(HT);
      nJets2pv_->Fill(njets);
      if(jets->size()>0)
	{
	  Jet0_Et2pv_->Fill((*jets)[0].et());
	}
      if(jets->size()>1)
	{
	  Jet0_Et2pv_->Fill((*jets)[1].et());
	} 
    }

  if(pvSrc->size()==4 && pvSrc->size()==5 && pvSrc->size()==6)
    {
      MET3pv_->Fill((*met)[0].et());
      HT3pv_->Fill(HT);
      nJets3pv_->Fill(njets);
      if(jets->size()>0)
	{
	  Jet0_Et3pv_->Fill((*jets)[0].et());
	}
      if(jets->size()>1)
	{
	  Jet0_Et3pv_->Fill((*jets)[1].et());
	} 
    }
  
  if(pvSrc->size()==7 && pvSrc->size()==8 && pvSrc->size()==9)
    {
      MET4pv_->Fill((*met)[0].et());
      HT4pv_->Fill(HT);
      nJets4pv_->Fill(njets);
      if(jets->size()>0)
	{
	  Jet0_Et4pv_->Fill((*jets)[0].et());
	}
      if(jets->size()>1)
	{
	  Jet0_Et4pv_->Fill((*jets)[1].et());
	} 
    }

  if(pvSrc->size()>=10)
    {
      MET5pv_->Fill((*met)[0].et());
      HT5pv_->Fill(HT);
      nJets5pv_->Fill(njets);
      if(jets->size()>0)
	{
	  Jet0_Et5pv_->Fill((*jets)[0].et());
	}
      if(jets->size()>1)
	{
	  Jet0_Et5pv_->Fill((*jets)[1].et());
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

	  if( (*met)[0].et() > METidx && HT > HTidx) HTidxMETidx_->Fill(HTidx,METidx);
	}
    }

  //-------------------------------------------------
  // Lepton pt, nMuons, nElectrons, nLeptons
  //-------------------------------------------------

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
      if(i<3) Muon_pt_[i]->Fill((*muons)[i].pt());
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

  RelIsoMu1_->Fill(RelIso1);
  RelIsoMu2_->Fill(RelIso2);

  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<3) Elec_pt_[i]->Fill((*electrons)[i].pt());
      nelectrons=nelectrons+1;
      nleptons=nleptons+1;
      lepHT=lepHT+(*electrons)[i].et();
      //std::cout << "electron charge: " << (*electrons)[i].charge() << std::endl;
      charge.push_back((*electrons)[i].charge());
      //if((*electrons)[i].genLepton()) std::cout << (*electrons)[i].genLepton()->pdgId() << std::endl;
    }
  nMuons_->Fill(nmuons);
  nElectrons_->Fill(nelectrons);
  nLeptons_->Fill(nleptons);
  
  double MT=lepHT+HT+(*met)[0].et();
  MT_->Fill(MT);
  
  if(nleptons==2)
    {
      int chargeSign=1;

      for(int cdx=0; cdx < (int)charge.size(); ++cdx)
	{
	  chargeSign=chargeSign*charge[cdx];  
	}
      if(chargeSign>0)MET_SSDiLepReco_->Fill((*met)[0].et());
      else if(chargeSign < 0) MET_OSDiLepReco_->Fill((*met)[0].et());
    }

  if(muons->size() >= 2)
    {
      double MuMu_p4_square = ((*muons)[0].p4()+(*muons)[1].p4()).Dot((*muons)[0].p4()+(*muons)[1].p4());
      invMuMuMass_->Fill(sqrt(MuMu_p4_square));
    }

}

void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
