#ifndef DeltaPhiFilter_h  
#define DeltaPhiFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/deltaPhi.h"

class DeltaPhiFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit DeltaPhiFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~DeltaPhiFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// inout collection labels
  edm::InputTag jets_;
  edm::InputTag mets_;

  /// cut on deltPhi, default values is 0.5
  int Jet_;
  double Cut_;
};  

#endif
