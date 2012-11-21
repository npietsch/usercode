#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"
DEFINE_FWK_MODULE(SUSYInitSubset);

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYGenEventReco.h"
DEFINE_FWK_MODULE(SUSYGenEventReco);

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYEventProducer.h"
DEFINE_FWK_MODULE(SUSYEventProducer);

#include "SUSYAnalysis/SUSYEventProducers/interface/PFConsistentMuonProducer.h"
DEFINE_FWK_MODULE(PFConsistentMuonProducer);

#include "TopQuarkAnalysis/TopEventProducers/interface/StringCutObjectEvtFilter.h"

#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
typedef StringCutObjectEvtFilter<SUSYGenEvent> SUSYGenEvtFilter;
DEFINE_FWK_MODULE(SUSYGenEvtFilter);

#include "SUSYAnalysis/SUSYObjects/interface/SUSYEvent.h"
typedef StringCutObjectEvtFilter<SUSYEvent> SUSYEvtFilter;
DEFINE_FWK_MODULE(SUSYEvtFilter);
