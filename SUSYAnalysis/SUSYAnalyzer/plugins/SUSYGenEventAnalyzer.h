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

  TH1F *EtJet1_2BQuarks_gq_;
  TH1F *EtJet1_2BQuarks_gg_;
  TH1F *EtJet1_2BQuarks_qq_;
  TH1F *EtJet1_2BQuarks_other_;
  TH1F *EtJet1_2BQuarks_;

  TH1F *EtJet1_012BQuarks_gq_;
  TH1F *EtJet1_012BQuarks_gg_;
  TH1F *EtJet1_012BQuarks_qq_;
  TH1F *EtJet1_012BQuarks_other_;
  TH1F *EtJet1_012BQuarks_;

  TH1F *EtJet1_3456BQuarks_gq_;
  TH1F *EtJet1_3456BQuarks_gg_;
  TH1F *EtJet1_3456BQuarks_qq_;
  TH1F *EtJet1_3456BQuarks_other_;
  TH1F *EtJet1_3456BQuarks_;

  TH1F *nrLep_ss_;
  TH1F *nrLep_os_;
  TH1F *nrLep_;

  TH1F *angleb1b2_;
  TH1F *mbb_;
  TH1F *HTB_;
  TH1F *DeltaMT_min_;
  };  
#endif  
