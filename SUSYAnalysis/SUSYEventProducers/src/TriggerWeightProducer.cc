#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/MET.h"

//
// class decleration
//

// Define class
// This is often done in .h file located in /interface or /plugins
class TriggerWeightProducer: public edm::EDProducer
{
public:
  explicit TriggerWeightProducer(const edm::ParameterSet&);
  ~TriggerWeightProducer();
  
private:
  //  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void beginJob();
  virtual void endJob();
  
  // decalare MET InputTag
  edm::InputTag inputMETs_;
  
  // declare input paramters for weighting
  double sig_;
  double eps_;

  // apply weighting?
  bool triggerWgt_;

  // MET trigger threshold
  double threshold_;

};

// Constructor
TriggerWeightProducer::TriggerWeightProducer(const edm::ParameterSet& iConfig):
  inputMETs_  (iConfig.getParameter<edm::InputTag> ("inputMETs")),
  sig_        (iConfig.getParameter<double>        ("sig")),
  eps_        (iConfig.getParameter<double>        ("eps")),
  triggerWgt_ (iConfig.getParameter<double>        ("triggerWgt")),
  threshold_  (iConfig.getParameter<double>        ("threshold"))
{
  // Register your products
  produces<double> ("TriggerWeight");
}

// Destructor
TriggerWeightProducer::~TriggerWeightProducer()
{
}

// Metohd called befor starting the event loop 
void TriggerWeightProducer::beginJob()
{
}

// loops over all events
void TriggerWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // get handle on MET collcetion
  edm::Handle<std::vector<pat::MET> > mets;
  iEvent.getByLabel(inputMETs_, mets);
  
  double weight=1.;

  if(triggerWgt_ == true)
    {
      double met=(*mets)[0].et();
      double sig=sig_;
      double eps=eps_;

      // implement wegthing algorithm here
      //weight = ...
    }    
      
  // put triggerwWeight into the Event
  std::auto_ptr<double> outputWeight(new double(weight));
  iEvent.put(outputWeight, "weight");
}


// Metohd called after ending the event loop 
void TriggerWeightProducer::endJob()
{
}

// Define the TriggerWeightProducer as plugin 
// This often done in files named SealModule.cc or SealModules.cc located in /src or /plugins

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( TriggerWeightProducer );
