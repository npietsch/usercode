#ifndef HTFilter_h  
#define HTFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class HTFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit HTFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~HTFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// jet collection label
  edm::InputTag jets_;
  /// cut on HT, default values is 300 GeV
  double Cut_;
};  

#endif
