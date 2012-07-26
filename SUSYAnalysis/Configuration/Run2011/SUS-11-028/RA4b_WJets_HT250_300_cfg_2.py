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

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/WJetsHT.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/WJetsHT.root"

#Choose input files
process.source = cms.Source("PoolSource",
                                                        fileNames = cms.untracked.vstring(   
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_308_1_Mm7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_309_1_uMC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_310_1_Op5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_311_1_aeb.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_31_1_pIS.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_312_1_MKs.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_313_1_XzO.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_314_1_RK3.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_315_1_Q7i.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_316_1_ks6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_317_1_IgR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_318_1_V7m.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_319_1_7z9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_3_1_iP7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_320_1_xSO.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_321_1_Mz6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_32_1_wiB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_322_1_JXc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_323_1_FCX.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_324_1_Qar.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_325_1_rCe.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_326_1_cps.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_327_1_1JR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_328_1_i4j.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_329_1_tZ9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_330_1_ufe.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_331_1_Bmv.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_33_1_qqo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_332_1_2MD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_333_1_Aj4.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_334_1_vCK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_335_1_X99.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_336_1_SL1.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_337_1_yTD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_338_1_VBO.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_339_1_oSI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_340_1_jkv.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_341_1_74m.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_34_1_nUw.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_342_1_bjG.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_343_1_G58.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_344_1_68a.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_345_1_vik.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_346_1_TLK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_347_1_Q08.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_348_1_p4w.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_349_1_HNa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_350_1_V74.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_351_1_yGn.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_35_1_Mv2.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_352_1_bnB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_353_1_YT9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_354_1_APy.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_355_1_M6T.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_356_1_q7B.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_357_1_x8A.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_358_1_eud.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_359_1_zjb.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_360_1_WqE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_361_1_gFc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_36_1_PBe.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_362_1_8sE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_363_1_s4q.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_364_1_ulR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_365_1_VaB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_366_1_jRP.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_367_1_8S1.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_368_1_PlN.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_369_1_ipD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_370_1_Mmu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_371_1_8Jo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_37_1_1KE.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_372_1_22w.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_373_1_rsc.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_374_1_h6g.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_375_1_X3L.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_376_1_bWK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_377_1_Bbf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_378_1_2Hf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_379_1_REw.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_380_1_Qz7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_381_1_WOI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_38_1_GN5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_382_1_mGi.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_383_1_C6n.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_384_1_Hc7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_385_1_xw5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_386_1_vku.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_387_1_wqo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_388_1_82r.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_389_1_oKQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_390_1_Yoo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_391_1_yjg.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_39_1_MRF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_392_1_lyK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_393_1_6S7.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_394_1_adI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_395_1_rYh.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_396_1_WuQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_397_1_yDH.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_398_1_xIf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_399_1_rD2.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_400_1_Fte.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_401_1_flx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_40_1_cEd.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_402_1_vlI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_403_1_O7x.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_404_1_gcp.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_405_1_pUo.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_406_1_t1V.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_407_1_tMx.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_408_1_u4V.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_409_1_Ese.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_410_1_zVU.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_411_1_mA6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_41_1_JeQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_412_1_5c6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_413_1_n8X.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_414_1_374.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_415_1_1ic.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_416_1_pr2.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_417_1_maM.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_4_1_7QQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_418_1_Uzz.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_419_1_4td.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_420_1_mkf.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_421_1_vaX.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_42_1_lvI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_422_1_YYB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_423_1_ady.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_424_1_Jl8.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_425_1_xhe.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_426_1_2SZ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_427_1_GIX.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_428_1_940.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_429_1_EIL.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_430_1_t1D.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_431_1_M1U.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_43_1_EYK.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_432_1_pym.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_433_1_wrD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_434_1_egR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_435_1_ZVa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_436_1_GV5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_437_1_Zp6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_438_1_rXF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_439_1_L0S.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_440_1_lks.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_441_1_p8L.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_44_1_pUh.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_442_1_j1B.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_45_1_esO.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_46_1_jK0.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_47_1_Mce.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_48_1_Dd6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_49_1_NDF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_50_1_CFe.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_51_1_BMl.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_5_1_jiC.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_52_1_GTI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_53_1_jzN.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_54_1_lAR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_55_1_KxY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_56_1_4Zp.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_57_1_kb0.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_58_1_VbF.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_59_1_Pmv.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_60_1_FiV.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_61_1_bIl.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_6_1_8OQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_62_1_yLY.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_63_1_9y6.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_64_1_ixh.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_65_1_Xos.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_66_1_Mhu.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_67_1_fEH.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_68_1_KQs.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_69_1_u0o.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_70_1_Vc5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_7_1_bOb.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_72_1_PYl.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_73_1_MTk.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_74_1_HIr.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_75_1_IAQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_76_1_Xh8.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_77_1_C1j.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_78_1_eX5.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_79_1_4um.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_80_1_yXB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_81_1_34i.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_8_1_dL9.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_82_1_yLt.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_83_1_TA3.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_84_1_dPI.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_85_1_CgR.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_86_1_m2p.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_87_1_Y6i.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_88_1_ofw.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_89_1_8Ud.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_90_1_oYk.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_91_1_hZa.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_9_1_msD.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_92_1_e6S.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_93_1_6cj.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_94_1_6K0.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_95_1_agi.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_96_1_OXB.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_97_1_oSQ.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_98_1_gEv.root',
    '/store/user/cakir/Summer11/WJets_HT250_300//Summer11_99_1_Bnk.root'
    )
)
