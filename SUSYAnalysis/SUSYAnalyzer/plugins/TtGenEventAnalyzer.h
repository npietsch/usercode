#ifndef TtGenEventAnalyzer_h  
#define TtGenEventAnalyzer_h

#include "TH1.h"
#include "TH2.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

class TtGenEventAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit TtGenEventAnalyzer(const edm::ParameterSet&);
  ~TtGenEventAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  edm::InputTag inputGenEvent_;
  edm::InputTag genEvtInfoHandle_;

  //edm::InputTag recoJets_;

  TH1F* Dummy_;
  TH2F* Dummy2_;

  TH1F *nLep_;
  TH1F *topPt_;
  TH1F *topEta_;
  TH1F *topPhi_;
  TH1F *topBarPt_;
  TH1F *topBarEta_;
  TH1F *topBarPhi_;
  TH1F *ttbarPt_;
  TH1F *ttbarEta_;
  TH1F *ttbarPhi_;
  TH1F *ttbarMass_;
  TH1F *mT_;

  TH1F  *NuPt_;
  TH1F  *LepPt_;

  TH2F *ttbarMass_MET_;
  TH2F *ttbarMass_HT_;
  TH2F *qScale_MET_;
  TH2F *qScale_HT_;
  TH2F *PDFScale_MET_;
  TH2F *PDFScale_HT_;

  TH2F *HT_MET_;
  TH2F *HT_LepPt_;
  TH2F *HT_YMET_;
  TH2F *HT_LepPtSig_;
  TH2F *HT_mT_;

  TH2F *HT_MET_acceptance_;
  TH2F *HT_LepPt_acceptance_;
  TH2F *HT_YMET_acceptance_;
  TH2F *HT_LepPtSig_acceptance_;
  TH2F *HT_mT_acceptance_;
};  

#endif  
