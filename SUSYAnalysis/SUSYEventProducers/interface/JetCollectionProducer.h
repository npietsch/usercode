#ifndef JetCollectionProducer_h
#define JetCollectionProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class JetCollectionProducer : public edm::EDProducer {

 public:
  /// default constructor
  explicit JetCollectionProducer(const edm::ParameterSet&);
  /// default destructor
  ~JetCollectionProducer(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// create new jet collection
  virtual void produce(edm::Event&, const edm::EventSetup&);
  

 private:
  /// jet input collection 
  edm::InputTag inputJets_;
 
  // histograms
  //...
};

#endif
