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
  edm::InputTag lightJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag pvSrc_;

  // TH2F histograms
  TH2F* JetEt_nrBjets_;

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

  TH2F *mW_SigMET_;
  TH2F *sigMET_nJets_;
  TH2F *HT_nJets_;

  std::vector<TH1F*> Jet_Et_;
  std::vector<TH1F*> Muon_pt_;
  std::vector<TH1F*> Elec_pt_;
  std::vector<TH1F*> Bjet_EtFrac_;
  std::vector<TH1F*> LightJet_EtFrac_;

  TH1F *Bjets_EtFrac_;
  TH1F *LightJets_EtFrac_;

  TH1F *mW_;

  TH1F *mW_MET0_;
  TH1F *mW_MET50_;
  TH1F *mW_MET100_;
  TH1F *mW_MET150_;
  TH1F *mW_MET200_;
  TH1F *mW_MET250_;
  TH1F *mW_MET300_;

  TH1F *mW_SigMET0_;
  TH1F *mW_SigMET2_;
  TH1F *mW_SigMET4_;
  TH1F *mW_SigMET6_;
  TH1F *mW_SigMET9_;
  TH1F *mW_SigMET12_;

  TH1F *mW_4Jets_;
  TH1F *mW_5Jets_;
  TH1F *mW_6Jets_;
  TH1F *mW_7Jets_;
  TH1F *mW_8Jets_;
  TH1F *mW_9Jets_;

  TH1F *mW_HT300_;
  TH1F *mW_HT400_;
  TH1F *mW_HT500_;
  TH1F *mW_HT600_;
  TH1F *mW_HT700_;
  TH1F *mW_HT800_;

  TH2F *mW_MET_;
  TH2F *mW_nJets_;
  TH2F *mW_HT_;
};  

#endif  
