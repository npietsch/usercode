#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYFilter/plugins/HTFilter.h"
DEFINE_FWK_MODULE(HTFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/TransverseMassFilter.h"
DEFINE_FWK_MODULE(TransverseMassFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/PFMuonConsistency.h"
DEFINE_FWK_MODULE(PFMuonConsistency);
