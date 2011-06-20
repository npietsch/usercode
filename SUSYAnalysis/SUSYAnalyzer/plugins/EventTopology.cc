#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "PhysicsTools/CandUtils/interface/EventShapeVariables.h"
#include "TVector3.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/EventTopology.h"

using namespace std;
 
EventTopology::EventTopology(const edm::ParameterSet& cfg):
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  mediumJets_   (cfg.getParameter<edm::InputTag>("mediumJets")),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") ) 
{ 
  edm::Service<TFileService> fs;
  
  nrLep_nrBjets_ = fs->make<TH2F>("nrLep_nrBjets" , "nrLep vs. nrBjets" , 5, 0., 5., 5, 0, 5.);
  nrJets_nrBjets_ = fs->make<TH2F>("nrJets_nrBjets" , "nrJets vs. nrBjets" , 12, 0., 12., 5, 0, 5.);
  nrMJets_nrBjets_ = fs->make<TH2F>("nrMJets_nrBjets" , "nrMJets vs. nrBjets" , 12, 0., 12., 5, 0, 5.);
  Jet0_Et_nrBjets_ = fs->make<TH2F>("Jet0_Et_nrBjets" , "Jet0 Et vs. nrBjets" , 90, 0., 900., 5, 0, 5.);

  sphericity_bjets_  = fs->make<TH1F>("sphericity_bjets" , "sphericity(bjets)" , 20, 0., 1.);         
  aplanarity_bjets_  = fs->make<TH1F>("aplanarity_bjets" ,"aplanarity(bjets)"  , 20, 0., 1.);   
  circularity_bjets_ = fs->make<TH1F>("circularity_bjets" ,"circularity(bjets)", 20, 0., 1.);        
  isotropy_bjets_    = fs->make<TH1F>("isotropy_bjets" , "isotropy(bjets)"     , 20, 0., 1.);
  
  sphericity_bjetsMET_  = fs->make<TH1F>("sphericity_bjetsMET" , "sphericity(bjetsMET)" , 20, 0., 1.);         
  aplanarity_bjetsMET_  = fs->make<TH1F>("aplanarity_bjetsMET" ,"aplanarity(bjetsMET)"  , 20, 0., 1.);   
  circularity_bjetsMET_ = fs->make<TH1F>("circularity_bjetsMET" ,"circularity(bjetsMET)", 20, 0., 1.);        
  isotropy_bjetsMET_    = fs->make<TH1F>("isotropy_bjetsMET" , "isotropy(bjetsMET)"     , 20, 0., 1.);
  
  sphericity_bjetsLep_  = fs->make<TH1F>("sphericity_bjetsLep" , "sphericity(bjetsLep)" , 20, 0., 1.);         
  aplanarity_bjetsLep_  = fs->make<TH1F>("aplanarity_bjetsLep" ,"aplanarity(bjetsLep)"  , 20, 0., 1.);   
  circularity_bjetsLep_ = fs->make<TH1F>("circularity_bjetsLep" ,"circularity(bjetsLep)", 20, 0., 1.);        
  isotropy_bjetsLep_    = fs->make<TH1F>("isotropy_bjetsLep" , "isotropy(bjetsLep)"     , 20, 0., 1.);
  
  sphericity_bjetsMETLep_  = fs->make<TH1F>("sphericity_bjetsMETLep" , "sphericity(bjetsMETLep)" , 20, 0., 1.);         
  aplanarity_bjetsMETLep_  = fs->make<TH1F>("aplanarity_bjetsMETLep" ,"aplanarity(bjetsMETLep)"  , 20, 0., 1.);   
  circularity_bjetsMETLep_ = fs->make<TH1F>("circularity_bjetsMETLep" ,"circularity(bjetsMETLep)", 20, 0., 1.);        
  isotropy_bjetsMETLep_    = fs->make<TH1F>("isotropy_bjetsMETLep" , "isotropy(bjetsMETLep)"     , 20, 0., 1.);
  
  for(int i=0; i<4; ++i)
    {
      char histname1[20];
      sprintf(histname1,"dR_bjet%i_met",i);
      dR_BjetMET_[i]=fs->make<TH1F>(histname1,"dR(bjet,MET)", 15, 0., 3.);
      char histname2[20];
      sprintf(histname2,"dPhi_bjet%i_met",i);
      dPhi_BjetMET_[i]=fs->make<TH1F>(histname2,"dPhi(bjet,MET)", 15, 0., 3.);
      char histname3[20];
      sprintf(histname3,"dTheta_bjet%i_met",i);
      dTheta_BjetMET_[i]=fs->make<TH1F>(histname3,"dTheta(bjet,MET)", 15, 0., 3.);
      char histname4[20];
      sprintf(histname4,"angle_bjet%i_met",i);
      angle_BjetMET_[i]=fs->make<TH1F>(histname4,"angle(bjet,MET)", 15, 0., 3.);
      
      for(int j=0; j<2; ++j)
	{
	  char histname1b[20];
	  sprintf(histname1b,"dR_bjet%i_lep%i",i,j);
	  dR_BjetLep_[i][j]=fs->make<TH1F>(histname1b,"dR(bjet,lep)", 15, 0., 3.);
	  char histname2b[20];
	  sprintf(histname2b,"dPhi_bjet%i_lep%i",i,j);
	  dPhi_BjetLep_[i][j]=fs->make<TH1F>(histname2b,"dPhi(bjet,lep)", 15, 0., 3.);
	  char histname3b[20];
	  sprintf(histname3b,"dTheta_bjet%i_lep%i",i,j);
	  dTheta_BjetLep_[i][j]=fs->make<TH1F>(histname3b,"dTheta(bjet,lep)", 15, 0., 3.);
	  char histname4b[20];
	  sprintf(histname4b,"angle_bjet%i_lep%i",i,j);
	  angle_BjetLep_[i][j]=fs->make<TH1F>(histname4b,"angle(bjet,lep)", 15, 0., 3.);
	}
      
      for(int k=i+1; k<4; ++k)
	{
	  char histname1b[20];
	  sprintf(histname1b,"dR_bjet%i_bjet%i",i,k);
	  dR_BjetBjet_[i][k]=fs->make<TH1F>(histname1b,"dR(bjet,bjet)", 15, 0., 3.);
	  char histname2b[20];
	  sprintf(histname2b,"dPhi_bjet%i_bjet%i",i,k);
	  dPhi_BjetBjet_[i][k]=fs->make<TH1F>(histname2b,"dPhi(bjet,bjet)", 15, 0., 3.);
	  char histname3b[20];
	  sprintf(histname3b,"dTheta_bjet%i_bjet%i",i,k);
	  dTheta_BjetBjet_[i][k]=fs->make<TH1F>(histname3b,"dTheta(bjet,bjet)", 15, 0., 3.);
	  char histname4b[20];
	  sprintf(histname4b,"angle_bjet%i_bjet%i",i,k);
	  angle_BjetBjet_[i][k]=fs->make<TH1F>(histname4b,"angle(bjet,bjet)", 15, 0., 3.);
	}
    }
  
  for(int i=0; i<2; ++i)
    {
      char histname1[20];
      sprintf(histname1,"dR_lep%i_met",i);
      dR_LepMET_[i]=fs->make<TH1F>(histname1,"dR(lep,MET)", 15, 0., 3.);
      char histname2[20];
      sprintf(histname2,"dPhi_lep%i_met",i);
      dPhi_LepMET_[i]=fs->make<TH1F>(histname2,"dPhi(lep,MET)", 15, 0., 3.);
      char histname3[20];
      sprintf(histname3,"dTheta_lep%i_met",i);
      dTheta_LepMET_[i]=fs->make<TH1F>(histname3,"dTheta(lep,MET)", 15, 0., 3.);
      char histname4[20];
      sprintf(histname4,"angle_lep%i_met",i);
      angle_LepMET_[i]=fs->make<TH1F>(histname4,"angle(lep,MET)", 15, 0., 3.); 
    }
  
  dRBjetMETMin_=fs->make<TH1F>("dRBjetMETMin","dRBjetMETMin", 15, 0., 3.);
  dPhiBjetMETMin_=fs->make<TH1F>("dPhiBjetMETMin","dPhiBjetMETMin", 15, 0., 3.);
  dThetaBjetMETMin_=fs->make<TH1F>("dThetaBjetMETMin","dThetaBjetMETMin", 15, 0., 3.);
  AngleBjetMETMin_=fs->make<TH1F>("AngleBjetMETMin", "AngleBjetMETMin",15, 0., 3.);
  
  dRBjetMETMax_=fs->make<TH1F>("dRBjetMETMax","dRBjetMETMax", 15, 0., 3.);
  dPhiBjetMETMax_=fs->make<TH1F>("dPhiBjetMETMax","dPhiBjetMETMax", 15, 0., 3.);
  dThetaBjetMETMax_=fs->make<TH1F>("dThetaBjetMETMax","dThetaBjetMETMax", 15, 0., 3.);
  AngleBjetMETMax_=fs->make<TH1F>("AngleBjetMETMax","AngleBjetMETMax", 15, 0., 3.);
  
  dRBjetBjetMin_=fs->make<TH1F>("dRBjetBjetMin", "dRBjetBjetMin",15, 0., 3.);
  dPhiBjetBjetMin_=fs->make<TH1F>("dPhiBjetBjetMin","dPhiBjetBjetMin", 15, 0., 3.);
  dThetaBjetBjetMin_=fs->make<TH1F>("dThetaBjetBjetMin","dThetaBjetBjetMin", 15, 0., 3.);
  AngleBjetBjetMin_=fs->make<TH1F>("AngleBjetBjetMin","AngleBjetBjetMin", 15, 0., 3.);
  
  dRBjetBjetMax_=fs->make<TH1F>("dRBjetBjetMax", "dRBjetBjetMax",15, 0., 3.);
  dPhiBjetBjetMax_=fs->make<TH1F>("dPhiBjetBjetMax","dPhiBjetBjetMax", 15, 0., 3.);
  dThetaBjetBjetMax_=fs->make<TH1F>("dThetaBjetBjetMax","dThetaBjetBjetMax", 15, 0., 3.);
  AngleBjetBjetMax_=fs->make<TH1F>("AngleBjetBjetMax","AngleBjetBjetMax", 15, 0., 3.);
  
  dRBjetLepMin_=fs->make<TH1F>("dRBjetLepMin", "dRBjetLepMin",15, 0., 3.);
  dPhiBjetLepMin_=fs->make<TH1F>("dPhiBjetLepMin","dPhiBjetLepMin", 15, 0., 3.);
  dThetaBjetLepMin_=fs->make<TH1F>("dThetaBjetLepMin","dThetaBjetLepMin", 15, 0., 3.);
  AngleBjetLepMin_=fs->make<TH1F>("AngleBjetLepMin","AngleBjetLepMin", 15, 0., 3.);
  
  dRBjetLepMax_=fs->make<TH1F>("dRBjetLepMax", "dRBjetLepMax",15, 0., 3.);
  dPhiBjetLepMax_=fs->make<TH1F>("dPhiBjetLepMax","dPhiBjetLepMax", 15, 0., 3.);
  dThetaBjetLepMax_=fs->make<TH1F>("dThetaBjetLepMax","dThetaBjetLepMax", 15, 0., 3.);
  AngleBjetLepMax_=fs->make<TH1F>("AngleBjetLepMax","AngleBjetLepMax", 15, 0., 3.);
  
  dRLepMETMin_=fs->make<TH1F>("dRLepMETMin","dRLepMETMin", 15, 0., 3.);
  dPhiLepMETMin_=fs->make<TH1F>("dPhiLepMETMin","dPhiLepMETMin", 15, 0., 3.);
  dThetaLepMETMin_=fs->make<TH1F>("dThetaLepMETMin","dThetaLepMETMin", 15, 0., 3.);
  AngleLepMETMin_=fs->make<TH1F>("AngleLepMETMin", "AngleLepMETMin",15, 0., 3.);
  
  dRLepMETMax_=fs->make<TH1F>("dRLepMETMax","dRLepMETMax", 15, 0., 3.);
  dPhiLepMETMax_=fs->make<TH1F>("dPhiLepMETMax","dPhiLepMETMax", 15, 0., 3.);
  dThetaLepMETMax_=fs->make<TH1F>("dThetaLepMETMax","dThetaLepMETMax" , 15, 0., 3.);
  AngleLepMETMax_=fs->make<TH1F>("AngleLepMETMax","AngleLepMETMax", 15, 0., 3.);

  dPhiMediumJetMETMin_=fs->make<TH1F>("dPhiMJetMETMin","dPhiMJetMETMin", 15, 0., 3.);

  nJets_dRLepMETMin_=fs->make<TH2F>("nJets_dRLepMETMin","nJets vs. dRLepMETMin", 15, 0., 3., 15., 0., 15.);
  nJets_dPhiLepMETMin_=fs->make<TH2F>("nJets_dPhiLepMETMin","nJets vs. dPhiLepMETMin", 15, 0., 3., 15., 0., 15.);
}

