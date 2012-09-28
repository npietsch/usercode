#include "FWCore/Framework/interface/MakerMacros.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TestAnalyzer.h"


using namespace std;

//============================================================ Constructor
TestAnalyzer::TestAnalyzer(const edm::ParameterSet& cfg):
muons_        (cfg.getParameter<edm::InputTag>("muons")),
electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
jets_         (cfg.getParameter<edm::InputTag>("jets"))
{ 
  edm::Service<TFileService> fs;
  nElectrons_ = fs->make<TH1F>("nElectrons","nElectrons", 16, -0.5, 15.5);
  nJets_      = fs->make<TH1F>("nJets"     ,"nJets",      16, -0.5, 15.5);
  nMuons_     = fs->make<TH1F>("nMuons"    ,"nMuons",     16, -0.5, 15.5);

  myTree = 0;
  myTree = new TTree("myTree","myTree");

  //Set branches to save into the tree
  myTree->Branch("elCharge", &elCharge);
  myTree->Branch("eventWeight", &eventWeight, "eventWeight/D");
  myTree->Branch("goodElectrons", &goodElectrons);
  myTree->Branch("goodJets", &goodJets);
  myTree->Branch("goodMuons", &goodMuons);
  myTree->Branch("muCharge", &muCharge);
  myTree->Branch("nLeptons", &nLeptons, "nLeptons/I");
}

//============================================================ Destructor
TestAnalyzer::~TestAnalyzer()
{
}

//============================================================ Loop
void TestAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){
  //--------------------- initialize some variables
  elCharge     .clear();
  eventWeight  = 1.;
  goodElectrons.clear();
  goodJets     .clear();
  goodMuons    .clear();
  muCharge     .clear();
  nLeptons     = 0;

  //--------------------- Handles
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);

  //--------------------- A few control plots
  nElectrons_->Fill(electrons->size(),eventWeight);
  nJets_     ->Fill(jets->size(),eventWeight);
  nMuons_    ->Fill(muons->size(),eventWeight);

  //--------------------- Fill branches
  //Eletrons
  for(int i=0,N=(int)electrons->size(); i<N; ++i){
    goodElectrons.push_back((*electrons)[i].p4());
    elCharge.push_back((*electrons)[i].charge());
  }
  //Jets
  for(int i=0,N=(int)jets->size(); i<N; ++i){
    goodJets.push_back((*jets)[i].p4());
  }
  //Muons
  for(int i=0,N=(int)muons->size(); i<N; ++i){
    goodMuons.push_back((*muons)[i].p4());
    muCharge.push_back((*muons)[i].charge());
  }
  nLeptons = electrons->size() + muons->size();

  //--------------------- Fill Tree
  myTree->Fill();
}



//============================================================ beginJob
void TestAnalyzer::beginJob(){  
} 


//============================================================ endJob
void TestAnalyzer::endJob(){
  //myTree->Write();
}

//============================================================ init
void TestAnalyzer::init(){  
} 




DEFINE_FWK_MODULE(TestAnalyzer);

