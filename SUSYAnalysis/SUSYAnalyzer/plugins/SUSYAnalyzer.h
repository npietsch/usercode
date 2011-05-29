#ifndef SUSYAnalyzer_h  
#define SUSYAnalyzer_h

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

class SUSYAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit SUSYAnalyzer(const edm::ParameterSet&);
  ~SUSYAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  //edm::InputTag inputGenEvent_;
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag pvSrc_;

  // TH1F histograms
  TH1F *MET_;
  TH1F *MET_SSDiLepReco_;
  TH1F *MET_OSDiLepReco_;
  TH1F *HT_;
  TH1F *SigMET_;
  TH1F *nJets_;
  TH1F *nMuons_;
  TH1F *nElectrons_;
  TH1F *nLeptons_;
  TH1F *MT_;
  TH1F *invMuMuMass_;
  TH1F *RelIsoMu1_;
  TH1F *RelIsoMu2_;

  TH1F *MET1pv_;
  TH1F *HT1pv_;
  TH1F *nJets1pv_;
  TH1F *Jet0_Et1pv_;
  TH1F *Jet1_Et1pv_;

  TH1F *MET2pv_;
  TH1F *HT2pv_;
  TH1F *nJets2pv_;
  TH1F *Jet0_Et2pv_;
  TH1F *Jet1_Et2pv_;

  TH1F *MET3pv_;
  TH1F *HT3pv_;
  TH1F *nJets3pv_;
  TH1F *Jet0_Et3pv_;
  TH1F *Jet1_Et3pv_;

  TH1F *MET4pv_;
  TH1F *HT4pv_;
  TH1F *nJets4pv_;
  TH1F *Jet0_Et4pv_;
  TH1F *Jet1_Et4pv_;

  TH1F *MET5pv_;
  TH1F *HT5pv_;
  TH1F *nJets5pv_;
  TH1F *Jet0_Et5pv_;
  TH1F *Jet1_Et5pv_;

  TH1F * Electron0_eta_;
  TH1F * Muon0_eta_;

  TH1F *nPV_;

  TH2F *HTidxMETidx_;
  TH2F *HT_SigMET_;
  TH2F *HT_MET_;

  std::vector<TH1F*> Jet_Et_;
  std::vector<TH1F*> Muon_pt_;
  std::vector<TH1F*> Elec_pt_;
};  

#endif  
