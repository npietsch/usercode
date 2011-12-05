#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYGenEventReco.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/GenEventReco.h"

DEFINE_FWK_MODULE(SUSYInitSubset);
DEFINE_FWK_MODULE(SUSYGenEventReco);
DEFINE_FWK_MODULE(GenEventReco);

#include "TopQuarkAnalysis/TopEventProducers/interface/StringCutObjectEvtFilter.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"

typedef StringCutObjectEvtFilter<SUSYGenEvent> SUSYGenEvtFilter;

DEFINE_FWK_MODULE(SUSYGenEvtFilter);
