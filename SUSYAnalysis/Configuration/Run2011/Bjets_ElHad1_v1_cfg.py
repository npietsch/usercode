from BjetsData_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_100_3_f1d.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_101_3_YcH.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_102_3_ofP.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_103_3_lhS.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_104_3_QYo.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_105_5_OHr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_106_3_WUh.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_107_3_CEK.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_108_3_ChW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_109_3_HqL.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_10_3_Opg.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_110_3_9Uj.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_111_3_LEG.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_112_3_gYS.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_113_3_Olg.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_114_3_TEO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_115_3_tN3.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_116_3_9sB.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_117_3_pG2.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_118_5_gSE.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_119_3_fmu.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_11_3_MET.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_120_3_aMe.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_121_3_O17.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_122_3_sqW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_123_3_qMj.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_124_3_ija.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_125_3_7AU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_126_3_6Pg.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_127_3_mAa.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_128_3_gk7.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_129_1_XlO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_12_3_ONJ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_130_3_CwW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_131_3_PNK.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_132_3_QIS.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_133_3_nuv.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_134_3_mf0.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_135_3_zFX.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_136_3_k9X.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_137_3_hp1.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_138_3_rLt.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_139_3_YSO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_13_3_jeU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_140_3_YiD.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_141_3_BAZ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_142_3_IZ6.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_143_3_p4P.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_144_3_Z16.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_145_3_Mnc.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_146_3_aW0.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_147_3_xQI.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_148_3_PdO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_149_3_Pvk.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_14_3_fgD.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_150_3_iWn.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_151_3_2WB.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_152_3_Ez6.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_153_3_1ta.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_154_3_6gE.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_155_3_CvW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_156_3_8Tw.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_157_3_nQt.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_158_3_0Dn.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_159_3_GNy.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_15_3_lef.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_160_3_Ecg.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_161_3_PEB.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_162_3_m3j.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_163_3_JRr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_164_3_jAZ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_165_3_keo.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_166_3_E9T.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_167_5_y8b.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_168_3_nN7.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_169_3_jX8.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_16_3_CpQ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_170_3_zyI.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_171_3_Jof.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_172_3_gfV.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_173_3_Jbp.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_174_3_HJN.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_175_3_ktf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_176_3_Zeg.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_177_3_4fc.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_178_1_sWi.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_179_3_R6E.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_17_3_wCr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_180_3_ceC.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_181_3_J6z.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_182_1_qnt.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_183_3_JFP.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_184_3_wbP.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_185_1_NZS.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_186_3_zMJ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_187_3_dSI.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_188_1_p8d.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_189_3_rnn.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_18_3_6GP.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_190_3_I3m.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_191_3_fOI.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_192_3_Qxf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_193_3_zf0.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_194_3_UmY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_195_3_COh.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_196_3_3oW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_197_3_eMM.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_198_3_ohq.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_199_3_PEC.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_19_3_U7p.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_1_3_ILI.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_200_3_0Zl.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_201_3_PtB.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_202_3_nDX.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_203_3_Ba5.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_204_3_IJO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_205_3_Cqf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_206_3_AWN.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_207_3_JxT.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_208_3_VQQ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_209_3_0gb.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_20_3_ktW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_210_3_gon.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_211_3_BTf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_212_3_Xtv.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_213_3_Tbo.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_214_3_pkx.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_215_3_aM3.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_216_3_GYm.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_217_3_nX5.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_218_3_PB4.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_219_3_PqX.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_21_3_QQl.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_220_3_9Hx.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_221_3_Ag0.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_222_3_9Uv.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_223_3_kGq.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_224_3_Iwy.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_225_3_Rad.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_226_3_UQm.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_227_3_IsE.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_228_3_y48.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_229_3_IZj.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_22_3_hwe.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_230_3_2PL.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_231_3_NLr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_232_1_0Tu.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_233_3_RCQ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_234_3_kyL.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_235_3_Tb7.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_236_3_8Mk.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_237_3_IWr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_238_3_Iqu.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_239_3_q5W.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_23_3_WGk.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_240_3_tBj.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_241_3_ZWU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_242_3_zXm.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_243_3_N2P.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_244_3_NYj.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_245_3_CJS.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_246_3_I8Y.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_247_3_YbY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_248_3_nTh.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_249_3_8ku.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_24_3_UKr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_250_3_UAW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_251_3_2sX.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_252_3_bJe.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_253_3_EsY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_254_3_pnw.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_255_3_whs.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_256_3_Kyq.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_257_3_1ru.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_258_3_jZp.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_259_3_hww.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_25_3_qhg.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_260_3_c38.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_261_3_KFT.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_262_3_QRh.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_263_3_6aU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_264_3_8YN.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_265_3_U0F.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_266_3_vE0.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_267_3_Br4.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_268_3_F9l.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_269_3_wAl.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_26_3_HOe.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_270_3_H9j.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_271_3_DBO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_272_3_4w1.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_273_3_Z1P.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_274_3_JZm.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_275_3_YmC.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_276_3_UjW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_277_3_yob.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_278_3_XiO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_279_3_mDq.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_27_3_Sv4.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_280_3_RUQ.root'
)
)