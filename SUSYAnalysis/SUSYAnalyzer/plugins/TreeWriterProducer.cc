#include "FWCore/Framework/interface/MakerMacros.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TreeWriterProducer.h"
// #include "DataFormats/Common/interface/TriggerResults.h"
// #include "FWCore/Common/interface/TriggerNames.h"
// #include "DataFormats/Luminosity/interface/LumiSummary.h"
// #include "FWCore/Framework/interface/LuminosityBlock.h"

// #include "TString.h"
// #include <fstream>
// #include <iostream>
// #include <iomanip>
// #include <sstream>

using namespace std;





//============================================================ Constructor
TreeWriterProducer::TreeWriterProducer(const edm::ParameterSet& cfg):
muons_        (cfg.getParameter<edm::InputTag>("muons")),
electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
jets_         (cfg.getParameter<edm::InputTag>("jets"))
{
  edm::Service<TFileService> fs;
  //Set branches to save into the tree
  tree=fs->make<TTree>("tree", "tree");
//   tree->Branch("event", &event, "event/I");
//   tree->Branch("muFilterLabels", &muFilterLabels);

//     produces<std::vector<std::vector<std::string> > >("muFilterLabels");
//   produces<std::int>( Prefix + "event"  + Suffix );
//   produces<int>("event");
  produces<int>("Mytest");
  produces <std::vector<float> > ( "MyTestVector");
//   produces<std::vector<std::vector<std::string> > >("MyTestVectorVector");
  
}

//============================================================ Destructor
TreeWriterProducer::~TreeWriterProducer()
{
}

