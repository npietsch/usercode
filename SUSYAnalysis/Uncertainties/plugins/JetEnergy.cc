#include <algorithm>

#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "SUSYAnalysis/Uncertainties/plugins/JetEnergy.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

JetEnergy::JetEnergy(const edm::ParameterSet& cfg):
  inputJets_           (cfg.getParameter<edm::InputTag>        ("inputJets"           )),
  inputMETs_           (cfg.getParameter<edm::InputTag>        ("inputMETs"           )),
  payload_             (cfg.getParameter<std::string>          ("payload"             )),  
  scaleType_           (cfg.getParameter<std::string>          ("scaleType"           )),  
  scaleFactor_         (cfg.getParameter<double>               ("scaleFactor"         )),
  scaleFactorB_        (cfg.getParameter<double>               ("scaleFactorB"        )),
  resolutionFactor_    (cfg.getParameter<std::vector<double> > ("resolutionFactors"   )),
  resolutionRanges_    (cfg.getParameter<std::vector<double> > ("resolutionEtaRanges" )),
  jetPTThresholdForMET_(cfg.getParameter<double>               ("jetPTThresholdForMET")),
  jetEMLimitForMET_    (cfg.getParameter<double>               ("jetEMLimitForMET"    ))
{
  // define allowed scale types
  allowedTypes_.push_back(std::string("abs"     ));
  allowedTypes_.push_back(std::string("rel"     ));
  allowedTypes_.push_back(std::string("jes:up"  ));
  allowedTypes_.push_back(std::string("jes:down"));
  allowedTypes_.push_back(std::string("top:up"  ));
  allowedTypes_.push_back(std::string("top:down"));

  //---------------------------------------------------------------------------------------------------------------
  // scale types:
  //
  // - _abs_ (normal scale factor)
  // - _rel_ (a scale factor proportional in eta)
  // - _jes_ (uncertainty UP and DOWN scaling according to the estimated JES uncertainties as derived from JetMET
  // - _top_
  //---------------------------------------------------------------------------------------------------------------

  // use label of input to create label for output
  outputJets_ = inputJets_.label();
  outputMETs_ = inputMETs_.label(); 

  // register products
  produces<std::vector<pat::Jet> >(outputJets_);
  produces<std::vector<pat::MET> >(outputMETs_); 
}

void
JetEnergy::beginJob()
{ 
  // check if scaleType is ok
  if(std::find(allowedTypes_.begin(), allowedTypes_.end(), scaleType_)==allowedTypes_.end()){
    edm::LogError msg("JetEnergy"); 
    msg << "Unknown scaleType: " << scaleType_ << " allowed types are: \n";
    for(std::vector<std::string>::const_iterator type=allowedTypes_.begin(); type!=allowedTypes_.end(); ++type){
      msg << *type << "\n";
    }
    msg << "Please modify your configuration accordingly \n";
    throw cms::Exception("Configuration Error");
  }		
}

