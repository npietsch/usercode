#ifndef DeltaPhiHTMHTFilter_h  
#define DeltaPhiHTMHTFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class DeltaPhiHTMHTFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit DeltaPhiHTMHTFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~DeltaPhiHTMHTFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// jet collection label
  edm::InputTag jets_;

  /// cut on phi between HT and MHT
  const std::vector<double> Cut_;
};  

#endif
