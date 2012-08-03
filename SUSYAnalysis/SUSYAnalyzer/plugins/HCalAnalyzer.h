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
  edm::InputTag jets_;
  edm::InputTag caloJets_;
  edm::InputTag lightJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;

  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;
  edm::InputTag BtagEventWeights_;
  edm::InputTag BtagJetWeights_;
  int btagBin_;
  int inclusiveBtagBin_; 

  bool useEventWgt_;
  bool useBtagEventWgt_;
  bool useInclusiveBtagEventWgt_;

  edm::InputTag TriggerWeight_;
  bool useTriggerEvtWgt_;

  double HT0_, HT1_, HT2_;
  double Y0_,  Y1_,  Y2_;

  // Dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // Event weighting
  TH1F* btagWeights_noWgt_;
  TH1F* btagWeights_PUWgt_;
  TH1F* nPU_noWgt_;
  TH1F* nPU_;
  TH1F* nPV_noWgt_;       
  TH1F* nPV_;
  
  // Basic kinematics
 
  TH2F* PFJetEt_Eta_;
  TH2F* CaloJetEt_Eta_;
  TH2F* GenJetEt_Eta_;
  TH2F* HOEnergy_Eta_;
  TH2F* PFMET_Eta_;
  TH2F* PFMET_Phi_;
  TH2F* CaloMET_Eta_;
  TH2F* CaloMET_Phi_;

  TH2F* EleIso_NPV_;
  TH1F* EleHOverEM_;
  TH2F* EleHOverEM_NPV_;

  TH2F* MuIso_NPV_;
  TH1F* MuHCal_;
  TH2F* MuHCal_NPV_;
  TH1F* MuHO_;
  TH2F* MuHO_NPV_;

  TH1F* PFJetEt_;
  TH1F* CaloJetEt_;
  TH1F* GenJetEt_;
  TH1F* HOEnergy_;
  TH1F* PFMET_;
  TH1F* CaloMET_;

  TH1F* MuPt_;
  TH1F* ElePt_;
  TH1F* YMET_;
  TH1F* HT_;
  TH1F* MHT_;
  TH1F* MuIso_;
  TH1F* EleIso_;

  TH1F* chargeEMFractionPF_;
  TH1F* neutralEMFractionPF_;
  TH1F* EMFractionCalo_;
  //TH1F* neutralEMFractionCalo_;

  TH1F* PFJetRelErr_;
  //TH1F* CaloJetRelErr_;

  TH1F* PFMETRelErr_;
  //TH1F* CaloMETRelErr_;

  TH1F* PFCSV_;
  TH1F* CaloCSV_;

};  

#endif  
