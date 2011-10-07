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

// is lepton
bool SUSYGenEvent::isLepton(const reco::GenParticle & genParticle) const
{
  bool lep=false;
  if(abs(genParticle.pdgId())==11 || abs(genParticle.pdgId())==13)
    {
      if(abs(genParticle.mother()->pdgId())==24 || abs(genParticle.mother()->pdgId())==23 ||
	 abs(genParticle.mother()->pdgId())==1000022 || abs(genParticle.mother()->pdgId())==1000023 ||
	 abs(genParticle.mother()->pdgId())==1000024 || abs(genParticle.mother()->pdgId())==1000025 ||
	 abs(genParticle.mother()->pdgId())==1000035 || abs(genParticle.mother()->pdgId())==1000037 ||
	 abs(genParticle.mother()->pdgId())==1000011 || abs(genParticle.mother()->pdgId())==1000012 ||
	 abs(genParticle.mother()->pdgId())==1000013 || abs(genParticle.mother()->pdgId())==1000014 ||
	 abs(genParticle.mother()->pdgId())==1000015 || abs(genParticle.mother()->pdgId())==1000016 ||
	 abs(genParticle.mother()->pdgId())==2000011 || abs(genParticle.mother()->pdgId())==2000012 ||
	 abs(genParticle.mother()->pdgId())==2000013 || abs(genParticle.mother()->pdgId())==2000014 ||
	 abs(genParticle.mother()->pdgId())==2000015 || abs(genParticle.mother()->pdgId())==2000016 ||
	 abs(genParticle.mother()->pdgId())==25 || abs(genParticle.mother()->pdgId())==35 ||
	 abs(genParticle.mother()->pdgId())==36 )
	{   
	  lep=true;
	}
    }
  return lep;
}

// returns number of leptons from the decay of W, Z
int
SUSYGenEvent::numberOfLeptons() const
{
  int lep=0;
  const reco::GenParticleCollection& partsColl = *parts_;
  for(unsigned int i = 0; i < partsColl.size(); ++i)
    {
      if(isLepton(partsColl[i])==true) ++lep;
    } 
  return lep;
}

// same sign di-lepton
bool SUSYGenEvent::SSignDiLepton() const
{
  int posCharge=0;
  int negCharge=0;
  bool sSDiLep=false;

  const reco::GenParticleCollection& partsColl = *parts_;

  for(unsigned int i = 0; i < partsColl.size(); ++i)
    {
      if(isLepton(partsColl[i])==true)
	{
	  if(partsColl[i].charge()>0) ++posCharge;
	  if(partsColl[i].charge()<0) ++negCharge;
	}
    } 
  if(posCharge>=2 || negCharge>=2) sSDiLep=true;

  return sSDiLep;
}

