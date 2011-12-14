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

  // Tom D's talk 12.12.11 RA4 meeting - AN2011-410_v4 77
  // only errors not cov!!!
  // Mu8_HT200  plateau : eps = 0.9925 +- 0.002201
  // Mu15_HT200 plateau : eps = 0.9955 +- 0.001012
  // El10_HT200:          eps = 0.9976 +- 0.001619
  // El15_HT200:          eps = 0.9993 +- 0.0005817
  // El15_HT250:          eps = 0.9988 +- 0.0004298
  // Ele15_HT250_PFMHT25
  //        eps =  0.9957 +- 0.001628
  //        mu  = 16.05   +- 0.3813
  //        sig = 26.28   +- 0.5808
  // Ele15_HT250_PFMHT40
  //        eps =  0.9966 +- 0.002081
  //        mu  = 39.64   +- 0.3172
  //        sig = 24.35   +- 0.4426
  // HT250_Mu15_PFMHT20
  //        eps =  0.9853 +- 0.002315
  //        mu  = 13.34   +- 0.6523
  //        sig = 16.45   +- 0.7605
  // HT250_Mu15_PFMHT40
  //        eps =  0.9798 +- 0.002771
  //        mu  = 40.14   +- 0.3216
  //        sig = 16.29   +- 0.3982
  // HT300_Mu15_PFMHT40
  //        eps =  0.9856 +- 0.003817
  //        mu  = 39.21   +- 0.4641
  //        sig = 17.58   +- 0.6321
  
  if(MuonTriggerWeight_ == true) {
      if( iEvent.run() <= 163869 ) { // 160404 - 163869 : Mu5_HT200_v* and Mu8_HT200_v*
	  sig=0;
	   mu=0;
	  eps=0.9925; // +- 0.002201
      } else if ( iEvent.run() <= 166861 ) { // (165088) - 166861 : Mu15_HT200_v*
	  sig=0;
	   mu=0;
	  eps=0.9955; // +- 0.001012
      } else if ( iEvent.run() <= 172802 ) { // - 172802 : HT250_Mu15_PFMHT20_v*
	  sig=16.45;
	   mu=13.34;
	  eps=0.9853;
      } else if ( iEvent.run() <= 178078 ) { // - 178078 : HT250_Mu15_PFMHT40_v*
           mu=40.14;
          sig=16.29;
          eps=0.9798;
     } else if  ( iEvent.run() <= 180252 ) { // - 178677 : HT300_Mu15_PFMHT40_v*
           mu=39.21;
          sig=17.58;
          eps=0.9856;
     }
  } else if(ElectronTriggerWeight_ == true) {
      if( iEvent.run() <= 163869 ) { // 160404 - 163869 : Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v*
	  sig=0;
	   mu=0;
	  eps=0.9976;
      } else if ( iEvent.run() <= 166861 ) { // (165088) - 166861 : Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*
	  sig=0;
	   mu=0;
	  eps=0.9993;
      } else if ( iEvent.run() <= 172802 ) { // - 172802 : Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*
	  sig=0;
	   mu=0;
	  eps=0.9988;
      } else if ( iEvent.run() <= 178078 ) { // - 178078 : Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_v*
           mu=16.05;
          sig=26.28;
          eps=0.9957;
     } else if  ( iEvent.run() <= 180252 ) { // - 178677 : Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_v* CHECK if trigger still there!!!!!!!
           mu=39.64;
          sig=24.35;
          eps=0.9966;
     }
  }

  if(MuonTriggerWeight_ == true || ElectronTriggerWeight_ == true) { 
      double cdf=eps*ROOT::Math::gaussian_cdf(met,sig,mu);
      if(cdf!=0) {
	  weight  = 1./eps/cdf;
//	  double dwmu  = (1./eps/ROOT::Math::gaussian_cdf(met,sig,mu*1.00001)-weight)/0.00001/mu;
//	  double dwsig = (1./eps/ROOT::Math::gaussian_cdf(met,sig*1.00001,mu)-weight)/0.00001/sig;
//	  weight_err = sqrt( pow(dwmu * mu_err,2) + pow(dwsig * sig_err,2) + pow(weight/eps * eps_err,2) );
	} else weight = 0 ;
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
