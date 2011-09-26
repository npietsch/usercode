#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "Btagging/BtagAnalyzer/plugins/BtagAnalyzer.h"
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
 
BtagAnalyzer::BtagAnalyzer(const edm::ParameterSet& cfg):
  met_              (cfg.getParameter<edm::InputTag>("met")),
  jets_             (cfg.getParameter<edm::InputTag>("jets")),
  bjets_            (cfg.getParameter<edm::InputTag>("bjets")), 
  matchedLightJets_ (cfg.getParameter<edm::InputTag>("matchedLightJets")),
  matchedBjets_     (cfg.getParameter<edm::InputTag>("matchedBjets")),
  muons_            (cfg.getParameter<edm::InputTag>("muons")),
  electrons_        (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_            (cfg.getParameter<edm::InputTag>("pvSrc") ),
  weight_           (cfg.getParameter<edm::InputTag>("weight") ),
  PUSource_         (cfg.getParameter<edm::InputTag>("PUInfo") ),
  RA2weight_        (cfg.getParameter<edm::InputTag>("RA2weight") ),
  useEvtWgt_        (cfg.getParameter<bool>("useEventWeight") )

{ 
  edm::Service<TFileService> fs;

  Dummy_=fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_=fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);
  
  BjetsPt_ = fs->make<TH1F>("BjetsPt","BjetsPt", 50, 0., 500.);
  LightJetsPt_ = fs->make<TH1F>("LightJetsPt","LightJetsPt", 50, 0., 500.);
  BtagsPt_ = fs->make<TH1F>("BtagsPt","BtagsPt", 50, 0., 500.);
  JetsPt_ = fs->make<TH1F>("BtagsPt","BtagsPt", 50, 0., 500.);

  BjetsBdisc_ = fs->make<TH1F>("BjetsBdisc","BjetsBdisc", 160, -20, 20.);
  LightJetsBdisc_ = fs->make<TH1F>("LightJetsBdisc","LightJetsBdisc", 160., -20, 20.);
  JetsBdisc_ = fs->make<TH1F>("JetsBdisc","JetsBdisc", 160, -20, 20.);

  BjetsBdiscLowPt_ = fs->make<TH1F>("BjetsBdiscLowPt","BjetsBdiscLowPt", 160, -20, 20.);
  LightJetsBdiscLowPt_ = fs->make<TH1F>("LightJetsBdiscLowPt","LightJetsBdiscLowPt", 160, -20, 20.);
  JetsBdiscLowPt_ = fs->make<TH1F>("JetsBdiscLowPt","JetsBdiscLowPt", 160, -20, 20.);

  BjetsBdiscHighPt_ = fs->make<TH1F>("BjetsBdiscHighPt","BjetsBdiscHighPt", 160, -20, 20.);
  LightJetsBdiscHighPt_ = fs->make<TH1F>("LightJetsBdiscHighPt","LightJetsBdiscHighPt", 160, -20, 20.);
  JetsBdiscHighPt_ = fs->make<TH1F>("JetsBdiscHighPt","JetsBdiscHighPt", 160, -20, 20.);

  NrHighPtBtags_ = fs->make<TH1F>("NrHighPtBtags","NrHighPtBtags", 12, 0.5, 12.5);
  NrLowPtBtags_ = fs->make<TH1F>("NrLowPtBtags","NrLowPtBtags", 12, 0.5, 12.5);

  NrHighPtJets_ = fs->make<TH1F>("NrHighPtJets","NrHighPtJets", 12, 0.5, 12.5);
  NrLowPtJets_ = fs->make<TH1F>("NrLowPtJets","NrLowPtJets", 12, 0.5, 12.5);
}

BtagAnalyzer::~BtagAnalyzer()
{
}


void BtagAnalyzer::beginJob()
{  
} 