// opposite sign di-lepton
bool SUSYGenEvent::OSignDiLepton() const
{
  int posCharge=0;
  int negCharge=0;
  bool oSDiLep=false;

  const reco::GenParticleCollection& partsColl = *parts_;

  for(unsigned int i = 0; i < partsColl.size(); ++i)
    {
      if(isLepton(partsColl[i])==true)
	{
	  if(partsColl[i].charge()>0) ++posCharge;
	  if(partsColl[i].charge()<0) ++negCharge;
	}
    } 
  if(posCharge>=1 && negCharge>=1) oSDiLep=true;

  return oSDiLep;
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

// returns number of bottom-quarks from the decay of top, gluino, stop, sbottom or neutral Higgs
int
SUSYGenEvent::numberOfBQuarks() const
{
  int bq=0;
  const reco::GenParticleCollection & partsColl = *parts_;
  for (unsigned int i = 0; i < partsColl.size(); ++i) {
    if(std::abs(partsColl[i].pdgId())==5 &&
       (std::abs(partsColl[i].mother()->pdgId())==6 || std::abs(partsColl[i].mother()->pdgId())==1000021 ||
	std::abs(partsColl[i].mother()->pdgId())==1000005 || std::abs(partsColl[i].mother()->pdgId())==1000006 ||
	std::abs(partsColl[i].mother()->pdgId())==2000005 || std::abs(partsColl[i].mother()->pdgId())==2000006 ||
	std::abs(partsColl[i].mother()->pdgId())==25 || std::abs(partsColl[i].mother()->pdgId())==35 ||
	std::abs(partsColl[i].mother()->pdgId())==36 ) )
      {
	//std::cout << "mother of BQuark: " << partsColl[i].mother()->pdgId() << std::endl;
	++bq;
      }
  }
  return bq;
}

// returns number of bottom-quarks from the decay of top, gluino, stop, sbottom or neutral Higgs
int
SUSYGenEvent::numberOfTops() const
{
  int tq=0;
  const reco::GenParticleCollection & partsColl = *parts_;
  for (unsigned int i = 0; i < partsColl.size(); ++i) {
    if(std::abs(partsColl[i].pdgId())==6 &&
       (std::abs(partsColl[i].mother()->pdgId())==1000021 ||
	std::abs(partsColl[i].mother()->pdgId())==1000005 || std::abs(partsColl[i].mother()->pdgId())==1000006 ||
	std::abs(partsColl[i].mother()->pdgId())==2000005 || std::abs(partsColl[i].mother()->pdgId())==2000006 ||
	std::abs(partsColl[i].mother()->pdgId())==25 || std::abs(partsColl[i].mother()->pdgId())==35 ||
	std::abs(partsColl[i].mother()->pdgId())==36 ) )
      {
	//std::cout << "mother of BQuark: " << partsColl[i].mother()->pdgId() << std::endl;
	++tq;
      }
  }
  return tq;
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
  bool chk=false;
  if(genParticle.pdgId()==1000021)
    {
      chk=true;
    }
  
  return chk;
}

// is squark of first or second generation
bool SUSYGenEvent::isSquark(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000001 ||
     abs(genParticle.pdgId())==1000002 ||
     abs(genParticle.pdgId())==1000003 ||
     abs(genParticle.pdgId())==1000004 ||
     abs(genParticle.pdgId())==2000001 ||
     abs(genParticle.pdgId())==2000002 ||
     abs(genParticle.pdgId())==2000003 ||
     abs(genParticle.pdgId())==2000004)
    {
      chk=true;
    }
  
  return chk;
}

// is squark of first or second generation
bool SUSYGenEvent::isAntiSquark(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000001 ||
     abs(genParticle.pdgId())==1000002 ||
     abs(genParticle.pdgId())==1000003 ||
     abs(genParticle.pdgId())==1000004 ||
     abs(genParticle.pdgId())==2000001 ||
     abs(genParticle.pdgId())==2000002 ||
     abs(genParticle.pdgId())==2000003 ||
     abs(genParticle.pdgId())==2000004)
    {
      chk=true;
    }
  
  return chk;
}

// is stop
bool SUSYGenEvent::isStop(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000006 ||
     abs(genParticle.pdgId())==2000006)
    {
      chk=true;
    }
  
  return chk;
}

// is stop
bool SUSYGenEvent::isSbottom(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000005 ||
     abs(genParticle.pdgId())==2000005)
    {
      chk=true;
    }
  
  return chk;
}

// is chargino
bool SUSYGenEvent::isChargino(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000024 ||
     abs(genParticle.pdgId())==1000037)
    {
      chk=true;
    }
  
  return chk;
}

// is neutralino
bool SUSYGenEvent::isNeutralino(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000022 ||
     abs(genParticle.pdgId())==1000023 ||
     abs(genParticle.pdgId())==1000025 ||
     abs(genParticle.pdgId())==1000035)
    {
      chk=true;
    }
  
  return chk;
}

// is neutralino
bool SUSYGenEvent::isNeutralHiggs(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==25 ||
     abs(genParticle.pdgId())==35 ||
     abs(genParticle.pdgId())==36)
    {
      chk=true;
    }

  return chk;
 }

