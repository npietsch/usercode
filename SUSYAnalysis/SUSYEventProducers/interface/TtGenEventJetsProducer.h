#ifndef TtGenEventJetsProducer_h
#define TtGenEventJetsProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class TtGenEventJetsProducer : public edm::EDProducer {

 public:
  /// default constructor
  explicit TtGenEventJetsProducer(const edm::ParameterSet&);
  /// default destructor
  ~TtGenEventJetsProducer(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// create new jet collection
  virtual void produce(edm::Event&, const edm::EventSetup&);
  

 private:
  /// input tags
  edm::InputTag inputGenEvent_;
  edm::InputTag inputJets_;
 
  // histograms
  //...
};

#endif
