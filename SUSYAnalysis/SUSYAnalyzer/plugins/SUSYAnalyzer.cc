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

using namespace std;
 
SUSYAnalyzer::SUSYAnalyzer(const edm::ParameterSet& cfg):
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  lightJets_         (cfg.getParameter<edm::InputTag>("lightJets")),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") )
{ 
  edm::Service<TFileService> fs;

  JetEt_nrBjets_ = fs->make<TH2F>("JetEt_nrBjets","JetEt nrBjets", 30,0.,300.,5,0.,5.);

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

  Electron0_eta_=fs-> make<TH1F>("Elec0_eta","Elec0 eta", 60, -3, 3);
  Muon0_eta_=fs-> make<TH1F>("Elec0_eta","Elec0 eta", 60, -3, 3);

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

  mW_=fs-> make<TH1F>("mW","mW", 40 , 0, 200);

  mW_MET50_=fs-> make<TH1F>("mW_MET50","mW_MET50", 40 , 0, 200);
  mW_MET100_=fs-> make<TH1F>("mW_MET100","mW MET100", 40 , 0, 200);
  mW_MET150_=fs-> make<TH1F>("mW_MET150","mW MET150", 40 , 0, 200);
  mW_MET200_=fs-> make<TH1F>("mW_MET200","mW MET200", 40 , 0, 200);
  mW_MET250_=fs-> make<TH1F>("mW_MET250","mW MET250", 40 , 0, 200);
  mW_MET300_=fs-> make<TH1F>("mW_MET300","mW MET300", 40 , 0, 200);

  mW_4Jets_=fs-> make<TH1F>("mW_4Jets","mW 4Jets", 40 , 0, 200);
  mW_5Jets_=fs-> make<TH1F>("mW_5Jets","mW 5Jets", 40 , 0, 200);
  mW_6Jets_=fs-> make<TH1F>("mW_6Jets","mW 6Jets", 40 , 0, 200);
  mW_7Jets_=fs-> make<TH1F>("mW_7Jets","mW 7Jets", 40 , 0, 200);
  mW_8Jets_=fs-> make<TH1F>("mW_8Jets","mW 8Jets", 40 , 0, 200);
  mW_9Jets_=fs-> make<TH1F>("mW_9Jets","mW 9Jets", 40 , 0, 200);

  mW_HT300_=fs-> make<TH1F>("mW_HT300","mW HT300", 40 , 0, 200);
  mW_HT400_=fs-> make<TH1F>("mW_HT400","mW HT400", 40 , 0, 200);
  mW_HT500_=fs-> make<TH1F>("mW_HT500","mW HT500", 40 , 0, 200);
  mW_HT600_=fs-> make<TH1F>("mW_HT600","mW HT600", 40 , 0, 200);
  mW_HT700_=fs-> make<TH1F>("mW_HT700","mW HT700", 40 , 0, 200);
  mW_HT800_=fs-> make<TH1F>("mW_HT800","mW HT800", 40 , 0, 200);

  mW_MET_=fs-> make<TH2F>("mW_MET","MET vs. mW", 40, 0., 1000.,16 , -0.5, 15.5 );
  mW_nJets_=fs-> make<TH2F>("mW_nJets","nJets vs. mW", 40, 0., 200.,16 , -0.5, 15.5 );
  mW_HT_=fs-> make<TH2F>("mW_HT","HT vs. mW", 40, 0., 2000.,16 , -0.5, 15.5 );
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

  double HTBjets=0;
  double HTLightJets=0;

  if(bjets->size()>0 && lightJets->size()>0 && jets->size()>0)
    {
      for(int i=0; i<(int)bjets->size(); ++i)
	{
	  double frac=((*bjets)[i].et())*(jets->size())/HT;
	  if(i<4) Bjet_EtFrac_[i]->Fill(frac);
	  HTBjets=HTBjets+(*bjets)[i].et();
	}
      for(int i=0; i<(int)lightJets->size(); ++i)
	{
	  double frac=((*lightJets)[i].et())*(lightJets->size())/HT;
	  if(i<4) LightJet_EtFrac_[i]->Fill(frac);
	  HTLightJets=HTLightJets+(*lightJets)[i].et();
	}
      double BjetsFrac=(HTBjets/(bjets->size()))/(HT/(jets->size()));
      double LightJetsFrac=(HTLightJets/(lightJets->size()))/(HT/(jets->size()));

      Bjets_EtFrac_->Fill(BjetsFrac);
      LightJets_EtFrac_->Fill(LightJetsFrac);
    }

  if(jets->size()>0)
    {
      JetEt_nrBjets_->Fill(HT/(jets->size()),bjets->size());
    }

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

  if(pvSrc->size()==2 || pvSrc->size()==3)
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

  if(pvSrc->size()==4 || pvSrc->size()==5 || pvSrc->size()==6)
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
  
  if(pvSrc->size()==7 || pvSrc->size()==8 || pvSrc->size()==9)
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

  if(muons->size()>0) Muon0_eta_->Fill((*muons)[0].eta());
  if(electrons->size()>0) Electron0_eta_->Fill((*electrons)[0].eta());

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

  //transverse W-mass
  double mW=0;
  if(muons->size()==1)
    {
      mW=sqrt(2*(((*met)[0].et())*((*muons)[0].et())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
    }
  if(electrons->size()==1)
    {
      mW=sqrt(2*(((*met)[0].et())*((*electrons)[0].et())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
    }
  
  else if(mW > 0)
    {
      mW_->Fill(mW);

      mW_MET_->Fill(mW,(*met)[0].et());
      mW_nJets_->Fill(mW,jets->size());
      mW_HT_->Fill(mW,HT);

      if((*met)[0].et()>= 50 &&(*met)[0].et()<100) mW_MET50_->Fill(mW);
      else if((*met)[0].et()>= 100 &&(*met)[0].et()<150) mW_MET100_->Fill(mW);
      else if((*met)[0].et()>= 150 &&(*met)[0].et()<200) mW_MET150_->Fill(mW);
      else if((*met)[0].et()>= 200 &&(*met)[0].et()<250) mW_MET200_->Fill(mW);
      else if((*met)[0].et()>= 250 &&(*met)[0].et()<300) mW_MET250_->Fill(mW);
      else if((*met)[0].et()>= 300) mW_MET300_->Fill(mW);
      
      if(jets->size()==4) mW_4Jets_->Fill(mW);
      else if(jets->size()==5) mW_5Jets_->Fill(mW);
      else if(jets->size()==6) mW_6Jets_->Fill(mW);
      else if(jets->size()==7) mW_7Jets_->Fill(mW);
      else if(jets->size()==8) mW_8Jets_->Fill(mW);
      else if(jets->size()>=9) mW_9Jets_->Fill(mW);

      if(HT >= 300 && HT < 400) mW_HT300_->Fill(HT);
      else if(HT >= 400 && HT < 500) mW_HT400_->Fill(HT);
      else if(HT >= 500 && HT < 600) mW_HT500_->Fill(HT);
      else if(HT >= 600 && HT < 700) mW_HT600_->Fill(HT);
      else if(HT >= 700 && HT < 800) mW_HT700_->Fill(HT);
      else if(HT >= 800) mW_HT800_->Fill(HT);
    }
}

void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
