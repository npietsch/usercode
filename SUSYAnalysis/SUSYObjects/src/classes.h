#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"

#include "DataFormats/Common/interface/Wrapper.h"
#include "TString.h"

namespace {

  struct dictionary {
    //edm::Wrapper<std::vector<std::vector<int> > > w_v_vint;

    SUSYGenEvent susygen;
    SUSYEvent susy;
    edm::Wrapper<SUSYGenEvent> w_susygen;
    edm::Wrapper<SUSYEvent> w_susy; 
  };
}
