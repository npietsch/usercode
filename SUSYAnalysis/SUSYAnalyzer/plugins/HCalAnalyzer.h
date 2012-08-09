#ifndef HCalAnalyzer_h  
#define HCalAnalyzer_h

#include "TH1.h"
#include "TH2.h"
#include "TRandom3.h"

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

class HCalAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit HCalAnalyzer(const edm::ParameterSet&);
  ~HCalAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  edm::InputTag met_;
  edm::InputTag caloMet_;
  edm::InputTag genMet_;
  edm::InputTag jets_;
  edm::InputTag genJets_;
  edm::InputTag caloJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;

  bool useJetID_;
  bool usePileUp_;

  // Dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // PU and PV
  TH1F* nPU_;
  TH1F* nPV_;
  
  // Basic kinematics
 
  //Jets 1D

  TH1F* nJets_;
  TH1F* nCaloJets_;
  TH1F* nGenJetsNoMatch_;
  TH1F* nGenJets_;
  TH1F* jetsEt_;
  TH1F* jetsEta_;
  TH1F* caloJetsEt_;
  TH1F* caloJetsEta_;
  TH1F* genJetsEt_;
  TH1F* genJetsEta_;
  TH1F* genJetsEtNoMatch_;
  TH1F* genJetsEtaNoMatch_;
  std::vector<TH1F*> jetEt_;
  std::vector<TH1F*> jetEta_;

  TH1F* HOEnergy_;
  TH1F* chargeEMFraction_;
  TH1F* neutralEMFraction_;
  TH1F* EMFractionCalo_;
  //TH1F* neutralEMFractionCalo_;

  TH1F* jetsRelErr_;
  TH1F* caloJetsRelErr_;

  //Jets 2D

  TH2F* jetsEt_Eta_;
  TH2F* caloJetsEt_Eta_;
  TH2F* genJetsEt_Eta_;
  TH2F* HOEnergy_Eta_;

  //bJets

  TH1F* nBjets_;
  TH1F* CSV_;
  TH1F* caloCSV_;
  TH1F* bJetsEt_;
  TH1F* bJetsEta_;
  std::vector<TH1F*> bJetEt_;
  std::vector<TH1F*> bJetEta_;

  TH1I* partonFlavour_;
  TH1F* correctlyBtaggedJetsEt_;
  TH1F* mistaggedBjetsEt_;
  TH1F* allPartonMatchedJetsEt_;
  TH1F* trueBjetsEt_;
  TH1F* trueLightJetsEt_;

  //Muon

  TH1F* muPt_;
  TH1F* muIso_;
  TH2F* muIso_NPV_;
  TH2F* muIso_NPU_;
  TH1F* muHCal_;
  TH2F* muHCal_NPV_;
  TH2F* muHCal_NPU_;
  TH1F* muHO_;
  TH2F* muHO_NPV_;
  TH2F* muHO_NPU_;

  //Electron

  TH1F* elePt_;
  TH1F* eleIso_;
  TH2F* eleIso_NPV_;
  TH2F* eleIso_NPU_;
  TH1F* eleHOverEM_;
  TH2F* eleHOverEM_NPV_;
  TH2F* eleHOverEM_NPU_;

  //Composite
  
  TH1F* HT_;
  TH1F* genHT_;
  TH1F* genHTNoMatch_;
  TH1F* HTRelErr_;
  TH1F* HTRelErrNoMatch_;
  TH1F* MHT_;
  TH1F* genMHT_;
  TH1F* genMHTNoMatch_;
  TH1F* MHTRelErr_;
  TH1F* MHTRelErrNoMatch_;
  TH1F* MET_;
  TH1F* YMET_;
  TH1F* caloMET_;
  TH2F* MET_Phi_;
  TH2F* caloMET_Phi_;
  TH1F* METRelErr_;
  TH1F* caloMETRelErr_;



};  

#endif  
