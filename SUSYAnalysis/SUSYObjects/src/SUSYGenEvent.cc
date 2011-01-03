#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"


/// default contructor
SUSYGenEvent::SUSYGenEvent(int generation, reco::GenParticleRefProd& decaySubset, reco::GenParticleRefProd& initSubset, reco::GenParticleRefProd& initSparticles)
{
  generation_ = generation; 
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

// returns number of bottom-quarks from the decay of top, stop or bottom 
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
  if(abs(genParticle.pdgId())==1000001 ||
     abs(genParticle.pdgId())==1000002 ||
     abs(genParticle.pdgId())==1000003 ||
     abs(genParticle.pdgId())==1000004 ||
     abs(genParticle.pdgId())==2000001 ||
     abs(genParticle.pdgId())==2000002 ||
     abs(genParticle.pdgId())==2000003 ||
     abs(genParticle.pdgId())==2000004)
    {
      isSquark=true;
    }
  
  return isSquark;
}

// is stop
bool SUSYGenEvent::isStop(const reco::GenParticle & genParticle) const
{
  bool isStop=false;
  if(abs(genParticle.pdgId())==1000006 ||
     abs(genParticle.pdgId())==2000006)
    {
      isStop=true;
    }
  
  return isStop;
}

// is stop
bool SUSYGenEvent::isSbottom(const reco::GenParticle & genParticle) const
{
  bool isSbottom=false;
  if(abs(genParticle.pdgId())==1000005 ||
     abs(genParticle.pdgId())==2000005)
    {
      isSbottom=true;
    }
  
  return isSbottom;
}

// is chargino
bool SUSYGenEvent::isChargino(const reco::GenParticle & genParticle) const
{
  bool isChargino=false;
  if(abs(genParticle.pdgId())==1000024 ||
     abs(genParticle.pdgId())==1000037)
    {
      isChargino=true;
    }
  
  return isChargino;
}

// is neutralino
bool SUSYGenEvent::isNeutralino(const reco::GenParticle & genParticle) const
{
  bool isNeutralino=false;
  if(abs(genParticle.pdgId())==1000022 ||
     abs(genParticle.pdgId())==1000023 ||
     abs(genParticle.pdgId())==1000025 ||
     abs(genParticle.pdgId())==1000035)
    {
      isNeutralino=true;
    }
  
  return isNeutralino;
}

// is neutralino
bool SUSYGenEvent::isNeutralHiggs(const reco::GenParticle & genParticle) const
{
  bool isNeutralHiggs=false;
  if(abs(genParticle.pdgId())==25 ||
     abs(genParticle.pdgId())==35 ||
     abs(genParticle.pdgId())==36)
    {
      isNeutralHiggs=true;
    }

  return isNeutralHiggs;
 }

