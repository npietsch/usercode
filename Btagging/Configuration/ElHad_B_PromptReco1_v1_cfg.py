from BjetsData_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_100_1_No3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_101_1_hkE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_102_1_LRW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_103_1_2YM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_104_1_8AJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_105_1_oFk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_106_1_bso.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_107_1_mUO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_108_1_unQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_109_1_Mee.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_10_1_TBj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_110_1_t7b.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_111_1_UVp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_112_1_BOY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_113_1_DZF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_114_1_7EU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_115_1_Kq8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_116_1_wfm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_117_1_vCT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_118_1_WII.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_119_1_8Gv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_11_1_L50.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_120_1_mu3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_121_2_bOZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_123_1_rtl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_124_1_bPH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_125_1_BZC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_126_1_F1j.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_127_1_3Im.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_128_1_0WT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_129_1_epJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_12_1_W9c.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_130_1_6K3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_131_2_CXr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_132_1_Zkn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_133_1_8SX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_134_1_PrT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_135_1_Ysi.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_136_1_Y4P.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_137_1_Vkl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_138_1_5W8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_139_1_9Zo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_13_1_icm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_140_1_WSK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_141_1_J9k.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_142_1_sfr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_143_1_VGd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_144_1_5St.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_145_1_MED.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_146_1_HA3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_147_1_8xJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_148_1_xpy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_149_1_3yA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_14_1_yLr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_150_1_7SP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_151_1_ECe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_152_1_YIM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_153_1_Oe1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_154_1_tg1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_157_4_015.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_158_1_Yhp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_159_1_8fz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_15_1_FnA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_160_1_FKd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_161_1_hIr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_162_1_TyU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_163_1_saC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_164_1_NFK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_165_1_SK7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_166_1_Due.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_167_1_Qtk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_168_1_YFK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_169_1_GHV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_16_1_yuB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_170_1_t6r.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_171_1_aMf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_173_2_PkW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_175_1_kj3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_176_1_LFv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_177_1_syL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_178_1_UKR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_179_1_uRd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_17_1_icw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_183_2_Yy2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_184_1_epW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_185_1_Vbe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_186_1_xn1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_187_2_CAf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_191_2_xST.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_192_2_f24.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_193_5_mQE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_196_1_rzR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_197_2_94H.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_198_2_ZoH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_199_1_FpF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_1_1_WKy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_200_1_6I2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_201_1_NCr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_202_1_JW8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_203_1_2bl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_204_1_r0Q.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_205_1_IwE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_206_1_me9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_207_1_l27.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_208_1_9jX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_209_1_NE6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_20_1_CcG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_210_1_a05.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_211_1_OGI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_212_1_WZC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_213_2_SCu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_217_1_os4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_218_1_HNR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_219_1_002.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_21_1_R5N.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_220_1_iAx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_221_1_9Gr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_222_1_2pr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_223_1_JcE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_224_1_A9T.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_225_1_2B4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_226_1_B0Q.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_227_1_soc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_228_1_Tps.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_229_1_DCz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_230_1_yzf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_231_1_Vs1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_232_1_5eJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_234_4_OQ1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_235_4_zeL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_236_1_r21.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_237_1_bLP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_238_1_KLY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_239_1_Qba.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_23_1_rFo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_240_1_IXo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_241_1_a8J.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_242_1_qIf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_243_1_yVY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_244_1_3p2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_245_1_egD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_248_1_uK9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_249_2_674.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_24_1_Hbw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_250_1_jNE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_251_1_pDT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_252_1_fH9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_253_1_JY4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_254_1_dMA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_255_1_vlX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_256_1_F6Q.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_257_1_Ky9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_259_1_LVH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_25_1_xOh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_260_1_y5F.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_261_1_d4S.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_262_1_Aaa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_263_1_POU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_264_1_i9e.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_265_1_TCM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_266_1_utq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_267_1_sD9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_268_1_Qin.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_269_1_NEc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_26_1_PaN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_270_1_JrX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_271_1_wSN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_272_1_mVU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_273_1_pLb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_274_1_xiT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_275_1_Vb3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_276_1_n7L.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_277_1_O48.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_278_1_OdN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_279_1_1B7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_27_1_RMS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_283_2_gxc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_284_1_30K.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_285_1_b3H.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_286_1_ORa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_287_1_9dW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_288_1_jN5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_28_1_FaM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_291_2_RHI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_294_1_336.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_295_1_kso.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_2_1_A1A.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_300_1_dKH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_301_1_d4k.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_302_1_K8G.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_303_1_bl5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_304_1_Xfd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_305_1_SFM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_306_1_JWs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_307_1_dEf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_308_1_ALA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_309_1_7vd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_30_2_403.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_310_1_DlG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_311_1_tUl.root'
)
)