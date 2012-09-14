#ifndef TestAnalyzer_h  
#define TestAnalyzer_h

#include "TH1.h"
#include "TH2.h"

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

class TestAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit TestAnalyzer(const edm::ParameterSet&);
  ~TestAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();

  // Input tags
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag jets_;

  // Histograms
  TH1F* JetsEt_;
  TH1F* JetsEta_;
  TH1F* nJets_;

};  

#endif  


