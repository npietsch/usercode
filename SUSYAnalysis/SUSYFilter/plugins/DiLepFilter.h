#ifndef DiLepFilter_h
#define DiLepFilter_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


class DiLepFilter : public edm::EDFilter {

public:
  /// default constructor
  explicit DiLepFilter(const edm::ParameterSet& configFile);
  /// default destructor
  ~DiLepFilter();

private:
  /// sanity check
  virtual void beginJob();
  /// event veto
  virtual bool filter(edm::Event& event, const edm::EventSetup& setup);

private:


  /// electron adn muon collection label
  const edm::InputTag goodElectrons_;
  const edm::InputTag goodMuons_;
  const edm::InputTag looseElectrons_;
  const edm::InputTag looseMuons_;

  /// true if cut window is vetoed, false if window is to be selected
  const bool isVeto_;

  /// cut on Z-mass, default values are 76GeV, 106GeV
  const std::vector<double> Cut_;

  /// filter on sign
  const int fltrChrg_;
};

#endif
