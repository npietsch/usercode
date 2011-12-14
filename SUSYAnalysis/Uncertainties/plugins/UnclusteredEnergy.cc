#include "SUSYAnalysis/Uncertainties/plugins/UnclusteredEnergy.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"

UnclusteredEnergy::UnclusteredEnergy(const edm::ParameterSet& cfg):
  inputJets_            (cfg.getParameter<edm::InputTag>("inputJets"           )),
  inputMETs_            (cfg.getParameter<edm::InputTag>("inputMETs"           )),
  scaleFactor_          (cfg.getParameter<double>       ("scaleFactor"         )),
  jetPTThresholdForMET_ (cfg.getParameter<double>       ("jetPTThresholdForMET")),
  maxJetEtaForMET_      (cfg.getParameter<double>       ("maxJetEtaForMET"     ))
{  

  // use label of input to create label for output
  outputMETs_ = inputMETs_.label(); 

  // register product
  produces<std::vector<pat::MET> >(outputMETs_); 
}


void
UnclusteredEnergy::beginJob()
{ 		
}


void
UnclusteredEnergy::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // get handels on input collections
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(inputJets_, jets);
  edm::Handle<std::vector<pat::MET> > mets;
  event.getByLabel(inputMETs_, mets);;  

  double dPx=0;
  double dPy=0;
  double dSumEt=0;

  for(std::vector<pat::Jet>::const_iterator jet = jets->begin(); jet != jets->end(); ++jet)
    {
    // consider jet scale shift only if the raw jet pt is below the thresholds given in the module definition
    if(jet->correctedJet("Uncorrected").pt() < jetPTThresholdForMET_ && jet->eta() < maxJetEtaForMET_ )
      {
	dPx    += jet->px()*scaleFactor_ - jet->px();
	dPy    += jet->py()*scaleFactor_ - jet->py();
	dSumEt += jet->et()*scaleFactor_ - jet->et() ;
      }
    }

  pat::MET met = *(mets->begin());
  double scaledMETPx = met.px() - dPx;
  double scaledMETPy = met.py() - dPy;
  double scaledMETEt = met.sumEt()+dSumEt;

  pat::MET scaledMET(reco::MET(scaledMETEt, reco::MET::LorentzVector(scaledMETPx, scaledMETPy, 0, sqrt(scaledMETPx*scaledMETPx+scaledMETPy*scaledMETPy)), reco::MET::Point(0,0,0)));
  
  std::auto_ptr<std::vector<pat::MET> > pMETs(new std::vector<pat::MET>);
  pMETs->push_back( scaledMET );  
  event.put(pMETs, outputMETs_);
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( UnclusteredEnergy );
