#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=12 
# nafJobSplitter.pl 235 RA4b_TTJets_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_16_1_4Mw.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_28_1_jFD.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_17_1_ffr.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_34_1_niU.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_19_1_8qw.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_11_1_486.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_8_1_pNA.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_27_1_xd0.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_23_1_L8K.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_39_1_YrB.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_31_1_9P9.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_47_1_189.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_3_1_Dgq.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_21_1_xOi.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_29_1_RMF.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_9_1_bix.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_22_1_xXz.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_53_1_h7e.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_15_1_ESP.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_46_1_9Fd.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_36_1_4jM.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_33_1_Wt2.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_44_1_tNl.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_38_1_jsC.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_12_1_hhA.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_7_1_ukV.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_37_1_8ml.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_42_1_3Ws.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_13_1_ASX.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_1_1_xYK.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_50_1_igQ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_30_1_0rJ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_20_1_50V.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_26_1_O6N.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_6_1_c4S.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_51_1_OkW.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_35_1_Ir8.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_54_1_udP.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_40_1_0MJ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_48_1_Uzr.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_24_1_enT.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_14_1_geK.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_41_1_ujw.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_2_1_dQa.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_25_1_Co1.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_43_1_3yO.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_49_1_9kn.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_32_1_gNs.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_18_1_zyA.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_10_1_jz2.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_45_1_kUk.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_4_1_FZo.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_5_1_Wtj.root',
'/store/user/cakir/TTjets_TuneZ2_matchingup_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_52_1_vpD.root'


)
)
