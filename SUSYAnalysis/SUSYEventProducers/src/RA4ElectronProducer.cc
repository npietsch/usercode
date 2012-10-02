#include <algorithm>
#include "SUSYAnalysis/SUSYEventProducers/interface/RA4ElectronProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/MakerMacros.h"


RA4ElectronProducer::RA4ElectronProducer(const edm::ParameterSet& cfg):
  inputElectrons_        (cfg.getParameter<edm::InputTag>("inputElectrons")),
  conversionsInputTag_   (cfg.getParameter<edm::InputTag>("conversionsInputTag")),
  beamSpotInputTag_      (cfg.getParameter<edm::InputTag>("beamSpotInputTag")),
  rhoIsoInputTag_        (cfg.getParameter<edm::InputTag>("rhoIsoInputTag")),
  primaryVertexInputTag_ (cfg.getParameter<edm::InputTag>("primaryVertexInputTag"))// ,
//   isoValInputTags_       (cfg.getParameter<std::vector<edm::InputTag> >("isoValInputTags"))


{
  edm::Service<TFileService> fs;

  // register products
  produces<std::vector<pat::Electron> >("RA4LooseElectrons");
  produces<std::vector<pat::Electron> >("RA4VetoElectrons");
  produces<std::vector<pat::Electron> >("RA4MediumElectrons");
  produces<std::vector<pat::Electron> >("RA4TightElectrons");
}

void
RA4ElectronProducer::beginJob()
{	
}

void
RA4ElectronProducer::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // create new jet collections
  std::auto_ptr<std::vector<pat::Electron> > ra4LooseElectrons(new std::vector<pat::Electron>);
  std::auto_ptr<std::vector<pat::Electron> > ra4VetoElectrons(new std::vector<pat::Electron>);
  std::auto_ptr<std::vector<pat::Electron> > ra4MediumElectrons(new std::vector<pat::Electron>);
  std::auto_ptr<std::vector<pat::Electron> > ra4TightElectrons(new std::vector<pat::Electron>);

  // handles
  edm::Handle<std::vector<pat::Electron> > electrons;
  event.getByLabel(inputElectrons_, electrons);

  edm::Handle<reco::ConversionCollection> conversions_h;
  event.getByLabel(conversionsInputTag_, conversions_h);

  edm::Handle<reco::BeamSpot> beamspot_h;
  event.getByLabel(beamSpotInputTag_, beamspot_h);

  edm::Handle<double> rhoIso_h;
  event.getByLabel(rhoIsoInputTag_, rhoIso_h);
  
  edm::Handle<reco::VertexCollection> vtxs;
  event.getByLabel(primaryVertexInputTag_, vtxs);

  const reco::BeamSpot &beamSpot = *(beamspot_h.product());

  // vertices

  // loop over jets
  for(std::vector<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron)
    {

      pat::Electron selectedElectron  = *electron;

      // kinematic variables
      bool isEB           = selectedElectron.isEB() ? true : false;
      float pt            = selectedElectron.pt();
      float eta           = selectedElectron.superCluster()->eta();
      
      // id variables
      float dEtaIn        = selectedElectron.deltaEtaSuperClusterTrackAtVtx();
      float dPhiIn        = selectedElectron.deltaPhiSuperClusterTrackAtVtx();
      float sigmaIEtaIEta = selectedElectron.sigmaIetaIeta();
      float hoe           = selectedElectron.hadronicOverEm();
      float ooemoop       = (1.0/selectedElectron.ecalEnergy() - selectedElectron.eSuperClusterOverP()/selectedElectron.ecalEnergy());
      
      // impact parameter variables
      float d0vtx         = 0.0;
      float dzvtx         = 0.0;
      if (vtxs->size() > 0)
	{
	  reco::VertexRef vtx(vtxs, 0);    
	  d0vtx = selectedElectron.gsfTrack()->dxy(vtx->position());
	  dzvtx = selectedElectron.gsfTrack()->dz(vtx->position());
	}
      else
	{
	  d0vtx = selectedElectron.gsfTrack()->dxy();
	  dzvtx = selectedElectron.gsfTrack()->dz();
	}
      
      double iso_ch = selectedElectron.chargedHadronIso();
      double iso_nh = selectedElectron.neutralHadronIso();
      double iso_em = selectedElectron.photonIso();
      
      // conversion rejection variables
      bool vtxFitConversion = ConversionTools::hasMatchedConversion((const reco::GsfElectron)selectedElectron, conversions_h, beamSpot.position());
      float mHits = selectedElectron.gsfTrack()->trackerExpectedHitsInner().numberOfHits();
      
      // rho for isolation
      double rho = *(rhoIso_h.product());
      
      bool veto   = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::VETO, isEB, pt, eta,
						dEtaIn, dPhiIn, sigmaIEtaIEta, hoe,
						ooemoop, d0vtx, dzvtx, iso_ch, iso_em, iso_nh, 
						vtxFitConversion, mHits, rho);
      bool loose  = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::LOOSE, isEB, pt, eta,
						dEtaIn, dPhiIn, sigmaIEtaIEta, hoe,
						ooemoop, d0vtx, dzvtx, iso_ch, iso_em, iso_nh, 
						vtxFitConversion, mHits, rho);
      bool medium = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::MEDIUM, isEB, pt, eta,
						dEtaIn, dPhiIn, sigmaIEtaIEta, hoe,
						ooemoop, d0vtx, dzvtx, iso_ch, iso_em, iso_nh, 
						vtxFitConversion, mHits, rho);
      bool tight  = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::TIGHT, isEB, pt, eta,
						dEtaIn, dPhiIn, sigmaIEtaIEta, hoe,
						ooemoop, d0vtx, dzvtx, iso_ch, iso_em, iso_nh, 
						vtxFitConversion, mHits, rho);
      
      if(veto == true)   ra4VetoElectrons->push_back(selectedElectron);
      if(loose == true)  ra4LooseElectrons->push_back(selectedElectron);
      if(medium == true) ra4MediumElectrons->push_back(selectedElectron);
      if(tight == true)  ra4TightElectrons->push_back(selectedElectron);	
    }

  event.put(ra4LooseElectrons,  "RA4LooseElectrons");
  event.put(ra4VetoElectrons,   "RA4VetoElectrons");
  event.put(ra4MediumElectrons, "RA4MediumElectrons");
  event.put(ra4TightElectrons,  "RA4TightElectrons");
}
