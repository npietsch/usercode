#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/RA4MuonAnalyzer.h"
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
 
RA4MuonAnalyzer::RA4MuonAnalyzer(const edm::ParameterSet& cfg):
  met_               (cfg.getParameter<edm::InputTag>("met") ),
  jets_              (cfg.getParameter<edm::InputTag>("jets") ),
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
  useTriggerEvtWgt_  (cfg.getParameter<bool>("useTriggerEventWeight") ),

  HT0_               (cfg.getParameter<double>("HT0") ),
  HT1_               (cfg.getParameter<double>("HT1") ),
  HT2_               (cfg.getParameter<double>("HT2") ),
  Y0_                (cfg.getParameter<double>("Y0") ),
  Y1_                (cfg.getParameter<double>("Y1") ),
  Y2_                (cfg.getParameter<double>("Y2") )

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

  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt", "btagWeights_noWgt",  4, 0.,   4. );
  btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt", "btagWeights_PUWgt",  4, 0.,   4. );
  nPU_noWgt_         = fs->make<TH1F>("nPU_noWgt",         "nPU_noWgt",         71, -0.5, 70.5);
  nPU_               = fs->make<TH1F>("nPU",               "nPU",               71, -0.5, 70.5);
  nPV_noWgt_         = fs->make<TH1F>("nPV_noWgt",         "nPV_noWgt",         71, -0.5, 70.5);
  nPV_               = fs->make<TH1F>("nPV",               "nPV",               71, -0.5, 70.5);

  Weight_        = fs->make<TH1F>("Weight",        "Weight",        50 , 0.,   10. );
  WeightPU_      = fs->make<TH1F>("WeightPU",      "WeightPU",      50 , 0.,   10. );
  WeightRA2_     = fs->make<TH1F>("WeightRA2",     "WeightRA2",     50 , 0.,   10. );
  WeightBtagEff_ = fs->make<TH1F>("WeightBtagEff", "WeightBtagEff", 50 , 0.,   10. );
  WeightTrigger_ = fs->make<TH1F>("WeightTrigger", "WeightTrigger", 50 , 0.,   10. );

  //-------------------------------------------------
  // Muon kinematics and ID
  //-------------------------------------------------

  pt_                            = fs->make<TH1F>("pt",                            "pt",                            60 ,  0., 600.);
  eta_                           = fs->make<TH1F>("eta",                           "eta",                           60 , -3.,   3.);
  isGlobalMuon_                  = fs->make<TH1F>("isGlobalMuon",                  "isGlobalMuon",                   2 ,  0.,   2.);
  isTrackerMuon_                 = fs->make<TH1F>("isTrackerMuon",                 "isTrackerMuon",                  2 ,  0.,   2.);
  isPFMuon_                      = fs->make<TH1F>("isPFMuon",                      "isPFMuon",                       2 ,  0.,   2.);
  pfIso_                         = fs->make<TH1F>("pfIso",                         "pfIso",                         50 ,  0.,   1.);
  normChi2_                      = fs->make<TH1F>("normChi2",                      "normChi2",                      20 ,  0.,  20.);
  nValidMuonHits_                = fs->make<TH1F>("nValidMuonHits",                "nValidMuonHits",                10 ,  0.,  10.);
  nMatchedStations_              = fs->make<TH1F>("nMatchedStations",              "nMatchedStations",              10 ,  0.,  10.);
  nPixelHits_                    = fs->make<TH1F>("nPixelHits",                    "nPixelHits",                    20 ,  0.,  20.);
  nTrackerLayersWithMeasurement_ = fs->make<TH1F>("nTrackerLayersWithMeasurement", "nTrackerLayersWithMeasurement", 10 ,  0.,  10.);

}

RA4MuonAnalyzer::~RA4MuonAnalyzer()
{
}

void
RA4MuonAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

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
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);

  //-------------------------------------------------
  // Event weighting
  //----------------------f--------------------------

  // declare and initialize different weights
  double weight=1;
  double weightPU=1;
  double weightRA2=1;
  double weightBtagEff=1;
  double weightTrigger=1;

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
      nPU_->Fill(nvtx,weightPU);
    }

  if(useTriggerEvtWgt_)
    {
      edm::Handle<double> TriggerWeightHandle;
      evt.getByLabel(TriggerWeight_, TriggerWeightHandle);
      weightTrigger=(*TriggerWeightHandle);
      weight=weight*weightTrigger;
    }

  Weight_->Fill(weight);
  WeightPU_->Fill(weightPU);
  WeightRA2_->Fill(weightRA2);
  WeightBtagEff_->Fill(weightBtagEff);
  WeightTrigger_->Fill(weightTrigger);

  // number of primary vertices
  nPV_noWgt_->Fill(PVSrc->size());
  nPV_->Fill(PVSrc->size(),weightPU);

  //-------------------------------------------------
  // Muon variables
  //-------------------------------------------------

  for(int idx=0; idx<(int)muons->size(); ++idx)
    {
      pt_           ->Fill((*muons)[idx].pt(),            weight);
      eta_          ->Fill((*muons)[idx].eta(),           weight);
      isGlobalMuon_ ->Fill((*muons)[idx].isGlobalMuon(),  weight);
      isTrackerMuon_->Fill((*muons)[idx].isTrackerMuon(), weight);
      isPFMuon_     ->Fill((*muons)[idx].isPFMuon(),      weight);

      pfIso_->Fill(((*muons)[idx].pfIsolationR03().sumChargedHadronPt + max(0., (*muons)[idx].pfIsolationR03().sumNeutralHadronEt + (*muons)[idx].pfIsolationR03().sumPhotonEt - 0.5*(*muons)[idx].pfIsolationR03().sumPUPt))/(*muons)[idx].pt(), weight);

      normChi2_                     ->Fill((*muons)[idx].globalTrack()->chi2()/(*muons)[idx].globalTrack()->ndof(), weight);
      nValidMuonHits_               ->Fill((*muons)[idx].globalTrack()->hitPattern().numberOfValidMuonHits(),      weight);
      nMatchedStations_             ->Fill((*muons)[idx].numberOfMatchedStations(),                               weight);
      nPixelHits_                   ->Fill((*muons)[idx].innerTrack()->hitPattern().numberOfValidPixelHits(),      weight);
      nTrackerLayersWithMeasurement_->Fill((*muons)[idx].track()->hitPattern().trackerLayersWithMeasurement(),     weight);

    }

}

void RA4MuonAnalyzer::beginJob()
{  
} 

void RA4MuonAnalyzer::endJob()
{
}
