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
  edm::InputTag looseTrackHighPurBjets_;
  edm::InputTag mediumTrackHighPurBjets_;
  edm::InputTag tightTrackHighPurBjets_;
  edm::InputTag looseTrackHighEffBjets_;
  edm::InputTag mediumTrackHighEffBjets_;
  edm::InputTag tightTrackHighEffBjets_;
  edm::InputTag pvSrc_;
  edm::InputTag weight_;
  edm::InputTag RA2weight_;
  bool useEvtWgt_;

  // TH1F
  TH1F *nbjets_[4][5];
  TH1F *Bdisc_[4][6];
  TH1F *BtagEt_[4][6];

  TH1F *nLooseBjetsTrackHighPur_;
  TH1F *nMediumBjetsTrackHighPur_;
  TH1F *nTightBjetsTrackHighPur_;
  TH1F *nLooseBjetsTrackHighEff_;
  TH1F *nMediumBjetsTrackHighEff_;
  TH1F *nTightBjetsTrackHighEff_;

  TH1F *nLooseBjetsTrackHighPur1pv_;
  TH1F *nMediumBjetsTrackHighPur1pv_;
  TH1F *nTightBjetsTrackHighPur1pv_;
  TH1F *nLooseBjetsTrackHighEff1pv_;
  TH1F *nMediumBjetsTrackHighEff1pv_;
  TH1F *nTightBjetsTrackHighEff1pv_;

  TH1F *nLooseBjetsTrackHighPur2pv_;
  TH1F *nMediumBjetsTrackHighPur2pv_;
  TH1F *nTightBjetsTrackHighPur2pv_;
  TH1F *nLooseBjetsTrackHighEff2pv_;
  TH1F *nMediumBjetsTrackHighEff2pv_;
  TH1F *nTightBjetsTrackHighEff2pv_;

  TH1F *nLooseBjetsTrackHighPur3pv_;
  TH1F *nMediumBjetsTrackHighPur3pv_;
  TH1F *nTightBjetsTrackHighPur3pv_;
  TH1F *nLooseBjetsTrackHighEff3pv_;
  TH1F *nMediumBjetsTrackHighEff3pv_;
  TH1F *nTightBjetsTrackHighEff3pv_;

  TH1F *nLooseBjetsTrackHighPur4pv_;
  TH1F *nMediumBjetsTrackHighPur4pv_;
  TH1F *nTightBjetsTrackHighPur4pv_;
  TH1F *nLooseBjetsTrackHighEff4pv_;
  TH1F *nMediumBjetsTrackHighEff4pv_;
  TH1F *nTightBjetsTrackHighEff4pv_;

  TH1F *nLooseBjetsTrackHighPur5pv_;
  TH1F *nMediumBjetsTrackHighPur5pv_;
  TH1F *nTightBjetsTrackHighPur5pv_;
  TH1F *nLooseBjetsTrackHighEff5pv_;
  TH1F *nMediumBjetsTrackHighEff5pv_;
  TH1F *nTightBjetsTrackHighEff5pv_;

  TH1F *bdiscTrackHighEff_;
  TH1F *bdiscTrackHighPur_;
  TH1F *bdiscTrackHighEff1pv_;
  TH1F *bdiscTrackHighPur1pv_;
  TH1F *bdiscTrackHighEff2pv_;
  TH1F *bdiscTrackHighPur2pv_;
  TH1F *bdiscTrackHighEff3pv_;
  TH1F *bdiscTrackHighPur3pv_;
  TH1F *bdiscTrackHighEff4pv_;
  TH1F *bdiscTrackHighPur4pv_;
  TH1F *bdiscTrackHighEff5pv_;
  TH1F *bdiscTrackHighPur5pv_;

  std::vector<TH1F*> angleb1b2_;
  std::vector<TH1F*>  mbb_;
  std::vector<TH1F*> deltaPhi_;
  std::vector<TH1F*> Jet1_Et_2Bjets_;
  std::vector<TH1F*> Bjet1_Et_;
  std::vector<TH1F*> Bjet2_Et_;
  std::vector<TH1F*> HT_2Bjets_;
  std::vector<TH1F*> HT_2Bjets_1LightJet_;
};  

#endif  
