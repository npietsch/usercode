#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "SUSYAnalysis/Uncertainties/plugins/LeptonEnergy.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


LeptonEnergy::LeptonEnergy(const edm::ParameterSet& cfg):
  inputMuons_              (cfg.getParameter<edm::InputTag>("inputMuons"             )),
  inputElectrons_          (cfg.getParameter<edm::InputTag>("inputElectrons"         )),
  inputMETs_               (cfg.getParameter<edm::InputTag>("inputMETs"              )),
  scaleFactorMu_           (cfg.getParameter<double>       ("scaleFactorMu"          )),
  scaleFactorEl_           (cfg.getParameter<double>       ("scaleFactorEl"          )),
  leptonPTThresholdForMET_ (cfg.getParameter<double>       ("leptonPTThresholdForMET"))

{
  // register products
  //produces<std::vector<pat::Muon> >     ("scaledMuons");
  //produces<std::vector<pat::Electron> > ("scaledElectrons");
  produces<std::vector<pat::MET> >      ("scaledMETsMu");
  produces<std::vector<pat::MET> >      ("scaledMETsEl");
}

void
LeptonEnergy::beginJob()
{ 		
}

void
LeptonEnergy::produce(edm::Event& event, const edm::EventSetup& setup)
{

  // access muons
  edm::Handle<std::vector<pat::Muon> > muons;
  event.getByLabel(inputMuons_, muons);
  // access electrons
  edm::Handle<std::vector<pat::Electron> > electrons;
  event.getByLabel(inputElectrons_, electrons);
  // access MET
  edm::Handle<std::vector<pat::MET> > mets;
  event.getByLabel(inputMETs_, mets);
  
  // create new collections for lepton and MET
  //std::auto_ptr<std::vector<pat::Muon> > pMuons(new std::vector<pat::Muon>);
  //std::auto_ptr<std::vector<pat::Electron> > pElectrons(new std::vector<pat::Electron>);
  std::auto_ptr<std::vector<pat::MET> > pMETsMu(new std::vector<pat::MET>);
  std::auto_ptr<std::vector<pat::MET> > pMETsEl(new std::vector<pat::MET>);


  pat::MET met = *(mets->begin());

  // scale muon energy
  double dPxMu=0;
  double dPyMu=0;
  double dSumEtMu=0;

  for(std::vector<pat::Muon>::const_iterator muon = muons->begin(); muon != muons->end(); ++muon)
    {      
      //pat::Muon scaledMuon = *muon;
      //pMuons->push_back( scaledMuon ); 

      if(muon->pt() > leptonPTThresholdForMET_)
	{
	  dPxMu    += muon->px()*scaleFactorMu_ - muon->px();
	  dPyMu    += muon->py()*scaleFactorMu_ - muon->py();
	  dSumEtMu += muon->et()*scaleFactorMu_ - muon->et() ;
	}
    }
  
  // scale electron energy
  double dPxEl=0;
  double dPyEl=0;
  double dSumEtEl=0;
  
  for(std::vector<pat::Electron>::const_iterator electron = electrons->begin(); electron != electrons->end(); ++electron)
    {
      //pat::Electron scaledElectron = *electron;
      //pElectrons->push_back( scaledElectron ); 

      if(electron->pt() > leptonPTThresholdForMET_)
	{
	  dPxEl    += electron->px()*scaleFactorEl_ - electron->px();
	  dPyEl    += electron->py()*scaleFactorEl_ - electron->py();
	  dSumEtEl += electron->et()*scaleFactorEl_ - electron->et() ;
	}
    }

  // scale MET
  double scaledMETPxMu = met.px() - dPxMu;
  double scaledMETPyMu = met.py() - dPyMu;
  double scaledMETEtMu = met.sumEt()+dSumEtMu;

  pat::MET scaledMETMu(reco::MET(scaledMETEtMu, reco::MET::LorentzVector(scaledMETPxMu, scaledMETPyMu, 0, sqrt(scaledMETPxMu*scaledMETPxMu+scaledMETPyMu*scaledMETPyMu)), reco::MET::Point(0,0,0)));
  pMETsMu->push_back( scaledMETMu ); 

  double scaledMETPxEl = met.px() - dPxEl;
  double scaledMETPyEl = met.py() - dPyEl;
  double scaledMETEtEl = met.sumEt()+dSumEtEl;

  pat::MET scaledMETEl(reco::MET(scaledMETEtEl, reco::MET::LorentzVector(scaledMETPxEl, scaledMETPyEl, 0, sqrt(scaledMETPxEl*scaledMETPxEl+scaledMETPyEl*scaledMETPyEl)), reco::MET::Point(0,0,0)));
  pMETsEl->push_back( scaledMETEl ); 

  // produce new lepton and MET collections
  //event.put(pElectrons, "scaledElectrons");
  //event.put(pMuons, "scaledMuons");
  event.put(pMETsMu,"scaledMETsMu");
  event.put(pMETsEl,"scaledMETsEl");

}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( LeptonEnergy );
