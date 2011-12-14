#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/MET.h"

#include "TMath.h"
#include "TROOT.h"
#include "Math/ProbFuncMathCore.h"

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

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
  double mu_;
  double sig_err_;
  double eps_err_;
  double mu_err_;

  // apply weighting?
  bool triggerWgt_;

  // MET trigger threshold
  double threshold_;

  HLTConfigProvider hltConfig_;

};

// Constructor
TriggerWeightProducer::TriggerWeightProducer(const edm::ParameterSet& iConfig):
  inputMETs_  (iConfig.getParameter<edm::InputTag> ("inputMETs")),
  sig_        (iConfig.getParameter<double>        ("sig")),
  eps_        (iConfig.getParameter<double>        ("eps")),
  mu_         (iConfig.getParameter<double>        ("mu")),
  sig_err_    (iConfig.getParameter<double>        ("sig_err")),
  eps_err_    (iConfig.getParameter<double>        ("eps_err")),
  mu_err_     (iConfig.getParameter<double>        ("mu_err")),
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

  double weight_err;
  if(triggerWgt_ == true)
    {
      double met=(*mets)[0].et();
      double sig=sig_;
      double mu=mu_;
      double eps=eps_;
      double sig_err=sig_err_;
      double mu_err=mu_err_;
      double eps_err=eps_err_;

      // implement wegthing algorithm here
      //weight = ...
      double cdf=eps_*ROOT::Math::gaussian_cdf(met,sig,mu);
      if(cdf!=0) {
           weight  = 1./eps/cdf;
           double dwmu  = (1./eps/ROOT::Math::gaussian_cdf(met,sig,mu*1.00001)-weight)/0.00001/mu;
           double dwsig = (1./eps/ROOT::Math::gaussian_cdf(met,sig*1.00001,mu)-weight)/0.00001/sig;
           weight_err = sqrt( pow(dwmu * mu_err,2) + pow(dwsig * sig_err,2) + pow(weight/eps * eps_err,2) );
      }
      else {
           weight_err=0;
      }

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
