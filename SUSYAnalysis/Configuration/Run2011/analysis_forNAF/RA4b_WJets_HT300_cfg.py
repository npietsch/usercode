from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_WJetsToLNu_TuneZ2_7TeV_madgraph_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(

'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_104_1_cgm.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_67_1_IPq.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_268_1_5zx.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_202_1_bKD.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_271_1_KUG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_36_1_yrk.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_243_1_pkf.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_242_1_5KE.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_33_1_9r8.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_17_1_OUJ.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_173_1_zgM.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_16_1_0z9.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_14_1_Un4.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_129_1_hQl.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_12_1_fVV.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_1_1_fcd.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_10_1_vGg.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_136_1_Q8o.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_259_1_5cE.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_144_1_6OQ.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_64_1_dug.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_147_1_NOO.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_148_1_EJn.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_11_1_SZC.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_81_1_1PD.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_2_1_y9P.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_76_1_uWV.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_176_1_1dO.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_224_1_hIm.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_35_1_qaU.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_6_1_9td.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_8_1_97r.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_43_1_dcj.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_180_1_jg9.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_19_1_WcA.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_77_1_J19.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_80_1_b5S.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_55_1_paG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_111_1_9Mv.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_171_1_G7w.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_130_1_LAD.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_169_1_PFA.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_127_1_O9O.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_254_1_E0W.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_109_1_Hor.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_196_1_gh3.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_188_1_TWI.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_207_1_TgA.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_65_1_sTM.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_155_1_FVS.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_45_1_NtJ.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_78_1_KcY.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_220_1_Rrq.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_94_1_BDJ.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_208_1_sRx.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_216_1_2D6.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_128_1_c4u.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_257_1_Z3a.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_22_1_dF9.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_172_1_Y3O.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_221_1_Dvw.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_96_1_tTo.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_156_1_dwj.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_59_1_qaY.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_13_1_5s9.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_26_1_vJG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_138_1_liv.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_181_1_NwW.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_32_1_FVw.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_87_1_EkQ.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_114_1_Xk1.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_21_1_viV.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_235_1_2aO.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_163_1_veM.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_121_1_6ZL.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_168_1_hzT.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_232_1_dMS.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_20_1_DCN.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_151_1_YT0.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_214_1_X6I.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_98_1_R8S.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_113_1_GDL.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_167_1_nNh.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_115_1_eDN.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_187_1_7sd.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_233_1_cjx.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_38_1_OuU.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_270_1_EFG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_110_1_Dsa.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_49_1_6HD.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_241_1_F8s.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_200_1_YBV.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_119_1_0lh.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_58_1_jZe.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_253_1_0hR.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_195_1_P36.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_154_1_dFm.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_79_1_X7n.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_50_1_AEB.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_209_1_IEB.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_82_1_ufu.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_39_1_k0k.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_53_1_19r.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_124_1_BMo.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_57_1_S2X.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_234_1_CNC.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_116_1_fuA.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_222_1_5cz.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_249_1_Wez.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_3_1_hHg.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_123_1_vfx.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_204_1_nfd.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_238_1_Enw.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_193_2_X1z.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_205_1_bUD.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_250_1_23r.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_246_1_jO4.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_186_1_IxG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_91_1_t9K.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_219_1_TXG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_30_1_HsX.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_89_1_0Z4.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_73_1_9Gs.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_179_1_5jD.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_218_1_YrI.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_146_1_qk8.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_166_1_kk7.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_46_1_ZYj.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_23_1_o5e.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_185_1_S90.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_42_1_LZB.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_88_1_AhL.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_159_2_XNL.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_54_2_ePi.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_68_2_AeO.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_161_2_ndu.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_236_2_R5R.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_40_2_VHG.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_162_2_hJE.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_117_2_fRN.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_153_2_pa5.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_248_2_Sls.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_125_1_7Km.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_75_1_KJf.root',
'/store/user/cakir/WJetsToLNu_300_HT_inf_TuneZ2_7TeV-madgraph-tauola/WJets_TuneZ2_HT300/be7e2272a1ab6b783b58997e6b2f9f8a/Summer11_198_1_AWE.root'


)
)