EventTopology::~EventTopology()
{
}

void
EventTopology::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{  
  //-------------------------------------
  // Handles
  //-------------------------------------
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > mediumJets;
  evt.getByLabel(mediumJets_, mediumJets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);

  //----------------------------------------------
  // Correlations
  //---------------------------------------------

  int nrElectrons=electrons->size();
  int nrMuons=muons->size();
  int nrJets=jets->size();
  int nrMediumJets=mediumJets->size();
  int nrBjets=bjets->size();

  nrLep_nrBjets_->Fill(nrElectrons+nrMuons,nrBjets);
  nrJets_nrBjets_->Fill(nrJets,nrBjets);
  nrMJets_nrBjets_->Fill(nrMediumJets,nrBjets);
  if(jets->size()>0) Jet0_Et_nrBjets_->Fill((*jets)[0].et(),nrBjets);

  //----------------------------------------------
  // deltaR, deltaPhi, deltaTheta, opening angle
  //----------------------------------------------

  double dRBjetMETMin=9;
  double dPhiBjetMETMin=9;
  double dThetaBjetMETMin=9;
  double AngleBjetMETMin=9;

  double dRBjetMETMax=-1;
  double dPhiBjetMETMax=-1;
  double dThetaBjetMETMax=-1;
  double AngleBjetMETMax=-1;

  double dRBjetBjetMin=9;
  double dPhiBjetBjetMin=9;
  double dThetaBjetBjetMin=9;
  double AngleBjetBjetMin=9;

  double dRBjetBjetMax=-1;
  double dPhiBjetBjetMax=-1;
  double dThetaBjetBjetMax=-1;
  double AngleBjetBjetMax=-1;

  double dRBjetLepMin=9;
  double dPhiBjetLepMin=9;
  double dThetaBjetLepMin=9;
  double AngleBjetLepMin=9;

  double dRBjetLepMax=-1;
  double dPhiBjetLepMax=-1;
  double dThetaBjetLepMax=-1;
  double AngleBjetLepMax=-1;

  double dRLepMETMin=9;
  double dPhiLepMETMin=9;
  double dThetaLepMETMin=9;
  double AngleLepMETMin=9;

  double dRLepMETMax=-1;
  double dPhiLepMETMax=-1;
  double dThetaLepMETMax=-1;
  double AngleLepMETMax=-1;

  for(int idx=0; idx<(int)bjets->size(); ++idx)
    {
      if(bjets->size()<=4)
	{
	  reco::Particle::LorentzVector Bjet1=(*bjets)[idx].p4();
	  
	  if(met->size()>0)
	    {
	      reco::Particle::LorentzVector MET=(*met)[0].p4();
	      double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
	      double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*met)[0].phi()));
	      double dTheta=abs(((*bjets)[idx].theta())-((*met)[0].theta()));
	      double Angle=abs(angle(Bjet1,MET));

	      dR_BjetMET_[idx]->Fill(dR);
	      dPhi_BjetMET_[idx]->Fill(dPhi);
	      dTheta_BjetMET_[idx]->Fill(dTheta);
	      angle_BjetMET_[idx]->Fill(Angle);

	      if(dR<dRBjetMETMin) dRBjetMETMin=dR;
	      if(dPhi<dPhiBjetMETMin) dPhiBjetMETMin=dPhi;
	      if(dTheta<dThetaBjetMETMin) dThetaBjetMETMin=dTheta;
	      if(Angle<AngleBjetMETMin) AngleBjetMETMin=Angle;

	      if(dR>dRBjetMETMax) dRBjetMETMax=dR;
	      if(dPhi>dPhiBjetMETMax) dPhiBjetMETMax=dPhi;
	      if(dTheta>dThetaBjetMETMax) dThetaBjetMETMax=dTheta;
	      if(Angle>AngleBjetMETMax) AngleBjetMETMax=Angle;
	    }
	  
	  for(int mdx=0; mdx<(int)muons->size(); ++mdx)
	    {
	      if(muons->size()<=2)
		{
		  reco::Particle::LorentzVector Muon=(*muons)[mdx].p4();
		  double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*muons)[mdx].eta(),(*muons)[mdx].phi()));
		  double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*muons)[mdx].phi()));
		  double dTheta=abs(((*bjets)[idx].theta())-((*muons)[mdx].theta()));
		  double Angle=abs(angle(Bjet1,Muon));

		  dR_BjetLep_[idx][mdx]->Fill(dR);
		  dPhi_BjetLep_[idx][mdx]->Fill(dPhi);
		  dTheta_BjetLep_[idx][mdx]->Fill(dTheta);
		  angle_BjetLep_[idx][mdx]->Fill(Angle);

		  if(dR<dRBjetLepMin) dRBjetLepMin=dR;
		  if(dPhi<dPhiBjetLepMin) dPhiBjetLepMin=dPhi;
		  if(dTheta<dThetaBjetLepMin) dThetaBjetLepMin=dTheta;
		  if(Angle<AngleBjetLepMin) AngleBjetLepMin=Angle;
		  
		  if(dR>dRBjetLepMax) dRBjetLepMax=dR;
		  if(dPhi>dPhiBjetLepMax) dPhiBjetLepMax=dPhi;
		  if(dTheta>dThetaBjetLepMax) dThetaBjetLepMax=dTheta;
		  if(Angle>AngleBjetLepMax) AngleBjetLepMax=Angle;
		}
	    }
	  for(int edx=0; edx<(int)electrons->size(); ++edx)
	    {
	      if(electrons->size()<=2)
		{
		  reco::Particle::LorentzVector Electron=(*electrons)[edx].p4();
		  double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*electrons)[edx].eta(),(*electrons)[edx].phi()));
		  double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*electrons)[edx].phi()));
		  double dTheta=abs(((*bjets)[idx].theta())-((*electrons)[edx].theta()));
		  double Angle=abs(angle(Bjet1,Electron));

		  dR_BjetLep_[idx][edx]->Fill(dR);
		  dPhi_BjetLep_[idx][edx]->Fill(dPhi);
		  dTheta_BjetLep_[idx][edx]->Fill(dTheta);
		  angle_BjetLep_[idx][edx]->Fill(Angle);

		  if(dR<dRBjetLepMin) dRBjetLepMin=dR;
		  if(dPhi<dPhiBjetLepMin) dPhiBjetLepMin=dPhi;
		  if(dTheta<dThetaBjetLepMin) dThetaBjetLepMin=dTheta;
		  if(Angle<AngleBjetLepMin) AngleBjetLepMin=Angle;
		  
		  if(dR>dRBjetLepMax) dRBjetLepMax=dR;
		  if(dPhi>dPhiBjetLepMax) dPhiBjetLepMax=dPhi;
		  if(dTheta>dThetaBjetLepMax) dThetaBjetLepMax=dTheta;
		  if(Angle>AngleBjetLepMax) AngleBjetLepMax=Angle;
		}
	    }

	  for(int bdx=idx+1; bdx<(int)bjets->size(); ++bdx)
	    {
	      if(bjets->size()<=4)
		{
		  reco::Particle::LorentzVector Bjet2=(*bjets)[bdx].p4();
		  double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*bjets)[bdx].eta(),(*bjets)[bdx].phi()));
		  double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*bjets)[bdx].phi()));
		  double dTheta=abs(((*bjets)[idx].theta())-((*bjets)[bdx].theta()));
		  double Angle=abs(angle(Bjet1,Bjet2));

		  dR_BjetBjet_[idx][bdx]->Fill(dR);
		  dPhi_BjetBjet_[idx][bdx]->Fill(dPhi);
		  dTheta_BjetBjet_[idx][bdx]->Fill(dTheta);
		  angle_BjetBjet_[idx][bdx]->Fill(Angle);

		  if(dR<dRBjetBjetMin) dRBjetBjetMin=dR;
		  if(dPhi<dPhiBjetBjetMin) dPhiBjetBjetMin=dPhi;
		  if(dTheta<dThetaBjetBjetMin) dThetaBjetBjetMin=dTheta;
		  if(Angle<AngleBjetBjetMin) AngleBjetBjetMin=Angle;
		  
		  if(dR>dRBjetBjetMax) dRBjetBjetMax=dR;
		  if(dPhi>dPhiBjetBjetMax) dPhiBjetBjetMax=dPhi;
		  if(dTheta>dThetaBjetBjetMax) dThetaBjetBjetMax=dTheta;
		  if(Angle>AngleBjetBjetMax) AngleBjetBjetMax=Angle;
		}
	    }
	}
    }

  for(int idx=0; idx<(int)muons->size(); ++idx)
    {
      if(muons->size()<=2)
	{
	  reco::Particle::LorentzVector Muon1=(*muons)[idx].p4();
	  
	  if(met->size()>0)
	    {
	      reco::Particle::LorentzVector MET=(*met)[0].p4();
	      double dR=abs(deltaR((*muons)[idx].eta(),(*muons)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
	      double dPhi=abs(deltaPhi((*muons)[idx].phi(),(*met)[0].phi()));
	      double dTheta=abs(((*muons)[idx].theta())-((*met)[0].theta()));
	      double Angle=abs(angle(Muon1,MET));

	      dR_LepMET_[idx]->Fill(dR);
	      dPhi_LepMET_[idx]->Fill(dPhi);
	      dTheta_LepMET_[idx]->Fill(dTheta);
	      angle_LepMET_[idx]->Fill(Angle);

	      if(dR<dRLepMETMin) dRLepMETMin=dR;
	      if(dPhi<dPhiLepMETMin) dPhiLepMETMin=dPhi;
	      if(dTheta<dThetaLepMETMin) dThetaLepMETMin=dTheta;
	      if(Angle<AngleLepMETMin) AngleLepMETMin=Angle;
	      
	      if(dR>dRLepMETMax) dRLepMETMax=dR;
	      if(dPhi>dPhiLepMETMax) dPhiLepMETMax=dPhi;
	      if(dTheta>dThetaLepMETMax) dThetaLepMETMax=dTheta;
	      if(Angle>AngleLepMETMax) AngleLepMETMax=Angle;
	    }
	}
    }

  for(int idx=0; idx<(int)electrons ->size(); ++idx)
    {
      if(electrons->size()<=2)
	{
	  reco::Particle::LorentzVector Electron1=(*electrons )[idx].p4();
	  
	  if(met->size()>0)
	    {
	      reco::Particle::LorentzVector MET=(*met)[0].p4();
	      double dR=abs(deltaR((*electrons )[idx].eta(),(*electrons )[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
	      double dPhi=abs(deltaPhi((*electrons )[idx].phi(),(*met)[0].phi()));
	      double dTheta=abs(((*electrons )[idx].theta())-((*met)[0].theta()));
	      double Angle=abs(angle(Electron1,MET));

	      dR_LepMET_[idx]->Fill(dR);
	      dPhi_LepMET_[idx]->Fill(dPhi);
	      dTheta_LepMET_[idx]->Fill(dTheta);
	      angle_LepMET_[idx]->Fill(Angle);
	      
	      if(dR<dRLepMETMin) dRLepMETMin=dR;
	      if(dPhi<dPhiLepMETMin) dPhiLepMETMin=dPhi;
	      if(dTheta<dThetaLepMETMin) dThetaLepMETMin=dTheta;
	      if(Angle<AngleLepMETMin) AngleLepMETMin=Angle;
	      
	      if(dR>dRLepMETMax) dRLepMETMax=dR;
	      if(dPhi>dPhiLepMETMax) dPhiLepMETMax=dPhi;
	      if(dTheta>dThetaLepMETMax) dThetaLepMETMax=dTheta;
	      if(Angle>AngleLepMETMax) AngleLepMETMax=Angle;
	    }
	}
    }

  dRBjetMETMin_->Fill(dRBjetMETMin);
  dPhiBjetMETMin_->Fill(dPhiBjetMETMin);
  dThetaBjetMETMin_->Fill(dThetaBjetMETMin);
  AngleBjetMETMin_->Fill(AngleBjetMETMin);

  dRBjetMETMax_->Fill(dRBjetMETMax);
  dPhiBjetMETMax_->Fill(dPhiBjetMETMax);
  dThetaBjetMETMax_->Fill(dThetaBjetMETMax);
  AngleBjetMETMax_->Fill(AngleBjetMETMax);

  dRBjetBjetMin_->Fill(dRBjetBjetMin);
  dPhiBjetBjetMin_->Fill(dPhiBjetBjetMin);
  dThetaBjetBjetMin_->Fill(dThetaBjetBjetMin);
  AngleBjetBjetMin_->Fill(AngleBjetBjetMin);

  dRBjetBjetMax_->Fill(dRBjetBjetMax);
  dPhiBjetBjetMax_->Fill(dPhiBjetBjetMax);
  dThetaBjetBjetMax_->Fill(dThetaBjetBjetMax);
  AngleBjetBjetMax_->Fill(AngleBjetBjetMax);

  dRBjetLepMin_->Fill(dRBjetLepMin);
  dPhiBjetLepMin_->Fill(dPhiBjetLepMin);
  dThetaBjetLepMin_->Fill(dThetaBjetLepMin);
  AngleBjetLepMin_->Fill(AngleBjetLepMin);

  dRBjetLepMax_->Fill(dRBjetLepMax);
  dPhiBjetLepMax_->Fill(dPhiBjetLepMax);
  dThetaBjetLepMax_->Fill(dThetaBjetLepMax);
  AngleBjetLepMax_->Fill(AngleBjetLepMax);

  dRLepMETMin_->Fill(dRLepMETMin);
  dPhiLepMETMin_->Fill(dPhiLepMETMin);
  dThetaLepMETMin_->Fill(dThetaLepMETMin);
  AngleLepMETMin_->Fill(AngleLepMETMin);

  dRLepMETMax_->Fill(dRLepMETMax);
  dPhiLepMETMax_->Fill(dPhiLepMETMax);
  dThetaLepMETMax_->Fill(dThetaLepMETMax);
  AngleLepMETMax_->Fill(AngleLepMETMax);

  double deltaPhiMediumJetMETMin=10;

  for(int jdx=0; jdx<(int)mediumJets->size(); ++jdx)
    {
      reco::Particle::LorentzVector MET=(*met)[0].p4();
      double dPhi=abs(deltaPhi((*mediumJets)[jdx].phi(),(*met)[0].phi()));
      if(dPhi<deltaPhiMediumJetMETMin && jdx<3) deltaPhiMediumJetMETMin=dPhi;
    }

  dPhiMediumJetMETMin_->Fill(deltaPhiMediumJetMETMin);

  nJets_dRLepMETMin_->Fill(dRLepMETMin,jets->size());
  nJets_dPhiLepMETMin_->Fill(dPhiLepMETMin,jets->size());

  //-------------------------------------
  // 3-Vectors for event shape variables
  //-------------------------------------

  std::vector<math::XYZVector> BjetsP3;
  std::vector<math::XYZVector> BjetsMETP3;
  std::vector<math::XYZVector> BjetsLepP3;
  std::vector<math::XYZVector> BjetsMETLepP3;

  for(int idx=0; idx<(int)bjets->size(); ++idx)
    {
      math::XYZVector BjetP3;
      
      BjetP3.SetX((*bjets)[idx].px());
      BjetP3.SetY((*bjets)[idx].py());
      BjetP3.SetZ((*bjets)[idx].pz());

      BjetsP3.push_back(BjetP3);
      BjetsMETP3.push_back(BjetP3);
      BjetsLepP3.push_back(BjetP3);
      BjetsMETLepP3.push_back(BjetP3);
    }
 
  if(met->size()>0)
    {
      math::XYZVector METP3;
      METP3.SetX((*met)[0].px());
      METP3.SetY((*met)[0].py());
      METP3.SetZ((*met)[0].pz());
      BjetsMETP3.push_back(METP3);
      BjetsMETLepP3.push_back(METP3);
    }

  for(int idx=0; idx<(int)muons->size(); ++idx)
    {
      math::XYZVector MuonP3;
      
      MuonP3.SetX((*muons)[idx].px());
      MuonP3.SetY((*muons)[idx].py());
      MuonP3.SetZ((*muons)[idx].pz());
      BjetsLepP3.push_back(MuonP3);
      BjetsMETLepP3.push_back(MuonP3);
    }

  for(int idx=0; idx<(int)electrons->size(); ++idx)
    {
      math::XYZVector ElectronP3;
      
      ElectronP3.SetX((*electrons)[idx].px());
      ElectronP3.SetY((*electrons)[idx].py());
      ElectronP3.SetZ((*electrons)[idx].pz());
      BjetsLepP3.push_back(ElectronP3);
      BjetsMETLepP3.push_back(ElectronP3);
    }

  //-------------------------------------
  // Define Event shape variables
  //-------------------------------------

  EventShapeVariables BjetsEvtshape(BjetsP3);
  EventShapeVariables BjetsMETEvtshape(BjetsMETP3);
  EventShapeVariables BjetsLepEvtshape(BjetsLepP3);
  EventShapeVariables BjetsMETLepEvtshape(BjetsMETLepP3);

  double sphericity_Bjets  = BjetsEvtshape.sphericity();
  double aplanarity_Bjets  = BjetsEvtshape.aplanarity();
  double circularity_Bjets = BjetsEvtshape.circularity();
  double isotropy_Bjets    = BjetsEvtshape.isotropy();
  
  double sphericity_BjetsMET  = BjetsMETEvtshape.sphericity();
  double aplanarity_BjetsMET  = BjetsMETEvtshape.aplanarity();
  double circularity_BjetsMET = BjetsMETEvtshape.circularity();
  double isotropy_BjetsMET    = BjetsMETEvtshape.isotropy();

  double sphericity_BjetsLep  = BjetsLepEvtshape.sphericity();
  double aplanarity_BjetsLep  = BjetsLepEvtshape.aplanarity();
  double circularity_BjetsLep = BjetsLepEvtshape.circularity();
  double isotropy_BjetsLep    = BjetsLepEvtshape.isotropy();

  double sphericity_BjetsMETLep  = BjetsMETLepEvtshape.sphericity();
  double aplanarity_BjetsMETLep  = BjetsMETLepEvtshape.aplanarity();
  double circularity_BjetsMETLep = BjetsMETLepEvtshape.circularity();
  double isotropy_BjetsMETLep    = BjetsMETLepEvtshape.isotropy();

  //-------------------------------------
  // Fill histograms
  //-------------------------------------

  sphericity_bjets_->Fill(sphericity_Bjets);          
  aplanarity_bjets_->Fill(aplanarity_Bjets);   
  circularity_bjets_->Fill(circularity_Bjets);        
  isotropy_bjets_->Fill(isotropy_Bjets);

  sphericity_bjetsMET_->Fill(sphericity_BjetsMET);          
  aplanarity_bjetsMET_->Fill(aplanarity_BjetsMET);   
  circularity_bjetsMET_->Fill(circularity_BjetsMET);        
  isotropy_bjetsMET_->Fill(isotropy_BjetsMET); 
      
  sphericity_bjetsLep_->Fill(sphericity_BjetsLep);          
  aplanarity_bjetsLep_->Fill(aplanarity_BjetsLep);   
  circularity_bjetsLep_->Fill(circularity_BjetsLep);        
  isotropy_bjetsLep_->Fill(isotropy_BjetsLep); 

  sphericity_bjetsMETLep_->Fill(sphericity_BjetsMETLep);          
  aplanarity_bjetsMETLep_->Fill(aplanarity_BjetsMETLep);   
  circularity_bjetsMETLep_->Fill(circularity_BjetsMETLep);        
  isotropy_bjetsMETLep_->Fill(isotropy_BjetsMETLep);
  
}

void EventTopology::beginJob()
{  
} 

void EventTopology::endJob()
{
}
