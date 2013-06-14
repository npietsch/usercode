#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/HerwigGenEvent.h"


/// default contructor
HerwigGenEvent::HerwigGenEvent(reco::GenParticleRefProd& genParticles)
{
  particles_ = genParticles;
}

// is gluino?
bool HerwigGenEvent::isGluino(const reco::GenParticle & genParticle) const
{
  bool gluino=false;
  if(genParticle.pdgId()==1000021 && genParticle.status() == 2)
    {
      gluino=true;
    }
  
  return gluino;
}

// is squark of first or second generation?
bool HerwigGenEvent::isSquark(const reco::Candidate* candidate) const
{
  bool squark=false;
  if(abs(candidate->pdgId())==1000001 ||
     abs(candidate->pdgId())==1000002 ||
     abs(candidate->pdgId())==1000003 ||
     abs(candidate->pdgId())==1000004 ||
     abs(candidate->pdgId())==2000001 ||
     abs(candidate->pdgId())==2000002 ||
     abs(candidate->pdgId())==2000003 ||
     abs(candidate->pdgId())==2000004)
    {
      squark=true;
    }
  
  return squark;
}

// gluinos
std::vector<unsigned int> HerwigGenEvent::GluinoIndices() const
{
  std::vector<unsigned int> gluinos;
  const reco::GenParticleCollection & partsColl = *particles_;

  for(unsigned int i = 0; i < partsColl.size(); ++i)
    {
      if(partsColl[i].pdgId()== 1000021 && partsColl[i].status()==2 && partsColl[i].numberOfDaughters()==3 )
	{
	  gluinos.push_back(i);
	}
    }
  return gluinos;
}

// number of gluinos
int HerwigGenEvent::nGluinos() const
{
  int ngluinos=0;
  //int ngluinos=GluinoIndices().size();

  return ngluinos;
}

// DecayA
std::string HerwigGenEvent::DecayA() const
{
  const reco::GenParticleCollection & partsColl = *particles_;
  std::vector<unsigned int> gluinos=GluinoIndices();
  std::string chain="Other";

  if(GluinoIndices().size()>0)
    {
      for(unsigned int gdx=0; gdx<partsColl[gluinos[0]].numberOfDaughters(); ++gdx)
	{
	  if(abs(partsColl[gluinos[0]].daughter(gdx)->pdgId()) == 1000022)
	    {
	      chain="Bino";
	    }
	}
    }
  
  return chain;
}

// DecayB
std::string HerwigGenEvent::DecayB() const
{
  const reco::GenParticleCollection & partsColl = *particles_;
  std::vector<unsigned int> gluinos=GluinoIndices();
  std::string chain="Other";

  if(GluinoIndices().size()>1)
    {
      for(unsigned int gdx=0; gdx<partsColl[gluinos[1]].numberOfDaughters(); ++gdx)
	{
	  if(abs(partsColl[gluinos[1]].daughter(gdx)->pdgId()) == 1000023 ||
	     abs(partsColl[gluinos[1]].daughter(gdx)->pdgId()) == 1000024  )
	    {
	      chain="Wino";
	    }
	}
    }
  
  return chain;
}


// is BinoBino
bool HerwigGenEvent::BinoBino() const
{
  bool binoBino=false;

  if(DecayA()=="Bino" && DecayB()=="Bino")
    {
      binoBino = true;
    }
  
  return binoBino;
}

// is BinoOther
bool HerwigGenEvent::BinoOther() const
{
  bool binoOther=false;

  if( (DecayA()=="Bino" && DecayB()=="Other") || (DecayA()=="Other" && DecayB()=="Bino") )
    {
      binoOther = true;
    }
  
  return binoOther;
}

// is BinoWino
bool HerwigGenEvent::BinoWino() const
{
  bool binoWino=false;

  if( (DecayA()=="Bino" && DecayB()=="Wino") || (DecayA()=="Wino" && DecayB()=="Bino") )
    {
      binoWino = true;
    }
  
  return binoWino;
}

// is WinoWino
bool HerwigGenEvent::WinoWino() const
{
  bool winoWino=false;

  if(DecayA()=="Wino" && DecayB()=="Wino")
    {
      winoWino = true;
    }
  
  return winoWino;
}

// is WinoOther
bool HerwigGenEvent::WinoOther() const
{
  bool winoOther=false;

  if( (DecayA()=="Wino" && DecayB()=="Other") || (DecayA()=="Other" && DecayB()=="Wino") )
    {
      winoOther = true;
    }
  
  return winoOther;
}

// is WinoOther
bool HerwigGenEvent::OtherOther() const
{
  bool otherOther=false;

  if( (DecayA()=="Other" && DecayB()=="Other"))
    {
      otherOther = true;
    }
  
  return otherOther;
}

// qqbarA
double HerwigGenEvent::qqbarA() const
{
  const reco::GenParticleCollection & partsColl = *particles_;
  std::vector<unsigned int> gluinos=GluinoIndices();
  double qqbarMass=0;
  math::XYZTLorentzVector P4;

  if(GluinoIndices().size()>0)
    {
      for(unsigned int gdx=0; gdx<partsColl[gluinos[0]].numberOfDaughters(); ++gdx)
	{
	  if(isSquark(partsColl[gluinos[0]].daughter(gdx)) == true)
	    {
	      std::cout << partsColl[gluinos[0]].daughter(gdx)->pdgId() << std::endl;
	      P4=P4+partsColl[gluinos[0]].daughter(gdx)->p4();
	    }
	}
      qqbarMass=P4.M();
    }
  
  return qqbarMass;
}

// qqbarB
double HerwigGenEvent::qqbarB() const
{
  const reco::GenParticleCollection & partsColl = *particles_;
  std::vector<unsigned int> gluinos=GluinoIndices();
  double qqbarMass=0;
  math::XYZTLorentzVector P4;

  if(GluinoIndices().size()>1)
    {
      for(unsigned int gdx=0; gdx<partsColl[gluinos[1]].numberOfDaughters(); ++gdx)
	{
	  if(isSquark(partsColl[gluinos[1]].daughter(gdx)) == true)
	    {
	      std::cout << partsColl[gluinos[1]].daughter(gdx)->pdgId() << std::endl;
	      P4=P4+partsColl[gluinos[1]].daughter(gdx)->p4();
	    }
	}
      qqbarMass=P4.M();
    }
  
  return qqbarMass;
}
