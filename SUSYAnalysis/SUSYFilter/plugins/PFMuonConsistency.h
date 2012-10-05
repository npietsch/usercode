#ifndef PFMuonConsistency_h  
#define PFMuonConsistency_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/deltaR.h"

class PFMuonConsistency : public edm::EDFilter {

 public:
  /// default constructor
  explicit PFMuonConsistency(const edm::ParameterSet& configFile);
  /// default destructor
  ~PFMuonConsistency();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// muon collections label
  edm::InputTag muons_;
  edm::InputTag pfCandidates_;
};  

#endif
