from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_WJetsToLNu_TuneZ2_7TeV_madgraph_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_301_1_Fxk.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_151_1_tq4.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_388_1_Umt.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_278_1_m0Z.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_338_1_oTP.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_210_1_OQN.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_141_1_AXa.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_281_1_fQa.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_271_1_8uZ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_421_1_ZNi.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_117_1_b7Z.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_363_1_2H1.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_204_1_841.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_424_1_44c.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_433_1_3Ep.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_426_1_xBS.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_85_1_18h.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_389_1_rNl.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_270_1_GpA.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_264_1_nYY.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_167_1_iXF.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_132_1_Mia.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_88_1_3ln.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_385_1_DBk.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_416_1_jjo.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_436_1_GpH.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_302_1_93S.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_38_1_5ty.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_203_1_OCY.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_45_1_hEt.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_437_1_jwc.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_109_1_oOx.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_168_1_XrF.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_265_1_ou6.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_57_1_lrm.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_170_1_HWA.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_115_1_nzO.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_69_1_QzW.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_126_1_PQu.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_153_1_hIz.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_190_1_fMO.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_41_1_aBs.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_361_1_dVv.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_406_1_GDt.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_294_1_agx.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_112_1_i0g.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_186_1_dNn.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_49_1_t3h.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_191_1_3zs.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_77_1_H4n.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_187_1_vDK.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_267_1_jM5.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_328_1_k3O.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_82_1_ZII.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_243_1_xVo.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_432_1_3yg.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_150_1_rnW.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_394_1_DuB.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_380_1_xZv.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_11_1_NNu.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_326_1_Ma3.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_196_1_aoy.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_220_1_Ewg.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_435_1_EOh.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_315_1_ShK.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_7_1_0B6.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_240_1_FK3.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_55_1_S5f.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_143_1_YDQ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_370_1_i4s.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_10_1_icG.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_371_1_PPZ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_321_1_QnK.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_331_1_2em.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_303_1_rZS.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_86_1_RQo.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_307_1_luO.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_296_1_dNe.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_284_1_AXR.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_305_1_UDz.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_304_1_BFG.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_175_1_OfB.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_59_1_Pk8.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_213_1_xjD.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_72_1_gii.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_373_1_vag.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_101_1_jD3.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_208_1_GGx.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_51_1_sOR.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_131_1_VTl.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_407_1_ZSR.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_107_1_TMl.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_130_1_tV9.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_319_1_ozL.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_300_1_Czb.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_138_1_i2k.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_353_1_XtG.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_342_1_Zkp.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_212_1_0OI.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_108_1_Kou.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_8_1_8w7.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_48_1_l5O.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_356_1_77I.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_133_1_zTE.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_299_1_E92.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_15_1_Eok.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_352_1_HkO.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_221_1_8Rd.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_295_1_KR6.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_285_1_rNn.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_209_1_ARn.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_345_1_B6i.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_79_1_bF1.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_81_1_KtN.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_87_1_nLW.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_379_1_ODS.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_354_1_nJp.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_129_1_7wG.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_355_1_MBs.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_128_1_pdL.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_290_1_spw.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_124_1_oRn.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_291_1_lNy.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_408_1_nT7.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_140_1_CHX.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_96_1_kti.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_135_1_o4b.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_169_1_Bx7.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_65_1_4eo.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_248_1_otj.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_1_1_DxI.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_123_1_Cfl.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_347_1_bh2.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_349_1_2KY.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_316_1_QLk.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_222_1_Th0.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_430_1_t5y.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_335_1_MQ8.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_91_1_9mQ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_70_1_b0a.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_54_1_4Ew.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_247_1_K28.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_4_1_3lP.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_78_1_AaY.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_238_1_Jkb.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_410_1_Bdb.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_224_1_LgD.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_329_1_dbm.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_12_1_iEs.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_375_1_zU4.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_113_1_CHl.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_332_1_6lA.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_137_1_N44.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_225_1_d31.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_5_1_lIJ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_324_1_155.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_73_1_Mqc.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_377_1_aJB.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_31_1_gbk.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_202_1_YKg.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_236_1_4TL.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_418_1_NBC.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_263_1_ezX.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_17_1_U43.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_172_1_Zhw.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_122_1_I2D.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_419_1_0ws.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_249_1_0zz.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_185_1_rWa.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_19_1_AVr.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_30_1_bG1.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_121_1_Lim.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_277_1_ZoK.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_256_1_7xE.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_297_1_c8o.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_412_1_Ehj.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_24_1_KRS.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_148_1_VWh.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_21_1_4vi.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_25_1_qJj.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_23_1_846.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_18_1_Wsc.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_29_1_BHX.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_201_1_5Vs.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_27_1_pTQ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_136_1_SvF.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_22_1_O4N.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_171_1_HCt.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_97_1_Kex.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_298_1_KR0.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_193_1_jNJ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_120_1_KF8.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_14_1_20h.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_16_1_SaB.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_404_1_QHP.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_364_1_jgc.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_83_1_vg8.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_106_1_MSm.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_230_1_EMW.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_53_1_vsw.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_162_1_nab.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_325_1_l8H.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_216_1_nOm.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_67_1_8dj.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_71_1_pKT.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_227_1_82W.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_74_1_tPt.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_95_1_Dzx.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_242_1_Bj7.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_181_1_klZ.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_197_1_mrL.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_13_1_YVh.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_93_1_8s4.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_312_1_9uM.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_399_1_RBD.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_369_1_Khs.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_145_1_jCe.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_382_1_pms.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_99_1_sge.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_397_1_Aru.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_246_1_JnO.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_50_1_X0q.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_195_1_afR.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_420_1_4uW.root',
'/store/user/schettle/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_429_1_maK.root'



)
)
