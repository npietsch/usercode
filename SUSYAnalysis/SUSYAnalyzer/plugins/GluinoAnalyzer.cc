#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/GluinoAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"

using namespace std;
 
GluinoAnalyzer::GluinoAnalyzer(const edm::ParameterSet& cfg):
  // collections of R44b objects
  jets_         (cfg.getParameter<edm::InputTag>("jets") ),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets" )),
  muons_        (cfg.getParameter<edm::InputTag>("muons" )),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons") ),
  met_          (cfg.getParameter<edm::InputTag>("met") ),
  inputGenEvent_(cfg.getParameter<edm::InputTag>("susyGenEvent") ),
  // for event weighting
  PVSrc_                (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_               (cfg.getParameter<edm::InputTag>("PUInfo") ),
  PUWeight_             (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_            (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  useEventWgt_          (cfg.getParameter<bool>("useEventWeight") )

{ 
  edm::Service<TFileService> fs;

  // Declare dummy histograms
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

  MET_   = fs->make<TH1F>("MET","MET", 40, 0.,  1000.);
  HT_    = fs->make<TH1F>("HT","HT",   40, 0.,  2000.);
  MHT_   = fs->make<TH1F>("MHT","MHT", 50, 0.,  1000.);
  nJets_ = fs->make<TH1F>("nJets","nJets", 14, 0.,  14.);

  // Declare mjj variables
  mjjLow_ = fs->make<TH1F>("mjjLow","mjjLow", 80, 0.,  800.);
  mjjHigh_ = fs->make<TH1F>("mjjHigh","mjjHigh", 80, 0.,  800.);
  mjjMin_  = fs->make<TH1F>("mjjMin","mjjMin", 80, 0.,  800.);
  mjjMax_  = fs->make<TH1F>("mjjMax","mjjMax", 80, 0.,  800.);
  mjjLow2_ = fs->make<TH1F>("mjjLow2","mjjLow2", 80, 0.,  800.);
}

GluinoAnalyzer::~GluinoAnalyzer()
{
}

void
GluinoAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

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
      
      weight=weightRA2*weightPU;
      
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
  // Jet quantities
  //-------------------------------------------------

  //if(susyGenEvent->decayCascadeA()=="gluino->neutralino1" && susyGenEvent->decayCascadeB()=="gluino->neutralino1")

  if(jets->size()>3)
    {
      // define four vectors
      reco::Particle::LorentzVector Jet1=(*jets)[0].p4();
      reco::Particle::LorentzVector Jet2=(*jets)[1].p4();
      reco::Particle::LorentzVector Jet3=(*jets)[2].p4();
      reco::Particle::LorentzVector Jet4=(*jets)[3].p4();
      
      reco::Particle::LorentzVector JetI1=(*jets)[jets->size()-1].p4();
      reco::Particle::LorentzVector JetI2=(*jets)[jets->size()-2].p4();
      
      // define invariant dijet masses
      double m1I1=sqrt((Jet1+JetI1).Dot(Jet1+JetI1));   
      double m1I2=sqrt((Jet1+JetI2).Dot(Jet1+JetI2));

      double m2I1=sqrt((Jet2+JetI1).Dot(Jet2+JetI1));

      double m14=sqrt((Jet1+Jet4).Dot(Jet1+Jet4));   
      double m24=sqrt((Jet2+Jet4).Dot(Jet2+Jet4));

      // softest jet fixed
      double minLow=min(m1I1,m2I1);

      // leading jet fixed
      double minHigh=min(m1I1,m1I2);
	 
      // min and max of above
      double minI=min(minLow,minHigh);
      double maxI=max(minLow,minHigh);
      
      double minLow2=min(m14,m24);

      // fill hisotgrams
      mjjLow_->Fill(minLow);
      mjjHigh_->Fill(minHigh);
      mjjMin_->Fill(minI);
      mjjMax_->Fill(maxI);
      mjjLow2_->Fill(minLow2);
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

}


void GluinoAnalyzer::beginJob()
{  
} 

void GluinoAnalyzer::endJob()
{
}
