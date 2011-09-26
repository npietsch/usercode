#ifndef BtagAnalyzer_h  
#define BtagAnalyzer_h

#include "TH1.h"
#include "TH2.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/angle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class BtagAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit BtagAnalyzer(const edm::ParameterSet&);
  ~BtagAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag bjets_;
  edm::InputTag matchedLightJets_;
  edm::InputTag matchedBJets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag pvSrc_;
  edm::InputTag weight_;
  edm::InputTag PUSource_;
  edm::InputTag RA2weight_;
  bool useEvtWgt_;

  // dummy histogram
  TH1F* Dummy_;
  TH2F* Dummy2_;

};  

#endif  
