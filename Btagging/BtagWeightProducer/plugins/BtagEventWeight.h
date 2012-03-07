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
  std::string rootDir_;
  double maxPt_;
  double maxEta_;
  double shift_;
  bool scaleJetEffSF_;
  bool scaleEventEffSF_;
  bool scaleEventMistagSF_;

  /// to load database
  std::map<std::string,PerformanceResult::ResultType> measureMap_;
  edm::ESHandle<BtagPerformance> perfHBTag;
  edm::ESHandle<BtagPerformance> perfHMisTag;

  std::map<std::string, TH2F*> effHists_;
  
  /// file with histos
  TFile * file_;
  TString dir_;

  double effBTag    (double, double);
  double effBTagSF_old  (double, double);
  double effBTagCjet(double, double);
  double effMisTag  (double, double);
  double effMisTagSF_old(double, double);
  std::vector<double> effBTagEvent0123(std::vector<double> , std::vector<double> , double scl_eff,double scl_mis);
  
  static float SFb_err[16];
  static float SFb_ptmin[16];
  double effBTagSF(double,double,double);
  double effMisTagSF(double, double);
  inline double SFL_0008_mean(double x);
  inline double SFL_0008_max(double x);
  inline double SFL_0008_min(double x);
  inline double SFL_0816_mean(double x);
  inline double SFL_0816_max(double x);
  inline double SFL_0816_min(double x);
  inline double SFL_1624_mean(double x);
  inline double SFL_1624_min(double x);
  inline double SFL_1624_max(double x);
  inline double SFL_0024_mean(double x);
  inline double SFL_0024_min(double x);
  inline double SFL_0024_max(double x);
};


#endif
