from BjetsData_cfg import *

process.TriggerWeightProducer.ElectronTriggerWeight = True

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_150_1_G9M.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_368_1_sGW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_298_1_6Ob.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_319_1_i1U.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_366_1_vM5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_449_1_CT8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_461_1_sba.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_297_1_XSx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_455_1_Wg7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_152_1_1Zy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_458_1_HtB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_460_1_mim.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_433_1_lsv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_272_1_Ic0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_222_1_7fl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_482_1_zaW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_200_1_9u2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_365_1_rFl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_434_1_VIe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_363_1_vVu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_246_1_GHi.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_187_1_W0G.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_259_1_jOj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_402_1_Q8c.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_197_1_SPs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_470_1_YWk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_106_1_6Q8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_554_1_og4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_429_1_Gb1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_400_1_L2c.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_22_1_zPO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_145_1_nUE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_230_1_FYe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_75_1_yFR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_47_1_SXg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_149_1_pqs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_457_1_Gmq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_479_1_gcX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_105_1_1Jh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_168_1_lVv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_555_1_pU0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_481_1_Xfz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_204_1_qI8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_641_1_nK4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_674_1_jea.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_459_1_kQE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_557_1_2UY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_403_1_7uV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_186_1_qZ7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_254_1_3mP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_248_1_upd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_15_1_nAG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_245_1_H60.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_201_1_5S3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_101_1_RFh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_454_1_8fK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_269_1_LDe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_232_1_lg9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_293_1_R75.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_292_1_Uqy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_364_1_0x0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_229_1_tfC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_294_1_z3s.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_296_1_fs7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_166_1_h74.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_20_1_wtE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_552_1_4Ia.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_76_1_j9n.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_185_1_9vD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_17_1_kHN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_202_1_buV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_553_1_kvo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_354_1_T3a.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_432_1_znL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_392_1_5Do.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_316_1_ltC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_270_1_4A3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_347_1_5qb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_295_1_cWn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_108_1_7ZW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_156_1_4q4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_146_1_DHn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_401_1_SWm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_394_1_Afu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_103_1_HNx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_431_1_Bdj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_73_1_fkl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_337_1_5DV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_514_1_4CA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_165_1_3AK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_104_1_13D.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_102_1_3lw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_362_1_cJH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_529_1_SSt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_453_1_VMf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_520_1_L1E.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_551_1_hg9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_242_1_sSv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_678_1_HIM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_345_1_038.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_158_1_A6y.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_167_1_cwf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_456_1_lkp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_612_1_9mX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_398_1_srb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_18_1_o3T.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_544_1_PKD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_39_1_s9G.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_573_1_wun.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_48_1_qhL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_203_1_yQn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_646_1_NiL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_4_1_BKg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_16_1_qHP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_574_1_j86.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_221_1_lhu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_572_1_V6y.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_1_1_BZq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_237_1_jwI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_649_1_1Ge.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_308_1_diA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_571_1_g87.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_512_1_8CE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_7_1_aPX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_207_1_dQi.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_611_1_5UW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_171_1_gnA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_599_1_BMZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_435_1_VVD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_143_1_UeS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_534_1_dqd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_594_1_J1K.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_14_1_XgZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_344_1_bCa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_182_1_RA9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_192_1_7VU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_543_1_YFF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_598_1_PMc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_609_1_yXD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_189_1_vCs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_77_1_5Dl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_303_1_SRy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_614_1_qxy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_263_1_JAi.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_118_1_XMR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_274_1_O53.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_471_1_mYS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_355_1_fWW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_120_1_h5m.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_430_1_jOU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_119_1_eF9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_531_1_Is9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_123_1_pyd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_376_1_0Uh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_305_1_nwD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_410_1_rB0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_622_1_rxV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_110_1_TqI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_117_1_n8J.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_194_1_HhW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_209_1_WkB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_616_1_ecZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_115_1_aXK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_648_1_feM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_195_1_UcM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_121_1_W9H.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_223_1_SLD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_62_1_5gO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_306_1_jTy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_559_1_kQC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_307_1_PvU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_114_1_jbY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_116_1_bNd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_211_1_NEc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_111_1_3Uf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_193_1_8Av.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_271_1_75z.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_370_1_8n1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_371_1_Wma.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_486_1_sTF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_188_1_2Pr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_367_1_o7s.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_206_1_OlG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_437_1_Chb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_304_1_ifC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_546_1_6NQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_556_1_5W7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_210_1_Knj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_488_1_ANF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_329_1_USG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_300_1_Yhj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_439_1_G15.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_191_1_2jI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_483_1_IR1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_301_1_qzs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_112_1_RJf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_462_1_q3u.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_645_1_0lA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_9_1_O4p.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_113_1_bk6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_409_1_vXw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_523_1_MhA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_436_1_EpI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_558_1_t6F.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_247_1_I0f.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_23_1_cuB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_484_1_w9m.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_406_1_2vW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_487_1_XZO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_260_1_64R.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_408_1_CEl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_109_1_Yvs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_13_1_zAz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_208_1_Knv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_21_1_Bq1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_404_1_Pvi.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_126_1_5JH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_264_1_BAg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_147_1_haK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_438_1_Pj4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_480_1_YxJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_231_1_Ve6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_405_1_mfB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_170_1_g86.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_369_1_iQm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_148_1_TN0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_41_1_WVb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_205_1_IFX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_107_1_fUQ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_485_1_I1y.root'



)
)