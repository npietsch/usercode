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
  matchedBJets_     (cfg.getParameter<edm::InputTag>("matchedBJets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") ),
  weight_       (cfg.getParameter<edm::InputTag>("weight") ),
  PUSource_     (cfg.getParameter<edm::InputTag>("PUInfo") ),
  RA2weight_    (cfg.getParameter<edm::InputTag>("RA2weight") ),
  useEvtWgt_    (cfg.getParameter<bool>("useEventWeight") )

{ 
  edm::Service<TFileService> fs;

  Dummy_=fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_=fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);

  //MET_ = fs->make<TH1F>("MET","MET", 40, 0., 1000.);

}

BtagAnalyzer::~BtagAnalyzer()
{
}

void
BtagAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //--------------------------------------------------
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
  edm::Handle<std::vector<pat::Jet> > matchedBJets;
  evt.getByLabel(matchedBJets_, matchedBJets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);

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

}

void BtagAnalyzer::beginJob()
{  
} 

void BtagAnalyzer::endJob()
{
}
