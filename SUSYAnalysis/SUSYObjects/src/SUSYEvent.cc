#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"

/// default contructor
SUSYEvent::SUSYEvent(int test, const std::vector<pat::Muon>& muons, const std::vector<pat::Electron>& electrons, const std::vector<pat::Jet>& jets, const std::vector<pat::MET>& mets)
{
  test_      = test;
  muons_     = muons;
  electrons_ = electrons;
  jets_      = jets;
  mets_      = mets;
}

int SUSYEvent::nMuons() const
{
  return muons_.size();
}

int SUSYEvent::nElectrons() const
{
  return electrons_.size();
}

int SUSYEvent::nJets() const
{
  return jets_.size();
}

double SUSYEvent::HT() const
{
  double HT=0;
  for(int idx=0; idx<(int)jets_.size(); ++idx)
    {
      HT=HT+jets_[idx].et();
    }
  return HT;
}

double SUSYEvent::MET() const
{
  return mets_[0].et();
}

double SUSYEvent::YMET() const
{
  double YMET= MET()/sqrt(HT());
  return YMET;
}

double SUSYEvent::Meff() const
{
  double Meff=0;
  for(int idx=0; idx<(int)muons_.size(); ++idx)
    {
      Meff=Meff+muons_[idx].et();
    }
  for(int idx=0; idx<(int)electrons_.size(); ++idx)
    {
      Meff=Meff+electrons_[idx].et();
    }
  Meff=Meff+HT();

  return Meff;
}

double SUSYEvent::HTOverMeff() const
{
  double HTOverMeff= HT()/Meff();
  return HTOverMeff;
}
