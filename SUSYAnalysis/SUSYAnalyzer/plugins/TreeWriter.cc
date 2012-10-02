#include "FWCore/Framework/interface/MakerMacros.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TreeWriter.h"
// #include "DataFormats/Common/interface/TriggerResults.h"
// #include "FWCore/Common/interface/TriggerNames.h"
// #include "DataFormats/Luminosity/interface/LumiSummary.h"
// #include "FWCore/Framework/interface/LuminosityBlock.h"


using namespace std;

//============================================================ Constructor
TreeWriter::TreeWriter(const edm::ParameterSet& cfg):
muons_        (cfg.getParameter<edm::InputTag>("muons")),
electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
// triggered_    (cfg.getParameter<edm::InputTag>("triggered_")),
//trigResultsTag(cfg.getParameter<edm::InputTag>("TriggerResults")),
jets_         (cfg.getParameter<edm::InputTag>("jets"))
{ 
  edm::Service<TFileService> fs;
  nElectrons_ = fs->make<TH1F>("nElectrons","nElectrons", 16, -0.5, 15.5);
  nJets_      = fs->make<TH1F>("nJets"     ,"nJets",      16, -0.5, 15.5);
  nMuons_     = fs->make<TH1F>("nMuons"    ,"nMuons",     16, -0.5, 15.5);

  //Set branches to save into the tree
  //tree = 0;
  //tree = new TTree("myTree","myTree");
  tree=fs->make<TTree>("tree", "tree");
  tree->Branch("elCharge", &elCharge);
  tree->Branch("event", &event, "event/I");
  tree->Branch("eventWeight", &eventWeight, "eventWeight/D");
  tree->Branch("goodElectrons", &goodElectrons);
  tree->Branch("goodJets", &goodJets);
  tree->Branch("goodMuons", &goodMuons);
  tree->Branch("lumiSection", &lumiSection, "lumiSection/I");
  tree->Branch("muCharge", &muCharge);
  tree->Branch("nLeptons", &nLeptons, "nLeptons/I");
  tree->Branch("run", &run, "run/I");
}

//============================================================ Destructor
TreeWriter::~TreeWriter()
{
}

//============================================================ Loop
void TreeWriter::analyze(const edm::Event& evt, const edm::EventSetup& setup){   
// edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
// edm::InputTag trigResultsTag("TriggerResults","","HLT"); //make sure have correct process on MC
// //data process=HLT, MC depends, Spring11 is REDIGI311X
// evt.getByLabel(trigResultsTag,trigResults);
// 
// const edm::TriggerNames& trigNames = evt.triggerNames(*trigResults);   
// std::string pathName="HLT_Jet370_v2";
// bool passTrig=trigResults->accept(trigNames.triggerIndex(pathName));  

//   //HLT
//   edm::Handle<edm::TriggerResults> HLTResults;
//   evt.getByLabel(hltResultsTag_,HLTResults);
//   if (HLTResults.isValid()) {
//     edm::TriggerNames triggerNames;
//     triggerNames.init(*HLTResults);
//     for (unsigned int iHLT = 0; iHLT < HLTResults->size(); iHLT++)
//       (event_->AddHLTrigger()).Init(HLTResults->accept(iHLT),triggerNames.triggerName(iHLT));
//   }
  
  
// cout<<"HLT_Jet370_v2 = " << passTrig << endl;
// cout<<"trigNames.size() = " << trigNames.size() << endl;
// cout<<"trigResults->accept(trigNames.size()) = " << trigResults->accept(trigNames.size()) << endl;
// cout<<"trigResults->accept(trigNames.triggerIndex(HLT_*)) = " << trigResults->accept(trigNames.triggerIndex("HLT_*")) << endl;




  //--------------------- initialize some variables
  elCharge     .clear();
  eventWeight  = 1.;
  goodElectrons.clear();
  goodJets     .clear();
  goodMuons    .clear();
  muCharge     .clear();
  nLeptons     = 0;

  event       = evt.id().event();
  lumiSection = evt.id().luminosityBlock();
  run         = evt.id().run();
  //cout<<"run | lumiSection | event : " << evt.id().run() << " | " << evt.id().luminosityBlock()  << " | " << evt.id().event() << endl;

  //using pat::Muon;
  //using pat::Electron;
  //using pat::Jet;

//   edm::Handle<std::map<std::string,bool> > triggered;
//   evt.getByLabel(triggered_, triggered);
    

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


  //cout<<"jets.size() = " << jets->size() << endl;


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
  tree->Fill();
}


//============================================================ beginJob
void TreeWriter::beginJob(){  
} 


//============================================================ endJob
void TreeWriter::endJob(){
  //tree->Write();
}

//============================================================ init
void TreeWriter::init(){  
} 




DEFINE_FWK_MODULE(TreeWriter);

