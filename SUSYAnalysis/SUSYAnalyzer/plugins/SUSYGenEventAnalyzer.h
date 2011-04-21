#ifndef SUSYGenEventAnalyzer_h  
#define SUSYGenEventAnalyzer_h

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
#include "DataFormats/PatCandidates/interface/Particle.h"

class SUSYGenEventAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit SUSYGenEventAnalyzer(const edm::ParameterSet&);
  ~SUSYGenEventAnalyzer();

  std::vector<double> SemiLepHypo(const pat::Jet&, const pat::Jet&, const pat::Jet&, const pat::Jet&, const pat::Particle&, const pat::MET&);

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  edm::InputTag inputGenEvent_;
  edm::InputTag initSubset_;
  edm::InputTag jets_;
  edm::InputTag bjets_;
  edm::InputTag matchedbjets_;
  edm::InputTag matchedqjets_;
  edm::InputTag matchedmuons_;
  edm::InputTag matchedelectrons_;
  edm::InputTag met_;

  TH1F *nrBQuarks_gq_ssDiLep_;
  TH1F *nrBQuarks_gg_ssDiLep_;
  TH1F *nrBQuarks_qq_ssDiLep_;
  TH1F *nrBQuarks_other_ssDiLep_;
  TH1F *nrBQuarks_ssDiLep_;
  TH1F *nrBQuarks_ssqq_ssDiLep_;
  TH1F *nrBQuarks_osqq_ssDiLep_;

  TH1F *nrBQuarks_gq_osDiLep_;
  TH1F *nrBQuarks_gg_osDiLep_;
  TH1F *nrBQuarks_qq_osDiLep_;
  TH1F *nrBQuarks_other_osDiLep_;
  TH1F *nrBQuarks_osDiLep_;
  TH1F *nrBQuarks_ssqq_osDiLep_;
  TH1F *nrBQuarks_osqq_osDiLep_;

  TH1F *nrBQuarks_gq_;
  TH1F *nrBQuarks_gg_;
  TH1F *nrBQuarks_qq_;
  TH1F *nrBQuarks_other_;
  TH1F *nrBQuarks_;
  TH1F *nrBQuarks_ssqq_;
  TH1F *nrBQuarks_osqq_;

  TH1F *nrBJets_gq_;
  TH1F *nrBJets_gg_;
  TH1F *nrBJets_qq_;
  TH1F *nrBJets_other_;
  TH1F *nrBJets_;
  TH1F *nrBJets_ssqq_;
  TH1F *nrBJets_osqq_;

  TH1F *nrBTags_gq_;
  TH1F *nrBTags_gg_;
  TH1F *nrBTags_qq_;
  TH1F *nrBTags_other_;
  TH1F *nrBTags_;
  TH1F *nrBTags_ssqq_;
  TH1F *nrBTags_osqq_;

  TH1F *nrLeptons_gq_;
  TH1F *nrLeptons_gg_;
  TH1F *nrLeptons_qq_;
  TH1F *nrLeptons_other_;
  TH1F *nrLeptons_ssqq_;
  TH1F *nrLeptons_osqq_;

  TH1F *nrLeptons_ss_;
  TH1F *nrLeptons_os_;
  TH1F *nrLeptons_;

  TH1F *nrJets_gq_;
  TH1F *nrJets_gg_;
  TH1F *nrJets_qq_;
  TH1F *nrJets_other_;
  TH1F *nrJets_ssqq_;
  TH1F *nrJets_osqq_;
  TH1F *nrJets_;

  TH1F *nrJets_gq_0l_;
  TH1F *nrJets_gg_0l_;
  TH1F *nrJets_qq_0l_;
  TH1F *nrJets_other_0l_;
  TH1F *nrJets_ssqq_0l_;
  TH1F *nrJets_osqq_0l_;
  TH1F *nrJets_0l_;
  
  TH1F *nrJets_gq_1l_;
  TH1F *nrJets_gg_1l_;
  TH1F *nrJets_qq_1l_;
  TH1F *nrJets_other_1l_;
  TH1F *nrJets_ssqq_1l_;
  TH1F *nrJets_osqq_1l_;
  TH1F *nrJets_1l_;

  TH1F *nrJets_gq_2l_;
  TH1F *nrJets_gg_2l_;
  TH1F *nrJets_qq_2l_;
  TH1F *nrJets_other_2l_;
  TH1F *nrJets_ssqq_2l_;
  TH1F *nrJets_osqq_2l_;
  TH1F *nrJets_2l_;

  TH1F *nrJets_gq_3l_;
  TH1F *nrJets_gg_3l_;
  TH1F *nrJets_qq_3l_;
  TH1F *nrJets_other_3l_;
  TH1F *nrJets_ssqq_3l_;
  TH1F *nrJets_osqq_3l_;
  TH1F *nrJets_3l_;

  TH1F *ratio_gq_;
  TH1F *ratio_gg_;
  TH1F *ratio_qq_;
  TH1F *ratio_other_;
  TH1F *ratio_;
  TH1F *ratio_ssqq_;
  TH1F *ratio_osqq_;

  TH1F *flavor_bjet1_;
  TH1F *flavor_bjet2_;
  TH1F *flavor_bjet3_;
  TH1F *flavor_bjet4_;

  TH1F *Jet1_Et_2BQuarks_gq_;
  TH1F *Jet1_Et_2BQuarks_gg_;
  TH1F *Jet1_Et_2BQuarks_qq_;
  TH1F *Jet1_Et_2BQuarks_other_;
  TH1F *Jet1_Et_2BQuarks_;

  TH1F *Jet1_Et_012BQuarks_gq_;
  TH1F *Jet1_Et_012BQuarks_gg_;
  TH1F *Jet1_Et_012BQuarks_qq_;
  TH1F *Jet1_Et_012BQuarks_other_;
  TH1F *Jet1_Et_012BQuarks_;

  TH1F *Jet1_Et_3456BQuarks_gq_;
  TH1F *Jet1_Et_3456BQuarks_gg_;
  TH1F *Jet1_Et_3456BQuarks_qq_;
  TH1F *Jet1_Et_3456BQuarks_other_;
  TH1F *Jet1_Et_3456BQuarks_;

  TH1F *angleb1b2_;
  TH1F *mbb_;
  TH1F *HTB_;
  TH1F *DeltaMT_min_;

  TH1F *deltaPhi_b1b2_;
  TH1F *deltaPhi_b1MET_;
  TH1F *deltaPhi_b2MET_;
  TH1F *deltaPhi_b12MET_;

  TH1F *deltaPhi_MuMET_;
  TH1F *deltaPhi_ElMET_;
  TH1F *deltaPhi_LepMET_;

  TH1F *deltaPhi_Lep1Lep2_;
  TH1F *deltaPhi_Lep1MET_;
  TH1F *deltaPhi_Lep2MET_; 
  TH1F *deltaPhi_Lep12MET_;

  TH1F *deltaPhi_Mu1Mu2_;
  TH1F *deltaPhi_Mu1MET_;
  TH1F *deltaPhi_Mu2MET_;
  TH1F *deltaPhi_Mu12MET_;

  TH1F *deltaPhi_El1El2_;
  TH1F *deltaPhi_El1MET_;
  TH1F *deltaPhi_El2MET_;
  TH1F *deltaPhi_El12MET_;

  TH1F *deltaPhi_MuEl_;
  TH1F *deltaPhi_MuElMET_;

  TH1F *sphericity_bjetsMET_;
  TH1F *aplanarity_bjetsMET_;
  TH1F *circularity_bjetsMET_;
  TH1F *isotropy_bjetsMET_;

  TH1F *Jet1_Et_2Bjets_;
  TH1F *Bjet1_Et_;
  TH1F *Bjet2_Et_;
  TH1F *HT_2Bjets_;
  TH1F *HT_2Bjets_1LightJet_;

  TH1F *MET_SSDiLep_;
  TH1F *MET_OSDiLep_;

  };  
#endif  