//============================================================ Loop
void TreeWriterProducer::produce(edm::Event& evt, const edm::EventSetup& setup){   
  std::auto_ptr<int>                               mytest ( new int(0) );
  *mytest.get() = 1;
  evt.put(mytest,"Mytest");

  std::auto_ptr<std::vector<float> > myTestVector   ( new std::vector<float>() );
  myTestVector->push_back(1.2);
  evt.put( myTestVector  , "MyTestVector"      );
  
//   std::auto_ptr<std::vector<std::vector<string> > > myTestVectorVector   ( new std::vector<std::vector<string> >() );
//   vector<string> v;
//   myTestVectorVector->push_back(v);
//   evt.put( myTestVectorVector  , "MyTestVectorVector"      );
  
  
  
  
  
  //--------------------- initialize some variables
  muFilterLabels.clear();
  event       = evt.id().event();

  //--------------------- Handles
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  
  cout<<endl;
  cout<<"//////////////////////////////////////////////////////////////////////////////"<<endl;
  cout<<"No. of Jets | Muons | electrons: " << jets->size() << " | " << muons->size() << " | " << electrons->size() << endl;
  cout<<"//////////////////////////////////////////////////////////////////////////////"<<endl;
  cout<<endl;
  //--------------------- Fill branches
  //--------------------- Eletrons
  if(electrons->size()) cout<<"==================================================================== electrons: " << electrons->size() << endl;
  for(int i=0,N=(int)electrons->size(); i<N; ++i){
    cout<<"------------------------------ electron no: " << i << endl;
    cout<<"electrons->at("<<i<<").charge()                      = " << electrons->at(i).charge() << endl;
    cout<<"electrons->at("<<i<<").p4()                          = " << electrons->at(i).p4();
    if(electrons->at(i).triggerObjectMatches().size() ==1) cout << " <--> " << electrons->at(i).triggerObjectMatches().begin()->p4();
    cout<<endl;    
    cout<<"electrons->at("<<i<<").triggerObjectMatches().size() = " << electrons->at(i).triggerObjectMatches().size() << endl;
    if(electrons->at(i).triggerObjectMatches().size() ==1){
      cout<<"electrons->at("<<i<<").triggerObjectMatches().begin():" << endl;
      cout<<setw(35)<<"p4() |"
      <<setw(35)<<"collection() |"
      <<setw(20)<<"conditionNames |"
      <<setw(15)<<"filterLabels |"
      <<setw(15)<<"pathNames"
      <<endl;
      cout<< electrons->at(i).triggerObjectMatches().begin()->p4()<<setw(35)
      <<setw(35)<< electrons->at(i).triggerObjectMatches().begin()->collection()
      <<setw(20)<< electrons->at(i).triggerObjectMatches().begin()->conditionNames().size()
      <<setw(15)<<electrons->at(i).triggerObjectMatches().begin()->filterLabels().size()
      <<setw(15)<<electrons->at(i).triggerObjectMatches().begin()->pathNames().size()
      <<endl
      <<endl;
//       cout<<"electrons->at("<<i<<").triggerObjectMatches().begin()->p4()                        = " << electrons->at(i).triggerObjectMatches().begin()->p4() << endl;
//       cout<<"electrons->at("<<i<<").triggerObjectMatches().begin()->collection()                = " << electrons->at(i).triggerObjectMatches().begin()->collection() << endl;      
//       cout<<"electrons->at("<<i<<").triggerObjectMatches().begin()->conditionNames().size()     = " << electrons->at(i).triggerObjectMatches().begin()->conditionNames().size() << endl;
//       cout<<"electrons->at("<<i<<").triggerObjectMatches().begin()->filterLabels().size()       = " << electrons->at(i).triggerObjectMatches().begin()->filterLabels().size() << endl;
//       cout<<"electrons->at("<<i<<").triggerObjectMatches().begin()->pathNames().size()          = " << electrons->at(i).triggerObjectMatches().begin()->pathNames().size() << endl;
//       cout<<"electrons->at("<<i<<").triggerObjectMatches().begin()->triggerObjectTypes().size() = " << electrons->at(i).triggerObjectMatches().begin()->triggerObjectTypes().size() << endl;
      printVector<string>("conditionNames", electrons->at(i).triggerObjectMatches().begin()->conditionNames());
      printVector<string>("filterLabels", electrons->at(i).triggerObjectMatches().begin()->filterLabels());
      printVector<string>("pathNames", electrons->at(i).triggerObjectMatches().begin()->pathNames());
      printVector<int>("triggerObjectTypes", electrons->at(i).triggerObjectMatches().begin()->triggerObjectTypes());
    }
  }
  
  //--------------------- Jets
//   for(int i=0,N=(int)jets->size(); i<N; ++i){
//     goodJets.push_back((*jets)[i].p4());
//   }
  //--------------------- Muons
  
  if(muons->size()) cout<<"==================================================================== muons: " << muons->size() << endl;
  for(int i=0,N=(int)muons->size(); i<N; ++i){
    std::vector<std::string> muFilterLabelsTemp;
    cout<<"------------------------------ muon no: " << i << endl;
    cout<<"muons->at("<<i<<").charge()                      = " << muons->at(i).charge() << endl;
    cout<<"muons->at("<<i<<").p4()                          = " << muons->at(i).p4();
    if(muons->at(i).triggerObjectMatches().size() ==1) cout << " <--> " <<muons->at(i).triggerObjectMatches().begin()->p4();
    cout<<endl;
    cout<<"muons->at("<<i<<").triggerObjectMatches().size() = " << muons->at(i).triggerObjectMatches().size() << endl;
    if(muons->at(i).triggerObjectMatches().size() ==1){
      cout<<"muons->at("<<i<<").triggerObjectMatches().begin():" << endl;
      cout<<setw(35)<<"p4() |"
      <<setw(35)<<"collection() |"
      <<setw(20)<<"conditionNames |"
      <<setw(15)<<"filterLabels |"
      <<setw(15)<<"pathNames"
      <<endl;
      cout<< muons->at(i).triggerObjectMatches().begin()->p4()<<setw(35)
      <<setw(35)<< muons->at(i).triggerObjectMatches().begin()->collection()
      <<setw(20)<< muons->at(i).triggerObjectMatches().begin()->conditionNames().size()
      <<setw(15)<<muons->at(i).triggerObjectMatches().begin()->filterLabels().size()
      <<setw(15)<<muons->at(i).triggerObjectMatches().begin()->pathNames().size()
      <<endl
      <<endl;
//       cout<<"muons->at("<<i<<").triggerObjectMatches().begin()->p4()                        = " << muons->at(i).triggerObjectMatches().begin()->p4() << endl;
//       cout<<"muons->at("<<i<<").triggerObjectMatches().begin()->collection()                = " << muons->at(i).triggerObjectMatches().begin()->collection() << endl;      
//       cout<<"muons->at("<<i<<").triggerObjectMatches().begin()->conditionNames().size()     = " << muons->at(i).triggerObjectMatches().begin()->conditionNames().size() << endl;
//       cout<<"muons->at("<<i<<").triggerObjectMatches().begin()->filterLabels().size()       = " << muons->at(i).triggerObjectMatches().begin()->filterLabels().size() << endl;
//       cout<<"muons->at("<<i<<").triggerObjectMatches().begin()->pathNames().size()          = " << muons->at(i).triggerObjectMatches().begin()->pathNames().size() << endl;
      printVector<string>("conditionNames", muons->at(i).triggerObjectMatches().begin()->conditionNames());
      printVector<string>("filterLabels", muons->at(i).triggerObjectMatches().begin()->filterLabels());
//       if(!muons->at(i).triggerObjectMatchesByFilter("hltL1sMu16Eta2p1").empty()) cout<<"yeahhh!!!" << endl;
      printVector<string>("pathNames", muons->at(i).triggerObjectMatches().begin()->pathNames());
      printVector<int>("triggerObjectTypes", muons->at(i).triggerObjectMatches().begin()->triggerObjectTypes());      
      muFilterLabelsTemp = muons->at(i).triggerObjectMatches().begin()->filterLabels();
    }
    cout<<endl;
    muFilterLabels.push_back(muFilterLabelsTemp);
  }
//   if(!negElec->triggerObjectMatchesByFilter("hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoFilter").empty())
//    {negElecMatchedTightEle8Leg = true;}

  //--------------------- Fill Tree
  tree->Fill();
//   evt.put(muFilterLabels,"muFilterLabels");
//   std::auto_ptr<int>                               handleValid ( new bool(false) );
  

    
//   evt.put(event,"event");
//   evt.put(muFilterLabels,"muFilterLabels");
  
  
}


//================================================================================= printVector
template <typename T>
void TreeWriterProducer::printVector(TString name, vector<T> v, Int_t length, ostream& os){
  printVectorSize(name,v);
  if(v.size()>0){
    for(Int_t i=0,N=v.size(); i<N; ++i){
      TString temp_name = name;
      temp_name += "[";
      temp_name += i;
      temp_name += "] = ";
      os << setw(length) << temp_name << v[i] << endl;
    }
    os<<endl;
  }
}


//================================================================================= printVectorSize
template <typename T>
void TreeWriterProducer::printVectorSize(TString name, vector<T> v, Int_t length, ostream& os){
  name += ".size() = ";
  os << setw(length) << name << v.size();
  os << endl;
}



//============================================================ beginJob
void TreeWriterProducer::beginJob(){
}


//============================================================ endJob
void TreeWriterProducer::endJob(){
  //tree->Write();
}


DEFINE_FWK_MODULE(TreeWriterProducer);

