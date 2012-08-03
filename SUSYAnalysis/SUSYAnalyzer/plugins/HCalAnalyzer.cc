#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/HCalAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/Common/interface/View.h"

#include "RecoJets/JetAnalyzers/interface/JetPlotsExample.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

using namespace std;
 
HCalAnalyzer::HCalAnalyzer(const edm::ParameterSet& cfg):
  met_               (cfg.getParameter<edm::InputTag>("met") ),
  caloMet_               (cfg.getParameter<edm::InputTag>("caloMet") ),
  jets_              (cfg.getParameter<edm::InputTag>("jets") ),  
  caloJets_              (cfg.getParameter<edm::InputTag>("caloJets") ),
  /*lightJets_         (cfg.getParameter<edm::InputTag>("lightJets") ),
    bjets_             (cfg.getParameter<edm::InputTag>("bjets") ),*/
  muons_             (cfg.getParameter<edm::InputTag>("muons") ),
  electrons_         (cfg.getParameter<edm::InputTag>("electrons") ),
  PVSrc_             (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_            (cfg.getParameter<edm::InputTag>("PUInfo") ),

  PUWeight_          (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_         (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEventWeights_  (cfg.getParameter<edm::InputTag>("BtagEventWeights") ),
  BtagJetWeights_    (cfg.getParameter<edm::InputTag>("BtagJetWeights") ),
  btagBin_           (cfg.getParameter<int>("btagBin") ),
  inclusiveBtagBin_  (cfg.getParameter<int>("inclusiveBtagBin") ),

  useEventWgt_       (cfg.getParameter<bool>("useEventWeight") ),
  useBtagEventWgt_   (cfg.getParameter<bool>("useBtagEventWeight") ),
  useInclusiveBtagEventWgt_  (cfg.getParameter<bool>("useInclusiveBtagEventWeight") ),

  TriggerWeight_     (cfg.getParameter<edm::InputTag>("TriggerWeight") ),
  useTriggerEvtWgt_  (cfg.getParameter<bool>("useTriggerEventWeight") )

  /*HT0_               (cfg.getParameter<double>("HT0") ),
  HT1_               (cfg.getParameter<double>("HT1") ),
  HT2_               (cfg.getParameter<double>("HT2") ),
  Y0_                (cfg.getParameter<double>("Y0") ),
  Y1_                (cfg.getParameter<double>("Y1") ),
  Y2_                (cfg.getParameter<double>("Y2") )*/

{ 
  edm::Service<TFileService> fs;

  //-------------------------------------------------
  // Dummy histograms
  //-------------------------------------------------

  Dummy_ =fs->make<TH1F>();
  Dummy2_=fs->make<TH2F>();

  Dummy_->SetDefaultSumw2(true);
  Dummy2_->SetDefaultSumw2(true);

  //-------------------------------------------------
  // Event weighting
  //-------------------------------------------------

  //btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt", "btagWeights_noWgt",  4, 0.,   4. );
  //btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt", "btagWeights_PUWgt",  4, 0.,   4. );
  //nPU_noWgt_         = fs->make<TH1F>("nPU_noWgt",         "nPU_noWgt",         50, 0.5, 50.5);
  //nPU_               = fs->make<TH1F>("nPU",               "nPU",               50, 0.5, 50.5);
  nPV_noWgt_         = fs->make<TH1F>("nPV_noWgt",         "nPV_noWgt",         50, 0.,  50  );
  nPV_               = fs->make<TH1F>("nPV",               "nPV",               50, 0.,  50  );

  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------

  PFJetEt_Eta_    = fs->make<TH2F>("PFJetEt_Eta",    "PFJetEt Eta",    100, 0., 1000., 100, -3., 3);
  CaloJetEt_Eta_    = fs->make<TH2F>("CaloJetEt_Eta",    "CaloJetEt Eta",    100, 0., 1000., 100, -3., 3);
  GenJetEt_Eta_ = fs->make<TH2F>("GenJetEt_Eta", "GenJetEt Eta", 100, 0., 1000., 100, -3., 3);
  HOEnergy_Eta_ = fs->make<TH2F>("HOEnergy_Eta", "HOEnergy Eta", 100, 0., 200., 100, -3., 3);
  PFMET_Eta_      = fs->make<TH2F>("PFMET_Eta",      "PFMET Eta",      100, 0., 1000., 100, -3., 3);
  PFMET_Phi_      = fs->make<TH2F>("PFMET_Phi",      "PFMET Phi",      100, 0., 1000., 100, -1*TMath::Pi(), TMath::Pi());
  CaloMET_Eta_      = fs->make<TH2F>("CaloMET_Eta",      "CaloMET Eta",      100, 0., 1000., 100, -3., 3);
  CaloMET_Phi_      = fs->make<TH2F>("CaloMET_Phi",      "CaloMET Phi",      100, 0., 1000., 100, -1*TMath::Pi(), TMath::Pi());

  EleIso_NPV_ = fs->make<TH2F>("EleIso_NPV",    "EleIso NPV",    50, 0., 50.,  50, 0., 1.);
  EleHOverEM_ = fs->make<TH1F>("EleHOverEM", "EleHOverEM", 50, 0., 1.);
  EleHOverEM_NPV_ = fs->make<TH2F>(" EleHOverEM_NPV",    " EleHOverEM NPV",    50, 0., 50.,  50, 0., 1.);

  MuIso_NPV_ = fs->make<TH2F>("MuIso_NPV",    "MuIso NPV",    50, 0., 50.,  50, 0., 1.);
  MuHCal_= fs->make<TH1F>("MuHCal", "MuHCal", 100, 0., 100.);
  MuHCal_NPV_ = fs->make<TH2F>("MuHCal_NPV",    "MuHCal NPV",    50, 0., 50.,  100, 0., 100.);
  MuHO_= fs->make<TH1F>("MuH0", "MuH0", 100, 0., 100.);
  MuHO_NPV_ = fs->make<TH2F>("MuHO_NPV",    "MuHO NPV",    50, 0., 50.,  100, 0., 100.);

  PFJetEt_    = fs->make<TH1F>("PFJetEt",    "PFJetEt",    100, 0., 1000.);
  CaloJetEt_    = fs->make<TH1F>("CaloJetEt",    "CaloJetEt",    100, 0., 1000.);
  GenJetEt_ = fs->make<TH1F>("GenJetEt", "GenJetEt", 100, 0., 1000.);
  HOEnergy_ = fs->make<TH1F>("HOEnergy", "HOEnergy", 100, 0., 200.);
  PFMET_      = fs->make<TH1F>("PFMET",      "PFMET",      100, 0., 1000.);
  CaloMET_      = fs->make<TH1F>("CaloMET",      "CaloMET",      100, 0., 1000.);

  chargeEMFractionPF_  = fs->make<TH1F>("chargeEMFractionPF",  "charge EM fractionPF",  100, 0., 1.);
  neutralEMFractionPF_ = fs->make<TH1F>("neutralEMFractionPF", "neutral EM fractionPF", 100, 0., 1.);
  EMFractionCalo_  = fs->make<TH1F>("EMFractionCalo",  "EM fractionCalo",  100, 0., 1.);

  PFJetRelErr_ = fs->make<TH1F>("PFJetRelErr", "PFJetRelErr", 300, -3., 3.);
  //CaloJetRelErr_ = fs->make<TH1F>("CaloJetRelErr", "CaloJetRelErr", 300, -3., 3.);
  PFMETRelErr_ = fs->make<TH1F>("METRelErr", "METRelErr", 300, -3., 3.);
  //CaloMETRelErr_ = fs->make<TH1F>("METRelErr", "METRelErr", 300, -3., 3.);

  MuPt_ = fs->make<TH1F>("MuPt",    "Mu Pt",    100, 0., 300.);
  ElePt_ = fs->make<TH1F>("ElePt",    "Ele Pt",    100, 0., 300.);
  YMET_ = fs->make<TH1F>("YMET","YMET", 40, 0., 40);
  HT_ = fs->make<TH1F>("HT",       "HT",       40,   0.,  2000.);
  MHT_ = fs->make<TH1F>("MET_A",   "MET_A",   100,   0.,  1000.);
  MuIso_ = fs->make<TH1F>("MuIso",   "MuIs0",   48,   0.,  1.2);
  EleIso_ = fs->make<TH1F>("EleIso",   "EleIso",   50,   0.,  2.);

  PFCSV_  = fs->make<TH1F>("PFCSV",  "PF CSV",   80, -2, 2);
  CaloCSV_  = fs->make<TH1F>("CaloCSV",  "Calo CSV",   80, -2, 2);
}

HCalAnalyzer::~HCalAnalyzer()
{
}

void
HCalAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //--------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::MET> > caloMet;
  evt.getByLabel(caloMet_, caloMet);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > caloJets;
  evt.getByLabel(caloJets_, caloJets);
  /*edm::Handle<std::vector<pat::Jet> > lightJets;
  evt.getByLabel(lightJets_, lightJets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);*/
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);

  //-------------------------------------------------
  // Event weighting
  //----------------------f--------------------------

  //std::cout << "Test1" << std::endl;

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
      if(useBtagEventWgt_ || useInclusiveBtagEventWgt_)
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
      //evt.getByLabel(PUInfo_, PUInfoHandle);

      /*m::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)
	{ 
	  if (iterPU->getBunchCrossing()==0)
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	    }
	    
      nPU_noWgt_->Fill(nvtx);
      nPU_->Fill(nvtx,weight);*/
      }

  if(useTriggerEvtWgt_)
    {
      edm::Handle<double> TriggerWeightHandle;
      evt.getByLabel(TriggerWeight_, TriggerWeightHandle);
      weight=weight*(*TriggerWeightHandle);
    }

  float pv = PVSrc->size();

  // number of primary vertices
  nPV_noWgt_->Fill(pv);
  nPV_->Fill(pv, weight);

  //-------------------------------------------------
  // Basic variables
  //-------------------------------------------------
  if(met->size()==0) return;

  double relErr;
  double HT=0;
  double HTx=0;
  double HTy=0;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      if ((*jets)[i].et() < 10.) continue;
      PFJetEt_Eta_   ->Fill((*jets)[i].et(),            (*jets)[i].eta(), weight);
      PFJetEt_   ->Fill((*jets)[i].et(),            weight);
      PFCSV_  ->Fill((*jets)[i].bDiscriminator("combinedSecondaryVertexBJetTags"), weight);
      HT+=(*jets)[i].et();
      HTx+=(*jets)[i].px();
      HTy+=(*jets)[i].py();

      chargeEMFractionPF_ ->Fill((*jets)[i].chargedEmEnergyFraction(), weight);
      neutralEMFractionPF_ ->Fill((*jets)[i].neutralEmEnergyFraction(), weight);

      if ( (*jets)[i].genJet() ) {
	if ( (*jets)[i].genJet()->et() > 0. ) {

	  GenJetEt_Eta_->Fill((*jets)[i].genJet()->et(),  (*jets)[i].eta(), weight);
	  GenJetEt_->Fill((*jets)[i].genJet()->et(),  weight);

	  relErr = ((*jets)[i].et()/(*jets)[i].genJet()->et())-1.;
	  PFJetRelErr_->Fill(relErr, weight);
	}
      }
    }
  if (HT > 0.) {
    double YMET=((*met)[0].et())/(sqrt(HT));
    YMET_->Fill(YMET, weight);
    HT_ ->Fill(HT, weight);
    MHT_->Fill(sqrt(HTx*HTx + HTy*HTy),weight);
  }
  double relIso=0.;
  if (muons->size() > 0. ) {
    MuPt_ ->Fill((*muons)[0].pt(), weight);
    if ((*muons)[0].pt() > 0. ) {
      relIso = ((*muons)[0].trackIso()+(*muons)[0].ecalIso()+(*muons)[0].hcalIso())/(*muons)[0].pt();
      MuIso_->Fill(relIso, weight);
      MuIso_NPV_->Fill(pv, relIso, weight);
    }
    MuHCal_->Fill((*muons)[0].calEnergy().had, weight);
    MuHCal_NPV_->Fill(pv,(*muons)[0].calEnergy().had, weight);
    MuHO_->Fill((*muons)[0].calEnergy().ho, weight);
    MuHO_NPV_->Fill(pv, (*muons)[0].calEnergy().ho, weight);
  }

  if (electrons->size() > 0. ) {
    ElePt_ ->Fill((*electrons)[0].pt(), weight);
    relIso=(*electrons)[0].dr03EcalRecHitSumEt();
    if(fabs((*electrons)[0].eta())<1.479) relIso=max(0.,(relIso-1.));
    if ((*electrons)[0].pt() > 0. ) {
      relIso= ((*electrons)[0].dr03TkSumPt()+relIso+(*electrons)[0].dr03HcalTowerSumEt())/(*electrons)[0].pt();
      EleIso_->Fill(relIso, weight);
      EleIso_NPV_->Fill(pv,relIso, weight);
    }
    EleHOverEM_->Fill((*electrons)[0].hcalOverEcal(), weight);
    EleHOverEM_NPV_->Fill(pv, (*electrons)[0].hcalOverEcal(),weight);
  }
  for(int i=0; i<(int)caloJets->size(); ++i)
    {
      CaloJetEt_Eta_   ->Fill((*caloJets)[i].et(),            (*caloJets)[i].eta(), weight);      
      CaloJetEt_   ->Fill((*caloJets)[i].et(),            weight);
      CaloCSV_  ->Fill((*caloJets)[i].bDiscriminator("combinedSecondaryVertexBJetTags"), weight);
      if ((*caloJets)[i].isCaloJet()) HOEnergy_Eta_->Fill((*caloJets)[i].hadEnergyInHO(), (*caloJets)[i].eta(), weight);
      if ((*caloJets)[i].isCaloJet()) HOEnergy_->Fill((*caloJets)[i].hadEnergyInHO(), weight);

      EMFractionCalo_ ->Fill((*caloJets)[i].emEnergyFraction(), weight);
      
    }
  
  PFMET_Eta_->Fill((*met)[0].et(), (*met)[0].eta(), weight); 
  PFMET_Phi_->Fill((*met)[0].et(), (*met)[0].phi(), weight);
  PFMET_->Fill((*met)[0].et(), weight); 

  if (caloMet->size()>0) {
    CaloMET_Eta_->Fill((*caloMet)[0].et(), (*caloMet)[0].eta(), weight); 
    CaloMET_Phi_->Fill((*caloMet)[0].et(), (*caloMet)[0].phi(), weight);
    CaloMET_->Fill((*caloMet)[0].et(), weight);
    /*
    if ( (*caloMet)[0].genMET()->et() > 0. ) {
      relErr = ((*caloMet)[0].et()/(*caloMet)[0].genMET()->et())-1.;
      CaloMETRelErr_->Fill(relErr, weight);
    }*/
  }
  
  if ( (*met)[0].genMET() ) {
    if ( (*met)[0].genMET()->et() > 0. ) {
      relErr = ((*met)[0].et()/(*met)[0].genMET()->et())-1.;
      PFMETRelErr_->Fill(relErr, weight);
    }
  }
}

void HCalAnalyzer::beginJob()
{  
} 

void HCalAnalyzer::endJob()
{
}
