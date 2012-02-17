#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
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
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

using namespace std;
 
SUSYAnalyzer::SUSYAnalyzer(const edm::ParameterSet& cfg):
  met_               (cfg.getParameter<edm::InputTag>("met") ),
  jets_              (cfg.getParameter<edm::InputTag>("jets") ),
  lightJets_         (cfg.getParameter<edm::InputTag>("lightJets") ),
  bjets_             (cfg.getParameter<edm::InputTag>("bjets") ),
  muons_             (cfg.getParameter<edm::InputTag>("muons") ),
  electrons_         (cfg.getParameter<edm::InputTag>("electrons") ),
  PVSrc_             (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_            (cfg.getParameter<edm::InputTag>("PUInfo") ),

  PUWeight_          (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_         (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEventWeights_  (cfg.getParameter<edm::InputTag>("BtagEventWeights") ),
  btagBin_           (cfg.getParameter<int>("btagBin") ),
  inclusiveBtagBin_  (cfg.getParameter<int>("inclusiveBtagBin") ),

  useEventWgt_       (cfg.getParameter<bool>("useEventWeight") ),
  useBtagEventWgt_   (cfg.getParameter<bool>("useBtagEventWeight") ),
  useInclusiveBtagEventWgt_  (cfg.getParameter<bool>("useInclusiveBtagEventWeight") ),

  TriggerWeight_     (cfg.getParameter<edm::InputTag>("TriggerWeight") ),
  useTriggerEvtWgt_  (cfg.getParameter<bool>("useTriggerEventWeight") ),

  HT0_               (cfg.getParameter<double>("HT0") ),
  HT1_               (cfg.getParameter<double>("HT1") ),
  HT2_               (cfg.getParameter<double>("HT2") ),
  Y0_                (cfg.getParameter<double>("Y0") ),
  Y1_                (cfg.getParameter<double>("Y1") ),
  Y2_                (cfg.getParameter<double>("Y2") )

{ 
  edm::Service<TFileService> fs;

  // set Sumw2 option
  Dummy_=fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_=fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);

  // event weighting
  nPV_noWgt_ = fs->make<TH1F>("nPV_noWgt","nPV_noWgt", 50, 0.,  50  );
  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0.,  50  );
  nPU_noWgt_ = fs->make<TH1F>("nPU_noWgt","nPU_noWgt", 50, 0.5, 50.5);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt","btagWeights_noWgt", 4, 0., 4.);
  btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt","btagWeights_PUWgt", 4, 0., 4.);
  nBtags_noWgt_ = fs->make<TH1F>("nBtags_noWgt","nBtags_noWgt", 4, 0., 4.); 
  nBtags_PUWgt_ = fs->make<TH1F>("nBtags_PUWgt","nBtags_PUWgt", 4, 0., 4.);
  nBtags_ = fs->make<TH1F>("nBtags","nBtags", 4, 0., 4.);

  // b-tagging
  TCHE_= fs->make<TH1F>("TCHE","TCHE", 80, -20., 20.);
  TCHP_= fs->make<TH1F>("TCHP","TCHP", 80, -20., 20.);
  SSVHE_= fs->make<TH1F>("SSVHE","SSVHE", 120, -2, 10.);
  SSVHP_= fs->make<TH1F>("SSVHP","SSVHP", 120, -2, 10.);

  nBjets_ = fs->make<TH1F>("nJets","nJets", 8, 0., 8.);

  // Jet Et, MET, HT, MT, nJets
  for(int idx=0; idx<6; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));
    }
  MET_ = fs->make<TH1F>("MET","MET", 50, 0., 1000.);
  HT_ = fs->make<TH1F>("HT","HT", 40, 0., 2000.);
  nJets_ = fs->make<TH1F>("nJets","njets",16 , -0.5, 15.5);

  // HT vs. met significance
  SigMET_ = fs->make<TH1F>("SigMET","SigMET", 40, 0., 40);
  significance_ = fs->make<TH1F>("significance","significance", 40, 0., 40);

  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0., 50);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  HT_MET_ = fs->make<TH2F>("HT_MET","HT vs. MET", 78, 220., 1000., 30, 0., 300. );
  HT_SigMET_ = fs->make<TH2F>("HT_SigMET","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);

  HT_significance_ = fs->make<TH2F>("HT_significance","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  significance_SigMET_ = fs->make<TH2F>("significance_SigMET","significance vs. SigMET", 80, 0., 40., 80, 0., 40.);

  HT_SigPtl_ = fs->make<TH2F>("HT_SigPtl","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
  HT_SigPtl_smeared_ = fs->make<TH2F>("HT_SigPtl_smeared","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
  SigPtl_smearFactor_ = fs->make<TH1F>("SigPtl_smearFactor","SigPtl_smearFactor", 100, 0., 10. );
  HT_SigMET_unweighted_ = fs->make<TH2F>("HT_SigMET_unweighted","HT vs. SigMET unweighted", 80, 0., 2000., 80, 0., 20. );

  //HISTS FOR STUDYING THE MET AND PT DEPENDENCE OF KAPPA
  ///////////////////////////////////////////////////////
  HT_SigMET_PT20_MET60       = fs->make<TH2F>("HT_SigMET_PT20_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  HT_SigMET_PT40_MET60       = fs->make<TH2F>("HT_SigMET_PT40_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  HT_SigMET_PT60_MET60       = fs->make<TH2F>("HT_SigMET_PT60_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
			     
  HT_SigPtl_PT20_MET20       = fs->make<TH2F>("HT_SigPtl_PT20_MET20","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
  HT_SigPtl_PT20_MET40       = fs->make<TH2F>("HT_SigPtl_PT20_MET40","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
  HT_SigPtl_PT20_MET60       = fs->make<TH2F>("HT_SigPtl_PT20_MET60","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
		
  HT_SigPtl_PT20_MET20_smeared       = fs->make<TH2F>("HT_SigPtl_PT20_MET20_smeared","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
  HT_SigPtl_PT20_MET40_smeared       = fs->make<TH2F>("HT_SigPtl_PT20_MET40_smeared","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
  HT_SigPtl_PT20_MET60_smeared       = fs->make<TH2F>("HT_SigPtl_PT20_MET60_smeared","HT vs. SigPtl", 80, 0., 2000., 80, 0., 20. );
	     
  HT_significance_PT20_MET20 = fs->make<TH2F>("HT_significance_PT20_MET20","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT20_MET40 = fs->make<TH2F>("HT_significance_PT20_MET40","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT20_MET60 = fs->make<TH2F>("HT_significance_PT20_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT40_MET60 = fs->make<TH2F>("HT_significance_PT40_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT60_MET60 = fs->make<TH2F>("HT_significance_PT60_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  ////////////////////////////

  MT_ = fs->make<TH1F>("MT","MT", 40, 0., 2000.);
  nMuons_ = fs->make<TH1F>("nMuons","nMuons",7 , -0.5, 6.5);
  nElectrons_ = fs->make<TH1F>("nElectrons","nElectrons",7 , -0.5, 6.5);
  nLeptons_ = fs->make<TH1F>("nLeptons","nLeptons",13 , -0.5, 12.5);

  invMuMuMass_= fs->make<TH1F>("invMuMuMass","invMuMuMass",200,0.,200);

  RelIsoMu1_= fs->make<TH1F>("RelIsoMu1","RelIso Muon 1",40,0.,1.0);
  RelIsoMu2_= fs->make<TH1F>("RelIsoMu2","RelIso Muon 2",100,0.,5.0);

  Electron0_eta_=fs-> make<TH1F>("Elec0_eta","Elec0 eta", 60, -3, 3);
  Muon0_eta_=fs-> make<TH1F>("Muon0_eta","Muon0 eta", 60, -3, 3);

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

  mW_=fs-> make<TH1F>("mW","mW", 40 , 0, 400);
  mW_posCharge_=fs-> make<TH1F>("mW_posCharge","mW_posCharge", 40 , 0, 400);
  mW_negCharge_=fs-> make<TH1F>("mW_negCharge","mW_negCharge", 40 , 0, 400);
  mW2_=fs-> make<TH1F>("mW2","mW2", 40 , 0, 600);
  mTop_=fs-> make<TH1F>("mTop","mTop", 50 , 0, 500);

  mW_MET_=fs-> make<TH2F>("mW_MET","MET vs. mW",  40, 0., 400., 25, 0., 500.);
  mW_nJets_=fs-> make<TH2F>("mW_nJets","nJets vs. mW", 40, 0., 400.,16 , -0.5, 15.5 );
  mW_HT_=fs-> make<TH2F>("mW_HT","HT vs. mW", 20, 0., 400., 40, 0., 2000.);
  mW_MT_=fs-> make<TH2F>("mW_MT","MT vs. mW", 20, 0., 400., 40, 0., 2000.);
  mW_MTHad_=fs-> make<TH2F>("mW_MTHad","MTHad vs. mW", 20, 0., 400., 40, 0., 2000.);

  mW_SigMET_=fs-> make<TH2F>("mW_SigMET","SigMET vs. mW",  40, 0., 400., 20, 0., 20.);
  sigMET_nJets_=fs-> make<TH2F>("sigMET_nJets","nJets vs. sigMET", 20, 0., 20.,16 , -0.5, 15.5 );
  HT_nJets_=fs-> make<TH2F>("HT_nJets","nJets vs. HT", 25, 0., 1000.,16 , -0.5, 15.5 );
}

SUSYAnalyzer::~SUSYAnalyzer()
{
}

void
SUSYAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

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
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);

  //-------------------------------------------------
  // Event weighting
  //-------------------------------------------------

  double weight=1;

  // declare and initialize different weights
  double weightPU=1;
  double weightRA2=1;
  double weightBtagEff=1;

  // if events should be weighted
  if(useEventWgt_)
    {
      // RA2 weight
      edm::Handle<double> RA2WeightHandle;
      evt.getByLabel(RA2Weight_, RA2WeightHandle);
      weightRA2=*RA2WeightHandle;

      weight=weightRA2;

      // PU weight
      edm::Handle<double> PUWeightHandle;
      evt.getByLabel(PUWeight_, PUWeightHandle);
      weightPU=(*PUWeightHandle);

      weight=weightRA2*weightPU;

      // number of b-tagged jets, events are weighted
      unsigned int nBtags = bjets->size();
      if(bjets->size() > 2) nBtags=3;
      nBtags_PUWgt_->Fill(nBtags, weight);
      
      if(useBtagEventWgt_ ||useInclusiveBtagEventWgt_)
	{
	  // Btag weight
	  edm::Handle<std::vector<double> > BtagEventWeightsHandle;
	  evt.getByLabel(BtagEventWeights_, BtagEventWeightsHandle);

	  if(useBtagEventWgt_)
	    {
	      weightBtagEff=(*BtagEventWeightsHandle)[btagBin_];
	      
	      btagWeights_noWgt_->Fill(0.,(*BtagEventWeightsHandle)[0]);
	      btagWeights_noWgt_->Fill(1, (*BtagEventWeightsHandle)[1]);
	      btagWeights_noWgt_->Fill(2, (*BtagEventWeightsHandle)[2]);
	      btagWeights_noWgt_->Fill(3, (*BtagEventWeightsHandle)[3]);
	      
	      btagWeights_PUWgt_->Fill(0.,(*BtagEventWeightsHandle)[0]*weight);
	      btagWeights_PUWgt_->Fill(1, (*BtagEventWeightsHandle)[1]*weight);
	      btagWeights_PUWgt_->Fill(2, (*BtagEventWeightsHandle)[2]*weight);
	      btagWeights_PUWgt_->Fill(3, (*BtagEventWeightsHandle)[3]*weight);
	    }
	  
	  if(useInclusiveBtagEventWgt_)
	    {
	      weightBtagEff=0;
	      for(int bwx=inclusiveBtagBin_; bwx<4; ++bwx)
		{
		  weightBtagEff=weightBtagEff+(*BtagEventWeightsHandle)[bwx];
		}
	    }
	}
      
      weight=weightRA2*weightPU*weightBtagEff;
      
      // number of PU interactions only in MC available, therefore filled in this loop
      edm::Handle<edm::View<PileupSummaryInfo> > PUInfoHandle;
      evt.getByLabel(PUInfo_, PUInfoHandle);

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)  // vector size is 3
	{ 
	  if (iterPU->getBunchCrossing()==0) // -1: previous BX, 0: current BX,  1: next BX
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	}

      nPU_noWgt_->Fill(nvtx);
      nPU_->Fill(nvtx,weight);
    }

  if(useTriggerEvtWgt_)
    {
      edm::Handle<double> TriggerWeightHandle;
      evt.getByLabel(TriggerWeight_, TriggerWeightHandle);
      weight=weight*(*TriggerWeightHandle);
    }

  // number of primary vertices
  nPV_noWgt_->Fill(PVSrc->size());
  nPV_->Fill(PVSrc->size(), weight);

  // number of b-tagged jets
  unsigned int nBtags = bjets->size();
  if(bjets->size() > 2) nBtags=3;
  nBtags_->Fill(nBtags,weight);
  nBtags_noWgt_->Fill(nBtags);

  //-------------------------------------------------
  // B-tagging
  //-------------------------------------------------

  // bdisc
  for(int i=0; i<(int)jets->size();++i)
    {
      TCHE_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
      TCHP_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
      SSVHE_->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight);
      SSVHP_->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight);
    }

  nBjets_->Fill(bjets->size(), weight);

  //-------------------------------------------------
  // Jet Et, MET, HT, nJets
  //-------------------------------------------------

  if(met->size()==0) return;

  double HT=0;
  int nJets=0;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      if(i<6) Jet_Et_[i]->Fill((*jets)[i].et(), weight);
      HT=HT+(*jets)[i].et();
      nJets=nJets+1;
    }
  
  MET_->Fill((*met)[0].et(), weight);
  HT_->Fill(HT, weight);
  nJets_->Fill(nJets, weight);


  //-------------------------------------------------
  // HT vs. met significance
  //-------------------------------------------------

  double sigMET=((*met)[0].et())/(sqrt(HT));
  double sigmaX2= (*met)[0].getSignificanceMatrix()(0,0);
  double sigmaY2= (*met)[0].getSignificanceMatrix()(1,1);
  double significance = 0;
  if(sigmaX2<1.e10 && sigmaY2<1.e10) significance = (*met)[0].significance();

  //Use the sqrt of significance
  if (significance > 0.) significance = sqrt(significance);

  significance_->Fill(significance, weight);
  HT_significance_->Fill(HT,significance, weight);
  significance_SigMET_->Fill(significance, sigMET, weight);

  SigMET_->Fill(sigMET, weight);
  HT_SigMET_->Fill(HT,sigMET, weight);
  HT_SigMET_unweighted_->Fill(HT,sigMET, 1.);
  HT_MET_->Fill(HT,(*met)[0].et(), weight);

  //-------------------------------------------------
  // Lepton pt, nMuons, nElectrons, nLeptons
  //-------------------------------------------------

  if(muons->size()>0) Muon0_eta_->Fill((*muons)[0].eta(), weight);
  if(electrons->size()>0) Electron0_eta_->Fill((*electrons)[0].eta(), weight);

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
      if(i<3) Muon_pt_[i]->Fill((*muons)[i].pt(), weight);
      nmuons=nmuons+1;
      nleptons=nleptons+1;
      lepHT=lepHT+(*muons)[i].et();
      charge.push_back((*muons)[i].charge());

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

  RelIsoMu1_->Fill(RelIso1, weight);
  RelIsoMu2_->Fill(RelIso2, weight);

  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<3) Elec_pt_[i]->Fill((*electrons)[i].pt(), weight);
      nelectrons=nelectrons+1;
      nleptons=nleptons+1;
      lepHT=lepHT+(*electrons)[i].et();
      charge.push_back((*electrons)[i].charge());
    }

  nMuons_->Fill(nmuons, weight);
  nElectrons_->Fill(nelectrons, weight);
  nLeptons_->Fill(nleptons, weight);

  double MT=lepHT+HT+(*met)[0].et();
  MT_->Fill(MT, weight);

  //transverse W-mass
  double mW=0;
  double mTop=0;
  double eta=3.0;
  double lepCharge=0;
  double mW2=0;
  double dRLepBjetMin=10;
  reco::Particle::LorentzVector METP4=(*met)[0].p4();

  const reco::LeafCandidate * singleLepton = 0; //Used to obtain the single lepton in the event. Used for SigPtl.
 
  if(muons->size()==1)
    {
      singleLepton = &(*muons)[0];
      
      mW=sqrt(2*(((*met)[0].et())*((*muons)[0].et())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
      eta=(*muons)[0].eta();
      mW2=sqrt(2*(((*met)[0].et())*((*muons)[0].energy())-((*met)[0].px())*((*muons)[0].px())-((*met)[0].py())*((*muons)[0].py())));
      eta=(*muons)[0].eta();
      lepCharge=(*muons)[0].charge();

      reco::Particle::LorentzVector LepP4=(*muons)[0].p4();
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	 double dRLepBjet=abs(deltaR((*bjets)[bdx].eta(),(*bjets)[bdx].phi(),(*muons)[0].eta(),(*muons)[0].phi()));
	 reco::Particle::LorentzVector BjetP4=(*bjets)[bdx].p4();
	 if(dRLepBjet < dRLepBjetMin)
	   {
	     dRLepBjetMin=dRLepBjet;
	     mTop=sqrt((METP4+LepP4+BjetP4).Dot(METP4+LepP4+BjetP4));
	   }
	}
    }  
  else if(electrons->size()==1)
    {
      singleLepton = &(*electrons)[0];

      mW=sqrt(2*(((*met)[0].et())*((*electrons)[0].et())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
      mW2=sqrt(2*(((*met)[0].et())*((*electrons)[0].energy())-((*met)[0].px())*((*electrons)[0].px())-((*met)[0].py())*((*electrons)[0].py())));
      eta=(*electrons)[0].eta();
      lepCharge=(*electrons)[0].charge();

      reco::Particle::LorentzVector LepP4=(*electrons)[0].p4();
      for(int bdx=0; bdx<(int)bjets->size(); ++bdx)
	{
	 double dRLepBjet=abs(deltaR((*bjets)[bdx].eta(),(*bjets)[bdx].phi(),(*electrons)[0].eta(),(*electrons)[0].phi()));
	 reco::Particle::LorentzVector BjetP4=(*bjets)[bdx].p4();
	 if(dRLepBjet < dRLepBjetMin)
	   {
	     dRLepBjetMin=dRLepBjet;
	     mTop=sqrt((METP4+LepP4+BjetP4).Dot(METP4+LepP4+BjetP4));
	   }
	}
    }

  //Fill HT_SigPtl_ histogram
  //Also fill other histograms, depending on MET and lepton PT
  if (singleLepton != 0 && HT > 0. && jets->size() >= 4) {
    double SigPtl = singleLepton->et() / sqrt(HT); 
    HT_SigPtl_->Fill(HT,SigPtl,weight);
    
    double MET=(*met)[0].et();

    //Smear the lepton pT. Do this using the MET significance.
    double MET_resolution = 0.;
    if (significance > 0.) MET_resolution = 1. / significance ;  
    TRandom3 rNum(0);
    double smearFactor = pow ( (1.+ MET_resolution) , rNum.Gaus() );
    SigPtl_smearFactor_->Fill(smearFactor, weight);
    HT_SigPtl_smeared_->Fill(HT, SigPtl * smearFactor, weight);
    
    //Fill histograms
    if (singleLepton->et() >= 60.) {
      if (MET >= 60.) {
	HT_SigMET_PT60_MET60->Fill(HT, sigMET, weight);
	HT_significance_PT60_MET60->Fill(HT, significance, weight);
      }
    }
    if (singleLepton->et() >= 40.) {
      if (MET >= 60.) {
	HT_SigMET_PT40_MET60->Fill(HT, sigMET, weight);
	HT_significance_PT40_MET60->Fill(HT, significance, weight);
      }
    }
    if (singleLepton->et() >= 20.) {
      if (MET >= 60.) {
	HT_SigMET_PT20_MET60->Fill(HT, sigMET, weight);
	HT_significance_PT20_MET60->Fill(HT, significance, weight);
	HT_SigPtl_PT20_MET60->Fill(HT, SigPtl, weight);
	HT_SigPtl_PT20_MET60_smeared->Fill(HT, SigPtl * smearFactor, weight);
      }
      if (MET >= 40.) {
	HT_significance_PT20_MET40->Fill(HT, significance, weight);
	HT_SigPtl_PT20_MET40->Fill(HT, SigPtl, weight);
	HT_SigPtl_PT20_MET40_smeared->Fill(HT, SigPtl * smearFactor, weight);
      }
      if (MET >= 20.) {
	HT_significance_PT20_MET20->Fill(HT, significance, weight);
	HT_SigPtl_PT20_MET20->Fill(HT, SigPtl, weight);
	HT_SigPtl_PT20_MET20_smeared->Fill(HT, SigPtl * smearFactor, weight);
      }
      
    }
    
  } 
}

void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
