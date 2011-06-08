#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/EventTopology.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "PhysicsTools/CandUtils/interface/EventShapeVariables.h"
#include "TVector3.h"


using namespace std;
 
EventTopology::EventTopology(const edm::ParameterSet& cfg):
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") ) 
{ 
  edm::Service<TFileService> fs;

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
      dR_BjetMET_[i]=fs->make<TH1F>(histname1,"dR(bjet,MET)", 30, 0., 3.);
      char histname2[20];
      sprintf(histname2,"dPhi_bjet%i_met",i);
      dPhi_BjetMET_[i]=fs->make<TH1F>(histname2,"dPhi(bjet,MET)", 30, 0., 3.);
      char histname3[20];
      sprintf(histname3,"dTheta_bjet%i_met",i);
      dTheta_BjetMET_[i]=fs->make<TH1F>(histname3,"dTheta(bjet,MET)", 30, 0., 3.);
      char histname4[20];
      sprintf(histname4,"angle_bjet%i_met",i);
      angle_BjetMET_[i]=fs->make<TH1F>(histname4,"angle(bjet,MET)", 30, 0., 3.);

      for(int j=0; j<2; ++j)
	{
	  char histname1b[20];
	  sprintf(histname1b,"dR_bjet%i_lep%i",i,j);
	  dR_BjetLep_[i][j]=fs->make<TH1F>(histname1b,"dR(bjet,lep)", 30, 0., 3.);
	  char histname2b[20];
	  sprintf(histname2b,"dPhi_bjet%i_lep%i",i,j);
	  dPhi_BjetLep_[i][j]=fs->make<TH1F>(histname2b,"dPhi(bjet,lep)", 30, 0., 3.);
	  char histname3b[20];
	  sprintf(histname3b,"dTheta_bjet%i_lep%i",i,j);
	  dTheta_BjetLep_[i][j]=fs->make<TH1F>(histname3b,"dTheta(bjet,lep)", 30, 0., 3.);
	  char histname4b[20];
	  sprintf(histname4b,"angle_bjet%i_lep%i",i,j);
	  angle_BjetLep_[i][j]=fs->make<TH1F>(histname4b,"angle(bjet,lep)", 30, 0., 3.);
	}

      for(int k=0; k<4; ++k)
	{
	  char histname1b[20];
	  sprintf(histname1b,"dR_bjet%i_lep%i",i,k);
	  dR_BjetBjet_[i][k]=fs->make<TH1F>(histname1b,"dR(bjet,bjet)", 30, 0., 3.);
	  char histname2b[20];
	  sprintf(histname2b,"dPhi_bjet%i_lep%i",i,k);
	  dPhi_BjetBjet_[i][k]=fs->make<TH1F>(histname2b,"dPhi(bjet,bjet)", 30, 0., 3.);
	  char histname3b[20];
	  sprintf(histname3b,"dTheta_bjet%i_lep%i",i,k);
	  dTheta_BjetBjet_[i][k]=fs->make<TH1F>(histname3b,"dTheta(bjet,bjet)", 30, 0., 3.);
	  char histname4b[20];
	  sprintf(histname4b,"angle_bjet%i_lep%i",i,k);
	  angle_BjetBjet_[i][k]=fs->make<TH1F>(histname4b,"angle(bjet,bjet)", 30, 0., 3.);
	}

    }
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
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);

  //----------------------------------------------
  // deltaR, deltaPhi, deltaTheta, opening angle
  //----------------------------------------------

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
		}
	    }
	  for(int edx=0; edx<(int)electrons->size(); ++edx)
	    {
	      std::cout << "Hallo 13" << std::endl;

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
		}
	    }
	}
    }

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
