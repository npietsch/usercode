#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "Btagging/BtagAnalyzer/plugins/BtagSystematicsAnalyzer.h"
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
 
BtagSystematicsAnalyzer::BtagSystematicsAnalyzer(const edm::ParameterSet& cfg):
  // collections of R44b objects
  jets_         (cfg.getParameter<edm::InputTag>("jets") ),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets" )),
  muons_        (cfg.getParameter<edm::InputTag>("muons" )),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons") ),
  met_          (cfg.getParameter<edm::InputTag>("met") ),
  // for event weighting
  PVSrc_                  (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_                 (cfg.getParameter<edm::InputTag>("PUInfo") ),
  PUWeight_               (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_              (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEventWeights_       (cfg.getParameter<edm::InputTag>("BtagEventWeights") ),
  BtagJetWeights_         (cfg.getParameter<edm::InputTag>("BtagJetWeights") ),
  BtagJetWeightsGrid_     (cfg.getParameter<edm::InputTag>("BtagJetWeightsGrid") ),
  BtagEventWeightsGrid_   (cfg.getParameter<edm::InputTag>("BtagEventWeightsGrid") ),
  MistagEventWeightsGrid_ (cfg.getParameter<edm::InputTag>("MistagEventWeightsGrid") ),
  // bool
  useEventWgt_          (cfg.getParameter<bool>("useEventWeight") ),
  useBtagEventWgt_      (cfg.getParameter<bool>("useBtagEventWeight") ),
  // int
  btagBin_              (cfg.getParameter<int>("btagBin") )

{ 
  edm::Service<TFileService> fs;

  Dummy_ = fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_ = fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);

  // ABCD plots
  for(int i=0; i<4; ++i)
    {
      char histnameA[40];
      sprintf(histnameA,"BtagWeightsA_%ibtags",i);
      BtagWeightsGridA_[i]=fs->make<TH1F>(histnameA,histnameA, 21, 0., 21.);

      char histnameB[40];
      sprintf(histnameB,"BtagWeightsB_%ibtags",i);
      BtagWeightsGridB_[i]=fs->make<TH1F>(histnameB,histnameB, 21, 0., 21.);

      char histnameC[40];
      sprintf(histnameC,"BtagWeightsC_%ibtags",i);
      BtagWeightsGridC_[i]=fs->make<TH1F>(histnameC,histnameC, 21, 0., 21.);

      char histnameD[40];
      sprintf(histnameD,"BtagWeightsD_%ibtags",i);
      BtagWeightsGridD_[i]=fs->make<TH1F>(histnameD,histnameD, 21, 0., 21.);
    }

  for(int i=0; i<4; ++i)
    {
      char histnameA[40];
      sprintf(histnameA,"MistagWeightsA_%ibtags",i);
      MistagWeightsGridA_[i]=fs->make<TH1F>(histnameA,histnameA, 21, 0., 21.);

      char histnameB[40];
      sprintf(histnameB,"MistagWeightsB_%ibtags",i);
      MistagWeightsGridB_[i]=fs->make<TH1F>(histnameB,histnameB, 21, 0., 21.);

      char histnameC[40];
      sprintf(histnameC,"MistagWeightsC_%ibtags",i);
      MistagWeightsGridC_[i]=fs->make<TH1F>(histnameC,histnameC, 21, 0., 21.);

      char histnameD[40];
      sprintf(histnameD,"MistagWeightsD_%ibtags",i);
      MistagWeightsGridD_[i]=fs->make<TH1F>(histnameD,histnameD, 21, 0., 21.);
    }

  // control plots
  nPV_noWgt_ = fs->make<TH1F>("nPV_noWgt","nPV_noWgt", 50, 0.,  50  );
  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0.,  50  );
  nPU_noWgt_ = fs->make<TH1F>("nPU_noWgt","nPU_noWgt", 50, 0.5, 50.5);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt","btagWeights_noWgt", 4, 0., 4.);
  btagWeights_ = fs->make<TH1F>("btagWeights","btagWeights", 4, 0., 4.);
  nBtags_noWgt_ = fs->make<TH1F>("nBtags_noWgt","nBtags_noWgt", 4, 0., 4.); 
  nBtags_ = fs->make<TH1F>("nBtags","nBtags", 4, 0., 4.);

  TCHE_= fs->make<TH1F>("TCHE","TCHE", 80, -20., 20.);
  TCHP_= fs->make<TH1F>("TCHP","TCHP", 80, -20., 20.);
  SSVHE_= fs->make<TH1F>("SSVHE","SSVHE", 120, -2, 10.);
  SSVHP_= fs->make<TH1F>("SSVHP","SSVHP", 120, -2, 10.);

  MET_ = fs->make<TH1F>("MET","MET", 40, 0.,  1000.);
  HT_  = fs->make<TH1F>("HT","HT",   40, 0.,  2000.);
  MHT_ = fs->make<TH1F>("MHT","MHT", 50, 0.,  1000.);
}

BtagSystematicsAnalyzer::~BtagSystematicsAnalyzer()
{
}

void BtagSystematicsAnalyzer::beginJob()
{  
} 

void
BtagSystematicsAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

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
  double weight0b=0;
  double weight1b=0;
  double weight2b=0;
  double weight3b=0;
  // obsolete
  //double weightBtagEff=1;

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
      
      // if events should be weighted according to b-tag efficiency and mistag-rates
      if(useBtagEventWgt_)
	{
	  // Btag weight
	  edm::Handle<std::vector<double> > BtagEventWeightsHandle;
	  evt.getByLabel(BtagEventWeights_, BtagEventWeightsHandle);

	  // define weights for each b-tag bin
	  weight0b=(*BtagEventWeightsHandle)[0];
	  weight1b=(*BtagEventWeightsHandle)[1];
	  weight2b=(*BtagEventWeightsHandle)[2];
	  weight3b=(*BtagEventWeightsHandle)[3];

	  // fill histograms to monitor b-tag weighting
	  btagWeights_noWgt_->Fill(0.,weight0b);
	  btagWeights_noWgt_->Fill(1, weight1b);
	  btagWeights_noWgt_->Fill(2, weight2b);
	  btagWeights_noWgt_->Fill(3, weight3b);

	  btagWeights_->Fill(0.,weight*weight0b);
	  btagWeights_->Fill(1, weight*weight1b);
	  btagWeights_->Fill(2, weight*weight2b);
	  btagWeights_->Fill(3, weight*weight3b);

	  //std::cout << "BtagSystematicsAnalyzer: " << (*BtagEventWeightsHandle).size() << std::endl;
	  //std::cout << "BtagSystematicsAnalyzer: " << weight0b << std::endl;
	  //std::cout << "BtagSystematicsAnalyzer: " << weight1b << std::endl;
	  //std::cout << "BtagSystematicsAnalyzer: " << weight2b << std::endl;
	  //std::cout << "BtagSystematicsAnalyzer: " << weight3b << std::endl;
	  //std::cout << "BtagSystematicsAnalyzer: " << weight0b+weight1b+weight2b+weight3b << std::endl;
	  //// obsolete
	  // weightBtagEvent=(*BtagEventWeightsHandle)[btagBin_];
	}

      //std::cout << "--------------------------------" << std::endl;
      //std::cout << "weightPU: "      << weightPU      << std::endl;
      //std::cout << "weightRA2: "     << weightRA2     << std::endl;
      //std::cout << "weight: " << weight << std::endl;
      //std::cout << "--------------------------------" << std::endl;
      
      // -----------------------------------------------------------------------

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

      // fill to monitor PU weighting
      nPU_noWgt_->Fill(nvtx);
      nPU_->Fill(nvtx,weight);
    }
  
  //------------------------------------------------------
  // control plots
  //------------------------------------------------------
  
  // number of primary vertices
  nPV_->Fill(PVSrc->size(), weight);
  nPV_noWgt_->Fill(PVSrc->size());

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

  //------------------------------------------------------
  // ABCD plots
  //------------------------------------------------------

  double sigMET=((*met)[0].et())/(sqrt(HT));

  if(useBtagEventWgt_)
    {
      // btag event weights grid 
      edm::Handle<std::vector<std::vector<double> > > BtagEventWeightsGridHandle;
      evt.getByLabel(BtagEventWeightsGrid_, BtagEventWeightsGridHandle);
      
      // loop over shifted scale factors
      for(int sdx=0; sdx<=20; ++sdx)
	{
	  // loop over b-tag bins
	  for(int idx=0; idx<4; ++idx)
	    {
	      // Fill event weight for scale factor sdx and b-tag bin idx in histogram
	      if(HT >= 375 && HT < 650 && sigMET >=3.25 && sigMET < 5.5)
		{
		  BtagWeightsGridA_[idx]->Fill(sdx,weight*(*BtagEventWeightsGridHandle)[sdx][idx]);
		}
	      else if(HT >= 650 && sigMET >= 3.25 && sigMET < 5.5)
		{
		  BtagWeightsGridB_[idx]->Fill(sdx,weight*(*BtagEventWeightsGridHandle)[sdx][idx]);
		}
	      else if(HT >= 375 && HT < 650 && sigMET >= 5.5)
		{
		  BtagWeightsGridC_[idx]->Fill(sdx,weight*(*BtagEventWeightsGridHandle)[sdx][idx]);
		}
	      else if(HT >= 650 && sigMET >= 5.5)
		{
		  BtagWeightsGridD_[idx]->Fill(sdx,weight*(*BtagEventWeightsGridHandle)[sdx][idx]);
		}
	    }
	}

      // mistag event weights grid 
      edm::Handle<std::vector<std::vector<double> > > MistagEventWeightsGridHandle;
      evt.getByLabel(MistagEventWeightsGrid_, MistagEventWeightsGridHandle);

      // loop over shifted scale factors
      for(int sdx=0; sdx<=20; ++sdx)
	{
	  // loop over b-tag bins
	  for(int idx=0; idx<4; ++idx)
	    {
	      // Fill event weight for scale factor sdx and b-tag bin idx in histogram
	      if(HT >= 375 && HT < 650 && sigMET >=3.25 && sigMET < 5.5)
		{
		  MistagWeightsGridA_[idx]->Fill(sdx,weight*(*MistagEventWeightsGridHandle)[sdx][idx]);
		}
	      else if(HT >= 650 && sigMET >= 3.25 && sigMET < 5.5)
		{
		  MistagWeightsGridB_[idx]->Fill(sdx,weight*(*MistagEventWeightsGridHandle)[sdx][idx]);
		}
	      else if(HT >= 375 && HT < 650 && sigMET >= 5.5)
		{
		  MistagWeightsGridC_[idx]->Fill(sdx,weight*(*MistagEventWeightsGridHandle)[sdx][idx]);
		}
	      else if(HT >= 650 && sigMET >= 5.5)
		{
		  MistagWeightsGridD_[idx]->Fill(sdx,weight*(*MistagEventWeightsGridHandle)[sdx][idx]);
		}
	    }
	}

    }
}

void BtagSystematicsAnalyzer::endJob()
{
}
