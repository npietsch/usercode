#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"
DEFINE_FWK_MODULE(SUSYInitSubset);

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYGenEventReco.h"
DEFINE_FWK_MODULE(SUSYGenEventReco);

#include "SUSYAnalysis/SUSYEventProducers/interface/HerwigGenEventProducer.h"
DEFINE_FWK_MODULE(HerwigGenEventProducer);

#include "SUSYAnalysis/SUSYEventProducers/interface/PFConsistentMuonProducer.h"
DEFINE_FWK_MODULE(PFConsistentMuonProducer);

#include "TopQuarkAnalysis/TopEventProducers/interface/StringCutObjectEvtFilter.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/HerwigGenEvent.h"

typedef StringCutObjectEvtFilter<SUSYGenEvent> SUSYGenEvtFilter;
typedef StringCutObjectEvtFilter<HerwigGenEvent> HerwigGenEventFilter;

DEFINE_FWK_MODULE(SUSYGenEvtFilter);
DEFINE_FWK_MODULE(HerwigGenEventFilter);
