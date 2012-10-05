#ifndef PFElectronConsistency_h  
#define PFElectronConsistency_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/deltaR.h"

class PFElectronConsistency : public edm::EDFilter {

 public:
  /// default constructor
  explicit PFElectronConsistency(const edm::ParameterSet& configFile);
  /// default destructor
  ~PFElectronConsistency();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// electron collections label
  edm::InputTag electrons_;
  edm::InputTag pfCandidates_;
};  

#endif
