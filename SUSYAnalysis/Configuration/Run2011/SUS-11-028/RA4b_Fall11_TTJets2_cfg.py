#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 245 RA4b_Fall11_TTJets1_cfg.py
#----------------------------------------------------

from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_TTJets.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"
process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/TTJetsFall11.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/TTJetsFall11.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1223_1_rto.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1224_1_phU.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1225_1_hbS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1226_1_PBf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1227_1_Ccj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1228_1_e1o.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1229_1_trm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_122_1_Xh2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1230_1_9Q9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1231_1_hCF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1232_1_sLD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1233_1_qXo.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1234_1_UhT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1235_1_1ea.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1236_1_2Vn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_123_1_CsC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_124_1_O7f.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_125_1_glB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_126_1_OwV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_127_1_umy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_128_1_J9s.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_129_1_iVF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_12_1_Oyn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_130_1_miA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_131_1_aZm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_132_1_GDl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_133_1_lpF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_134_1_Xd0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_135_1_hzW.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_136_1_3AV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_137_1_MF7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_138_1_atk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_139_1_y50.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_13_1_Xfv.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_140_1_qZ3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_141_1_mQT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_142_1_EQM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_143_1_MKA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_144_1_wjl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_145_1_8Uc.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_146_1_jNc.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_147_1_WVw.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_148_1_HTe.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_149_1_sXr.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_14_1_6cJ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_150_1_sFm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_151_1_Baf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_152_1_1Ul.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_153_1_ljz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_154_1_4MF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_155_1_OJn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_156_1_uqp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_157_1_rCU.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_158_1_R2K.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_159_1_2Jx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_15_1_lWj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_160_1_CfX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_161_1_Od9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_162_1_9Nc.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_163_1_AFI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_164_1_dYK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_165_1_M55.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_166_1_XZy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_167_1_1eh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_168_1_wwi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_169_1_Cez.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_16_1_Vab.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_170_1_AJB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_171_1_WKu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_172_1_4pL.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_173_1_LG6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_174_1_ykk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_175_1_aTp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_176_1_XjN.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_177_1_HJ7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_178_1_1fG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_179_1_FIL.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_17_1_tzQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_180_1_gga.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_181_1_uEr.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_182_1_Itk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_183_1_mY6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_184_1_2CC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_185_1_uEH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_186_1_zGE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_187_2_uZ0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_188_1_FyH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_189_2_bpu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_18_1_8ke.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_190_2_jsn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_191_2_3Aq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_192_1_laB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_193_1_Tzd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_194_1_wOu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_195_2_TP0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_196_2_9gF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_197_2_yXe.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_198_2_FWg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_199_1_2RZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_19_1_q6G.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1_1_rgu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_200_2_dxg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_201_2_irB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_202_1_V01.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_203_1_dE6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_204_1_sb3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_205_2_pY7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_206_1_aGi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_207_2_ti5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_208_2_eZg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_209_2_yh4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_20_1_9xS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_210_1_Vfc.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_211_1_JoB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_212_1_xzX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_213_1_LNv.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_214_2_qnu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_215_2_dO0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_216_1_wpH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_217_1_9IE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_218_1_3SQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_219_2_sjg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_21_1_G1Q.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_220_1_tSQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_221_2_uNw.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_222_1_W2Y.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_223_2_CFj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_225_2_QIo.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_226_1_Euz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_227_2_3Bi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_229_1_uyN.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_22_1_49s.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_230_1_Y31.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_231_1_lJR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_232_1_s16.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_233_1_9r7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_234_1_HkM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_235_1_BTh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_236_1_4zo.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_237_1_cAl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_238_1_Nzs.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_239_1_TqP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_23_1_bZx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_240_1_3HB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_241_1_0VU.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_242_1_VHF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_243_1_A9D.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_244_1_Z3l.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_245_1_vLT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_246_1_ISb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_247_1_M87.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_248_1_9WX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_249_1_yEj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_24_1_wfO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_250_1_zbn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_251_1_PTD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_252_1_Jw0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_253_1_77B.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_254_1_dMM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_255_1_HTF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_256_1_bJ7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_257_1_bzC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_258_1_egX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_259_1_2Yh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_25_1_lp5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_260_1_8aX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_261_1_gGH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_262_1_Q6s.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_263_1_g5h.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_264_1_UGz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_265_1_2VF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_266_1_4uP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_267_1_Xa2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_268_1_bZ2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_269_1_BdS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_26_1_nTM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_270_1_nRC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_271_1_QlH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_272_1_7hX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_273_1_JIl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_274_1_1DH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_275_2_XEE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_276_1_JOH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_277_1_Q0p.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_278_1_Xyw.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_279_1_BsQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_27_1_usg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_280_1_apj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_281_1_k1Q.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_282_1_1vB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_283_1_MwV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_284_1_QwJ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_285_1_tvk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_286_1_Psz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_287_1_ogC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_288_1_WKF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_289_1_Gkh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_28_1_3hB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_290_1_5Lx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_291_1_zPV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_292_1_lBq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_294_1_UdL.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_295_1_cQ6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_296_1_fPE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_297_1_k8m.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_298_1_rxt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_299_1_wIe.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_29_1_ZEw.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_2_1_7Og.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_300_1_51r.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_301_1_g23.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_302_1_AK7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_303_1_CNq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_304_1_ioT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_305_1_BW4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_306_1_XrX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_307_1_2Tq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_308_1_qPn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_309_1_zmA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_30_1_BSO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_310_1_Xcq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_311_1_aa2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_312_1_7jg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_313_1_HKe.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_314_1_PRU.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_315_1_gGH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_316_1_RL2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_317_1_Yy3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_318_1_a4d.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_319_1_tj6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_31_1_gLk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_320_1_6Ko.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_321_1_cd3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_322_1_ZZP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_323_1_Twm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_324_1_ovX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_325_1_TLk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_326_1_7cj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_327_1_82s.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_328_1_2nG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_329_1_M25.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_32_1_KWX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_330_1_mXc.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_331_1_uzG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_332_1_vJN.root'
)
)
