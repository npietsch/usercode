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
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_21_1_icR.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_6_1_NaJ.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_19_1_h8W.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_7_1_0i2.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_1_1_Xlx.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_25_1_C9T.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_33_1_nlM.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_24_1_sS2.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_28_1_32L.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_41_1_AHq.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_47_1_o4i.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_20_1_yIB.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_38_1_038.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_15_1_Xr7.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_23_1_5fZ.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_4_1_ria.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_34_1_gNJ.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_22_1_Qw2.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_27_1_OEU.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_30_1_1rQ.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_26_1_AWI.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_5_1_zD8.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_42_1_j6f.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_45_1_ylH.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_11_1_Wy0.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_12_1_MHa.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_43_1_DBn.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_36_1_OpW.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_29_1_zBx.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_13_1_oc1.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_35_1_kRa.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_14_1_T9y.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_37_1_2ao.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_17_1_Nd6.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_9_1_U2H.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_39_1_BuP.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_40_1_Yfj.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_10_1_PDJ.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_44_1_HqJ.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_46_1_7GX.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_31_1_eEH.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_8_1_R40.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_16_1_kOI.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_32_1_lXM.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_18_1_wz7.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_2_1_Eyj.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_3_1_cTe.root',
'/store/user/cakir/TTjets_TuneZ2_scaleup_7TeV-madgraph-tauola/SUSYPAT_TTJets_ScaleUp/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_48_1_M2E.root'    



)
)
