#ifndef TransverseMassFilter_h  
#define TransverseMassFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class TransverseMassFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit TransverseMassFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~TransverseMassFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
  /// input collection labels
  edm::InputTag met_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
  /// cut on transverse mass
  std::vector<double> Cut_;
};  

#endif
