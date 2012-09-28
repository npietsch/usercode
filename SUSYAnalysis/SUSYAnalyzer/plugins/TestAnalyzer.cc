#include "FWCore/Framework/interface/MakerMacros.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TestAnalyzer.h"


using namespace std;

TestAnalyzer::TestAnalyzer(const edm::ParameterSet& cfg):
muons_        (cfg.getParameter<edm::InputTag>("muons")),
electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
jets_         (cfg.getParameter<edm::InputTag>("jets"))
{ 
  edm::Service<TFileService> fs;
  JetsEt_     = fs->make<TH1F>("JetsEt" ,"JetsEt",  90, 0., 900.);
  JetsEta_    = fs->make<TH1F>("JetsEta","JetsEta",    60, -3, 3);
  nJets_      = fs->make<TH1F>("nJets"  ,"nJets",   16, -0.5, 15.5);
  nelectrons_ = fs->make<TH1F>("nElectrons"  ,"nElectrons",   16, -0.5, 15.5);
  nMuons_     = fs->make<TH1F>("nMuons"  ,"nMuons",   16, -0.5, 15.5);
  nLeptons_   = fs->make<TH1F>("nLeptons"  ,"nLeptons",   16, -0.5, 15.5);
  MuMuMass_   = fs->make<TH1F>("MuMuMass_" ,"MuMuMass_",  200, 0., 500.);

  myTree = 0;
  myTree = new TTree("myTree","myTree");

  //Set branches to save into the tree
  myTree->Branch("diMuMass", &diMuMass, "diMuMass/D");
  myTree->Branch("eventWeight", &eventWeight, "eventWeight/D");
  myTree->Branch("goodElectrons", &goodElectrons);
  myTree->Branch("goodJets", &goodJets);
  myTree->Branch("goodMuons", &goodMuons);
  myTree->Branch("nLeptons", &nLeptons, "nLeptons/I");

}

TestAnalyzer::~TestAnalyzer()
{
}

void TestAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){
  //initialize some variables
  diMuMass    = 0.;
  eventWeight = 1.;
  goodElectron.clear();
  goodMuon.clear();
  goodElectron.clear();
  nLeptons    = 0;

  //-------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  
  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------
  
  // Jets
  for(int idx=0; idx<(int)jets->size(); ++idx){
    JetsEt_->Fill((*jets)[idx].et(),eventWeight);
    JetsEta_->Fill((*jets)[idx].eta(),eventWeight);
  }
  nJets_->Fill(jets->size(),eventWeight);
  
  nelectrons_->Fill(electrons->size(),eventWeight);
  nMuons_->Fill(muons->size(),eventWeight);
  nLeptons_->Fill(muons->size() + electrons->size(),eventWeight);
  
  for(Int_t i=0,N=muons->size();i<N-1; ++i){
    for(Int_t j=i+1; j<N; ++j){
      //if(muons[i]->charge==muons[j]->charge()) continue;
      if((*muons)[i].charge()==(*muons)[j].charge()) continue;
      double mass = ((*muons)[i].p4() + (*muons)[j].p4()).mass();
      MuMuMass_->Fill(mass, eventWeight);
      diMuMass=mass;
      //cout<<"mass = " << mass << endl;
      

    }

    //LorentzV dummy((*muons)[i].p4());
    //math::XYZTLorentzVector dummy((*muons)[i].p4());
    //goodMuon.push_back(dummy);
    goodMuon.push_back((*muons)[i].p4());

  }
  nLeptons = muons->size() + electrons->size();
  








  myTree->Fill();
}




void TestAnalyzer::beginJob(){  
} 

void TestAnalyzer::endJob(){
  //myTree->Write();
}

void TestAnalyzer::init(){  




} 















DEFINE_FWK_MODULE(TestAnalyzer);

