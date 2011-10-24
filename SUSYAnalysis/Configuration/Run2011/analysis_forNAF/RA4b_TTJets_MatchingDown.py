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
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_34_1_Eav.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_23_1_dkz.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_17_1_ChI.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_40_1_4Wb.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_1_1_es2.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_18_1_tT7.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_36_1_SE5.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_4_1_WsQ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_5_1_J4b.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_27_1_fJg.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_30_1_xRD.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_37_1_vqw.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_47_1_VDQ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_48_1_YNb.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_32_1_915.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_22_1_H5C.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_29_1_vkC.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_28_1_U86.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_24_1_l4h.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_14_1_181.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_41_1_3qQ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_6_1_YgK.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_15_1_sJV.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_49_1_ScS.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_16_1_90a.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_13_1_jn0.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_19_1_XsH.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_9_1_TeY.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_31_1_40A.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_33_1_8q0.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_3_1_7UA.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_35_1_c4j.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_2_1_rKP.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_43_1_iOL.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_52_1_RLT.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_53_1_r2i.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_54_1_q17.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_12_1_r3G.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_11_1_NLm.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_38_1_ar0.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_42_1_ml1.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_44_1_DFz.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_45_1_D6q.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_50_1_Wpq.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_39_1_AVF.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_21_1_etr.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_46_1_BxS.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_26_1_yai.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_8_1_Egg.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_10_1_UQJ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_25_1_FvJ.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_7_1_FPT.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_51_1_fA6.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_20_1_osE.root',
'/store/user/cakir/TTjets_TuneZ2_matchingdown_7TeV-madgraph-tauola/SUSYPAT_TTJets_MatchingDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_55_1_iFd.root'



)
)
