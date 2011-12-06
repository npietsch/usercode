#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/GenEvent.h"

#include "DataFormats/Common/interface/Wrapper.h"
#include "TString.h"

namespace {

  struct dictionary {
    SUSYGenEvent susygen;
    SUSYEvent susy;
    GenEvent gen;
    edm::Wrapper<SUSYGenEvent> w_susygen;
    edm::Wrapper<SUSYEvent> w_susy;
    edm::Wrapper<GenEvent> w_gen;
  };
}
