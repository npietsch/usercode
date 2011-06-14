#ifndef EventTopology_h  
#define EventTopology_h

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
#include "DataFormats/PatCandidates/interface/Particle.h"

class EventTopology : public edm::EDAnalyzer {

 public:
  
  explicit EventTopology(const edm::ParameterSet&);
  ~EventTopology();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	
  //edm::InputTag inputGenEvent_;
  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag mediumJets_;
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag pvSrc_;

  // TH2F histograms
  TH2F *nrLep_nrBjets_;
  TH2F *nrJets_nrBjets_;
  TH2F *nrMJets_nrBjets_;
  TH2F *Jet0_Et_nrBjets_;

  // TH1F histograms
  TH1F *sphericity_bjets_;         
  TH1F *aplanarity_bjets_;   
  TH1F *circularity_bjets_;        
  TH1F *isotropy_bjets_;

  TH1F *sphericity_bjetsMET_;         
  TH1F *aplanarity_bjetsMET_;   
  TH1F *circularity_bjetsMET_;        
  TH1F *isotropy_bjetsMET_;

  TH1F *sphericity_bjetsLep_;         
  TH1F *aplanarity_bjetsLep_;   
  TH1F *circularity_bjetsLep_;        
  TH1F *isotropy_bjetsLep_;

  TH1F *sphericity_bjetsMETLep_;         
  TH1F *aplanarity_bjetsMETLep_;   
  TH1F *circularity_bjetsMETLep_;        
  TH1F *isotropy_bjetsMETLep_;

  TH1F *dR_BjetMET_[4];
  TH1F *dPhi_BjetMET_[4];
  TH1F *dTheta_BjetMET_[4];
  TH1F *angle_BjetMET_[4];

  TH1F *dR_BjetLep_[4][2];
  TH1F *dPhi_BjetLep_[4][2];
  TH1F *dTheta_BjetLep_[4][2];
  TH1F *angle_BjetLep_[4][2];

  TH1F *dR_BjetBjet_[4][4];
  TH1F *dPhi_BjetBjet_[4][4];
  TH1F *dTheta_BjetBjet_[4][4];
  TH1F *angle_BjetBjet_[4][4];

  TH1F *dR_LepMET_[2];
  TH1F *dPhi_LepMET_[2];
  TH1F *dTheta_LepMET_[2];
  TH1F *angle_LepMET_[2];
  
  TH1F *dRBjetMETMin_;
  TH1F *dPhiBjetMETMin_;
  TH1F *dThetaBjetMETMin_;
  TH1F *AngleBjetMETMin_;

  TH1F *dRBjetMETMax_;
  TH1F *dPhiBjetMETMax_;
  TH1F *dThetaBjetMETMax_;
  TH1F *AngleBjetMETMax_;

  TH1F *dRBjetBjetMin_;
  TH1F *dPhiBjetBjetMin_;
  TH1F *dThetaBjetBjetMin_;
  TH1F *AngleBjetBjetMin_;

  TH1F *dRBjetBjetMax_;
  TH1F *dPhiBjetBjetMax_;
  TH1F *dThetaBjetBjetMax_;
  TH1F *AngleBjetBjetMax_;

  TH1F *dRBjetLepMin_;
  TH1F *dPhiBjetLepMin_;
  TH1F *dThetaBjetLepMin_;
  TH1F *AngleBjetLepMin_;

  TH1F *dRBjetLepMax_;
  TH1F *dPhiBjetLepMax_;
  TH1F *dThetaBjetLepMax_;
  TH1F *AngleBjetLepMax_;

  TH1F *dRLepMETMin_;
  TH1F *dPhiLepMETMin_;
  TH1F *dThetaLepMETMin_;
  TH1F *AngleLepMETMin_;

  TH1F *dRLepMETMax_;
  TH1F *dPhiLepMETMax_;
  TH1F *dThetaLepMETMax_;
  TH1F *AngleLepMETMax_;

  TH1F *dPhiMediumJetMETMin_;
};

#endif  
