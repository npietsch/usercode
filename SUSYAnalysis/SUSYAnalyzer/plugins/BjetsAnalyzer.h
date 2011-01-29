#ifndef BjetsAnalyzer_h  
#define BjetsAnalyzer_h

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

class BjetsAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit BjetsAnalyzer(const edm::ParameterSet&);
  ~BjetsAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  //edm::InputTag inputGenEvent_;
  edm::InputTag src_;
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag bjets_;

  TH1F *nbjets_[4][5];
  TH1F *bdisc_[4][6];
  TH1F *EtBtag_[4][6];

  TH1F *nLooseBjetsTrackHighPur_;
  TH1F *nMediumBjetsTrackHighPur_;
  TH1F *nTightBjetsTrackHighPur_;

  TH1F *nLooseBjetsTrackHighEff_;
  TH1F *nMediumBjetsTrackHighEff_;
  TH1F *nTightBjetsTrackHighEff_;
};  

#endif  
