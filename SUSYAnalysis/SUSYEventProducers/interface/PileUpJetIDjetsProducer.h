#ifndef PileUpJetIDjetsProducer_h
#define PileUpJetIDjetsProducer_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class PileUpJetIDjetsProducer : public edm::EDProducer {

 public:
  /// default constructor
  explicit PileUpJetIDjetsProducer(const edm::ParameterSet&);
  /// default destructor
  ~PileUpJetIDjetsProducer(){};
  
 private:
  /// create new jet collection
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:
  edm::InputTag inputJets_;
  edm::InputTag inputMETs_;
  edm::InputTag discriminator_;
  edm::InputTag flag_;
  edm::InputTag wp_;

  std::string outputJets_;
  std::string outputMETs_;

  TH1F* PileUpJetIDdiscriminator_;
};

#endif
