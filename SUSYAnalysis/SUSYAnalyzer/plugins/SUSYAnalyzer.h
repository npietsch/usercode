#ifndef SUSYAnalyzer_h  
#define SUSYAnalyzer_h

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

class SUSYAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit SUSYAnalyzer(const edm::ParameterSet&);
  ~SUSYAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag lightJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag PVSrc_;
  edm::InputTag PUInfo_;

  edm::InputTag PUWeight_;
  edm::InputTag RA2Weight_;
  edm::InputTag BtagEventWeights_;
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
  TH1F Dummy_ ;
  TH2F Dummy2_;

  // Event weighting
  TH1F btagWeights_noWgt_;
  TH1F btagWeights_PUWgt_;
  TH1F nPU_noWgt_;
  TH1F nPU_;
  TH1F nPV_noWgt_;       
  TH1F nPV_;
  
  // Btagging
  TH1F TCHE_;
  TH1F TCHP_;
  TH1F SSVHE_;
  TH1F SSVHP_;
  
  TH1F nBjets_noWgt_;
  TH1F nBjets_noWgt_2_;
  TH1F nBjets_;
  TH1F nBjets_2_;

  // Basic kinematics
  std::vector<TH1F*> Jet_Et_;
  TH1F MET_;
  TH1F HT_; 
  TH1F nJets_;

  // Ymet
  TH1F YMET_;

  TH1F HT_YMET_;
  TH1F HT_YMET_noWgt_;
  TH1F HT_MET_;

  // MET significance
  TH1F METSig_;

  TH2F HT_METSig_;
  TH2F HT_METSig_noWgt_;

  // Lepton variables
  std::vector<TH1F*> Muon_Pt_;
  std::vector<TH1F*> Muon_Eta_;
  std::vector<TH1F*> Electron_Pt_;
  std::vector<TH1F*> Electron_Eta_;

  TH1F nMuons_;
  TH1F nElectrons_;
  TH1F nLeptons_;

  // MT
  TH1F MT_;

  // Correlation between HT and YMET / MET significance
  TH2F HT_LepPtSig_ = fs->make<TH2F>("HT_LepPtSig","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  TH2F HT_LepPtSig_smeared_ = fs->make<TH2F>("HT_LepPtSig_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  TH2F LepPtSig_smearFactor_ = fs->make<TH1F>("LepPtSig_smearFactor","LepPtSig_smearFactor", 100, 0., 10. );
  TH2F HT_SigMET_unweighted_ = fs->make<TH2F>("HT_SigMET_unweighted","HT vs. SigMET unweighted", 80, 0., 2000., 80, 0., 20. );

  TH2F HT_SigMET_PT20_MET60       = fs->make<TH2F>("HT_SigMET_PT20_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  TH2F HT_SigMET_PT40_MET60       = fs->make<TH2F>("HT_SigMET_PT40_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
  TH2F HT_SigMET_PT60_MET60       = fs->make<TH2F>("HT_SigMET_PT60_MET60","HT vs. SigMET", 80, 0., 2000., 80, 0., 20.);
			     
  TH2F HT_LepPtSig_PT20_MET20       = fs->make<TH2F>("HT_LepPtSig_PT20_MET20","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  TH2F HT_LepPtSig_PT20_MET40       = fs->make<TH2F>("HT_LepPtSig_PT20_MET40","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  TH2F HT_LepPtSig_PT20_MET60       = fs->make<TH2F>("HT_LepPtSig_PT20_MET60","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
		
  TH2F HT_LepPtSig_PT20_MET20_smeared       = fs->make<TH2F>("HT_LepPtSig_PT20_MET20_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  TH2F HT_LepPtSig_PT20_MET40_smeared       = fs->make<TH2F>("HT_LepPtSig_PT20_MET40_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
  TH2F HT_LepPtSig_PT20_MET60_smeared       = fs->make<TH2F>("HT_LepPtSig_PT20_MET60_smeared","HT vs. LepPtSig", 80, 0., 2000., 80, 0., 20. );
	     
  TH2F HT_significance_PT20_MET20 = fs->make<TH2F>("HT_significance_PT20_MET20","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  TH2F HT_significance_PT20_MET40 = fs->make<TH2F>("HT_significance_PT20_MET40","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  TH2F HT_significance_PT20_MET60 = fs->make<TH2F>("HT_significance_PT20_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  TH2F HT_significance_PT40_MET60 = fs->make<TH2F>("HT_significance_PT40_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);
  TH2F HT_significance_PT60_MET60 = fs->make<TH2F>("HT_significance_PT60_MET60","HT vs. significance", 80, 0., 2000., 80, 0., 20.);

};  

#endif  
