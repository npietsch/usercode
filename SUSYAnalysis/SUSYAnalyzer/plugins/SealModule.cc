#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYAnalyzer.h"
DEFINE_FWK_MODULE(SUSYAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYGenEventAnalyzer.h"
DEFINE_FWK_MODULE(SUSYGenEventAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/BjetsAnalyzer.h"
DEFINE_FWK_MODULE(BjetsAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/EventTopology.h"
DEFINE_FWK_MODULE(EventTopology);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/TtGenEventAnalyzer.h"
DEFINE_FWK_MODULE(TtGenEventAnalyzer);
