#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYInitSubset.h"
DEFINE_FWK_MODULE(SUSYInitSubset);

#include "SUSYAnalysis/SUSYEventProducers/interface/SUSYGenEventReco.h"
DEFINE_FWK_MODULE(SUSYGenEventReco);

#include "SUSYAnalysis/SUSYEventProducers/interface/GenEventReco.h"
DEFINE_FWK_MODULE(GenEventReco);

#include "SUSYAnalysis/SUSYEventProducers/interface/PFConsistentMuonProducer.h"
DEFINE_FWK_MODULE(PFConsistentMuonProducer);


#include "TopQuarkAnalysis/TopEventProducers/interface/StringCutObjectEvtFilter.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"

typedef StringCutObjectEvtFilter<SUSYGenEvent> SUSYGenEvtFilter;

DEFINE_FWK_MODULE(SUSYGenEvtFilter);
