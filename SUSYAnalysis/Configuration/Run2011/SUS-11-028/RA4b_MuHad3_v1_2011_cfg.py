from BjetsData_cfg import *

process.TriggerWeightProducer.MuonTriggerWeight = True

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_405_1_s7V.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_188_1_I0I.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_473_0_1a5.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_703_1_ouI.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_458_1_VxF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_754_1_VQN.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_404_1_Z9B.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_368_1_sCv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_186_1_WTT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_254_1_GrO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_561_1_E7l.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_493_1_blX.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_187_1_H3E.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_375_1_zYx.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_19_1_O8Y.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_436_0_2SZ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_562_1_g7i.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_557_1_5Xv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_494_1_x6O.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_377_1_TcP.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_371_1_0OF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_632_0_ZPU.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_406_1_n6B.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_727_1_Bvs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_115_1_rYO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_399_1_PJe.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_437_0_b8C.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_230_1_mvQ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_184_1_VLk.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_205_1_mTQ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_210_1_mnr.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_571_1_TH0.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_677_1_JW8.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_17_1_FhB.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_430_0_q0Q.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_462_1_HKT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_434_0_86a.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_763_1_ITS.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_345_1_T1H.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_299_1_Kh8.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_105_1_XO7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_307_1_QVc.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_206_1_zTA.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_408_1_yQa.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_147_1_1co.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_435_0_0Am.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_429_0_l3R.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_302_1_nJJ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_586_1_Vn6.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_460_1_2qo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_431_0_JB4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_581_1_gNL.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_67_0_Q1u.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_671_1_1Bv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_724_1_A1J.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_189_1_1Pj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_673_1_JoJ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_21_1_col.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_292_1_xEu.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_143_1_wLT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_726_1_vhn.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_207_1_Xjy.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_783_1_IX1.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_715_1_5JX.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_269_1_0Gc.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_365_1_vsH.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_142_1_mIu.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_200_0_15q.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_587_1_aBW.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_208_1_0CR.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_125_1_Yvg.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_366_1_gc9.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_730_1_eKb.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_486_1_gwo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_407_1_jmA.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_488_1_Td5.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_204_1_Twu.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_228_1_jxp.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_491_1_fwi.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_146_1_Ba8.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_77_0_dt4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_433_0_1AJ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_193_1_Bbo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_297_1_k7t.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_457_1_oMV.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_203_0_44A.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_672_1_vgr.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_713_1_ul1.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_401_1_lWc.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_753_1_9cl.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_630_0_UQf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_123_1_LCl.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_403_1_4mq.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_364_1_DT4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_428_0_x8f.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_716_1_Pok.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_426_1_DWr.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_482_1_u6W.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_775_1_j0X.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_720_1_gJ2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_668_1_vxF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_402_1_3FU.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_145_1_Bh2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_455_1_dfz.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_718_1_ro2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_370_1_eli.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_490_1_iaT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_48_1_lqW.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_159_1_8GW.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_183_1_CzN.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_266_1_ZQc.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_102_1_Wxm.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_698_1_oZm.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_721_1_EwP.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_725_1_Cuk.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_485_1_Mvo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_231_1_VHl.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_592_1_aIs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_367_1_drQ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_358_1_n1Y.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_751_1_s15.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_760_1_6uN.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_481_1_Nlv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_560_1_Y8C.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_295_1_tLX.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_483_1_eNo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_570_1_rlD.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_268_1_uf1.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_664_1_Eym.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_294_1_VJE.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_1_1_KZL.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_287_0_NcQ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_300_1_tVa.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_628_1_vO2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_182_1_9CF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_663_1_w4w.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_479_1_gdA.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_452_1_eLp.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_487_1_5WU.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_723_1_5W7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_714_1_QEm.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_119_1_e7R.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_305_1_4Vk.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_198_1_AQR.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_117_1_d1Q.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_22_1_qb3.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_306_1_kxq.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_414_1_fxr.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_110_1_Ggw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_111_1_dJ3.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_722_1_Oxc.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_273_1_pPf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_719_1_eWL.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_194_1_BAx.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_168_1_yyL.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_109_1_7Hv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_114_1_lps.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_158_1_PKw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_369_1_xSz.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_652_1_gPA.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_380_1_nAL.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_629_1_kEG.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_301_1_io2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_582_1_ci9.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_2_1_nvO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_492_1_TDM.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_412_1_62p.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_378_1_Od7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_107_1_Lt7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_18_1_h6y.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_409_1_vXa.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_376_1_PLI.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_106_1_n2P.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_622_1_7ui.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_118_1_Egn.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_144_1_Vid.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_120_1_G5I.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_379_1_N7K.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_373_1_jnF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_246_1_3JY.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_413_1_6Mv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_374_1_XS2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_634_1_M3B.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_456_1_9VX.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_23_1_qSi.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_76_0_wG3.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_209_1_aNs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_400_1_vfU.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_304_1_5iT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_227_1_oLC.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_214_1_LKy.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_411_1_AJw.root'


)
)
