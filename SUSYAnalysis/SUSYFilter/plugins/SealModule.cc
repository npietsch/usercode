#include "FWCore/Framework/interface/MakerMacros.h"

#include "SUSYAnalysis/SUSYFilter/plugins/HTFilter.h"
DEFINE_FWK_MODULE(HTFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/TransverseMassFilter.h"
DEFINE_FWK_MODULE(TransverseMassFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/PFMuonConsistency.h"
DEFINE_FWK_MODULE(PFMuonConsistency);

#include "SUSYAnalysis/SUSYFilter/plugins/MHTFilter.h"
DEFINE_FWK_MODULE(MHTFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/YmetFilter.h"
DEFINE_FWK_MODULE(YmetFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/DeltaPhiFilter.h"
DEFINE_FWK_MODULE(DeltaPhiFilter);

#include "SUSYAnalysis/SUSYFilter/plugins/DiLepFilter.h"
DEFINE_FWK_MODULE(DiLepFilter);
