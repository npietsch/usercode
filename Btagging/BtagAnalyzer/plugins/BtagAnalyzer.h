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

  // dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // Jets
  TH1F* JetsPt_;
  TH1F* JetsEta_;
  TH1F* JetsBdisc_;
  TH1F* NrJets_;

  TH1F* HighPtJetsEta_;
  TH1F* HighPtJetsBdisc_;
  TH1F* NrHighPtJets_;
  
  TH1F* LowPtJetsEta_;
  TH1F* LowPtJetsBdisc_;
  TH1F* NrLowPtJets_;
  
  TH1F* dPhiJetMET_;

  // Bjets
  TH1F* BjetsPt_;
  TH1F* BjetsEta_;
  TH1F* BjetsBdisc_;
  TH1F* NrBjets_;

  TH1F* HighPtBjetsEta_;
  TH1F* HighPtBjetsBdisc_;
  TH1F* NrHighPtBjets_;
  
  TH1F* LowPtBjetsEta_;
  TH1F* LowPtBjetsBdisc_;
  TH1F* NrLowPtBjets_;
  
  TH1F* dPhiBjetMET_;

  // Btags
  TH1F* BtagsPt_;
  TH1F* BtagsEta_;
  TH1F* NrBtags_;

  TH1F* HighPtBtagsEta_;
  TH1F* NrHighPtBtags_;
  
  TH1F* LowPtBtagsEta_;
  TH1F* NrLowPtBtags_;
  
  TH1F* dPhiBtagMET_;

  // Btags for >= 1 btag
  TH1F* BtagsPt_1b_;
  TH1F* BtagsEta_1b_;
  
  TH1F* HighPtBtagsEta_1b_;
    
  TH1F* LowPtBtagsEta_1b_;
 
  TH1F* dPhiBtagMET_1b_;

  // Btags for >= 2 btags
  TH1F* BtagsPt_2b_;
  TH1F* BtagsEta_2b_;
    
  TH1F* HighPtBtagsEta_2b_;
    
  TH1F* LowPtBtagsEta_2b_;
    
  TH1F* dPhiBtagMET_2b_;

  // Btags for >= 3 btags
  TH1F* BtagsPt_3b_;
  TH1F* BtagsEta_3b_;
    
  TH1F* HighPtBtagsEta_3b_;
    
  TH1F* LowPtBtagsEta_3b_;
    
  TH1F* dPhiBtagMET_3b_;

};  

#endif  