// is slepton
bool SUSYGenEvent::isSlepton(const reco::GenParticle & genParticle) const
{
  bool chk=false;
  if(abs(genParticle.pdgId())==1000011 ||
     abs(genParticle.pdgId())==1000012 ||
     abs(genParticle.pdgId())==1000013 ||
     abs(genParticle.pdgId())==1000014 ||
     abs(genParticle.pdgId())==1000015 ||
     abs(genParticle.pdgId())==1000016 ||
     abs(genParticle.pdgId())==2000011 ||
     abs(genParticle.pdgId())==2000012 ||
     abs(genParticle.pdgId())==2000013 ||
     abs(genParticle.pdgId())==2000014 ||
     abs(genParticle.pdgId())==2000015 ||
     abs(genParticle.pdgId())==2000016)
    {
      chk=true;
    }

  return chk;
}

// is gluino decay
bool SUSYGenEvent::GluinoDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool gluinoDecay=false;
  if (isGluino(initSpartsColl[0])==true  || isGluino(initSpartsColl[1])==true) gluinoDecay=true;
  return gluinoDecay;
}

// is squark decay
bool SUSYGenEvent::SquarkDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;
  
  bool squarkDecay=false;
  if (isSquark(initSpartsColl[0])==true || isSquark(initSpartsColl[1])==true ) squarkDecay=true;
  
  return squarkDecay;
}

// is gluino-gluino decay
bool SUSYGenEvent::GluinoGluinoDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;
  
  bool gluinoGluinoDecay=false;
  if (isGluino(initSpartsColl[0])==true  && isGluino(initSpartsColl[1])==true) gluinoGluinoDecay=true;
  return gluinoGluinoDecay;
}

// is squark-squark decay
bool SUSYGenEvent::SquarkSquarkDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  
  if (initSpartsColl.size() < 2) return false;

  bool squarkSquarkDecay=false;
  if (isSquark(initSpartsColl[0])==true  && isSquark(initSpartsColl[1])==true) squarkSquarkDecay=true;
  
//   std::cout << "------------------------------------" << std::endl;
//   std::cout <<  "initSpartsColl[0].pdgId(): " << initSpartsColl[0].pdgId() << std::endl;
//   std::cout <<  "initSpartsColl[0].threeCharge(): " << initSpartsColl[0].threeCharge() << std::endl;
//   std::cout <<  "initSpartsColl[1].pdgId(): " << initSpartsColl[1].pdgId() << std::endl;
//   std::cout <<  "initSpartsColl[1].threeCharge(): " << initSpartsColl[1].threeCharge() << std::endl;
//   std::cout << "------------------------------------" << std::endl;

  return squarkSquarkDecay;
}

// is same sign squark-squark decay
bool SUSYGenEvent::SSignSquarkSquarkDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;
  
  bool sSignSquarkSquarkDecay=false;
  if (SquarkSquarkDecay()==true && ((initSpartsColl[0].threeCharge())*(initSpartsColl[1].threeCharge())>0)) sSignSquarkSquarkDecay=true;
  return sSignSquarkSquarkDecay;
}

// is opposite sign squark-squark decay
bool SUSYGenEvent::OSignSquarkSquarkDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;
  
  bool oSignSquarkSquarkDecay=false;
  if (SquarkSquarkDecay()==true &&((initSpartsColl[0].threeCharge())*(initSpartsColl[1].threeCharge())<0)) oSignSquarkSquarkDecay=true;
  return oSignSquarkSquarkDecay;
}

// is gluino-squark decay
bool SUSYGenEvent::GluinoSquarkDecay() const
{
  bool gluinoSquarkDecay=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  if ( (isGluino(initSpartsColl[0])==true  && isSquark(initSpartsColl[1])==true) ||
       (isSquark(initSpartsColl[0])==true  && isGluino(initSpartsColl[1])==true) )
    {
      gluinoSquarkDecay=true;
    }
  
  return gluinoSquarkDecay;
}

