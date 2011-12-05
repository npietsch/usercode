#ifndef YmetFilter_h  
#define YmetFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class YmetFilter : public edm::EDFilter {

 public:
  /// default constructor
  explicit YmetFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~YmetFilter();
  
 private:
  /// sanity check 
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);
  
 private:
  /// inout collection labels
  edm::InputTag jets_;
  edm::InputTag mets_;

  /// cut on Ymet, default values is 0 GeV
  double Cut_;
};  

#endif