void
JetEnergy::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // access jets
  edm::Handle<std::vector<pat::Jet> > jets;
  event.getByLabel(inputJets_, jets);
  // access MET
  edm::Handle<std::vector<pat::MET> > mets;
  event.getByLabel(inputMETs_, mets);
  
  // create two new collections for jets and MET
  std::auto_ptr<std::vector<pat::Jet> > pJets(new std::vector<pat::Jet>);
  std::auto_ptr<std::vector<pat::MET> > pMETs(new std::vector<pat::MET>);

  //-----------------------------
  // scale jet energy
  //-----------------------------

  double dPx = 0., dPy = 0., dSumEt = 0., METCorr2 = 0.;
  
  // loop over jets
  for(std::vector<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet)
    {
      pat::Jet scaledJet = *jet;
 
      // if absolute scale factor 
      if(scaleType_=="abs")
	{
	  scaleJetEnergy( scaledJet, scaleFactor_ );
	  // This seems to be a factor for b-jets applied in addition
	  if (abs(scaledJet.partonFlavour()) == 5)
	    {
	      scaleJetEnergy( scaledJet, scaleFactorB_ );
	    }
	  // scale jet energy by resolution factor
	  scaleJetEnergy( scaledJet, resolutionFactor(scaledJet) );
	}
      
      // if eta dependent scale factor
      if(scaleType_=="rel")
	{
	  // scale factor proportional to eta
	  scaleJetEnergy( scaledJet, 1+(fabs(scaledJet.eta())*(scaleFactor_-1. )) );
	  // scale jet energy by resolution factor
	  scaleJetEnergy( scaledJet, resolutionFactor(scaledJet) );
	}
  
      // if jes:up, jes:down, top:up or top:down
      if(scaleType_.substr(0, scaleType_.find(':'))=="jes" || scaleType_.substr(0, scaleType_.find(':'))=="top" )
	{
	  // -------------------- has to be looked through --------------------
	  
	  // handle to the jet corrector parameters collection
	  edm::ESHandle<JetCorrectorParametersCollection> jetCorrParameters;
	  // get the jet corrector parameters collection from the global tag
	  setup.get<JetCorrectionsRecord>().get(payload_, jetCorrParameters);
	  // get the uncertainty parameters from the collection
	  JetCorrectorParameters const & param = (*jetCorrParameters)["Uncertainty"];
	  // instantiate the jec uncertainty object
	  JetCorrectionUncertainty* deltaJEC = new JetCorrectionUncertainty(param);
	  deltaJEC->setJetEta(jet->eta()); deltaJEC->setJetPt(jet->pt()); 
	  
	  // --------------------------------------------------------------------
	  
	  // additional JES uncertainty from Top group; sum of squared shifts of jet energy to be applied
	  float topShift2 = 0.;

	  // if top:up or top:down
	  if(scaleType_.substr(0, scaleType_.find(':'))=="top")
	    {
	      // add the recommended PU correction on top 
	      float pileUp = 0.352/jet->pt()/jet->pt(); // <- ??
	      // add bjet uncertainty on top
	      float bjet = 0.;
	      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
		{
		  bjet = ((50<jet->pt() && jet->pt()<200) && fabs(jet->eta())<2.0) ? 0.02 : 0.03;
		}
	      // add flat uncertainty for release differences and calibration changes (configurable)
	      float sw = (1.-scaleFactor_);
	      // add top systematics to JES uncertainty
	      topShift2 += pileUp*pileUp + bjet*bjet + sw*sw;
	    }
	  
	  // scale jet energy
	  if(scaleType_.substr(scaleType_.find(':')+1)=="up"){
	    // JetMET JES uncertainty
	    float jetMet = deltaJEC->getUncertainty(true);
	    scaleJetEnergy(scaledJet, 1+std::sqrt(jetMet*jetMet+topShift2)); // topShift2=0 when not using scale type top
	  }
	  else if(scaleType_.substr(scaleType_.find(':')+1)=="down"){
	    // JetMET JES uncertainty
	    float jetMet = deltaJEC->getUncertainty(false);
	    scaleJetEnergy(scaledJet, 1-std::sqrt(jetMet*jetMet+topShift2)); // topShift2=0 when not using scale type top 
	  }
	  // scale jet energy by resolution factor
	  scaleJetEnergy(scaledJet,resolutionFactor(scaledJet));
	  delete deltaJEC;
	}
      // push back jet with rescaled energy
      pJets->push_back(scaledJet);
      
      // consider jet scale shift only if the raw jet pt and emf  !!!!!!!!!!!!!!!
      // is above the thresholds given in the module definition   !!!!!!!!!!!!!!!
      if(jet->correctedJet("Uncorrected").pt() > jetPTThresholdForMET_ && jet->emEnergyFraction() < jetEMLimitForMET_)
	{
	  dPx    += scaledJet.px() - jet->px();
	  dPy    += scaledJet.py() - jet->py();
	  //dSumEt += scaledJet.et() - jet->et();
	}
    }
      
  //-----------------------------
  // scale MET accordingly
  //-----------------------------

  pat::MET met = *(mets->begin());

  double scaledMETPx = met.px() - dPx;
  double scaledMETPy = met.py() - dPy;
  dSumEt = sqrt( scaledMETPx* scaledMETPx + scaledMETPy* scaledMETPy);

  // If you are using raw pfmet, you could use, as the raw jet uncertainty, the data/MC residual JES in quadrature with
  // the official JES uncertainty (https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription)

  pat::MET scaledMET(reco::MET(met.sumEt()+dSumEt, reco::MET::LorentzVector(scaledMETPx, scaledMETPy, 0, sqrt(scaledMETPx*scaledMETPx+scaledMETPy*scaledMETPy)), reco::MET::Point(0,0,0)));
  
  // push back rescaled MET
  pMETs->push_back( scaledMET );
  
  // write collections with scaled jets and MET to the event
  event.put(pJets, outputJets_);
  event.put(pMETs, outputMETs_);
}


// -------------------- has to be looked through --------------------

