#include "FWCore/Framework/interface/MakerMacros.h"


#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"
#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYGenEventReco.h"

DEFINE_FWK_MODULE(SUSYInitSubset);
DEFINE_FWK_MODULE(SUSYGenEventReco);

#include "TopQuarkAnalysis/TopEventProducers/interface/StringCutObjectEvtFilter.h"
#include "AnalysisDataFormats/TopObjects/interface/SUSYGenEvent.h"

DEFINE_FWK_MODULE(SUSYGenEvtFilter);
