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

  TH1F *number_of_BQuarks_;
  TH1F *number_of_BQuarks_sgsg_;
  TH1F *number_of_BQuarks_sqsq_;
  TH1F *number_of_BQuarks_sgsq_;
  TH2F *number_of_BQuarks_jet1_et_;
  TH1F *jet1_et_0BQuarks_;
  TH1F *jet1_et_2BQuarks_;
  TH1F *jet1_et_4BQuarks_;
};  
#endif  