double
JetEnergy::resolutionFactor(const pat::Jet& jet)
{
  if(!jet.genJet()) { return 1.; }
  // check if vectors are filled properly
  if((2*resolutionFactor_.size())!=resolutionRanges_.size()){
    // eta range==infinity
    if(resolutionFactor_.size()==resolutionRanges_.size()&&resolutionRanges_.size()==1&&resolutionRanges_[0]==-1.){
      resolutionRanges_[0]=0;
      resolutionRanges_.push_back(-1.);
    }
    // others
    else{
      edm::LogError msg("JetEnergyResolution");
      msg << "\n resolutionEtaRanges or resolutionFactors in module JetEnergy not filled properly.\n";
      msg << "\n resolutionEtaRanges needs a min and max value for each entry in resolutionFactors.\n";
      throw cms::Exception("invalidVectorFilling");
    }
  }
  // calculate eta dependend JER factor
  double modifiedResolution = 1.;
  for(unsigned int numberOfJERvariation=0; numberOfJERvariation<resolutionFactor_.size(); ++numberOfJERvariation){
    int etaMin = 2*numberOfJERvariation;
    int etaMax = etaMin+1;
    if(std::abs(jet.eta())>=resolutionRanges_[etaMin]&&(std::abs(jet.eta())<resolutionRanges_[etaMax]||resolutionRanges_[etaMax]==-1.)){
      modifiedResolution*=resolutionFactor_[numberOfJERvariation];
      // take care of negative scale factors 
      if(resolutionFactor_[numberOfJERvariation]<0){
	edm::LogError msg("JetEnergyResolution");
	msg << "\n chosen scale factor " << resolutionFactor_[numberOfJERvariation] << " is not valid, must be positive.\n";
	throw cms::Exception("negJERscaleFactors");
      }
    }
  }
  // calculate pt smearing factor
  double factor = 1. + (modifiedResolution-1.)*(jet.pt() - jet.genJet()->pt())/jet.pt();
  return (factor<0 ? 0. : factor);
}

// --------------------------------------------------------------------

void
JetEnergy::scaleJetEnergy(pat::Jet& jet, double factor)
{
  jet.scaleEnergy( factor );

  if(jet.isPFJet()){
    pat::PFSpecific specificPF = jet.pfSpecific();
    specificPF.mChargedHadronEnergy = factor * specificPF.mChargedHadronEnergy;
    specificPF.mNeutralHadronEnergy = factor * specificPF.mNeutralHadronEnergy;
    specificPF.mPhotonEnergy        = factor * specificPF.mPhotonEnergy       ;
    specificPF.mElectronEnergy      = factor * specificPF.mElectronEnergy     ;
    specificPF.mMuonEnergy          = factor * specificPF.mMuonEnergy         ;
    specificPF.mHFHadronEnergy      = factor * specificPF.mHFHadronEnergy     ;
    specificPF.mHFEMEnergy          = factor * specificPF.mHFEMEnergy         ;
    specificPF.mChargedEmEnergy     = factor * specificPF.mChargedEmEnergy    ;
    specificPF.mChargedMuEnergy     = factor * specificPF.mChargedMuEnergy    ;
    specificPF.mNeutralEmEnergy     = factor * specificPF.mNeutralEmEnergy    ;
    jet.setPFSpecific(specificPF);
  }
  else if(jet.isCaloJet() || jet.isJPTJet()){
    pat::CaloSpecific specificCalo = jet.caloSpecific();
    specificCalo.mMaxEInEmTowers         = factor * specificCalo.mMaxEInEmTowers        ;
    specificCalo.mMaxEInHadTowers        = factor * specificCalo.mMaxEInHadTowers       ;
    specificCalo.mHadEnergyInHO          = factor * specificCalo.mHadEnergyInHO         ;
    specificCalo.mHadEnergyInHB          = factor * specificCalo.mHadEnergyInHB         ;
    specificCalo.mHadEnergyInHF          = factor * specificCalo.mHadEnergyInHF         ;
    specificCalo.mHadEnergyInHE          = factor * specificCalo.mHadEnergyInHE         ;
    specificCalo.mEmEnergyInEB           = factor * specificCalo.mEmEnergyInEB          ;
    specificCalo.mEmEnergyInEE           = factor * specificCalo.mEmEnergyInEE          ;
    specificCalo.mEmEnergyInHF           = factor * specificCalo.mEmEnergyInHF          ;
    specificCalo.mEnergyFractionHadronic = factor * specificCalo.mEnergyFractionHadronic;
    specificCalo.mEnergyFractionEm       = factor * specificCalo.mEnergyFractionEm      ;
    jet.setCaloSpecific(specificCalo);

    if(jet.isJPTJet()){
      pat::JPTSpecific specificJPT = jet.jptSpecific();
      specificJPT.mChargedHadronEnergy          = factor * specificJPT.mChargedHadronEnergy         ;
      specificJPT.mNeutralHadronEnergy          = factor * specificJPT.mNeutralHadronEnergy         ;
      specificJPT.mChargedEmEnergy              = factor * specificJPT.mChargedEmEnergy             ;
      specificJPT.mNeutralEmEnergy              = factor * specificJPT.mNeutralEmEnergy             ;
      specificJPT.mSumPtOfChargedWithEff        = factor * specificJPT.mSumPtOfChargedWithEff       ;
      specificJPT.mSumPtOfChargedWithoutEff     = factor * specificJPT.mSumPtOfChargedWithoutEff    ;
      specificJPT.mSumEnergyOfChargedWithEff    = factor * specificJPT.mSumEnergyOfChargedWithEff   ;
      specificJPT.mSumEnergyOfChargedWithoutEff = factor * specificJPT.mSumEnergyOfChargedWithoutEff;
      jet.setJPTSpecific(specificJPT);
    }
  }
}

DEFINE_FWK_MODULE( JetEnergy );
