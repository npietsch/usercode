#include <algorithm>

#include "FWCore/Framework/interface/Event.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/TtGenEventJetsProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TtGenEventAnalyzer.h"

TtGenEventJetsProducer::TtGenEventJetsProducer(const edm::ParameterSet& cfg):
  inputGenEvent_ (cfg.getParameter<edm::InputTag>("genEvent")),
  inputJets_     (cfg.getParameter<edm::InputTag>("inputJets"))

{
  edm::Service<TFileService> fs;

  // register products
  produces<std::vector<pat::Jet> >("MatchedGenJets");
  produces<std::vector<pat::Jet> >("MatchedRecoJets");
}

void
TtGenEventJetsProducer::beginJob()
{	
}

void
TtGenEventJetsProducer::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // handles
  edm::Handle<TtGenEvent> genEvent;
  event.getByLabel(inputGenEvent_, genEvent);
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(inputJets_, jets);
  
  // create new jet collections
  std::auto_ptr<std::vector<pat::Jet> > matchedGenJets(new std::vector<pat::Jet>);
  std::auto_ptr<std::vector<pat::Jet> > matchedRecoJets(new std::vector<pat::Jet>);
  
  // loop over jets
//   for(std::vector<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet)
//     {
//       pat::Jet selectedJet  = *jet;
      
//       // if genParton is not from gluino three-body decay
//       if(selectedJet.genParton())
// 	{
// 	  if(selectedJet.genParton()->mother()->pdgId()==1000021) matchedGenJets->push_back(selectedJet);
// 	}
      
//       // if matched parton is gluon
//       if(selectedJet.genParton())
// 	{
// 	  if(selectedJet.partonFlavour()!=21) matchedRecoJets->push_back(selectedJet);
// 	}
//     }

  event.put(matchedGenJets,"MatchedGenJets");
  event.put(matchedRecoJets,"MatchedRecoJets");
}

DEFINE_FWK_MODULE(TtGenEventJetsProducer);
