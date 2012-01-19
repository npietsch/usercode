#ifndef JetsProducer_h
#define JetsProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class JetsProducer : public edm::EDProducer {

 public:
  /// default constructor
  explicit JetsProducer(const edm::ParameterSet&);
  /// default destructor
  ~JetsProducer(){};
  
 private:
  /// check settings
  virtual void beginJob();
  /// create new jet collection
  virtual void produce(edm::Event&, const edm::EventSetup&);
  

 private:
  /// jet input collection 
  edm::InputTag inputJets_;
 
  /// jet output collection 
  std::string outputJets_;

  // histograms
  //...
};

#endif
