from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_10_1_eDz.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_11_1_Lmg.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_12_1_GFc.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_13_1_TPX.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_14_1_hSQ.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_15_1_dJw.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_16_1_oD9.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_17_1_sQq.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_18_1_pTo.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_19_1_iUm.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_1_1_SHC.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_20_1_Iba.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_21_1_ECE.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_23_1_g1L.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_24_2_Av7.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_25_2_Q5i.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_26_2_C7H.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_27_2_pPq.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_28_2_7ma.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_29_2_9C9.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_2_1_yEP.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_30_2_wV2.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_31_2_HGl.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_32_2_Tsx.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_33_2_i5w.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_36_2_UMc.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_37_1_MXK.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_38_1_YTQ.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_39_1_fj4.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_3_1_4Z6.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_41_1_VZd.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_42_1_H3G.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_43_1_ykL.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_44_1_cpq.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_46_1_3nu.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_47_1_Q4S.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_49_1_KZj.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_4_1_uey.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_5_1_bgn.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_6_1_zKw.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_7_1_8gx.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_8_1_FwV.root',
'/store/user/cakir/TTJets_TuneZ2_7TeV-madgraph-tauola/TTJets_Summer11/0e24d4d1378744493e43c69206f0c6d5/Summer11_9_1_Ctk.root'
)
)
