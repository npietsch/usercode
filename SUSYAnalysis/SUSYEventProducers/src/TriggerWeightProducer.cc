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
  // apply muon trigger weighting?
  bool MuonTriggerWeight_;
  // apply muon trigger weighting?
  bool ElectronTriggerWeight_;
};

// Constructor
TriggerWeightProducer::TriggerWeightProducer(const edm::ParameterSet& iConfig):
  inputMETs_             (iConfig.getParameter<edm::InputTag> ("inputMETs")),
  MuonTriggerWeight_     (iConfig.getParameter<bool>          ("MuonTriggerWeight")),
  ElectronTriggerWeight_ (iConfig.getParameter<bool>          ("ElectronTriggerWeight"))
{
  // Register your products
  produces<double>("triggerWeight");
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

  // declare instance of class HLTConfigProvider
  //HLTConfigProvider hltConfig_;

  // get prescale factor of trigger "triggerName"
  //double prescale = hltConfig_.prescaleValue(iEvent,iSetup,"triggerName"); 

  double weight=1.;
  double weight_err=0;

  double met=(*mets)[0].et();

  double sig=1;
  double mu=1;
  double eps=1;
  double sig_err=0;
  double mu_err=0;
  double eps_err=0;
  
  if(MuonTriggerWeight_ == true)
    {
      if(iEvent.run() >= 123456)
	{
	  //sig=abc;
	  //mu==xyz;
	  //eps=lmn;
	}
      if(iEvent.run() >= 234567)
	{
	  //sig=...;
	  //...
	}
      //...
    }
  
  else if(ElectronTriggerWeight_ == true)
    {
      if(iEvent.run() >= 123456)
	{
	  //sig=abc;
	  //mu==xyz;
	  //eps=lmn;
	}
      if(iEvent.run() >= 234567)
	{
	  //sig=...;
	  //...
	}
      //...
    }

  if(MuonTriggerWeight_ == true || ElectronTriggerWeight_ == true)
    { 
      double cdf=eps*ROOT::Math::gaussian_cdf(met,sig,mu);
      if(cdf!=0)
	{
	  weight  = 1./eps/cdf;
	  double dwmu  = (1./eps/ROOT::Math::gaussian_cdf(met,sig,mu*1.00001)-weight)/0.00001/mu;
	  double dwsig = (1./eps/ROOT::Math::gaussian_cdf(met,sig*1.00001,mu)-weight)/0.00001/sig;
	  weight_err = sqrt( pow(dwmu * mu_err,2) + pow(dwsig * sig_err,2) + pow(weight/eps * eps_err,2) );
	}
    }
  
  // put triggerwWeight into the Event
  std::auto_ptr<double> outputWeight(new double(weight));
  iEvent.put(outputWeight, "triggerWeight");
}


// Metohd called after ending the event loop 
void TriggerWeightProducer::endJob()
{
}

// Define the TriggerWeightProducer as plugin 
// This often done in files named SealModule.cc or SealModules.cc located in /src or /plugins

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( TriggerWeightProducer );
