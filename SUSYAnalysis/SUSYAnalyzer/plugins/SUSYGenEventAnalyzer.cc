#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYGenEventAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "AnalysisDataFormats/TopObjects/interface/SUSYGenEvent.h"


using namespace std;

SUSYGenEventAnalyzer::SUSYGenEventAnalyzer(const edm::ParameterSet& cfg):
  inputGenEvent_(cfg.getParameter<edm::InputTag>("SEvent"))
{ 
  edm::Service<TFileService> fs;

  number_of_BQuarks_ = fs->make<TH1F>("nr_BQuarks",    "nr BQuarks",     6, 0.5, 6.5);
}

SUSYGenEventAnalyzer::~SUSYGenEventAnalyzer()
{
}

void
SUSYGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<SUSYGenEvent> SEvent;
  evt.getByLabel(inputGenEvent_, SEvent);
  
  number_of_BQuarks_->Fill(SEvent->numberOfLeptons());
}

 
 

void SUSYGenEventAnalyzer::beginJob()
{  
} 

void SUSYGenEventAnalyzer::endJob()
{
}
