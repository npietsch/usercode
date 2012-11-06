#ifndef PFConsistentMuonProducer_h
#define PFConsistentMuonProducer_h

#include "TH1.h"
#include "TH2.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/Math/interface/deltaR.h"


class PFConsistentProducer : public edm::EDProducer {

 public:
  explicit PFConsistentMuonProducer(const edm::ParameterSet&);
  ~PFConsistentMuonProducer() {};
  
 private:
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:
  /// muon collections label
  edm::InputTag muons_;
  edm::InputTag pfMuons_;
};

#endif
