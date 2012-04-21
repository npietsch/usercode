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
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag met_;
  edm::InputTag inputGenEvent_;
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;

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

  TH1F* min123_;
  TH1F* min123_right_;
  TH1F* min123_wrong_;
  TH1F* min123_noMatch_;

  TH1F* min124_;

  // Basic kinematics
  std::vector<TH1F*> Jet_Et_;
  std::vector<TH1F*> Jet_Eta_;

  TH1F* Jets_Et_;
  TH1F* GluonJets_Et_;
  TH1F* Jets_Eta_;
  TH1F* Jets_Phi_;
  TH1F* Jets_Theta_;
  TH1F* MET_;
  TH1F* HT_; 
  TH1F* nJets_;

  std::vector<TH1F*> Muon_Pt_;
  std::vector<TH1F*> Muon_Eta_;

  std::vector<TH1F*> Electron_Pt_;
  std::vector<TH1F*> Electron_Eta_;

  TH1F* nMuons_;
  TH1F* nElectrons_;
  TH1F* nLeptons_;

  TH1F* MT_;

};  

#endif  

