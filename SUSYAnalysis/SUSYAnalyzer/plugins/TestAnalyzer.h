#ifndef TestAnalyzer_h  
#define TestAnalyzer_h

#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include <vector>
#include <Math/LorentzVector.h>
#include <math.h>

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

//#ifdef __MAKECINT__
//#pragma link C++ class ROOT::Math::PtEtaPhiM4D<float>+;
//#endif

//typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> > LorentzV;


using namespace std;

class TestAnalyzer : public edm::EDAnalyzer {
  
  public:
    
    explicit TestAnalyzer(const edm::ParameterSet&);
    ~TestAnalyzer();
    
  private:
    
    virtual void beginJob() ;
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob();
    virtual void init();
    
    // Input tags
    edm::InputTag muons_;
    edm::InputTag electrons_;
    edm::InputTag jets_;
//     edm::InputTag triggered_;
    //edm::InputTag trigResultsTag; //make sure have correct process on MC
    
    
    
    TH1F* nElectrons_;
    TH1F* nJets_;
    TH1F* nMuons_;

    //tree for saving the nTuple
    TTree* tree;
    
    //variables to save -> thats what the nTuple will consist of
    vector<int> elCharge;
    int event;
    double eventWeight;
    vector<math::XYZTLorentzVector> goodElectrons;
    vector<math::XYZTLorentzVector> goodJets;
    vector<math::XYZTLorentzVector> goodMuons;
    int lumiSection;
    vector<int> muCharge;
    int nLeptons;
    int run;
    

};


#endif  


