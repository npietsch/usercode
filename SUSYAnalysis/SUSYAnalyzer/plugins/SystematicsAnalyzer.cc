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
  PVSrc_          (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_         (cfg.getParameter<edm::InputTag>("PUInfo") ),
  PUWeight_       (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_      (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEffWeights_ (cfg.getParameter<edm::InputTag>("BtagEffWeights") ),
  BtagEffGrid_    (cfg.getParameter<edm::InputTag>("BtagEffGrid") ),
  // bool
  useEvtWgt_    (cfg.getParameter<bool>("useEventWeight") )

{ 
  edm::Service<TFileService> fs;

  Dummy_=fs->make<TH1F>();
  Dummy_->SetDefaultSumw2(true);

  Dummy2_=fs->make<TH2F>();
  Dummy2_->SetDefaultSumw2(true);

  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0., 50);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  // Declare histograms for ABCD mehtod
  // ...

  // Declare histograms for control quantities
  // ...

}

SystematicsAnalyzer::~SystematicsAnalyzer()
{
}

void
SystematicsAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //--------------------------------------------------
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

  double weight=1;

  // declare and initialize different weights
  double weightPU=1;
  double weightRA2=1;
  double weightBtagEff=1;

  // if events should be weighted
  if(useEvtWgt_)
    {
      // PU weight
      edm::Handle<double> PUWeightHandle;
      evt.getByLabel(PUWeight_, PUWeightHandle);
      
      weightPU=*PUWeightHandle;

      // RA2 weight
      edm::Handle<double> RA2WeightHandle;
      evt.getByLabel(RA2Weight_, RA2WeightHandle);
      
      weightRA2=*RA2WeightHandle;

      // Btag weight
      // ...

      //std::cout << "--------------------------------" << std::endl;
      //std::cout << "weightPU: "      << weightPU      << std::endl;
      //std::cout << "weightRA2: "     << weightRA2     << std::endl;
      //std::cout << "weightBtagEff: " << weightBtagEff << std::endl;
      //std::cout << "------------------------ -------" << std::endl;
      
      // calculate overall weight
      weight=weightPU*weightRA2*weightBtagEff;
      
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

      nPU_->Fill(nvtx);

    }

  //-------------------------------------------------
  // ABCD quantities
  //-------------------------------------------------

  // To access memeber funtion XY of object with index INDEX of collection with Handle HANDLENAME:
  // (*HANDELNAME)[INDEX].XY()
  // e.g. (*jets)[0].eta(), (*met)[0].et()

  //-------------------------------------------------
  // control plots
  //-------------------------------------------------

  // number of primary vertices
  nPV_->Fill(PVSrc->size(), weight);
}


void SystematicsAnalyzer::beginJob()
{  
} 

void SystematicsAnalyzer::endJob()
{
}
