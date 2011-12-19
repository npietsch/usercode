from BjetsData_cfg import *

process.TriggerWeightProducer.ElectronTriggerWeight = True

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(

'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_309_1_4jW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_177_1_Ktm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_244_1_ksH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_256_1_OTe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_258_1_qds.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_163_1_7tB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_451_1_2O6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_513_1_u4N.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_71_1_zE9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_268_1_KeZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_57_1_uwN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_359_1_5jw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_396_1_r7C.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_506_1_Mk8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_278_1_Ft1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_452_1_hBL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_227_1_yVG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_72_1_trp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_238_1_Pgk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_321_1_QEW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_140_1_oeh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_228_1_Inq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_277_1_GSW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_399_1_Ft7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_335_1_hHA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_46_1_257.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_473_1_lxN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_141_1_1Yw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_142_1_hPx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_524_1_qwj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_198_1_Ytp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_291_1_3S3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_334_1_FMC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_288_1_rr1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_241_1_5qF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_162_1_F3n.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_324_1_FY7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_184_1_GYl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_323_1_zPz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_100_1_AmO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_43_1_QQ0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_474_1_03f.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_45_1_ueq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_226_1_rNZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_161_1_mgG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_257_1_DKx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_333_1_6GX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_224_1_p8Y.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_129_1_UBA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_516_1_qpV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_472_1_67a.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_519_1_A99.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_290_1_CB2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_536_1_7Yn.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_476_1_sg7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_320_1_jiz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_243_1_lWx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_68_1_pnX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_175_1_3j2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_225_1_qjo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_155_1_YwP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_91_1_wvF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_361_1_VyW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_267_1_WcV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_262_1_hHo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_89_1_I67.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_99_1_Z4S.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_312_1_YKe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_83_1_1IO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_160_1_ZUK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_92_1_Ihh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_503_1_d9R.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_358_1_R4V.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_183_1_0eN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_322_1_XzF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_360_1_Am6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_518_1_Otu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_450_1_t9n.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_174_1_rS2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_40_1_6ke.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_582_1_Oj9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_252_1_LKH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_281_1_rcM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_499_1_rIY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_495_1_4q0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_382_1_hwN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_380_1_tdy.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_25_1_Hoa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_502_1_guf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_42_1_d1r.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_378_1_w1X.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_414_1_Pki.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_418_1_DCI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_379_1_bHE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_216_1_ZCj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_500_1_rS7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_415_1_3Ln.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_501_1_I9c.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_496_1_kXL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_417_1_pTi.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_217_1_Z7n.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_29_1_UbV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_588_1_jjH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_375_1_BI9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_549_1_EuP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_37_1_u9G.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_213_1_rrD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_587_1_Foc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_446_1_4es.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_490_1_QhM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_214_1_JND.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_240_1_xRv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_589_1_xnP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_69_1_672.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_561_1_oqX.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_373_1_CXG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_139_1_2s1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_416_1_mDT.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_413_1_IbI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_255_1_wmC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_497_1_Mm9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_562_1_hvg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_374_1_m92.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_663_1_SIB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_407_1_8my.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_492_1_npR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_585_1_MUd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_397_1_cap.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_377_1_Pj3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_393_1_xGd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_212_1_lfj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_128_1_D9f.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_665_1_jv0.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_498_1_xSI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_86_1_I4f.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_289_1_rzN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_27_1_Z3h.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_28_1_z3I.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_517_1_o8h.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_664_1_8yx.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_494_1_fx7.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_233_1_DTr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_586_1_I4D.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_583_1_hGk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_275_1_rkf.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_657_1_yOu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_491_1_fRb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_287_1_xws.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_395_1_FIZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_266_1_LhB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_660_1_Plp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_493_1_VMJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_253_1_6GL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_412_1_Ldc.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_658_1_78O.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_137_1_AQo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_411_1_yJY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_98_1_6bS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_26_1_D9O.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_530_1_0cS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_547_1_5eS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_489_1_F5Z.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_584_1_AE4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_36_1_wjI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_24_1_w4P.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_545_1_bPI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_620_1_5jY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_662_1_HeW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_250_1_9Rl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_581_1_22u.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_580_1_jHl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_448_1_cuO.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_239_1_Srz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_659_1_Aef.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_661_1_IY1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_655_1_pIt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_548_1_zwA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_623_1_ZV8.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_346_1_BFN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_654_1_zPp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_30_1_s0s.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_265_1_CWa.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_276_1_RlH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_427_1_LHK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_136_1_wH5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_515_1_IbJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_97_1_FDE.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_656_1_inF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_532_1_jhr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_579_1_4mg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_325_1_MEj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_356_1_LPd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_138_1_qda.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_159_1_hnw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_651_1_pJd.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_621_1_TXU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_578_1_0FM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_653_1_RDr.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_125_1_kGv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_619_1_iMI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_577_1_tZI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_381_1_TqD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_652_1_xlo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_566_1_OZJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_19_1_qAp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_576_1_Cg4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_357_1_b3U.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_615_1_3N9.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_617_1_EBZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_122_1_wLk.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_8_1_uj6.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_650_1_ePY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_215_1_mlG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_302_1_MZu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_618_1_ozs.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_10_1_gjj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_190_1_8QH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_372_1_ssM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_74_1_BaP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_Prompt2011B_179431_v2/Summer11_575_1_BfD.root'


)
)
