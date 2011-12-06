from BjetsData_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_100_1_mzD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_101_1_a72.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_102_1_hdX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_103_1_5Jg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_104_1_Po6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_105_1_AaX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_106_1_Tt9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_107_1_aDr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_108_1_k70.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_109_1_IR1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_10_1_09P.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_110_1_mAU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_111_1_gGz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_112_1_fPa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_113_1_7ZQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_114_1_5rx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_115_1_EHt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_116_1_JSC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_117_1_JiU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_118_1_5bE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_119_1_b5E.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_11_1_dLo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_120_1_Vdn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_121_1_bxZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_122_1_EHh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_123_1_IK1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_124_1_9Er.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_125_1_5Qp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_126_1_aPR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_127_1_j5p.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_128_1_Rop.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_129_1_MXf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_12_1_e2P.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_130_1_SWT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_131_1_4hJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_132_1_mFj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_133_1_bBa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_134_1_NQD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_135_1_6xR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_136_1_p5j.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_137_1_CMZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_138_1_75G.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_139_1_8r4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_13_1_cAJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_140_1_XoJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_141_1_eNn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_142_1_D3z.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_143_1_enA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_144_1_RxS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_145_1_vb2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_146_1_3UZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_147_1_Psd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_148_1_BvH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_149_1_MPf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_14_1_4kU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_150_1_2gh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_151_1_LDr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_152_1_4vP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_153_1_CT8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_154_1_BRN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_155_1_sEf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_156_1_kVU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_157_1_qze.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_158_1_89X.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_159_1_DW9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_15_1_I7S.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_160_1_pJn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_161_1_izV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_162_1_WCN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_163_1_M6C.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_164_1_6EG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_165_1_5eY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_166_1_N7D.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_167_1_nao.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_16_1_xJ0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_17_1_Jqc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_18_1_5zC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_19_1_mGj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_1_1_eic.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_20_1_OB4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_21_1_Woj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_22_1_Zop.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_23_1_VQd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_24_1_wxt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_25_1_W6L.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_26_1_Qg6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_27_1_5GK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_28_1_xcR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_29_1_UH1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_2_1_eP5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_30_1_IDO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_31_1_FJt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_32_1_OhQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_33_1_iqh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_34_1_an5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_35_1_wyI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_36_1_q13.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_37_1_jjs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_38_1_7o8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_39_1_Fho.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_3_1_8UB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_40_1_PqQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_41_1_05C.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_42_1_6M7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_43_1_ICo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_44_1_NbL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_45_1_2B2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_46_1_Vsg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_47_1_hzt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_48_1_tpk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_49_1_yqQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_4_1_JBR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_50_1_GZU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_51_1_TcM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_52_1_4pm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_53_1_AEp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_54_1_K69.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_55_1_kig.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_56_1_0M6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_57_1_rZx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_58_1_GI7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_59_1_llG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_5_1_5nD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_60_1_zwm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_61_1_gZ8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_62_1_iPA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_63_1_knY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_64_1_Dy5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_65_1_wxs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_66_1_wWI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_67_1_sbU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_68_1_kvI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_69_1_4ge.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_6_1_Yqs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_70_1_SzU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_71_1_N9R.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_72_1_2CY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_73_1_7Jf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_74_1_zQ8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_75_1_Y2u.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_76_1_QhD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_77_1_YFp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_78_1_qsL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_79_1_fcS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_7_1_KyX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_80_1_oLO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_81_1_bT1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_82_1_BOS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_83_1_nR9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_84_1_Qk7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_85_1_MYI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_86_1_5bV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_87_1_IW5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_88_1_52l.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_89_1_Em4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_8_1_kJw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_90_1_9ET.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_91_1_NQ3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_92_2_FQp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_93_1_iGB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_94_1_o2r.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_95_1_UQY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_96_1_BGe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_97_1_axK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_98_1_70g.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_99_1_IgG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011A_178677/89b9a1e690a60eb51f0eff9b59c35417/Summer11_9_1_RC4.root'
)
)