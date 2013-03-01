from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 34.8
process.weightProducer.NumberEvts = 8702716 
process.weightProducer.Lumi = 1000 ## Lumi in 1/p

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_WJetsHT250.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_WJetsHT250.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_WJetsHT250.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_WJetsHT.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_WJetsHT.root"

#Choose input files
process.source = cms.Source("PoolSource",
                                                        fileNames = cms.untracked.vstring(
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_100_1_Bml.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_101_1_fW5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_10_1_vPs.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_102_1_8Qq.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_103_1_AoZ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_104_1_uL9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_105_1_yXD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_106_1_fs2.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_107_1_usa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_108_1_Hpn.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_109_1_cbC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_110_1_x4E.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_111_1_bLp.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_11_1_hc9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_112_1_coT.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_113_1_uZZ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_114_1_mfI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_115_1_ocT.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_116_1_kOY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_117_1_125.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_118_1_Fod.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_119_1_ajY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_1_1_WJc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_120_1_uVz.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_121_1_iJu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_12_1_ypl.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_122_1_yZS.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_123_1_Ave.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_124_1_wPw.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_125_1_Y1a.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_126_1_yUZ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_127_1_nj7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_128_1_QTq.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_129_1_iS0.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_130_1_eXZ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_131_1_zUN.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_13_1_6jx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_132_1_ZBB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_133_1_8Zt.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_134_1_cbu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_135_1_lem.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_136_1_KTE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_137_1_Pe9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_138_1_SZE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_139_1_Wk5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_140_1_6tF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_141_1_Dk4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_14_1_2lB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_142_1_kwJ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_143_1_5en.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_144_1_E5Y.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_145_1_asE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_146_1_6ha.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_147_1_XOa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_148_1_kEh.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_149_1_BM4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_150_1_Oub.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_151_1_phs.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_15_1_O6U.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_152_1_ryf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_153_1_QKc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_154_1_5c5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_155_1_GRb.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_156_1_J8K.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_157_1_sL7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_158_1_QUk.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_159_1_pLu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_160_1_ayV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_161_1_Qxs.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_16_1_ui2.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_162_1_ejG.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_163_1_99z.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_164_1_Vzq.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_165_1_7e0.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_166_1_x3D.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_167_1_mdt.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_168_1_LUP.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_169_1_L4W.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_170_1_csQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_171_1_OM4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_17_1_AhC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_172_1_moP.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_173_1_MTi.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_174_1_94i.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_175_1_NUc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_176_1_I9e.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_177_1_2zu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_178_1_PSx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_179_1_TTQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_180_1_zi8.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_181_1_teI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_18_1_Tz4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_182_1_AxV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_183_1_0G3.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_184_1_QNf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_185_1_LEF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_186_1_DIo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_187_1_37A.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_188_1_PbN.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_189_1_CcC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_190_1_qQI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_191_1_KiL.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_19_1_BdV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_192_1_n94.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_193_1_arC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_194_1_5Nj.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_195_1_Lkp.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_196_1_N6s.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_197_1_rzc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_198_1_3sP.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_199_1_EKi.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_200_1_7mR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_201_1_Wvn.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_20_1_uKn.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_202_1_wFY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_203_1_BFH.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_204_1_sJV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_205_1_c3Z.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_206_1_W4N.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_207_1_Ewg.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_208_1_ySa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_209_1_EiV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_210_1_Zr5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_211_1_zTt.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_21_1_ypF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_212_1_BCu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_213_1_cSo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_214_1_jh5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_215_1_9QT.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_216_1_sq3.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_217_1_erT.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_218_1_x8D.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_219_1_YbV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_2_1_i7u.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_220_1_4LK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_221_1_5cY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_22_1_KTO.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_222_1_do7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_223_1_2wf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_224_1_qJw.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_225_1_1YY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_226_1_NVl.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_227_1_Uji.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_228_1_AAC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_229_1_jiE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_230_1_Ox0.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_231_1_Rox.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_23_1_hHx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_232_1_r8K.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_233_1_tAW.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_234_1_TMj.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_235_1_rV6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_236_1_hR4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_237_1_TL4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_238_1_hDg.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_239_1_6qA.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_240_1_aFa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_241_1_84I.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_24_1_NOr.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_242_1_ER5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_243_1_mXL.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_244_1_SnY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_246_1_txo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_247_1_sNK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_248_1_Fjz.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_249_1_GUs.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_250_1_hhJ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_251_1_Lnn.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_25_1_kT6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_252_1_hKQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_253_1_Bo4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_254_1_lHS.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_255_1_OMU.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_256_1_hCQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_257_1_0Vc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_258_1_t0K.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_259_1_2UM.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_260_1_OrE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_261_1_AtJ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_26_1_yFx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_262_1_qhv.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_263_1_QzG.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_264_1_xKO.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_265_1_jzo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_266_1_Slo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_267_1_8tI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_268_1_5pk.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_269_1_9xU.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_270_1_LUK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_271_1_Ek9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_27_1_Lfk.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_272_1_sR2.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_273_1_p30.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_274_1_LKF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_275_1_ndk.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_276_1_Kil.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_277_1_OkQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_278_1_3uW.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_279_1_iXM.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_280_1_2CY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_281_1_hSi.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_28_1_kNo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_282_1_iKu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_283_1_cOu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_284_1_Bql.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_285_1_Vwj.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_286_1_ZmH.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_287_1_bHA.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_288_1_FNB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_289_1_s5p.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_290_1_QHD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_291_1_PXx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_29_1_po1.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_292_1_yOd.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_293_1_H9q.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_294_1_J86.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_295_1_YCI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_296_1_aHg.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_297_1_i9F.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_298_1_0Xz.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_299_1_H85.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_300_1_psz.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_301_1_x7Z.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_30_1_leV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_302_1_vJe.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_303_1_NBn.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_304_1_BTi.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_305_1_8jW.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_306_1_vmw.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_307_1_MGI.root'
)
)