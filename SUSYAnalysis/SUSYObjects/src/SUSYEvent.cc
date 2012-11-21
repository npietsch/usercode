#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CommonTools/CandUtils/interface/pdgIdUtils.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"

/// default contructor
SUSYEvent::SUSYEvent(int test, std::vector<pat::Muon>& muons, std::vector<pat::Electron>& electrons, std::vector<pat::Jet>& jets, std::vector<pat::MET>& mets)
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