// is slepton
bool SUSYGenEvent::isSlepton(const reco::GenParticle & genParticle) const
{
  bool isSlepton=false;
  if(abs(genParticle.pdgId())==100011 ||
     abs(genParticle.pdgId())==100012 ||
     abs(genParticle.pdgId())==100013 ||
     abs(genParticle.pdgId())==100014 ||
     abs(genParticle.pdgId())==100015 ||
     abs(genParticle.pdgId())==100016 ||
     abs(genParticle.pdgId())==200011 ||
     abs(genParticle.pdgId())==200012 ||
     abs(genParticle.pdgId())==200013 ||
     abs(genParticle.pdgId())==200014 ||
     abs(genParticle.pdgId())==200015 ||
     abs(genParticle.pdgId())==200016)
    {
      isSlepton=true;
    }

  return isSlepton;
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

// create susy daughter
const reco::Candidate* SUSYGenEvent::createSdaughter(const reco::Candidate* mother) const
{
  const reco::Candidate* sdaughter=mother;
  for (int i=0; i<(int)mother->numberOfDaughters(); ++i)
    { 
      if(abs(mother->daughter(i)->pdgId())>1000000)
	{
	  sdaughter=mother->daughter(i);

	  if(abs(mother->daughter(i)->pdgId())>1000000 && abs(mother->daughter(i)->pdgId()) != abs(mother->pdgId()) )
	    {
	      sdaughter=mother->daughter(i);
	      break;
	    }
	}
    }
  return sdaughter;
}

// returns sparticle name
std::string SUSYGenEvent::sparticleName(const reco::Candidate* candidate) const
{
 
  reco::GenParticle* genParticle=new reco::GenParticle(candidate->threeCharge(),candidate->p4(), candidate->vertex(),candidate->pdgId(), candidate->status(), false );
  
  std::string sparticleName="none";

  if(isGluino(*genParticle) == true) sparticleName="gluino";
  else if(isSquark(*genParticle) == true) sparticleName="squark";
  else if(isStop(*genParticle)   == true) sparticleName="stop";
  else if(isSbottom(*genParticle)== true) sparticleName="sbottom";
  else if(isChargino(*genParticle)== true)sparticleName="chargino";
  else if(isNeutralino(*genParticle)== true)sparticleName="neutralino";
  else if(isSlepton(*genParticle)== true)sparticleName="slepton";
  else 
    {
      sparticleName ="other";
      //std::cout << "other genParticle->pdgId: " << genParticle->pdgId() << std::endl;
    }
  //std::cout << "SUSYGenEvent::sparticleName: " << sparticleName << std::endl;

  return sparticleName; 
}

// decay cascade
std::string SUSYGenEvent::decayCascade(int idx) const
{  
  std::string decayCascade="none";
  
  const reco::GenParticleCollection & partsColl = *parts_;
  for(int i=0; i<(int)partsColl.size(); ++i )
    {
      if(partsColl[i].numberOfMothers()==2 && abs(partsColl[i].pdgId())>1000000)
	{
	  //std::cout << "partsColl[i].pdgId(): " << partsColl[i].pdgId() << std::endl;
	  // 1st generation
	  const reco::Candidate* initialSparticle = partsColl[i].mother(0)->daughter(idx);
	  //std::cout << "initialSparticle>pdgId(): " << initialSparticle->pdgId() << std::endl;
	  decayCascade=sparticleName(initialSparticle);

	  // 2nd generation
	  if(generation_ < 2) break;
	  const reco::Candidate* daughter=createSdaughter(initialSparticle);
	  //std::cout << "daughter->pdgId(): " << daughter->pdgId() << std::endl;

 	  while(initialSparticle->pdgId() == daughter->pdgId())
 	    {
	      if(initialSparticle==daughter) break;

	      initialSparticle=daughter;
	      const reco::Candidate* newdaughter2=createSdaughter(daughter);
	      daughter=newdaughter2;
	    }
	  if(initialSparticle==daughter) break;
	  
	  decayCascade=decayCascade+"->"+sparticleName(daughter);

	  // 3rd generation
	  if(generation_ < 3) break;
	  const reco::Candidate* granddaughter=createSdaughter(daughter);
	  //std::cout << "granddaughter->pdgId(): " << granddaughter->pdgId() << std::endl;

 	  while(daughter->pdgId() == granddaughter->pdgId())
 	    {
	      if(daughter==granddaughter) break;

	      daughter=granddaughter;
	      const reco::Candidate* newdaughter3=createSdaughter(granddaughter);
	      granddaughter=newdaughter3;
	    }
	  if(daughter==granddaughter) break;
	  
	  decayCascade=decayCascade+"->"+sparticleName(granddaughter);

	  // fourth generation
	  if(generation_ < 4) break;
	  const reco::Candidate* greatgranddaughter=createSdaughter(granddaughter);
	  //std::cout << "greatgranddaughter->pdgId(): " << greatgranddaughter->pdgId() << std::endl;

 	  while (granddaughter->pdgId() == greatgranddaughter->pdgId())
 	    {
	      if(granddaughter==greatgranddaughter) break;

	      granddaughter=greatgranddaughter;
	      const reco::Candidate* newdaughter4=createSdaughter(greatgranddaughter);
	      greatgranddaughter=newdaughter4;
	    }
	  if(granddaughter==greatgranddaughter) break;
	  
	  decayCascade=decayCascade+"->"+sparticleName(greatgranddaughter);

	  // fifth generation
	  if(generation_ < 5) break;
	  const reco::Candidate*  grandgreatgreatgranddaughter=createSdaughter(greatgranddaughter);
	  //std::cout << " grandgreatgreatgranddaughter->pdgId(): " <<  grandgreatgreatgranddaughter->pdgId() << std::endl;

 	  while (greatgranddaughter->pdgId() ==  grandgreatgreatgranddaughter->pdgId())
 	    {
	      if(greatgranddaughter== grandgreatgreatgranddaughter) break;

	      greatgranddaughter= grandgreatgreatgranddaughter;
	      const reco::Candidate* newdaughter5=createSdaughter( grandgreatgreatgranddaughter);
	       grandgreatgreatgranddaughter=newdaughter5;
	    }
	  if(greatgranddaughter== grandgreatgreatgranddaughter) break;
	  
	  decayCascade=decayCascade+"->"+sparticleName( grandgreatgreatgranddaughter);

	  
	  break;
	}
    }
  //std::cout << "decayCascade: " << decayCascade  << std::endl;
  return decayCascade;
}

// decay cascadeA
std::string SUSYGenEvent::decayCascadeA() const
{
  return decayCascade(0);
}
// decay cascadeB
std::string SUSYGenEvent::decayCascadeB() const
{
  return decayCascade(1);
}
