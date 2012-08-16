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
  inputRecoJets_ (cfg.getParameter<edm::InputTag>("inputRecoJets")),
  inputGenJets_  (cfg.getParameter<edm::InputTag>("inputGenJets"))
{
  edm::Service<TFileService> fs;

  // register products
  produces<std::vector<reco::GenJet> >("MatchedGenJets");
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
  edm::Handle<std::vector<pat::Jet> > recoJets;
  event.getByLabel(inputRecoJets_, recoJets);
  edm::Handle<std::vector<reco::GenJet> > genJets;
  event.getByLabel(inputGenJets_, genJets);

  // create new jet collections
  std::auto_ptr<std::vector<reco::GenJet> > matchedGenJets(new std::vector<reco::GenJet>);
  std::auto_ptr<std::vector<pat::Jet> > matchedRecoJets(new std::vector<pat::Jet>);
  
  // loop over gen jets
//    for(std::vector<reco::GenJet>::const_iterator jet=genJets->begin(); jet!=genJets->end(); ++jet)
//      {
//        reco::GenJet selectedJet  = *jet;
      
//        // if gen jet can be matched to TtGenEvent
//        if((genEvent->isSemiLeptonic(WDecay::kMuon) ||  genEvent->isSemiLeptonic(WDecay::kElec)))
// 	 {
// 	   std::cout << "reco pT: " << selectedJet.pt() << std::endl;
// 	   std::cout << "gen pT: " << genEvent->hadronicDecayB()->pt() << std::endl;

// 	   if(selectedJet.genParticle()->pt() == genEvent->hadronicDecayB()->pt() ||
// 	      selectedJet.genParticle()->pt() == genEvent->leptonicDecayB()->pt())
// 	     {
// 	       //std::cout << "B-QUARK MATCH" <<  std::endl;
// 	        matchedGenJets->push_back(selectedJet);

// 	     }
// 	   for(int ddx=0; ddx<(int)genEvent->hadronicDecayW()->numberOfDaughters(); ++ddx)
// 	     {
// 	       if(selectedJet.genParticle()->pt() == genEvent->hadronicDecayW()->daughter(ddx)->pt())
// 		 {
// 		   //std::cout << "LIGHT QUARK MATCH" <<  std::endl;
// 		   matchedGenJets->push_back(selectedJet);
// 		 }
// 	     }
	   
// 	 } 
//      }

  // loop over reco jets
   for(std::vector<pat::Jet>::const_iterator jet=recoJets->begin(); jet!=recoJets->end(); ++jet)
     {
       pat::Jet selectedJet  = *jet;
      
       // if reco jet can be matched to TtGenEvent
       if(selectedJet.genParton() && (genEvent->isSemiLeptonic(WDecay::kMuon) ||  genEvent->isSemiLeptonic(WDecay::kElec)))
	 {
	   //std::cout << "reco pT: " << selectedJet.genParton()->pt() << std::endl;
	   //std::cout << "gen pT: " << genEvent->hadronicDecayB()->pt() << std::endl;

	   if(selectedJet.genParton()->pt() == genEvent->hadronicDecayB()->pt() ||
	      selectedJet.genParton()->pt() == genEvent->leptonicDecayB()->pt())
	     {
	       matchedRecoJets->push_back(selectedJet);

	     }
	   for(int ddx=0; ddx<(int)genEvent->hadronicDecayW()->numberOfDaughters(); ++ddx)
	     {
	       if(selectedJet.genParton()->pt() == genEvent->hadronicDecayW()->daughter(ddx)->pt())
		 {
		   matchedRecoJets->push_back(selectedJet);
		 }
	     }
	   
	 } 
     }
   
   event.put(matchedGenJets,"MatchedGenJets");
   event.put(matchedRecoJets,"MatchedRecoJets");
}

DEFINE_FWK_MODULE(TtGenEventJetsProducer);
