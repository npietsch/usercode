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

class SUSYGenEventAnalyzer : public edm::EDAnalyzer {

 public:
  
  explicit SUSYGenEventAnalyzer(const edm::ParameterSet&);
  ~SUSYGenEventAnalyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  edm::InputTag inputGenEvent_;
  edm::InputTag initSubset_;
  edm::InputTag jets_;

  TH1F *nrBQuarks_gq_;
  TH1F *nrBQuarks_gg_;
  TH1F *nrBQuarks_qq_;
  TH1F *nrBQuarks_other_;
  TH1F *nrBQuarks_;

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
  };  
#endif  
