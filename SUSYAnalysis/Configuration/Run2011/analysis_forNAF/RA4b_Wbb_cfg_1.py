#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 16 RA4b_LM13_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_90_1_hBm.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_66_1_msJ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_115_1_UNE.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_214_1_9XF.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_228_1_cuX.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_61_1_kU8.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_77_1_0kA.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_235_1_vNU.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_276_1_mf9.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_50_1_h95.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_3_1_TvF.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_209_1_6vG.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_331_1_aYc.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_199_1_w84.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_168_1_3Bx.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_86_1_Sds.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_317_1_P3Q.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_308_1_efj.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_69_1_NbJ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_122_1_aCS.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_126_1_n3M.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_314_1_kRo.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_283_1_PzN.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_309_1_FYt.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_297_1_e9a.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_181_1_XnC.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_154_1_5tK.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_131_1_2o0.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_4_1_eoQ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_237_1_QAi.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_194_1_frk.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_220_1_3X7.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_55_1_VE0.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_119_1_lUn.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_305_1_2JV.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_225_1_6BK.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_95_1_SF5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_296_1_z4j.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_88_1_qzi.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_332_1_Zd5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_242_1_snh.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_325_1_Dyl.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_288_1_PT4.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_113_1_WdV.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_108_1_bsY.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_73_1_gN5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_219_1_0jJ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_162_1_Rmz.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_253_1_Eu1.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_132_1_go7.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_28_1_jDV.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_187_1_RIT.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_140_1_7td.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_104_1_ioE.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_72_1_x6o.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_335_1_pan.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_323_1_QQB.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_207_1_X7D.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_197_1_N9i.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_124_1_t1b.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_93_1_w7c.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_40_1_8Oa.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_178_1_HBb.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_261_1_Qag.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_24_1_WlQ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_244_1_IHw.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_233_1_HND.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_311_1_vCN.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_14_1_pgl.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_23_1_Na7.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_307_1_P4F.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_147_1_mRl.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_260_1_aah.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_299_1_qh8.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_116_1_4ML.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_241_1_DjV.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_25_1_ssz.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_30_1_BvI.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_167_1_GE1.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_313_1_E2Y.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_112_1_mUF.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_157_1_kUs.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_433_1_Zo7.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_183_1_Ndb.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_268_1_klL.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_51_1_HYh.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_42_1_k56.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_48_1_Ln5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_249_1_hnc.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_230_1_GHX.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_139_1_MqV.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_10_1_LXd.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_217_1_lmN.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_129_1_ig1.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_106_1_9Di.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_120_1_rAF.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_256_1_Uiy.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_273_1_U0H.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_211_1_vJS.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_182_1_PeR.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_324_1_3wf.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_300_1_Wow.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_47_1_GI2.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_328_1_GIG.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_80_1_7zu.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_226_1_85g.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_26_1_YS8.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_274_1_krZ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_304_1_Hbz.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_284_1_NxH.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_294_1_32D.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_11_1_ho2.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_312_1_7GF.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_264_1_s0g.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_38_1_TF5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_321_1_94Y.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_334_1_GQe.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_145_1_WxW.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_315_1_oGK.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_84_1_Twm.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_52_1_Yec.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_170_1_in2.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_180_1_WGY.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_91_1_Yb4.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_107_1_6V4.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_259_1_CwG.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_206_1_k4f.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_165_1_jQ9.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_19_1_bTg.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_196_1_INY.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_195_1_3To.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_173_1_ppz.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_223_1_J6B.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_213_1_t0O.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_65_1_PWK.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_293_1_vu5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_234_1_rDx.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_102_1_bMo.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_74_1_x9l.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_190_1_VDk.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_142_1_6U6.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_118_1_xbC.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_278_1_YBm.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_184_1_wRY.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_416_1_4jv.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_57_1_M6D.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_318_1_HYY.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_204_1_pZv.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_426_1_iIF.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_248_1_u82.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_97_1_faW.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_447_1_FzX.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_59_1_lSu.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_404_1_7aV.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_435_1_xxU.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_246_1_fZr.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_289_1_Lq2.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_440_1_3V0.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_239_1_KGu.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_449_1_NGN.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_407_1_nP6.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_451_1_GjG.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_429_1_WY3.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_359_1_91e.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_450_1_Ork.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_401_1_lYg.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_419_1_HYM.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_203_1_2rU.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_62_1_DuU.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_134_1_VLo.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_159_1_bI5.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_346_1_zZs.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_446_1_814.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_117_1_fi9.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_362_1_ft6.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_381_1_f8W.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_327_1_rJf.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_420_1_1mP.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_452_1_rNC.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_405_1_7p1.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_431_1_VOX.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_160_1_2TA.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_270_1_o0j.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_437_1_6Lt.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_445_1_aWh.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_384_1_igX.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_279_1_kjG.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_46_1_iQl.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_413_1_I2D.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_238_1_XUm.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_224_1_X0z.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_282_1_5SJ.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_6_1_bEC.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_193_1_e5U.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_277_1_NKa.root',
'/store/user/cakir/WbbToLNu_TuneZ2_7TeV-madgraph-pythia6-tauola/SUSYPAT_WbbJets/27ea4c3403b4ce5da6d8f3d236870fb8/Summer11_285_1_Hzz.root'
    

   )
)