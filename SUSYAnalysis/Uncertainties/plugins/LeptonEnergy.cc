#include <algorithm>

#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "SUSYAnalysis/Uncertainties/plugins/LeptonEnergy.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "FWCore/Framework/interface/MakerMacros.h"

LeptonEnergy::LeptonEnergy(const edm::ParameterSet& cfg):
  inputMuons_              (cfg.getParameter<edm::InputTag>("inputMuons"             )),
  inputElectrons_          (cfg.getParameter<edm::InputTag>("inputElectrons"         )),
  scaleType_               (cfg.getParameter<std::string>  ("scaleType"              )),  
  scaleFactor_             (cfg.getParameter<double>       ("scaleFactor"            )),
  leptonPTThresholdForMET_ (cfg.getParameter<double>       ("leptonPTThresholdForMET"))

{
  // use label of input to create label for output
  outputMuons_     = inputMuons_.label();
  outputElectrons_ = inputElectrons_.label();
  outputMETs_      = inputMETs_.label(); 

  // register products
  produces<std::vector<pat::Muon> >     (outputMuons_);
  produces<std::vector<pat::Electron> > (outputElectrons_);
  produces<std::vector<pat::MET> >      (outputMETs_); 
}

void
LeptonEnergy::beginJob()
{ 		
}

void
LeptonEnergy::produce(edm::Event& event, const edm::EventSetup& setup)
{
//   // access jets
//   edm::Handle<std::vector<pat::Jet> > jets;
//   event.getByLabel(inputJets_, jets);
//   // access MET
//   edm::Handle<std::vector<pat::MET> > mets;
//   event.getByLabel(inputMETs_, mets);
  
//   // create two new collections for jets and MET
//   std::auto_ptr<std::vector<pat::Jet> > pJets(new std::vector<pat::Jet>);
//   std::auto_ptr<std::vector<pat::MET> > pMETs(new std::vector<pat::MET>);

//   // loop ans rescale jets
//   double dPx = 0., dPy = 0., dSumEt = 0.;
//   for(std::vector<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet){
//     pat::Jet scaledJet = *jet;
    
//     if(scaleType_=="abs"){
//       //scaledJet.scaleEnergy( scaleFactor_ );
//       scaleLeptonEnergy( scaledJet, scaleFactor_ );
//       if (abs(scaledJet.partonFlavour()) == 5) {
//         //scaledJet.scaleEnergy( scaleFactorB_ );
// 	scaleLeptonEnergy( scaledJet, scaleFactorB_ );
//       }
//       //scaledJet.scaleEnergy( resolutionFactor(scaledJet) );
//       scaleLeptonEnergy( scaledJet, resolutionFactor(scaledJet) );
//     }
//     if(scaleType_=="rel"){
//       //scaledJet.scaleEnergy( 1+(fabs(scaledJet.eta())*(scaleFactor_-1. )));    
//       scaleLeptonEnergy( scaledJet, 1+(fabs(scaledJet.eta())*(scaleFactor_-1. )) );
//       //scaledJet.scaleEnergy( resolutionFactor(scaledJet) );
//       scaleLeptonEnergy( scaledJet, resolutionFactor(scaledJet) );
//     }    
//     if(scaleType_.substr(0, scaleType_.find(':'))=="jes" || 
//        scaleType_.substr(0, scaleType_.find(':'))=="top" ){
//       // handle to the jet corrector parameters collection
//       edm::ESHandle<JetCorrectorParametersCollection> jetCorrParameters;
//       // get the jet corrector parameters collection from the global tag
//       setup.get<JetCorrectionsRecord>().get(payload_, jetCorrParameters);
//       // get the uncertainty parameters from the collection
//       JetCorrectorParameters const & param = (*jetCorrParameters)["Uncertainty"];
//       // instantiate the jec uncertainty object
//       JetCorrectionUncertainty* deltaJEC = new JetCorrectionUncertainty(param);
//       deltaJEC->setJetEta(jet->eta()); deltaJEC->setJetPt(jet->pt()); 

//       // additional JES uncertainty from Top group
//       // sum of squared shifts of jet energy to be applied
//       float topShift2 = 0.;
//       if(scaleType_.substr(0, scaleType_.find(':'))=="top"){
// 	// add the recommended PU correction on top  
// 	float pileUp = 0.352/jet->pt()/jet->pt();
// 	// add bjet uncertainty on top
// 	float bjet = 0.;
// 	if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
// 	  bjet = ((50<jet->pt() && jet->pt()<200) && fabs(jet->eta())<2.0) ? 0.02 : 0.03;
// 	// add flat uncertainty for release differences and calibration changes (configurable)
// 	float sw = (1.-scaleFactor_);
// 	// add top systematics to JES uncertainty
// 	topShift2 += pileUp*pileUp + bjet*bjet + sw*sw;
//       }

//       // scale jet energy
//       if(scaleType_.substr(scaleType_.find(':')+1)=="up"){
// 	// JetMET JES uncertainty
// 	float jetMet = deltaJEC->getUncertainty(true);
// 	//scaledJet.scaleEnergy( 1+std::sqrt(jetMet*jetMet + topShift2) );
// 	scaleLeptonEnergy( scaledJet, 1+std::sqrt(jetMet*jetMet + topShift2) );
//       }
//       else if(scaleType_.substr(scaleType_.find(':')+1)=="down"){
// 	// JetMET JES uncertainty
// 	float jetMet = deltaJEC->getUncertainty(false);
// 	//scaledJet.scaleEnergy( 1-std::sqrt(jetMet*jetMet + topShift2) );
// 	scaleLeptonEnergy( scaledJet, 1-std::sqrt(jetMet*jetMet + topShift2) );
//       }

//       //scaledJet.scaleEnergy( resolutionFactor(scaledJet) );
//       scaleLeptonEnergy( scaledJet, resolutionFactor(scaledJet) );
//       delete deltaJEC;
//     }
//     pJets->push_back( scaledJet );
    
//     // consider jet scale shift only if the raw jet pt is above the thresholds given in the module definition
//     if(jet->correctedJet("Uncorrected").pt() > jetPTThresholdForMET_)
//       {
// 	dPx    += scaledJet.px() - jet->px();
// 	dPy    += scaledJet.py() - jet->py();
// 	dSumEt += scaledJet.et() - jet->et();
//       }
//   }
//   // scale MET accordingly
//   pat::MET met = *(mets->begin());
//   double scaledMETPx = met.px() - dPx;
//   double scaledMETPy = met.py() - dPy;
//   pat::MET scaledMET(reco::MET(met.sumEt()+dSumEt, reco::MET::LorentzVector(scaledMETPx, scaledMETPy, 0, sqrt(scaledMETPx*scaledMETPx+scaledMETPy*scaledMETPy)), reco::MET::Point(0,0,0)));
//   pMETs->push_back( scaledMET );
//   event.put(pJets, outputJets_);
//   event.put(pMETs, outputMETs_);
}

DEFINE_FWK_MODULE( LeptonEnergy );
