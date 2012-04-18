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

  // Dummy histograms
  Dummy_  =fs->make<TH1F>();
  Dummy2_ =fs->make<TH2F>();

  Dummy_->SetDefaultSumw2(true);
  Dummy2_->SetDefaultSumw2(true);

  // Event weighting
  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt", "btagWeights_noWgt",  4, 0.,   4. );
  btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt", "btagWeights_PUWgt",  4, 0.,   4. );
  nPU_noWgt_         = fs->make<TH1F>("nPU_noWgt",         "nPU_noWgt",         50, 0.5, 50.5);
  nPU_               = fs->make<TH1F>("nPU",               "nPU",               50, 0.5, 50.5);
  nPV_noWgt_         = fs->make<TH1F>("nPV_noWgt",         "nPV_noWgt",         50, 0.,  50  );
  nPV_               = fs->make<TH1F>("nPV",               "nPV",               50, 0.,  50  );

  // Btagging
  TCHE_  = fs->make<TH1F>("TCHE",  "TCHE",   80, -20, 20);
  TCHP_  = fs->make<TH1F>("TCHP",  "TCHP",   80, -20, 20);
  SSVHE_ = fs->make<TH1F>("SSVHE", "SSVHE", 120,  -2, 10);
  SSVHP_ = fs->make<TH1F>("SSVHP", "SSVHP", 120,  -2, 10);

  nBjets_noWgt_    = fs->make<TH1F>("nBjets_noWgt",   "nBjets_noWgt",   4, 0, 4);
  nBjets_noWgt_2_  = fs->make<TH1F>("nBjets_noWgt_2", "nBjets_noWgt_2", 8, 0, 8);
  nBjets_          = fs->make<TH1F>("nBjets_",        "nBjets_",        4, 0, 4);
  nBjets_2_        = fs->make<TH1F>("nBjets_2",       "nBjets_2",       8, 0, 8);

  // Basic kinematics
  for(int idx=0; idx<6; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Et",idx);
      Jet_Et_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));
    }
  MET_   = fs->make<TH1F>("MET",   "MET",   50,   0.,  1000.);
  HT_    = fs->make<TH1F>("HT",    "HT",    40,   0.,  2000.);
  nJets_ = fs->make<TH1F>("nJets", "njets", 16 , -0.5,  15.5);

  // Ymet
  YMET_= fs->make<TH1F>("YMET","YMET", 40, 0., 40);

  HT_YMET_       = fs->make<TH2F>("HT_YMET",       "HT vs. YMET", 80,   0., 2000., 80, 0.,  20.);
  HT_YMET_noWgt_ = fs->make<TH2F>("HT_YMET_noWgt", "HT vs. YMET", 80,   0., 2000., 80, 0.,  20.);
  HT_MET_        = fs->make<TH2F>("HT_MET",        "HT vs. MET",  78, 220., 1000., 30, 0., 300.);

  // MET significance
  METSig_ = fs->make<TH1F>("METSig","METSig", 40, 0., 40);

  HT_METSig_       = fs->make<TH2F>("HT_METSig",       "HT vs. METSig", 80,   0., 2000., 80, 0.,  20.);
  HT_METSig_noWgt_ = fs->make<TH2F>("HT_METSig_noWgt", "HT vs. METSig", 80,   0., 2000., 80, 0.,  20.);

  // Lepton variables
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon%i_Pt",idx);
      Muon_Pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));

      char histname2[20];
      sprintf(histname2,"Muon%i_Eta",idx);
      Muon_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Electron%i_Pt",idx);
      Electron_Pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));

      char histname2[20];
      sprintf(histname2,"Electron%i_Eta",idx);
      Electron_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }
  nMuons_      = fs->make<TH1F>("nMuons",     "nMuons",      7, -0.5,  6.5);
  nElectrons_  = fs->make<TH1F>("nElectrons", "nElectrons",  7, -0.5,  6.5);
  nLeptons_    = fs->make<TH1F>("nLeptons",   "nLeptons",   13, -0.5, 12.5);

  // MT
  MT_          = fs->make<TH1F>("MT","MT", 40, 0., 2000.);

  // Correlation between HT and YMET / MET significance
  HT_LepPtSig_ = fs->make<TH2F>("HT_LepPtSig","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_smeared_ = fs->make<TH2F>("HT_LepPtSig_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  LepPtSig_smearFactor_ = fs->make<TH1F>("LepPtSig_smearFactor","LepPtSig_smearFactor", 100, 0., 10. );
  HT_SigMET_unweighted_ = fs->make<TH2F>("HT_SigMET_unweighted","HT vs. SigMET unweighted", 80, 0., 2000., 80, 0., 20. );

  HT_SigMET_PT20_MET60       = fs->make<TH2F>("HT_SigMET_PT20_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  HT_SigMET_PT40_MET60       = fs->make<TH2F>("HT_SigMET_PT40_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  HT_SigMET_PT60_MET60       = fs->make<TH2F>("HT_SigMET_PT60_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
			     
  HT_LepPtSig_PT20_MET20       = fs->make<TH2F>("HT_LepPtSig_PT20_MET20","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET40       = fs->make<TH2F>("HT_LepPtSig_PT20_MET40","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET60       = fs->make<TH2F>("HT_LepPtSig_PT20_MET60","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
		
  HT_LepPtSig_PT20_MET20_smeared       = fs->make<TH2F>("HT_LepPtSig_PT20_MET20_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET40_smeared       = fs->make<TH2F>("HT_LepPtSig_PT20_MET40_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  HT_LepPtSig_PT20_MET60_smeared       = fs->make<TH2F>("HT_LepPtSig_PT20_MET60_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
	     
  HT_significance_PT20_MET20 = fs->make<TH2F>("HT_significance_PT20_MET20","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT20_MET40 = fs->make<TH2F>("HT_significance_PT20_MET40","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT20_MET60 = fs->make<TH2F>("HT_significance_PT20_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT40_MET60 = fs->make<TH2F>("HT_significance_PT40_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  HT_significance_PT60_MET60 = fs->make<TH2F>("HT_significance_PT60_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);

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

  // declare and initialize different weights
  double weight=1;
  double weightPU=1;
  double weightRA2=1;
  double weightBtagEff=1;

  if(useEventWgt_)
    {
      // RA2 weight
      edm::Handle<double> RA2WeightHandle;
      evt.getByLabel(RA2Weight_, RA2WeightHandle);
      weightRA2=*RA2WeightHandle;
      
      // PU weight
      edm::Handle<double> PUWeightHandle;
      evt.getByLabel(PUWeight_, PUWeightHandle);
      weightPU=(*PUWeightHandle);
      
      // Btag efficiency weights
      if(useBtagEventWgt_ ||useInclusiveBtagEventWgt_)
	{
	  // Btag weights
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
      for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)
	{ 
	  if (iterPU->getBunchCrossing()==0)
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

  //-------------------------------------------------
  // Btagging
  //-------------------------------------------------

  for(int i=0; i<(int)jets->size();++i)
    {
      TCHE_  ->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
      TCHP_  ->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
      SSVHE_ ->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight);
      SSVHP_ ->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight);
    }

  nBjets_noWgt_   ->Fill(bjets->size());
  nBjets_noWgt_2_ ->Fill(bjets->size());
  nBjets_         ->Fill(bjets->size(),weight);
  nBjets_2_       ->Fill(bjets->size(),weight);

  //-------------------------------------------------
  // Jet Et, MET, HT, nJets
  //-------------------------------------------------

  if(met->size()==0) return;

  double HT=0;
  int njets=0;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      if(i<6) Jet_Et_[i]->Fill((*jets)[i].et(), weight);
      HT=HT+(*jets)[i].et();
      njets=njets+1;
    }
  
  MET_->Fill((*met)[0].et(), weight);
  HT_->Fill(HT, weight);
  nJets_->Fill(njets, weight);

  //-------------------------------------------------
  // YMET
  //-------------------------------------------------

  double YMET=((*met)[0].et())/(sqrt(HT));  
  YMET_->Fill(YMET, weight);

  // YMET vs. HT
  HT_YMET_       ->Fill(HT, YMET,           weight);
  HT_YMET_noWgt_ ->Fill(HT, YMET,               1.);
  HT_MET_        ->Fill(HT, (*met)[0].et(), weight);

  //-------------------------------------------------
  // MET significance
  //-------------------------------------------------

  double sigmaX2 = (*met)[0].getSignificanceMatrix()(0,0);
  double sigmaY2 = (*met)[0].getSignificanceMatrix()(1,1);
  double METSig  = 0;
  if(sigmaX2<1.e10 && sigmaY2<1.e10) METSig = (*met)[0].significance();
  // Use the sqrt of the significance
  if (METSig > 0.) METSig = sqrt(METSig);

  METSig_->Fill(METSig, weight);

  // METSig vs. HT
  HT_METSig_      ->Fill(HT, METSig, weight);
  HT_METSig_noWgt_->Fill(HT, METSig,     1.);

  // METSig vs. YMET
  METSig_YMET_ ->Fill(METSig, YMET, weight);

  //-------------------------------------------------
  // Lepton variables 
  //-------------------------------------------------

  int nLeptons=0;
  int nMuons=0;
  int nElectrons=0;
  double LepHT=0;

  // loop over muons
  for(int i=0; i<(int)muons->size(); ++i)
    {
      if(i<2)
	{
	  Muon_pt_[i] ->Fill((*muons)[i].pt(),  weight);
	  Muon_eta_[i]->Fill((*muons)[i].eta(), weight);
	}
      nMuons=nMuons+1;
      nLeptons=nLeptons+1;
      LepHT=LepHT+(*muons)[i].pt());
    }

  // loop over electrons
  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<2)
	{
	  Electron_pt_[i] ->Fill((*electrons)[i].pt(),  weight);
	  Electron_eta_[i]->Fill((*electrons)[i].eta(), weight);
	}
      nElectrons=nElectrons+1;
      nLeptons=nLeptons+1;
      LepHT=LepHT+(*electrons)[i].pt());
    }

  nMuons_    ->Fill(nMuons,     weight);
  nElectrons_->Fill(nElectrons, weight);
  nLeptons_  ->Fill(nLeptons,   weight);

  // MT
  double MT=LepHT+HT+(*met)[0].et();
  MT_->Fill(MT, weight);
  
  const reco::LeafCandidate * singleLepton = 0;
  if(muons->size()==1) singleLepton = &(*muons)[0];
  else if(electrons->size()==1) singleLepton = &(*electrons)[0];

  //-----------------------------------------------------------
  // Study Correlation between HT and YMET / MET significnace
  //----------------------------------------------------------

  if(singleLepton != 0 && HT > 0. && jets->size()>=4)
    {
      double LepPtSig = singleLepton->et() / sqrt(HT); 
      HT_LepPtSig_->Fill(HT, LepPtSig, weight);
      
      double MET=(*met)[0].et();
      
      //Smear the lepton pT. Do this using the MET signficance
      double MET_resolution = 0.;
      if (METSig > 0.) MET_resolution = 1. / METSig ;  
      TRandom3 rNum(0);
      double smearFactor = pow ( (1.+ MET_resolution) , rNum.Gaus() );
      LepPtSig_smearFactor_->Fill(smearFactor, weight);
      HT_LepPtSig_smeared_->Fill(HT, LepPtSig * smearFactor, weight);
      
      //Fill histograms
      if (singleLepton->et() >= 60.) {
	if (MET >= 60.) {
	  HT_SigMET_PT60_MET60->Fill(HT, YMET, weight);
	  HT_METSig_PT60_MET60->Fill(HT, METSig, weight);
	}
      }
      if (singleLepton->et() >= 40.) {
	if (MET >= 60.) {
	  HT_SigMET_PT40_MET60->Fill(HT, YMET, weight);
	  HT_METSig_PT40_MET60->Fill(HT, METSig, weight);
	}
      }
      if (singleLepton->et() >= 20.) {
	if (MET >= 60.) {
	  HT_SigMET_PT20_MET60->Fill(HT, YMET, weight);
	  HT_METSig_PT20_MET60->Fill(HT, METSig, weight);
	  HT_LepPtSig_PT20_MET60->Fill(HT, LepPtSig, weight);
	  HT_LepPtSig_PT20_MET60_smeared->Fill(HT, LepPtSig * smearFactor, weight);
	}
	if (MET >= 40.) {
	  HT_METSig_PT20_MET40->Fill(HT, METSig, weight);
	  HT_LepPtSig_PT20_MET40->Fill(HT, LepPtSig, weight);
	  HT_LepPtSig_PT20_MET40_smeared->Fill(HT, LepPtSig * smearFactor, weight);
	}
	if (MET >= 20.) {
	  HT_METSig_PT20_MET20->Fill(HT, METSig, weight);
	  HT_LepPtSig_PT20_MET20->Fill(HT, LepPtSig, weight);
	  HT_LepPtSig_PT20_MET20_smeared->Fill(HT, LepPtSig * smearFactor, weight);
	}  
      }    
    } 
  
//   //-------------------------------------------------
//   // ABCD plots
//   //-------------------------------------------------
 
//   bool ATight = HT >= HT0_ && HT < HT1_ && YMET >= Y0_ && YMET < Y1_;
//   bool BTight = HT >= HT2_ && YMET >= Y0_ && YMET < Y1_;
//   bool CTight = HT >= HT0_ && HT < HT1_ && YMET >= Y2_;
//   bool DTight = HT >= HT2_ && YMET >= Y2_;

//   if(ATight)
//     {
//       MET_A_->Fill((*met)[0].et(),weight);      
//       if(singleLepton != 0)
// 	{
// 	  Lep_Pt_A_->Fill(singleLepton->pt(),weight);
// 	}
//       for(int jdx=0; jdx<(int)jets->size(); ++jdx)
// 	{
// 	  Jet_Et_A_[jdx]->Fill((*jets)[jdx].et(),weight);
// 	}
//     }
}

void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
