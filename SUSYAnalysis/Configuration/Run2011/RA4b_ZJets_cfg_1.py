from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_DYJetsToLL_TuneZ2_M_50_7TeV_madgraph_tauola.root"


# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_578_0_pur.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_384_2_Cqo.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_420_2_Sbw.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_431_2_skZ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_438_2_svl.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_423_2_gXX.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_451_1_pg0.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_52_0_iOk.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_133_0_dIB.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_456_1_4R9.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_82_0_CnX.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_497_0_0g7.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_36_0_llU.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_381_2_yKG.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_367_2_r5T.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_126_0_x0e.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_434_2_9RT.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_573_0_kfU.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_540_0_2DM.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_394_2_cUu.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_447_0_uUO.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_362_0_yh6.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_42_0_NiA.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_286_0_B5U.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_443_0_24s.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_378_1_vEH.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_311_2_kPU.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_442_0_1DF.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_191_2_KgM.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_440_2_UKR.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_452_2_6NP.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_409_2_S2i.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_441_0_Tqu.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_186_2_No8.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_51_2_wFO.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_254_2_1VP.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_119_1_gye.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_405_1_kf6.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_491_1_Wsk.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_231_0_tH8.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_414_0_aHx.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_490_1_297.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_47_0_KSY.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_48_2_OFo.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_87_0_77X.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_53_3_uuq.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_63_0_e41.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_588_0_SC2.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_92_0_ymT.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_390_3_0xt.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_385_3_5t6.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_116_0_C9R.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_197_0_BdB.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_173_0_xpz.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_290_0_aPX.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_611_0_COT.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_168_3_pxI.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_306_3_oBo.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_0_X2S.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_310_3_4As.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_93_0_1VA.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_105_3_wS0.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_59_0_Lqq.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_49_0_glR.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_246_3_lMd.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_413_0_uKj.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_424_0_1R1.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_73_3_Ufi.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_410_2_BAc.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_383_0_GZw.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_404_0_Rxd.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_569_0_b1l.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_70_3_6X4.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_370_3_yLz.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_101_3_7pm.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_314_0_mtc.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_0_7DD.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_176_3_EQz.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_108_0_NlC.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_291_3_7ec.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_208_0_SqK.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_401_3_T1e.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_159_0_uMG.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_178_0_Di7.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_220_0_Gwi.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_444_3_CGV.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_403_2_khi.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_570_0_qpk.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_142_0_8vd.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_37_0_IzB.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_183_0_bTd.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_437_2_Iky.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_65_0_Hx0.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_41_0_TUm.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_478_0_THt.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_233_0_65Y.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_0_Lza.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_267_0_JVW.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_476_0_AYu.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_355_2_uyj.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_250_0_g2Z.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_204_0_2We.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_144_1_T5S.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_315_4_vS0.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_0_K8h.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_130_0_asO.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_433_0_lVF.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_391_0_wfV.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_449_2_Aqn.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_450_0_iFa.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_436_2_Fgt.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_374_2_rLJ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_195_3_YjX.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_448_2_Ucb.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_56_3_jH3.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_316_0_49T.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_137_4_kcZ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_272_0_gJb.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_114_0_QM4.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_329_3_9Db.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_210_2_J23.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_294_2_qaR.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_419_1_FWA.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_281_4_4Oj.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_343_0_BAy.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_253_2_sTs.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_287_0_vKu.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_0_WEc.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_172_0_4h1.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_610_0_PFZ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_40_4_Hhl.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_148_0_nLH.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_58_1_3ie.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_222_2_ama.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_354_0_IBV.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_318_1_llJ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_323_2_qQY.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_4_QXf.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_432_4_Zjd.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_389_3_McH.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_416_4_cM1.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_397_5_87s.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_445_4_iPO.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_91_4_TdD.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_535_1_qHG.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_2_JB3.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_346_2_QKz.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_321_2_PKt.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_348_2_4T7.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_353_2_iVS.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_532_0_WgS.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_332_2_FDz.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_112_0_scw.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_68_0_w4G.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_400_2_Opx.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_393_2_3Nd.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_426_2_eOW.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_520_0_5yn.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_229_0_FTW.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_435_2_47w.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_621_0_mri.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_412_2_mOf.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_430_2_Mha.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_425_2_lod.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_421_2_wpY.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_428_2_hER.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_387_2_pKD.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_386_2_UXj.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_372_2_vHm.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_20_2_JpY.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_572_0_zWJ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_546_0_u3I.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_366_0_Q3v.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_557_0_Z4C.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_308_2_AIQ.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_269_0_I7z.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_563_0_JEG.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_364_2_v7m.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_187_0_SNc.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_317_2_4kg.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_628_0_lhn.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_322_2_r0r.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_560_0_jSE.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_363_0_iPW.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_358_2_hSD.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_303_2_4Jy.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_340_2_ZKc.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_545_0_FuK.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_566_0_WzG.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_320_2_wgU.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_292_0_Q1c.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_352_2_zwR.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_347_2_bBW.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_304_2_chs.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_342_2_gOy.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_152_0_FMN.root',
'/store/user/fcostanz/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/ZJets_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_359_2_q5d.root'



)
)
