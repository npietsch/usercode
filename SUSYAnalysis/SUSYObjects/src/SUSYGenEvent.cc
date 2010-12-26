#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "AnalysisDataFormats/SUSYObjects/interface/SUSYGenEvent.h"


/// default contructor
SUSYGenEvent::SUSYGenEvent(reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& initSubset, reco::GenParticleRefProd& initSparticles)
{
  parts_ = decaySubset; 
  initPartons_= initSubset;
  initSparticles_= initSparticles;
}

// returns candidate
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

// returns number of all leptons
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

// has to be looked through
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

// returns number of bottom-quarks
int
SUSYGenEvent::numberOfBQuarks() const
{
  int bq=0;
  const reco::GenParticleCollection & partsColl = *parts_;
  for (unsigned int i = 0; i < partsColl.size(); ++i) {
    if(std::abs(partsColl[i].pdgId())==SUSYDecayID::bID &&
       (std::abs(partsColl[i].mother()->pdgId())==SUSYDecayID::tID ||
	std::abs(partsColl[i].mother()->pdgId())==1000005 || std::abs(partsColl[i].mother()->pdgId())==1000006 ||
	std::abs(partsColl[i].mother()->pdgId())==2000005 || std::abs(partsColl[i].mother()->pdgId())==2000006) )
      {
	++bq;
      }
  }
  return bq;
}

// has to be looked through
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

// is gluino
bool SUSYGenEvent::isGluino(const reco::GenParticle & genParticle) const
{
  bool isGluino=false;
  if(genParticle.pdgId()==1000021)
    {
      isGluino=true;
    }
  
  return isGluino;
}


// is squark of first or second generation
bool SUSYGenEvent::isSquark(const reco::GenParticle & genParticle) const
{
  bool isSquark=false;
  if(genParticle.pdgId()==1000001 ||
     genParticle.pdgId()==1000002 ||
     genParticle.pdgId()==1000003 ||
     genParticle.pdgId()==1000004 ||
     genParticle.pdgId()==2000001 ||
     genParticle.pdgId()==2000002 ||
     genParticle.pdgId()==2000003 ||
     genParticle.pdgId()==2000004)
    {
      isSquark=true;
    }
  
  return isSquark;
}

// is gluino decay
bool SUSYGenEvent::GluinoDecay() const
{
  bool gluinoDecay=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  if (isGluino(initSpartsColl[0])==true  || isGluino(initSpartsColl[1])==true) gluinoDecay=true;
  
  return gluinoDecay;
}

// is squark decay
bool SUSYGenEvent::SquarkDecay() const
{
  bool squarkDecay=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  if (isSquark(initSpartsColl[0])==true || isSquark(initSpartsColl[1])==true ) squarkDecay=true;
  
  return squarkDecay;
}

// is gluino-gluino decay
bool SUSYGenEvent::GluinoGluinoDecay() const
{
  bool gluinoGluinoDecay=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  if (isGluino(initSpartsColl[0])==true  && isGluino(initSpartsColl[1])==true) gluinoGluinoDecay=true;
  
  return gluinoGluinoDecay;
}

// is squark-squark decay
bool SUSYGenEvent::SquarkSquarkDecay() const
{
  bool squarkSquarkDecay=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  if (isSquark(initSpartsColl[0])==true  && isSquark(initSpartsColl[1])==true) squarkSquarkDecay=true;
  
  return squarkSquarkDecay;
}

// is gluino-squark decay
bool SUSYGenEvent::GluinoSquarkDecay() const
{
  bool gluinoSquarkDecay=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  if ( (isGluino(initSpartsColl[0])==true  && isSquark(initSpartsColl[1])==true) ||
       (isSquark(initSpartsColl[0])==true  && isGluino(initSpartsColl[1])==true) )
    {
      gluinoSquarkDecay=true;
    }
  
  return gluinoSquarkDecay;
}

// decay chain A
int SUSYGenEvent::decayChainA() const
{
  int initialSparticle=0;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  initialSparticle=initSpartsColl[0].pdgId();
    
  return initialSparticle;
}

// decay chain B
int SUSYGenEvent::decayChainB() const
{
  int initialSparticle=0;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  initialSparticle=initSpartsColl[1].pdgId();

  return initialSparticle;
}
