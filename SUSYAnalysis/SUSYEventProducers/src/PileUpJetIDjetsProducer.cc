#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/ValueMap.h"

#include "SUSYAnalysis/SUSYEventProducers/interface/PileUpJetIDjetsProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "CMGTools/External/interface/PileupJetIdentifier.h"


PileUpJetIDjetsProducer::PileUpJetIDjetsProducer(const edm::ParameterSet& cfg):
  inputJets_     (cfg.getParameter<edm::InputTag>(     "inputJets")),
  inputMETs_     (cfg.getParameter<edm::InputTag>(     "inputMETs")),
  discriminator_ (cfg.getParameter<edm::InputTag>( "discriminator")),
  flag_          (cfg.getParameter<edm::InputTag>(          "flag")),
  wp_            (cfg.getParameter<edm::InputTag>(            "wp"))
{
  edm::Service<TFileService> fs;
  PileUpJetIDdiscriminator_= fs->make<TH1F>("PileUpJetIDdiscriminator"," PileUpJetIDdiscriminator", 90, -2., 1.);
 
  // use label of input to create label for output
  outputJets_ = inputJets_.label();
  outputMETs_ = inputMETs_.label(); 

  // register products
  produces<std::vector<pat::Jet> >(outputJets_);
  produces<std::vector<pat::MET> >(outputMETs_); 
}

void
PileUpJetIDjetsProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<edm::View<pat::Jet> > jets;
  evt.getByLabel(inputJets_, jets);
  edm::Handle<std::vector<pat::MET> > mets;
  evt.getByLabel(inputMETs_, mets);

  std::auto_ptr<std::vector<pat::Jet> > pJets(new std::vector<pat::Jet>);
  std::auto_ptr<std::vector<pat::MET> > pMETs(new std::vector<pat::MET>);

  double dPx = 0.;
  double dPy = 0.;
  double dSumEt = 0.;

  edm::Handle<edm::ValueMap<float> > puJetIdMVA;
  evt.getByLabel(discriminator_, puJetIdMVA);

  edm::Handle<edm::ValueMap<int> > puJetIdFlag;
  evt.getByLabel(flag_, puJetIdFlag);

  for ( unsigned int i=0; i<jets->size(); ++i ) {
    const pat::Jet & patjet = jets->at(i);
    float mva   = (*puJetIdMVA)[jets->refAt(i)];
    int  idflag = (*puJetIdFlag)[jets->refAt(i)];
    PileUpJetIDdiscriminator_->Fill(mva);

    if (wp_.label()=="Loose"){
      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose )) {
	pJets->push_back(patjet);
	continue;
      }
    }

    if (wp_.label()=="Medium"){
      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kMedium )) {
	pJets->push_back(patjet);
	continue;
      }
    }
    
    if (wp_.label()=="Tight"){
      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kTight )) {
	pJets->push_back(patjet);
	continue;
      }
    }
    dPx += (jets->at(i)).px();
    dPy += (jets->at(i)).py();
    dSumEt += (jets->at(i)).et();

  }

  // scale MET accordingly
  pat::MET met = *(mets->begin());
  double newMETPx = met.px() + dPx;
  double newMETPy = met.py() + dPy;
  pat::MET newMET(reco::MET(met.sumEt()+dSumEt, reco::MET::LorentzVector(newMETPx, newMETPy, 0, sqrt(newMETPx*newMETPx+newMETPy*newMETPy)), reco::MET::Point(0,0,0)));
  pMETs->push_back( newMET );

  evt.put(pJets, outputJets_);
  evt.put(pMETs, outputMETs_);
}
