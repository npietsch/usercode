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
  edm::InputTag bjets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  edm::InputTag pvSrc_;

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
};  

#endif  