void
BtagAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //-------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);

  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);

  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);

  edm::Handle<std::vector<pat::Jet> > matchedLightJets;
  evt.getByLabel(matchedLightJets_, matchedLightJets);

  edm::Handle<std::vector<pat::Jet> > matchedBjets;
  evt.getByLabel(matchedBjets_, matchedBjets);

  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);

  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);


  //-------------------------------------------------
  // Weighting
  //-------------------------------------------------

  double weight=1;
  double weightPU=1;
  double weightRA2=1;

  if(useEvtWgt_)
    {
      //std::cout << "use event weight" << std::endl;
      edm::Handle<double> weightHandle;
      evt.getByLabel(weight_, weightHandle);
      weightPU=*weightHandle;

      edm::Handle<edm::View<PileupSummaryInfo> > PUInfo;
      evt.getByLabel(PUSource_, PUInfo);

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      
      for(iterPU = PUInfo->begin(); iterPU != PUInfo->end(); ++iterPU)  // vector size is 3
	{ 
	  if (iterPU->getBunchCrossing()==0) // -1: previous BX, 0: current BX,  1: next BX
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	}

      edm::Handle<double> RA2weightHandle;
      evt.getByLabel(RA2weight_, RA2weightHandle);
      weightRA2=*RA2weightHandle;

      weight=weightPU*weightRA2;

      //std::cout << "-------------------------------------" << std::endl;
      //std::cout << "weightPU: " << weightPU << std::endl;
      //std::cout << "weightRA2: " << weightRA2 << std::endl;
      //std::cout << "weight: " << weight << std::endl;
      //std::cout << "-------------------------------------" << std::endl;
    }

  // matched bjets
  for(int i=0; i < (int)matchedBjets->size(); ++i)
    {
      BjetsPt_->Fill((*matchedBjets)[i].pt(),weight);
      BjetsBdisc_->Fill((*matchedBjets)[i].bDiscriminator("trackCountingHighEffBJetTags"),weight);

      if((*matchedBjets)[i].pt()>240)
	{
	  BjetsBdiscHighPt_->Fill((*matchedBjets)[i].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	}
      else
	{
	  BjetsBdiscLowPt_->Fill((*matchedBjets)[i].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	}
    }

  // matched light jets
  for(int j=0; j < (int)matchedLightJets->size(); ++j)
    {
      LightJetsPt_->Fill((*matchedLightJets)[j].pt(),weight);
      LightJetsBdisc_->Fill((*matchedLightJets)[j].bDiscriminator("trackCountingHighEffBJetTags"),weight);

      if((*matchedLightJets)[j].pt()>240)
	{
	  LightJetsBdiscHighPt_->Fill((*matchedLightJets)[j].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	}
      else
	{
	  LightJetsBdiscLowPt_->Fill((*matchedLightJets)[j].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	}
    }

  int HighPtBtags=0;
  int LowPtBtags=0;

  // btags
  for(int k=0; k < (int)bjets->size(); ++k)
    {
      BtagsPt_->Fill((*bjets)[k].pt(),weight);
      
      if((*bjets)[k].pt()>240) HighPtBtags=HighPtBtags+1;
      else LowPtBtags=LowPtBtags+1;
    }

  NrHighPtBtags_->Fill(HighPtBtags,weight);
  NrLowPtBtags_->Fill(LowPtBtags,weight);

  int HighPtJets=0;
  int LowPtJets=0;

  // jets
  for(int l=0; l < (int)jets->size(); ++l)
    {
      JetsPt_->Fill((*jets)[l].pt(),weight);
      JetsBdisc_->Fill((*jets)[l].bDiscriminator("trackCountingHighEffBJetTags"),weight);

      if((*jets)[l].pt()>240)
	{
	  JetsBdiscHighPt_->Fill((*jets)[l].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	  HighPtJets=HighPtJets+1;
	}
      else
	{
	  JetsBdiscLowPt_->Fill((*jets)[l].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	  LowPtJets=LowPtJets+1;
	}
    }

  NrHighPtJets_->Fill(HighPtJets,weight);
  NrLowPtJets_->Fill(LowPtJets,weight);

}

void BtagAnalyzer::endJob()
{
}
