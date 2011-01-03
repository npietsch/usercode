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


using namespace std;
 
SUSYAnalyzer::SUSYAnalyzer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("source")),
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons"))
{ 
  edm::Service<TFileService> fs;

  MET_ = fs->make<TH1F>("MET","MET", 50, 0., 1000.);
  HT_ = fs->make<TH1F>("HT","HT", 100, 0., 2000.);
  nJets_ = fs->make<TH1F>("njets","njets",15 , 0.5, 15.5);
}

SUSYAnalyzer::~SUSYAnalyzer()
{
}

void
SUSYAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{  
  //--------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<reco::GenParticleCollection> src;
  evt.getByLabel(src_, src);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  //-------------------------------------------------
  // MET, HT, njets
  //-------------------------------------------------

  //const std::vector<pat::MET>& Met=*met;
  //const std::vector<pat::Jet>& Jets=*jets;

  double HT=0;
  int njets=0;
  
  //std::cout << "Nr. of jets: " << jets->size() << std::endl;
  
  for(int i=0; i<(int)jets->size(); ++i)
    {
      HT=HT+(*jets)[i].et();
      njets=njets+1;
    }

  MET_->Fill((*met)[0].et());
  HT_->Fill(HT);
  nJets_->Fill(njets);
}


void SUSYAnalyzer::beginJob()
{  
} 

void SUSYAnalyzer::endJob()
{
}
