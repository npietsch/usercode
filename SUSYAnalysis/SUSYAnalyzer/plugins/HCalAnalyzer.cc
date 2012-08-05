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
#include "DataFormats/Common/interface/ValueMap.h"

#include "RecoJets/JetAnalyzers/interface/JetPlotsExample.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

#include "CMGTools/External/interface/PileupJetIdentifier.h"

using namespace std;
 
HCalAnalyzer::HCalAnalyzer(const edm::ParameterSet& cfg):
  met_               (cfg.getParameter<edm::InputTag>("met") ),
  caloMet_           (cfg.getParameter<edm::InputTag>("caloMet") ),
  jets_              (cfg.getParameter<edm::InputTag>("jets") ),  
  caloJets_          (cfg.getParameter<edm::InputTag>("caloJets") ),
  bjets_             (cfg.getParameter<edm::InputTag>("bjets") ),
  muons_             (cfg.getParameter<edm::InputTag>("muons") ),
  electrons_         (cfg.getParameter<edm::InputTag>("electrons") ),
  PVSrc_             (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_            (cfg.getParameter<edm::InputTag>("PUInfo") ),

  useJetID_          (cfg.getParameter<bool>("useJetID") ),
  usePileUp_         (cfg.getParameter<bool>("usePileUp") )

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
  // PU and PV
  //-------------------------------------------------

  nPU_               = fs->make<TH1F>("nPU", "nPU", 81, 0.5, 80.5 );
  nPV_               = fs->make<TH1F>("nPV", "nPV", 81, 0.5, 80.5 );

  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------

  //Jets 1D

  nJets_      = fs->make<TH1F>("nJets",       "nJets",       16, -0.5,  15.5);
  nCaloJets_  = fs->make<TH1F>("nCaloJets",   "nCaloJets",   16, -0.5,  15.5);
  jetsEt_     = fs->make<TH1F>("jetsEt",      "jetsEt",     100,   0., 1000.);
  jetsEta_    = fs->make<TH1F>("jetsEta",     "jetsEta",    100, -2.5,   2.5);
  caloJetsEt_ = fs->make<TH1F>("caloJetsEt",  "caloJetsEt", 100,   0.,  1000);
  caloJetsEta_= fs->make<TH1F>("caloJetsEta", "caloJetsEta",100, -2.5,   2.5);
  genJetsEt_  = fs->make<TH1F>("genJetsEt",   "genJetsEt",  100,   0.,  100.);
  genJetsEta_ = fs->make<TH1F>("genJetsEta",  "genJetsEta", 100, -2.5,   2.5);

  TString histoname;
  for(int idx=0; idx<4; ++idx) {
    histoname="jet"; histoname+=idx+1; histoname+="Et";
    jetEt_.push_back(fs->make<TH1F>(histoname,histoname, 100, 0., 1000.));

    histoname+="a";
    jetEta_.push_back(fs->make<TH1F>(histoname,histoname, 100, -2.5, 2.5));
  }
  

  HOEnergy_            = fs->make<TH1F>("HOEnergy",            "HOEnergy",              100, 0.,  10.);
  chargeEMFraction_  = fs->make<TH1F>("chargeEMFraction",  "charge EM fraction",  100, 0.,   1.);
  neutralEMFraction_ = fs->make<TH1F>("neutralEMFraction", "neutral EM fraction", 100, 0.,   1.);
  EMFractionCalo_      = fs->make<TH1F>("EMFractionCalo",      "EM fractionCalo",       100, 0.,   1.);

  jetsRelErr_     = fs->make<TH1F>("PFJetRelErr",   "jetsRelErr",   300, -3., 3.);
  caloJetsRelErr_ = fs->make<TH1F>("CaloJetRelErr", "CaloJetRelErr", 300, -3., 3.);
  METRelErr_     = fs->make<TH1F>("METRelErr",     "METRelErr",     300, -3., 3.);
  caloMETRelErr_ = fs->make<TH1F>("METRelErr",     "METRelErr",     300, -3., 3.);


  //Jets 2D

  jetsEt_Eta_     = fs->make<TH2F>("jetEt_Eta",     "jetEt Eta",     100, 0., 1000., 100, -3., 3);
  caloJetsEt_Eta_ = fs->make<TH2F>("caloJetEt_Eta", "caloJetEt Eta", 100, 0., 1000., 100, -3., 3);
  genJetsEt_Eta_  = fs->make<TH2F>("genJetEt_Eta",  "genJetEt Eta",  100, 0., 1000., 100, -3., 3);
  HOEnergy_Eta_   = fs->make<TH2F>("HOEnergy_Eta",  "HOEnergy Eta",  100, 0.,   10., 100, -3., 3);

  //bJets

  nBjets_  = fs->make<TH1F>("nbJets",  "nbJets",    16, -0.5,  15.5);
  CSV_     = fs->make<TH1F>("CSV",   "CSV",    80,  -2.,     2);
  caloCSV_ = fs->make<TH1F>("CaloCSV", "Calo CSV",  80,  -2.,     2);
  bJetsEt_  = fs->make<TH1F>("bJetEt",  "bJetEt",   100,   0., 1000.);
  bJetsEta_ = fs->make<TH1F>("bJetEta", "bJetEta",  100, -2.5,   2.5);

  for(int idx=0; idx<4; ++idx) {
    histoname="bJet"; histoname+=idx+1; histoname+="Et";
    bJetEt_.push_back(fs->make<TH1F>(histoname,histoname, 100, 0., 1000.));

    histoname+="a";
    bJetEta_.push_back(fs->make<TH1F>(histoname,histoname, 100, -2.5, 2.5));
  }

  partonFlavour_          = fs->make<TH1I>("partonFlavour",          "partonFlavour",           27, -5.5, 21.5);
  correctlyBtaggedJetsEt_ = fs->make<TH1F>("correctlyBtaggedJetsEt", "correctlyBtaggedJetsEt", 200,   0., 500.);
  mistaggedBjetsEt_       = fs->make<TH1F>("mistaggedBjetsEt",       "mistaggedBjetsEt",       200,   0., 500.);
  allPartonMatchedJetsEt_ = fs->make<TH1F>("allPartonMatchedJetsEt", "allPartonMatchedJetsEt", 200,   0., 500.);
  trueBjetsEt_            = fs->make<TH1F>("trueBjetsEt",            "trueBjetsE",             200,   0., 500.);
  trueLightJetsEt_        = fs->make<TH1F>("trueLightJetsEt",        "trueLightJetsEt",        200,   0., 500.);

  //Muon

  muPt_       = fs->make<TH1F>("muPt",       "mu Pt",      100,   0., 300.);
  muIso_      = fs->make<TH1F>("muIso",      "muIso",       48,   0.,  1.2);
  muIso_NPV_  = fs->make<TH2F>("muIso_NPV",  "muIso NPV",   81, -0.5,  80.5,  50, 0.,   1.);
  muIso_NPU_  = fs->make<TH2F>("muIso_NPU",  "muIso NPV",   81, -0.5 , 80.5,  50, 0.,   1.);
  muHCal_     = fs->make<TH1F>("muHCal",     "muHCal",     100,   0., 100.);
  muHCal_NPV_ = fs->make<TH2F>("muHCal_NPV", "muHCal NPV",  81, -0.5,  80.5, 100, 0., 100.);
  muHCal_NPU_ = fs->make<TH2F>("muHCal_NPU", "muHCal NPU",  81, -0.5,  80.5, 100, 0., 100.);
  muHO_       = fs->make<TH1F>("muH0",       "muH0",       100,   0., 100.);
  muHO_NPV_   = fs->make<TH2F>("muHO_NPV",   "muHO NPV",    81, -0.5,  80.5, 100, 0., 100.);
  muHO_NPU_   = fs->make<TH2F>("muHO_NPU",   "muHO NPU",    81, -0.5,  80.5, 100, 0., 100.);

  //Electron

  elePt_          = fs->make<TH1F>("elePt",           "ele Pt",          100,   0., 300.);
  eleIso_         = fs->make<TH1F>("eleIso",          "eleIso",           50,   0.,   2.);
  eleIso_NPV_     = fs->make<TH2F>("eleIso_NPV",      "eleIso NPV",       81, -0.5,  80.5,  50, 0., 1.); 
  eleIso_NPU_     = fs->make<TH2F>("eleIso_NPU",      "eleIso NPU",       81, -0.5,  80.5,  50, 0., 1.);
  eleHOverEM_     = fs->make<TH1F>("eleHOverEM",      "eleHOverEM",       50,   0.,   1.);
  eleHOverEM_NPV_ = fs->make<TH2F>(" eleHOverEM_NPV", " eleHOverEM NPV",  81,   0.,   50.,  50, 0., 1.);
  eleHOverEM_NPU_ = fs->make<TH2F>(" eleHOverEM_NPU", " eleHOverEM NPU",  81,   0.,   50.,  50, 0., 1.);

  //Composite

  HT_          = fs->make<TH1F>("HT",          "HT",           40, 0., 2000.);
  MHT_         = fs->make<TH1F>("MET",         "MET",         100, 0., 1000.);
  MET_         = fs->make<TH1F>("MET",         "MET",         100, 0., 1000.);
  YMET_        = fs->make<TH1F>("YMET",        "YMET",         80, 0., 20.);
  caloMET_     = fs->make<TH1F>("caloMET",     "caloMET",     100, 0., 1000.);
  MET_Eta_     = fs->make<TH2F>("MET_Eta",     "MET Eta",     100, 0.,  1000., 100, -3., 3);
  MET_Phi_     = fs->make<TH2F>("MET_Phi",     "MET Phi",     100, 0.,  1000., 100, -1*TMath::Pi(), TMath::Pi());
  caloMET_Eta_ = fs->make<TH2F>("caloMET_Eta", "caloMET Eta", 100, 0.,  1000., 100, -3., 3);
  caloMET_Phi_ = fs->make<TH2F>("caloMET_Phi", "caloMET Phi", 100, 0.,  1000., 100, -1*TMath::Pi(), TMath::Pi());

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
  edm::Handle<edm::View<pat::Jet> > jets;
  evt.getByLabel(jets_, jetsTmp);
  if (useJetID_) {
    edm::Handle<edm::ValueMap<float> > puJetIdMVA;
    evt.getByLabel("puJetMvaAK5PF","fullDiscriminant", puJetIdMVA);
    
    edm::Handle<edm::ValueMap<int> > puJetIdFlag;
    evt.getByLabel("puJetMvaAK5PF","fullId", puJetIdFlag);
 
    for ( unsigned int i=0; i<jetsTmp->size(); ++i ) {
      const pat::Jet & patjet = jetsTmp->at(i);
      float mva   = (*puJetIdMVA)[jetsTmp->refAt(i)];
      int    idflag = (*puJetIdFlag)[jetsTmp->refAt(i)];
      cout << "jet " << i << " pt " << patjet.pt() << " eta " << patjet.eta() << " PU JetID MVA " << mva; 
      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose )) {
	cout << " pass loose wp";
      }
      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kMedium )) {
	cout << " pass medium wp";
	jets.push_back(jetsTmp->at(i));
      }
      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kTight )) {
	cout << " pass tight wp";
      }
      cout << endl;
    }
  }
    
  else {
    for ( unsigned int i=0; i<jetsTmp->size(); ++i ) {
      jets.push_back(jetsTmp->at(i));
    }
  }

  edm::Handle<std::vector<pat::Jet> > caloJets;
  evt.getByLabel(caloJets_, caloJets);

  std::vector<pat::Jet> bjets;
  if (useJetID_) {
    for ( unsigned int i=0; i<jets.size(); ++i ) {
      if (jets[i].bDiscriminator("combinedSecondaryVertexBJetTags") > 0.679) {
	bjets.push_back(jets.at(i));
      }
    }
  }
  else {
    edm::Handle<std::vector<pat::Jet> > bjetsTmp;
    for ( unsigned int i=0; i<bjetsTmp->size(); ++i ) {
      bjets.push_back(bjetsTmp->at(i));
    }
  }

  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);

  //-------------------------------------------------
  // PU and PV
  //-------------------------------------------------
  
   std::cout<<"here pu"<<std::endl;

  double nvtx=-1;
  double weight=1.;
  if (usePileUp_) {
    edm::Handle<edm::View<PileupSummaryInfo> > PUInfoHandle;
    evt.getByLabel(PUInfo_, PUInfoHandle);
    
    edm::View<PileupSummaryInfo>::const_iterator iterPU;
    
    for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)
      { 
	if (iterPU->getBunchCrossing()==0)
	  {
	    nvtx = iterPU->getPU_NumInteractions();
	  }
      }
  }

  nPU_->Fill(nvtx,weight);
  float pv = PVSrc->size();
  nPV_->Fill(pv, weight);

  //-------------------------------------------------
  // Basic variables
  //-------------------------------------------------

  //Jets
  std::cout<<"here jets"<<std::endl;
  if(met->size()==0) return;

  double relErr;
  double HT=0;
  double HTx=0;
  double HTy=0;

  for(int i=0; i<(int)jets.size(); ++i) {

      nJets_      ->Fill( jets.size(),            weight);
      jetsEt_     ->Fill(jets[i].et(),            weight);
      jetsEta_    ->Fill(jets[i].eta(),            weight);
      jetsEt_Eta_ ->Fill(jets[i].et(),  jets[i].eta(), weight);

      if (i<4) {
	jetEt_[i]   ->Fill(jets[i].et(),            weight);
	jetEta_[i]   ->Fill(jets[i].eta(),            weight);
      }

      chargeEMFraction_ ->Fill(jets[i].chargedEmEnergyFraction(), weight);
      neutralEMFraction_ ->Fill(jets[i].neutralEmEnergyFraction(), weight);

      if ( jets[i].genJet() ) {
	if ( jets[i].genJet()->et() > 0. ) {
	  
	  genJetsEt_->Fill(jets[i].genJet()->et(),  weight);
	  genJetsEta_->Fill(jets[i].genJet()->eta(),  weight);
	  genJetsEt_Eta_->Fill(jets[i].genJet()->et(),  jets[i].genJet()->eta(), weight);

	  relErr = (jets[i].et()/jets[i].genJet()->et())-1.;
	  jetsRelErr_->Fill(relErr, weight);
	}
      }

      CSV_  ->Fill(jets[i].bDiscriminator("combinedSecondaryVertexBJetTags"), weight);

      HT+=jets[i].et();
      HTx+=jets[i].px();
      HTy+=jets[i].py();

      int flavour=jets[i].partonFlavour();
      float pt=jets[i].pt();
      partonFlavour_ ->Fill(flavour, weight);
      if (flavour == 0) continue;
      allPartonMatchedJetsEt_->Fill(pt, weight);
      if (abs(flavour) == 5){
	trueBjetsEt_->Fill(pt, weight);
	if (jets[i].bDiscriminator("combinedSecondaryVertexBJetTags") > 0.679) correctlyBtaggedJetsEt_->Fill(pt, weight);
      }
      else{
	trueLightJetsEt_->Fill(pt, weight);
	if (jets[i].bDiscriminator("combinedSecondaryVertexBJetTags") > 0.679) mistaggedBjetsEt_->Fill(pt, weight);
      }
  }
  
  std::cout<<"composit"<<std::endl;
  if (HT > 0.) {
    std::cout<<"YMET"<<std::endl;
    double YMET=((*met)[0].et())/(sqrt(HT));
    std::cout<<"YMET FIll"<<std::endl;
    YMET_->Fill(YMET, weight);
     std::cout<<"HT fill"<<std::endl;
    HT_ ->Fill(HT, weight);
     std::cout<<"MHT fill"<<std::endl;
    MHT_->Fill(sqrt(HTx*HTx + HTy*HTy),weight);
  }

  std::cout<<"met"<<std::endl;
  MET_->Fill((*met)[0].et(), weight); 
  MET_Eta_->Fill((*met)[0].et(), (*met)[0].eta(), weight); 
  MET_Phi_->Fill((*met)[0].et(), (*met)[0].phi(), weight);

  std::cout<<"calo met"<<std::endl;
  if (caloMet->size()>0) {

    caloMET_->Fill((*caloMet)[0].et(), weight);
    caloMET_Eta_->Fill((*caloMet)[0].et(), (*caloMet)[0].eta(), weight); 
    caloMET_Phi_->Fill((*caloMet)[0].et(), (*caloMet)[0].phi(), weight);
    /*
    if ( (*caloMet)[0].genMET()->et() > 0. ) {
      relErr = ((*caloMet)[0].et()/(*caloMet)[0].genMET()->et())-1.;
      CaloMETRelErr_->Fill(relErr, weight);
      }*/
  }
  
  
  std::cout<<"here gen met"<<std::endl;

  if ( (*met)[0].genMET() ) {
    if ( (*met)[0].genMET()->et() > 0. ) {
      relErr = ((*met)[0].et()/(*met)[0].genMET()->et())-1.;
      METRelErr_->Fill(relErr, weight);
    }
  }

  //calo jets

   std::cout<<"here calo jets"<<std::endl;

  for(int i=0; i<(int)caloJets->size(); ++i)
    {
      
      nCaloJets_   ->Fill(caloJets->size(),            weight);
      caloJetsEt_   ->Fill((*caloJets)[i].et(),            weight);
      caloJetsEta_   ->Fill((*caloJets)[i].eta(),            weight);
      caloJetsEt_Eta_   ->Fill((*caloJets)[i].et(),            (*caloJets)[i].eta(), weight);

      HOEnergy_->Fill((*caloJets)[i].hadEnergyInHO(), weight);
      HOEnergy_Eta_->Fill((*caloJets)[i].hadEnergyInHO(), (*caloJets)[i].eta(), weight);
      EMFractionCalo_ ->Fill((*caloJets)[i].emEnergyFraction(), weight);
      

      /*if ( (*caloJets)[i].genJet() ) {
	if ( (*caloJets)[i].genJet()->et() > 0. ) {
	  relErr = ((*caloJets)[i].et()/(*caloJets)[i].genJet()->et())-1.;
	  caloJetsRelErr_->Fill(relErr, weight);
	}
	}*/

      caloCSV_  ->Fill((*caloJets)[i].bDiscriminator("combinedSecondaryVertexBJetTags"), weight);

    }

  //bJets

   std::cout<<"here b jets"<<std::endl;

  for(int i=0; i<(int)bjets.size(); ++i)
    {
    
      nBjets_   ->Fill(bjets.size(),            weight);
      bJetsEt_   ->Fill(bjets[i].et(),            weight);
      bJetsEta_   ->Fill(bjets[i].eta(),            weight);

      if (i<4) {
	bJetEt_[i]   ->Fill(bjets[i].et(),            weight);
	bJetEta_[i]   ->Fill(bjets[i].eta(),            weight);
      }
    }

  //muon

  double relIso=0.;
  if (muons->size() > 0. ) {
    muPt_ ->Fill((*muons)[0].pt(), weight);
    if ((*muons)[0].pt() > 0. ) {
      relIso = ((*muons)[0].trackIso()+(*muons)[0].ecalIso()+(*muons)[0].hcalIso())/(*muons)[0].pt();
      muIso_->Fill(relIso, weight);
      muIso_NPV_->Fill(pv, relIso, weight);
      muIso_NPU_->Fill(nvtx, relIso, weight);
    }
    muHCal_->Fill((*muons)[0].calEnergy().had, weight);
    muHCal_NPV_->Fill(pv,(*muons)[0].calEnergy().had, weight);
    muHCal_NPU_->Fill(nvtx,(*muons)[0].calEnergy().had, weight);
    muHO_->Fill((*muons)[0].calEnergy().ho, weight);
    muHO_NPV_->Fill(pv, (*muons)[0].calEnergy().ho, weight);
    muHO_NPU_->Fill(nvtx, (*muons)[0].calEnergy().ho, weight);
  }

  //electron

  if (electrons->size() > 0. ) {
    elePt_ ->Fill((*electrons)[0].pt(), weight);
    relIso=(*electrons)[0].dr03EcalRecHitSumEt();
    if(fabs((*electrons)[0].eta())<1.479) relIso=max(0.,(relIso-1.));
    if ((*electrons)[0].pt() > 0. ) {
      relIso= ((*electrons)[0].dr03TkSumPt()+relIso+(*electrons)[0].dr03HcalTowerSumEt())/(*electrons)[0].pt();
      eleIso_->Fill(relIso, weight);
      eleIso_NPV_->Fill(pv,relIso, weight);
      eleIso_NPU_->Fill(nvtx,relIso, weight);
    }
    eleHOverEM_->Fill((*electrons)[0].hcalOverEcal(), weight);
    eleHOverEM_NPV_->Fill(pv, (*electrons)[0].hcalOverEcal(),weight);
    eleHOverEM_NPU_->Fill(nvtx, (*electrons)[0].hcalOverEcal(),weight);
  }
}

void HCalAnalyzer::beginJob()
{  
} 

void HCalAnalyzer::endJob()
{
}
