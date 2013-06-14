#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/GenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/HerwigGenEvent.h"

#include "DataFormats/Common/interface/Wrapper.h"
#include "TString.h"

namespace {

  struct dictionary {
    SUSYGenEvent susygen;
    SUSYEvent susy;
    GenEvent gen;
    HerwigGenEvent herwiggen;
    edm::Wrapper<SUSYGenEvent> w_susygen;
    edm::Wrapper<SUSYEvent> w_susy;
    edm::Wrapper<GenEvent> w_gen;
    edm::Wrapper<HerwigGenEvent> w_herwiggen;
  };
}
