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
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_41_1_zp6.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_7_1_NMa.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_15_1_2PQ.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_9_1_b4n.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_35_1_ZM7.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_40_1_6DA.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_38_1_PLP.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_28_1_29a.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_23_1_I04.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_24_1_82E.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_6_1_Kao.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_33_1_5EH.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_8_1_IKD.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_17_1_j8Z.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_34_1_FBc.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_4_1_1C9.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_43_1_9cX.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_21_1_F7u.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_3_1_gVl.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_45_1_5KR.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_37_1_npG.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_30_1_pNS.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_2_1_18Q.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_44_1_HkW.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_10_1_uCf.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_46_1_EyG.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_18_1_FJL.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_29_1_6R1.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_47_1_a9N.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_25_1_6NH.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_20_1_uJf.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_31_1_6Gz.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_13_1_Jvq.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_26_1_jhE.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_14_1_0DU.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_49_1_6Y7.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_32_1_djp.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_19_1_c4I.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_36_1_Jgz.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_12_1_bnD.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_48_1_buX.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_1_1_f2h.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_39_1_y5W.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_27_1_S7L.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_16_1_aPL.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_5_1_CHY.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_11_1_kNP.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_22_1_0rz.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_50_1_HXc.root',
'/store/user/cakir/TTjets_TuneZ2_scaledown_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleDown/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_42_1_Cgu.root'


)
)
