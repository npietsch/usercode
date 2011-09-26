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
  edm::InputTag matchedBjets_;
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

  TH1F* BjetsPt_;
  TH1F* LightJetsPt_;
  TH1F* BtagsPt_;
  TH1F* JetsPt_;

  TH1F* BjetsBdisc_;
  TH1F* LightJetsBdisc_;
  TH1F* JetsBdisc_;

  TH1F* BjetsBdiscLowPt_;
  TH1F* LightJetsBdiscLowPt_;
  TH1F* JetsBdiscLowPt_;

  TH1F* BjetsBdiscHighPt_;
  TH1F* LightJetsBdiscHighPt_;
  TH1F* JetsBdiscHighPt_;

  TH1F* NrHighPtBtags_;
  TH1F* NrLowPtBtags_;

  TH1F* NrHighPtJets_;
  TH1F* NrLowPtJets_;

};  

#endif  
