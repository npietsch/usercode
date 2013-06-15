#ifndef HerwigGenEventAnalyzer_h  
#define HerwigGenEventAnalyzer_h

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
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

class HerwigGenEventAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit HerwigGenEventAnalyzer(const edm::ParameterSet&);
  ~HerwigGenEventAnalyzer();

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
  edm::InputTag genParticles_;

  edm::InputTag HerwigGenEvent_;

  //----------------------------
  // Histograms
  //----------------------------

  // Dummy histograms
  TH1F* Dummy_;
  TH2F* Dummy2_;

  // Event weighting and Pile-up
  TH1F* nPV_;    
  TH1F* nPU_;

  TH1F* weights_;

  // GenEvent variables
  TH1F* qqbarBino_;
  TH1F* qqbarWino_;

  TH1F* qqbarBinoTest_;
  TH1F* qqbarWinoTest_;

  TH1F* dijetBino1_;
  TH1F* dijetWino1_;

  TH1F* dijetBino2_;
  TH1F* dijetWino2_;

  TH1F* dijetBino3_;
  TH1F* dijetWino3_;

  TH1F* dijetMass_;

  // mjj variables
  TH1F* minj3_;
  TH1F* min123_;
  TH1F* min234_;

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
  TH1F* mT_;
  TH1F* YMET_;
  TH1F* METSig_;
  TH1F* nJets_;
  TH1F* DeltaPtSum_;
  TH2F* DeltaPtSum_MHT_;
  TH2F* HT_MHT_; 

  TH1F* nJets70_;
  TH1F* nJets80_;
  TH1F* nJets100_;
  TH1F* nJets120_;
  TH1F* nJets150_;
  TH1F* nJets200_;

  TH1F* TCHE_;
  TH1F* TCHP_;
  TH1F* SSVHE_;
  TH1F* SSVHP_;
  
  TH1F* nBjets_noWgt_;
  TH1F* nBjets_noWgt_2_;
  TH1F* nBjets_;
  TH1F* nBjets_2_;

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

  // Correlations
  TH2F* MHT_nJets_;
};  

#endif  

