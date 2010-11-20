#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "AnalysisDataFormats/TopObjects/interface/SUSYGenEvent.h"


/// default contructor
SUSYGenEvent::SUSYGenEvent(reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& initSubset)
{
  parts_ = decaySubset; 
  initPartons_= initSubset;
}

const reco::GenParticle*
SUSYGenEvent::candidate(int id, unsigned int parentId) const
{
  const reco::GenParticle* cand=0;
  const reco::GenParticleCollection & partsColl = *parts_;
  for( unsigned int i = 0; i < partsColl.size(); ++i ) {
    if( partsColl[i].pdgId()==id ){
      if(parentId==0?true:partsColl[i].mother()&&std::abs(partsColl[i].mother()->pdgId())==(int)parentId){
	cand = &partsColl[i];
      }
    }
  }
  return cand;
}

int
SUSYGenEvent::numberOfLeptons(bool fromWBoson) const
{
  int lep=0;
  const reco::GenParticleCollection& partsColl = *parts_;
  for(unsigned int i = 0; i < partsColl.size(); ++i) {
    if(reco::isLepton(partsColl[i])) {
      if(fromWBoson){
	if(partsColl[i].mother() &&  std::abs(partsColl[i].mother()->pdgId())==SUSYDecayID::WID){
	  ++lep;
	}
      }
      else{
	++lep;
      }
    }
  }
  return lep;
}

int
SUSYGenEvent::numberOfLeptons(Wdecay::LepType typeRestriction, bool fromWBoson) const
{
  int leptonType=-1;
  switch(typeRestriction){
    // resolve whether or not there is
    // any restriction in lepton types
  case Wdecay::Elec:
    leptonType=SUSYDecayID::elecID;
    break;
  case Wdecay::Muon:
    leptonType=SUSYDecayID::muonID;
    break;
  case Wdecay::Tau:
    leptonType=SUSYDecayID::tauID;
    break;
  case Wdecay::None:
    break;
  }
  int lep=0;
  const reco::GenParticleCollection & partsColl = *parts_;
  for(unsigned int i = 0; i < partsColl.size(); ++i) {
    if(fromWBoson){
      // restrict to particles originating from the W boson
      if( !(partsColl[i].mother() &&  std::abs(partsColl[i].mother()->pdgId())==SUSYDecayID::WID) ){
	continue;
      }
    }
    if(leptonType>0){
      // in case of lepton type restriction
      if( std::abs(partsColl[i].pdgId())==leptonType ){
	++lep;
      }
    }
    else{
      // take any lepton type into account else
      if( reco::isLepton(partsColl[i]) ){
	++lep;
      }
    }
  }
  return lep;
}

int
SUSYGenEvent::numberOfBQuarks(bool fromTopQuark) const
{
  int bq=0;
  const reco::GenParticleCollection & partsColl = *parts_;
  for (unsigned int i = 0; i < partsColl.size(); ++i) {
   //depend if radiation qqbar are included or not
    if(std::abs(partsColl[i].pdgId())==SUSYDecayID::bID){
      if(fromTopQuark){
	if(partsColl[i].mother() &&  std::abs(partsColl[i].mother()->pdgId())==SUSYDecayID::tID){
	  ++bq;
	}
      }
      else{
	++bq;
      }
    }
  }
  return bq;
}

std::vector<const reco::GenParticle*>
SUSYGenEvent::radiatedGluons(int pdgId) const{
  std::vector<const reco::GenParticle*> rads;
  for (reco::GenParticleCollection::const_iterator part = parts_->begin(); part < parts_->end(); ++part) {
    if ( part->mother() && part->mother()->pdgId()==pdgId ){
      if(part->pdgId()==SUSYDecayID::glueID){
	if( dynamic_cast<const reco::GenParticle*>( &(*part) ) == 0){
	  throw edm::Exception( edm::errors::InvalidReference, "Not a GenParticle" );
	}
      }
      rads.push_back( part->clone() );
    }
  }
  return rads;
}
