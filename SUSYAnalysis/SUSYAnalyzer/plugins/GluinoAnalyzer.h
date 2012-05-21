#ifndef GluinoAnalyzer_h  
#define GluinoAnalyzer_h

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
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class GluinoAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit GluinoAnalyzer(const edm::ParameterSet&);
  ~GluinoAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
     
  //----------------------------
  // Input tags
  //----------------------------
         
  edm::InputTag jets_;
  edm::InputTag looseJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag vetoMuons_;
  edm::InputTag vetoElectrons_;
  edm::InputTag met_;
  edm::InputTag inputGenEvent_;
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;
  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;

  //----------------------------
  // Histograms
  //----------------------------

  // Dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // Event weighting and Pile-up
  TH1F* nPV_;    
  TH1F* nPU_;
  
  // mjj variables
  TH1F* mjjMCTruth_;
  TH1F* mjj_;

  TH1F* min123_;
  TH1F* min123_random_;
  TH1F* min123_right_;
  TH1F* min123_wrong_;
  TH1F* min123_noMatch_;

  TH1F* random_;
  TH1F* Jet2_Phi_;
  TH1F* Jet2_Eta_;
  TH1F* Jet2_Theta_;
  TH1F* Jet2_Phi_random_;
  TH1F* deltaPhi_;

  TH1F* min124_;
  TH1F* min124_random_;

  // Basic kinematics
  std::vector<TH1F*> Jet_Pt_;
  std::vector<TH1F*> Jet_Eta_;
  std::vector<TH1F*> DeltaPhi_MHT_Jet_;
  std::vector<TH1F*> DeltaPhi_MET_Jet_;
  std::vector<TH1F*> Delta_Pt_;
  std::vector<TH2F*> Delta_Pt_MHT_;
  std::vector<TH2F*> RecoJetPt_MHT_;
  std::vector<TH2F*> GenJetPt_MHT_;
  TH1F* Jets_Pt_;
  TH1F* GluonJets_Pt_;
  TH1F* Jets_Eta_;
  TH1F* Jets_Phi_;
  TH1F* Jets_Theta_;
  TH1F* MET_;
  TH1F* MHT_;
  TH1F* HT_;
  TH1F* YMET_; 
  TH1F* nJets_;
  TH1F* DeltaPtSum_;
  TH2F* DeltaPtSum_MHT_;
  TH2F* HT_MHT_; 

  std::vector<TH1F*> Muon_Pt_;
  std::vector<TH1F*> Muon_Eta_;

  std::vector<TH1F*> Electron_Pt_;
  std::vector<TH1F*> Electron_Eta_;

  TH1F* nMuons_;
  TH1F* nElectrons_;
  TH1F* nLeptons_;

  TH1F* nVetoMuons_;
  TH1F* nVetoElectrons_;
  TH1F* nVetoLeptons_;

  TH1F* MT_;

};  

#endif  

