#ifndef DeltaPhiHTMETFilter_h  
#define DeltaPhiHTMETFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class DeltaPhiHTMETFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit DeltaPhiHTMETFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~DeltaPhiHTMETFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// jet collection label
  edm::InputTag jets_;
  edm::InputTag mets_;

  /// cut on phi between HT and MET
  const std::vector<double> Cut_;
};  

#endif
