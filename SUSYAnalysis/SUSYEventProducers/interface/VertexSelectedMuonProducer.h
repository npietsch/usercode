#ifndef VertexSelectedMuonProducer_h
#define VertexSelectedMuonProducer_h

#include "TH1.h"
#include "TH2.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class VertexSelectedMuonProducer : public edm::EDProducer {

 public:
  explicit VertexSelectedMuonProducer(const edm::ParameterSet&);
  ~VertexSelectedMuonProducer() {};
  
 private:
  virtual void produce(edm::Event&, const edm::EventSetup&);

 private:
  edm::InputTag src_;
  edm::InputTag primaryVertex_;
  
  bool dxyCut_;
  bool dzCut_;
  double dxyCutValue_;
  double dzCutValue_;

  TH1F* dxy_;
  TH1F* dz_;
};

#endif
