#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/SystematicsAnalyzer.h"
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
 
SystematicsAnalyzer::SystematicsAnalyzer(const edm::ParameterSet& cfg):
  // collections of R44b objects
  jets_         (cfg.getParameter<edm::InputTag>("jets") ),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets" )),
  muons_        (cfg.getParameter<edm::InputTag>("muons" )),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons") ),
  met_          (cfg.getParameter<edm::InputTag>("met") ),
  // for event weighting
  PVSrc_                (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_               (cfg.getParameter<edm::InputTag>("PUInfo") ),
  PUWeight_             (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_            (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEventWeights_     (cfg.getParameter<edm::InputTag>("BtagEventWeights") ),
  // bool
  useEventWgt_          (cfg.getParameter<bool>("useEventWeight") ),
  useBtagEventWgt_      (cfg.getParameter<bool>("useBtagEventWeight") ),
  // int
  btagBin_              (cfg.getParameter<int>("btagBin") ),
  //SUSY GenEvent
  inputGenEvent_(cfg.getParameter<edm::InputTag>("susyGenEvent"))
{ 
  edm::Service<TFileService> fs;

  Dummy_=fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_=fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);

  // Declare histograms for control quantities
  nPV_noWgt_ = fs->make<TH1F>("nPV_noWgt","nPV_noWgt", 50, 0.,  50  );
  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0.,  50  );
  nPU_noWgt_ = fs->make<TH1F>("nPU_noWgt","nPU_noWgt", 50, 0.5, 50.5);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt","btagWeights_noWgt", 4, 0., 4.);
  btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt","btagWeights_PUWgt", 4, 0., 4.);
  nBtags_noWgt_ = fs->make<TH1F>("nBtags_noWgt","nBtags_noWgt", 4, 0., 4.); 
  nBtags_PUWgt_ = fs->make<TH1F>("nBtags_PUWgt","nBtags_PUWgt", 4, 0., 4.);
  nBtags_ = fs->make<TH1F>("nBtags","nBtags", 4, 0., 4.);

  TCHE_= fs->make<TH1F>("TCHE","TCHE", 80, -20., 20.);
  TCHP_= fs->make<TH1F>("TCHP","TCHP", 80, -20., 20.);
  SSVHE_= fs->make<TH1F>("SSVHE","SSVHE", 120, -2, 10.);
  SSVHP_= fs->make<TH1F>("SSVHP","SSVHP", 120, -2, 10.);

  MET_ = fs->make<TH1F>("MET","MET", 50, 0.,  1000.);
  HT_  = fs->make<TH1F>("HT","HT",   40, 0.,  2000.);
  MHT_ = fs->make<TH1F>("MHT","MHT", 50, 0.,  1000.);
  nJets_ = fs->make<TH1F>("nJets","nJets", 14, 0., 14);
  
  JetsPt_ = fs->make<TH1F>("JetsPt","JetsPt", 90, 0., 90);
  JetsEta_  = fs->make<TH1F>("JetsPt","JetsPt", 60, -3, 3);
  
  for(int idx=0; idx<4; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Pt",idx);
      JetPt_.push_back(fs->make<TH1F>(histname,histname, 90, 0., 900.));
    }
  
  // Declare histograms for ABCD mehtod
  HT_SigMET_ = fs->make<TH2F>("HT_SigMET","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  HT_SigMET2_ = fs->make<TH2F>("HT_SigMET2","HT vs. SigMET2", 36, 200., 2000., 40, 0., 20.);

  //Declare HT-SigMET hist for each SUSY sub processes
  HT_SigMET_gg_ = fs->make<TH2F>("HT_SigMET_gg","HT vs. SigMET (gg)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_gs_ = fs->make<TH2F>("HT_SigMET_gs","HT vs. SigMET (gs)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_ss_ = fs->make<TH2F>("HT_SigMET_ss","HT vs. SigMET (ss)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_sb_ = fs->make<TH2F>("HT_SigMET_sb","HT vs. SigMET (sb)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_tb_ = fs->make<TH2F>("HT_SigMET_tb","HT vs. SigMET (tb)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_bb_ = fs->make<TH2F>("HT_SigMET_bb","HT vs. SigMET (bb)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_ll_ = fs->make<TH2F>("HT_SigMET_ll","HT vs. SigMET (ll)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_nn_ = fs->make<TH2F>("HT_SigMET_nn","HT vs. SigMET (nn)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_ng_ = fs->make<TH2F>("HT_SigMET_ng","HT vs. SigMET (ng)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_ns_ = fs->make<TH2F>("HT_SigMET_ns","HT vs. SigMET (ns)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unknown_ = fs->make<TH2F>("HT_SigMET_unknown","HT vs. SigMET (unknown)", 80, 0., 2000., 80, 0., 20. );

  HT_SigMET_unweighted_gg_ = fs->make<TH2F>("HT_SigMET_unweighted_gg","HT vs. SigMET (gg)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_gs_ = fs->make<TH2F>("HT_SigMET_unweighted_gs","HT vs. SigMET (gs)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_ss_ = fs->make<TH2F>("HT_SigMET_unweighted_ss","HT vs. SigMET (ss)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_sb_ = fs->make<TH2F>("HT_SigMET_unweighted_sb","HT vs. SigMET (sb)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_tb_ = fs->make<TH2F>("HT_SigMET_unweighted_tb","HT vs. SigMET (tb)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_bb_ = fs->make<TH2F>("HT_SigMET_unweighted_bb","HT vs. SigMET (bb)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_ll_ = fs->make<TH2F>("HT_SigMET_unweighted_ll","HT vs. SigMET (ll)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_nn_ = fs->make<TH2F>("HT_SigMET_unweighted_nn","HT vs. SigMET (nn)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_ng_ = fs->make<TH2F>("HT_SigMET_unweighted_ng","HT vs. SigMET (ng)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_ns_ = fs->make<TH2F>("HT_SigMET_unweighted_ns","HT vs. SigMET (ns)", 80, 0., 2000., 80, 0., 20. );
  HT_SigMET_unweighted_unknown_ = fs->make<TH2F>("HT_SigMET_unweighted_unknown","HT vs. SigMET (unknown)", 80, 0., 2000., 80, 0., 20. );

}

SystematicsAnalyzer::~SystematicsAnalyzer()
{
}

void
SystematicsAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //-------------------------------------------------
  // Fetch input collection from the event content
  //-------------------------------------------------

  // collections of RA4b objects
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);

  edm::Handle<SUSYGenEvent> susyGenEvent;
  evt.getByLabel(inputGenEvent_, susyGenEvent);

  // collection of PV vertices
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
      
      if(useBtagEventWgt_)
	{
	  // Btag weight
	  edm::Handle<std::vector<double> > BtagEventWeightsHandle;
	  evt.getByLabel(BtagEventWeights_, BtagEventWeightsHandle);
	  weightBtagEff=(*BtagEventWeightsHandle)[btagBin_];
	
	  btagWeights_noWgt_->Fill(0.,(*BtagEventWeightsHandle)[0]);
	  btagWeights_noWgt_->Fill(1, (*BtagEventWeightsHandle)[1]);
	  btagWeights_noWgt_->Fill(2, (*BtagEventWeightsHandle)[2]);
	  btagWeights_noWgt_->Fill(3, (*BtagEventWeightsHandle)[3]);

	  btagWeights_PUWgt_->Fill(0.,(*BtagEventWeightsHandle)[0]*weight);
	  btagWeights_PUWgt_->Fill(1, (*BtagEventWeightsHandle)[1]*weight);
	  btagWeights_PUWgt_->Fill(2, (*BtagEventWeightsHandle)[2]*weight);
	  btagWeights_PUWgt_->Fill(3, (*BtagEventWeightsHandle)[3]*weight);

 	  //std::cout << "SystematicsAnalyzer: " << (*BtagEventWeightsHandle).size() << std::endl;
 	  //std::cout << "SystematicsAnalyzer: " << (*BtagEventWeightsHandle)[0] << std::endl;
 	  //std::cout << "SystematicsAnalyzer: " << (*BtagEventWeightsHandle)[1] << std::endl;
 	  //std::cout << "SystematicsAnalyzer: " << (*BtagEventWeightsHandle)[2] << std::endl;
 	  //std::cout << "SystematicsAnalyzer: " << (*BtagEventWeightsHandle)[3] << std::endl;
	}
 
      weight=weightRA2*weightPU*weightBtagEff;
      
      //std::cout << "--------------------------------" << std::endl;
      //std::cout << "weightPU: "      << weightPU      << std::endl;
      //std::cout << "weightRA2: "     << weightRA2     << std::endl;
      //std::cout << "weightBtagEff: " << weightBtagEff << std::endl << std::endl;
      //std::cout << "weight: " << weight << std::endl;
      //std::cout << "--------------------------------" << std::endl;
      
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

  //-------------------------------------------------
  // control plots
  //-------------------------------------------------

  // number of primary vertices
  nPV_noWgt_->Fill(PVSrc->size());
  nPV_->Fill(PVSrc->size(), weight);

  // number of b-tagged jets
  unsigned int nBtags = bjets->size();
  if(bjets->size() > 2) nBtags=3;
  nBtags_->Fill(nBtags,weight);
  nBtags_noWgt_->Fill(nBtags);

  // bdisc
  for(int i=0; i<(int)bjets->size();++i)
    {
      TCHE_->Fill((*bjets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
      TCHP_->Fill((*bjets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
      SSVHE_->Fill((*bjets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight);
      SSVHP_->Fill((*bjets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight);
    }

  // MET, HT, MHT
  double MET=(*met)[0].et();
  double HT=0;
  double MHT=0;

  if(jets->size()>0)
    {
      reco::Particle::LorentzVector P4=(*jets)[0].p4();
      for(int i=1; i< (int)jets->size(); ++i)
	{
	  P4=P4+(*jets)[i].p4();
  	}   
      MHT=P4.Et();
    }
  
  // keep HT saparate from MHT calculation
  for(int i=0; i<(int)jets->size();++i)
    {
      HT=HT+(*jets)[i].et();
    }
  
  MET_->Fill(MET,weight);
  HT_->Fill(HT,weight);
  MHT_->Fill(MHT,weight);
  nJets_->Fill(jets->size(),weight);

  // Jets
  for(int jdx=0; jdx<(int)jets->size(); ++jdx)
    {
      JetsPt_->Fill((*jets)[jdx].pt(),weight);
      JetsEta_->Fill((*jets)[jdx].eta(),weight);
      
      if(jdx < 4) JetPt_[jdx]->Fill((*jets)[jdx].pt(),weight);
    }
  
  //-------------------------------------------------
  // ABCD quantities
  //-------------------------------------------------

  // To access memeber funtion XY of object with index INDEX of collection with Handle HANDLENAME:
  // (*HANDELNAME)[INDEX].XY()
  // e.g. (*jets)[0].eta(), (*met)[0].et()

  double sigMET=((*met)[0].et())/(sqrt(HT));
  
  HT_SigMET_->Fill(HT,sigMET, weight);
  HT_SigMET2_->Fill(HT,sigMET, weight);

  //Determine the SUSY sub process and fill the appropriate hist
  //------------------------------------------------------------
  TH2F* HT_SigMET_hist2Fill = 0;
  TH2F* HT_SigMET_unweighted_hist2Fill = 0;
  unsigned numMatchedProcs = 0;

  if (susyGenEvent->GluinoGluinoDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_gg_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_gg_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->GluinoSquarkDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_gs_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_gs_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->SquarkSquarkDecay() == true) {
    //Check if squark-antisquark 
    if (susyGenEvent->ParticleAntiParticleDecay() == true) {
      HT_SigMET_hist2Fill = HT_SigMET_sb_ ;
      HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_sb_ ;
    }
    else {
      HT_SigMET_hist2Fill = HT_SigMET_ss_ ;
      HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_ss_ ;
    }
    numMatchedProcs++;
  }
  if (susyGenEvent->StopStopDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_tb_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_tb_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->SbottomSbottomDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_bb_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_bb_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->SleptonSleptonDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_ll_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_ll_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->EWinoEWinoDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_nn_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_nn_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->EWinoGluinoDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_ng_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_ng_ ;
    numMatchedProcs++;
  }
  if (susyGenEvent->EWinoSquarkDecay() == true) {
    HT_SigMET_hist2Fill = HT_SigMET_ns_ ;
    HT_SigMET_unweighted_hist2Fill = HT_SigMET_unweighted_ns_ ;
    numMatchedProcs++;
  }
  //Check that numMatchedProcs is 1. If not, give an error.
  if (numMatchedProcs == 1 && HT_SigMET_hist2Fill != 0 && HT_SigMET_unweighted_hist2Fill != 0 ) {
    //Note that the hist is filled with weight one.
    HT_SigMET_hist2Fill->Fill(HT, sigMET, weight);
    HT_SigMET_unweighted_hist2Fill->Fill(HT, sigMET, 1.);
  }
  else if (numMatchedProcs == 0) {
    //std::cout << "SUSYGenEventAnalyzer::analyze >> ERROR: Could not find subprocess in event" << std::endl;
    HT_SigMET_unknown_->Fill(HT,sigMET, weight);
    HT_SigMET_unweighted_unknown_->Fill(HT,sigMET, 1.);
  }
  else {
    std::cout << "SystematicsAnalyzer::analyze >> ERROR: More than one subprocess matched in event"  << std::endl;
  }
  //--------------------//----------------------------------------
  





}


void SystematicsAnalyzer::beginJob()
{  
} 

void SystematicsAnalyzer::endJob()
{
}
