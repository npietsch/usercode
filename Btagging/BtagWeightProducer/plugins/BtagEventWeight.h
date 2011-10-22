#ifndef BtagEventWeight_h
#define BtagEventWeight_h

#include <memory>
#include <string>
#include <iostream>

#include "TH1.h"
#include "TH2.h"
#include "TFile.h"
#include "TString.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "RecoBTag/Records/interface/BTagPerformanceRecord.h"
#include "RecoBTag/PerformanceDB/interface/BtagPerformance.h"
#include "CondFormats/PhysicsToolsObjects/interface/BinningPointByMap.h"
#include "FWCore/Framework/interface/ESHandle.h"

/// This module calculates a b tag scale factor (SF) for the whole event with >=2 b tags,
/// which is put into the CMSSW event
/// as a double, which can be used as an event weight in the analyzers of interest.
/// cfg parameters:
/// jets_             jet collection
/// bTagAlgo_         name of the b tag algorithm (supported: SSVHEM)
/// sysVar_           name of the systematic variation (noSys, bTagSFUp, bTagSFDown, misTagSFUp, misTagSFDown)
/// verbose_          set to 0 if no output on terminal is desired, 1 for moderate and 2 for detailed output
/// filename_         if not set to "", efficiencies are loaded from histos in filename_, which have been
///                   created with BTagEfficiencyAnalyzer.cc

//dk 21.10.11
// for RA4b we need weights for 0,1,2,3>=-btags: w0,w1,w2,w3
// to fit the dependency on eps = b-jet b-tag efficiency and eta = non b-jet mistag rate 
// susvar

class BtagEventWeight : public edm::EDProducer {

 public:
  explicit BtagEventWeight(const edm::ParameterSet&);
  ~BtagEventWeight();
  
 private:
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob();

 private:
  edm::InputTag jets_;
  std::string bTagAlgo_;
  std::string sysVar_;
  int verbose_;
  std::string filename_;
  double maxPt_;
  double maxEta_;
  
  /// to load database
  std::map<std::string,PerformanceResult::ResultType> measureMap_;
  edm::ESHandle<BtagPerformance> perfHBTag;
  edm::ESHandle<BtagPerformance> perfHMisTag;
  
  /// histogram container
  /// for output
  std::map<std::string, TH1F*> hists_;
  /// efficiency histos as input
  //std::map<std::string, TH1F*> effHists_;
  std::map<std::string, TH2F*> effHists_;
  
  /// file with histos
  TFile * file_;

  
  double effBTag    (double, double);
  double effBTagSF  (double, double);
  double effBTagCjet(double, double);
  double effMisTag  (double, double);
  double effMisTagSF(double, double);
  double effBTagEvent(std::vector<double> &, std::vector<double> &);
//dk
  std::vector<double> effBTagEvent0123(std::vector<double> , std::vector<double> , double scl_eff,double scl_mis);

  
};

#endif
