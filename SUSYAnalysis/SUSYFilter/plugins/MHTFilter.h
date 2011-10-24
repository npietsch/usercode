#ifndef MHTFilter_h  
#define MHTFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class MHTFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit MHTFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~MHTFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// jet collection label
  edm::InputTag jets_;
  /// cut on MHT, default values is 60 GeV
  double Cut_;
};  

#endif
