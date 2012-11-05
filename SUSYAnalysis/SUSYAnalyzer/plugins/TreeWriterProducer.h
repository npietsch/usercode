#ifndef TreeWriterProducer_h  
#define TreeWriterProducer_h

#include "TTree.h"
#include <vector>
#include <Math/LorentzVector.h>
#include <math.h>

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#ifdef __MAKECINT__
#pragma link C++ class std::vector<std::vector<std::string> >+;
//#pragma link C++ class ROOT::Math::PtEtaPhiM4D<float>+;
#endif 

//typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > LorentzV;

using namespace std;

class TreeWriterProducer : public edm::EDProducer {
  
  public:
    
    explicit TreeWriterProducer(const edm::ParameterSet&);
    ~TreeWriterProducer();
    
  private:
    virtual void beginJob() ;
    //virtual void produce(const edm::Event&, const edm::EventSetup&);
    virtual void produce(edm::Event&, const edm::EventSetup&);
    virtual void endJob();
    
    template <typename T>
    void printVector(TString name, vector<T> v, Int_t length=30, ostream& os=cout);
    template <typename T>
    void printVectorSize(TString name, vector<T> v, Int_t length=30, ostream& os=cout); 
    
    // Input tags
    edm::InputTag muons_;
    edm::InputTag electrons_;
    edm::InputTag jets_;
    //     edm::InputTag triggered_;
    //edm::InputTag trigResultsTag; //make sure have correct process on MC
    
    //tree for saving the nTuple
    TTree* tree;
    
    //variables to save -> thats what the nTuple will consist of
    int event;
    std::vector<std::vector<std::string> > muFilterLabels;    
};


#endif  






