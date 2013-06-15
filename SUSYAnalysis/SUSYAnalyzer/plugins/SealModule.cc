#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYAnalyzer.h"
DEFINE_FWK_MODULE(SUSYAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/SystematicsAnalyzer.h"
DEFINE_FWK_MODULE(SystematicsAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/SUSYGenEventAnalyzer.h"
DEFINE_FWK_MODULE(SUSYGenEventAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/BjetsAnalyzer.h"
DEFINE_FWK_MODULE(BjetsAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/EventTopology.h"
DEFINE_FWK_MODULE(EventTopology);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/TtGenEventAnalyzer.h"
DEFINE_FWK_MODULE(TtGenEventAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/RA4Analyzer.h"
DEFINE_FWK_MODULE(RA4Analyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/Out.h"
DEFINE_FWK_MODULE(Out);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/GluinoAnalyzer.h"
DEFINE_FWK_MODULE(GluinoAnalyzer);

#include "SUSYAnalysis/SUSYAnalyzer/plugins/HerwigGenEventAnalyzer.h"
DEFINE_FWK_MODULE(HerwigGenEventAnalyzer);