bool SUSYGenEvent::ParticleAntiParticleDecay() const
{
  bool decayTrue=false;
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  long pdgProduct = (long) initSpartsColl[0].pdgId() * initSpartsColl[1].pdgId();

  if ( pdgProduct < 0  ) {
    decayTrue=true;
  }
  
  return decayTrue;
}

void SUSYGenEvent::GetParentPDGNos() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) {
    std::cout << "Two parents not found!" << std::endl;
    return;
  }

  std::cout << "Parent PDG IDs are: " << initSpartsColl[0].pdgId() << " " <<  initSpartsColl[1].pdgId()<< std::endl;
  return;
}


bool SUSYGenEvent::StopStopDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool decayTrue=false;
  if (isStop(initSpartsColl[0]) && isStop(initSpartsColl[1])) decayTrue=true;
  return decayTrue;
}
bool SUSYGenEvent::SbottomSbottomDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool decayTrue=false;
  if (isSbottom(initSpartsColl[0]) && isSbottom(initSpartsColl[1]) ) decayTrue=true;
  return decayTrue;
}
bool SUSYGenEvent::SleptonSleptonDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool decayTrue=false;
  if (isSlepton(initSpartsColl[0])  && isSlepton(initSpartsColl[1]) ) decayTrue=true;
  return decayTrue;
}
bool SUSYGenEvent::EWinoEWinoDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool decayTrue=false;
  if ( (isChargino(initSpartsColl[0]) || isNeutralino(initSpartsColl[0]))  && (isChargino(initSpartsColl[1]) || isNeutralino(initSpartsColl[1])) ) decayTrue=true;
  return decayTrue;
}

bool SUSYGenEvent::EWinoGluinoDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool decayTrue=false;
  if ( (isChargino(initSpartsColl[0]) || isNeutralino(initSpartsColl[0]))  && isGluino(initSpartsColl[1]) ) decayTrue=true;
  if ( (isChargino(initSpartsColl[1]) || isNeutralino(initSpartsColl[1]))  && isGluino(initSpartsColl[0]) ) decayTrue=true;
  return decayTrue;
}

bool SUSYGenEvent::EWinoSquarkDecay() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  bool decayTrue=false;
  if ( (isChargino(initSpartsColl[0]) || isNeutralino(initSpartsColl[0]))  && isSquark(initSpartsColl[1]) ) decayTrue=true;
  if ( (isChargino(initSpartsColl[1]) || isNeutralino(initSpartsColl[1]))  && isSquark(initSpartsColl[0]) ) decayTrue=true;
  return decayTrue;
}


// decay chain A
int SUSYGenEvent::decayChainA() const
{
  //std::cout << "(*initSpartsColl_)[0].pdgId(): " <<  (*initSparticles_)[0].pdgId() << std::endl;

  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;
  if (initSpartsColl.size() < 1) return false;

  int initialSparticle=initSpartsColl[0].pdgId();
    
  return initialSparticle;
}

// decay chain B
int SUSYGenEvent::decayChainB() const
{
  const reco::GenParticleCollection & initSpartsColl = *initSparticles_;

  if (initSpartsColl.size() < 2) return false;

  int initialSparticle = initSpartsColl[1].pdgId();

  return initialSparticle;
}

// x1-x2 ratio
double SUSYGenEvent::ratio() const
{
  double x1=0;
  double x2=0;
  double r=0;
  const reco::GenParticleCollection & initPartsColl = *initPartons_;

  x1=initPartsColl[0].pz();
  x2=initPartsColl[1].pz();

  //std::cout << "x1 :" << x1 << std::endl;
  //std::cout << "x2 :" << x2 << std::endl;

  if(abs(x1)>abs(x2) && (x2 != 0) ) r=abs(x1/x2);
  else if(abs(x2)>abs(x1) && (x1 != 0) ) r=abs(x2/x1);

  return r;
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
