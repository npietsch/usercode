from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 48.49

process.weightProducer.NumberEvts = 5327746
process.weightProducer.Lumi = 1000 ## Lumi in 1/p

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_WJetsHT300.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_WJetsHT300.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_WJetsHT300.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/WJetsHT.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/WJetsHT.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_299_1_AS8.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_300_1_icS.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_301_1_zVr.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_30_1_lcJ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_302_1_eYa.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_303_1_pdR.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_304_1_rHV.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_305_1_QTk.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_306_1_jRr.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_307_1_KUu.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_308_1_1iZ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_309_1_u21.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_310_1_XdO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_311_1_CzN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_31_1_oqE.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_312_1_zDR.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_313_1_5un.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_314_1_7yE.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_315_1_LYM.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_316_1_VRO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_317_1_JHa.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_318_1_cKo.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_319_1_0MR.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_3_1_yki.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_320_1_MgB.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_321_1_fQ4.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_32_1_ELE.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_322_1_YBD.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_323_1_hqq.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_324_1_7jV.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_325_1_QEF.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_326_1_8BG.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_327_1_naO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_328_1_eqY.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_329_1_cq5.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_330_1_6wU.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_331_1_hmP.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_33_1_BGU.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_332_1_xik.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_333_1_4C0.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_334_1_Lr7.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_335_1_7Ef.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_336_1_Enf.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_337_1_BWD.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_338_1_CvV.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_339_1_VT4.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_340_1_vpk.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_341_1_uTe.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_34_1_BSf.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_342_1_qKK.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_343_1_ePn.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_344_1_DsO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_345_1_ddQ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_346_1_n1B.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_347_1_eob.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_348_1_a3Y.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_349_1_7hj.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_350_1_atk.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_351_1_Ssz.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_35_1_DO2.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_352_1_A3E.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_353_1_9Yw.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_354_1_Lil.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_355_1_JE4.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_356_1_YCM.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_357_1_5bx.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_358_1_H8k.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_359_1_DZ0.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_360_1_FX9.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_361_1_Pkt.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_36_1_szP.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_362_1_Cga.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_363_1_8jP.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_364_1_Yze.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_365_1_ufE.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_366_1_Jcy.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_367_1_sHQ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_368_1_sT3.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_369_1_sBC.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_370_1_lHz.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_371_1_nEC.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_37_1_gFb.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_372_1_XVt.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_373_1_Zzl.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_374_1_xIz.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_375_1_dwJ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_376_1_hZ0.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_377_1_zYn.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_378_1_U3m.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_379_1_NAN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_380_1_3fa.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_381_1_LO6.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_38_1_yCf.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_382_1_6JS.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_383_1_hg9.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_384_1_BVT.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_385_1_ak2.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_386_1_fsq.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_387_1_3ad.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_388_1_cf3.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_389_1_qRQ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_390_1_qAP.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_391_1_auf.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_39_1_LSx.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_392_1_AUH.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_393_1_VZk.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_394_1_tGn.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_395_1_VGP.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_396_1_HLw.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_397_1_bl1.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_398_1_LQd.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_399_1_U2r.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_400_1_b5M.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_401_1_r4b.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_40_1_aje.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_402_1_B7r.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_403_1_CJ6.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_404_1_t5C.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_405_1_6us.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_406_1_TRa.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_407_1_ANd.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_408_1_KK9.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_409_1_vPx.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_410_1_ag8.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_411_1_rKO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_41_1_VWW.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_412_1_lnt.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_413_1_MKl.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_414_1_AbV.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_415_1_McG.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_416_1_qo8.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_417_1_mxV.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_418_1_ps9.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_419_1_Vyg.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_4_1_ZO9.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_420_1_ckU.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_421_1_lYc.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_42_1_d0x.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_422_1_EHS.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_423_1_y1D.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_424_1_EHn.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_425_1_eOk.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_426_1_XMd.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_427_1_8DI.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_428_1_3GF.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_429_1_0nN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_430_1_FIQ.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_431_1_3sN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_43_1_aKl.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_433_1_XYg.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_435_1_rnf.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_436_1_zF4.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_437_1_moN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_438_1_JzE.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_439_1_XIE.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_440_1_DH8.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_441_1_zqs.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_44_1_z2s.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_442_1_s8y.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_443_1_eJy.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_444_1_51c.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_445_1_MJh.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_446_1_eNU.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_447_1_eWw.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_448_1_l7F.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_449_1_POS.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_450_1_x9Y.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_451_1_du9.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_45_1_iKe.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_46_1_LmK.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_47_1_5Rm.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_48_1_1Mm.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_49_1_8yC.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_50_1_rJz.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_51_1_sqR.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_5_1_OGr.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_52_1_xWC.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_53_1_8j4.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_54_1_Bef.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_55_1_mJN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_56_1_g5f.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_57_1_lXd.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_58_1_nXS.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_59_1_6yG.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_60_1_4Gg.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_61_1_Qcp.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_6_1_OwS.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_62_1_HhK.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_63_1_iVb.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_64_1_9k0.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_65_1_hr6.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_66_1_bc2.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_67_1_kXY.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_68_1_Gxn.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_69_1_x8t.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_70_1_22a.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_71_1_wvV.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_7_1_JpO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_72_1_srN.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_73_1_zDv.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_74_1_rI4.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_75_1_oEj.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_76_1_9wk.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_77_1_00Q.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_78_1_ysW.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_79_1_xgd.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_80_1_Npf.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_81_1_3t0.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_8_1_1sY.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_82_1_Vkv.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_83_1_ACF.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_84_1_6Iq.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_85_1_ZsL.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_86_1_1jA.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_87_1_s8s.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_88_1_ffO.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_89_1_T4O.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_90_1_tIc.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_91_1_0Ql.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_9_1_u98.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_92_1_3IG.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_93_1_zUb.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_94_1_lKI.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_95_1_lUY.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_96_1_cgw.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_97_1_B7E.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_98_1_A3i.root',
'/store/user/isabell/Summer11/WJets_HT300_Inf_new/Summer11_99_1_j3P.root'
)
)
