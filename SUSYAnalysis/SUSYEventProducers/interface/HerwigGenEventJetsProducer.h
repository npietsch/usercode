#ifndef HerwigGenEventJetsProducer_h
#define HerwigGenEventJetsProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class HerwigGenEventJetsProducer : public edm::EDProducer {

 public:
  /// default constructor
  explicit HerwigGenEventJetsProducer(const edm::ParameterSet&);
  /// default destructor
  ~HerwigGenEventJetsProducer(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// create new jet collection
  virtual void produce(edm::Event&, const edm::EventSetup&);
  

 private:
  /// input tags
  edm::InputTag inputGenEvent_;
  edm::InputTag inputRecoJets_;
  edm::InputTag inputGenJets_;

  // histograms
  //...
};

#endif
