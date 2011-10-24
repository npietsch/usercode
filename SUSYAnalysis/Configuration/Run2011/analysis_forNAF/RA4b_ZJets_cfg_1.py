from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_DYJetsToLL_TuneZ2_M_50_7TeV_madgraph_tauola.root"


# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_63_2_LJu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_305_1_GrJ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_371_1_0me.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_297_1_NPk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_173_1_kev.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_452_1_jTR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_185_1_8FR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_369_1_P41.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_159_1_Ihr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_101_1_Z6h.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_184_1_H38.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_394_1_AGZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_381_1_fsa.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_389_1_aS5.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_20_1_ZQP.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_441_1_f48.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_120_1_0R1.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_177_1_WKY.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_123_1_bAB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_175_1_FvR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_296_1_h7p.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_168_1_9gs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_167_1_Q9m.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_118_1_WhN.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_447_1_YfK.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_456_1_xzL.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_107_1_PTu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_444_1_vCs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_171_1_u3T.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_393_1_4YG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_176_1_7uA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_27_1_S36.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_166_1_yMV.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_119_1_EP0.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_99_1_nDn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_169_1_oR3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_31_1_j3y.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_431_1_3pP.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_272_1_Dgq.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_268_1_jlo.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_38_2_04r.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_61_2_CVR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_70_1_Mhq.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_240_1_oIz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_226_1_lDi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_34_2_Yqn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_58_2_WRX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_247_1_JkH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_265_1_KQ2.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_408_1_lSQ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_246_1_wpk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_203_1_UEz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_186_1_3HP.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_285_1_A5P.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_29_1_Ept.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_288_1_YKH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_113_1_wVj.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_30_1_fYU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_384_1_Pz4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_174_1_5LU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_21_1_ApD.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_301_1_pNr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_3_1_GN1.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_181_1_MRp.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_315_1_SSl.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_306_1_1tc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_157_1_UPM.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_165_1_i87.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_115_1_K0b.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_435_1_dMm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_23_1_Txs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_450_1_OwX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_453_1_NY0.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_436_1_0xB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_451_1_ynJ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_377_1_yHL.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_122_1_274.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_18_1_JHE.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_290_1_PyG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_164_1_HEl.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_294_1_Xjz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_11_1_Ywy.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_1_1_vSc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_367_1_bJO.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_366_1_Orr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_105_1_Fk8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_9_1_D70.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_428_1_KTG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_302_1_mTD.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_32_1_zNo.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_307_1_rbw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_114_1_COn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_459_1_aWS.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_370_1_vOi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_308_1_OXw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_15_1_i0j.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_117_1_mFK.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_454_1_L8e.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_289_1_x9q.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_304_1_yg4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_310_1_pW6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_449_1_VDi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_98_1_WfO.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_160_1_M8T.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_7_1_w5k.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_172_1_Zu8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_5_1_tqT.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_455_1_pOA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_2_1_FXz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_158_1_5t5.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_14_1_76e.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_295_1_d0H.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_303_1_EdG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_372_1_HV1.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_183_1_XSx.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_383_1_Ssu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_24_1_IvR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_433_1_FQJ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_300_1_g5j.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_102_1_jTC.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_112_1_GBE.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_17_1_OPX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_368_1_sbZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_188_1_NEr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_121_1_0oH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_391_1_C5b.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_427_1_wE1.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_293_1_z9m.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_374_1_Mp3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_388_1_mW6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_111_1_Fm6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_375_1_XzR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_187_1_FzA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_103_1_xaJ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_97_1_1xw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_106_1_txp.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_457_1_Ygh.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_4_1_6qu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_430_1_1Nm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_16_1_uJ7.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_438_1_Cpj.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_28_1_r6O.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_26_1_snH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_311_1_fdl.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_286_1_2vh.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_25_1_mEI.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_8_1_yC4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_429_1_XdA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_19_1_DAa.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_22_1_2AG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_292_1_FKG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_10_1_xI4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_170_1_nY5.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_382_1_pug.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_363_1_vZg.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_446_1_Meu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_442_1_ZMW.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_12_1_Fn3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_104_1_qTX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_162_1_Skw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_390_1_Qwd.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_108_1_Rjc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_364_1_iUh.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_161_1_L5S.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_437_1_euW.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_13_1_rdl.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_178_1_LkZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_6_1_peU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_100_1_xIr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_373_1_z4G.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_440_1_Cok.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_309_1_EM3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_443_1_7Vs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_448_1_cpD.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_378_1_mC3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_287_1_JMB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_179_1_VLN.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_445_1_Vcx.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_298_1_kWG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_316_1_eCH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_385_1_LBp.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_432_1_kt7.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_434_1_BVd.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_380_1_7kT.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_163_1_JRZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_291_1_0QX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_379_1_YV6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_392_1_Iol.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_386_1_W6w.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_439_1_Kr2.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_365_1_Kix.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_182_1_TmR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_387_1_uod.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_376_1_q5u.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_313_1_otR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_180_1_pfG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_312_1_xzz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_299_1_duU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_96_1_Fdb.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_458_1_DOR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_124_1_WXH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_249_1_Y1u.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_238_1_Yo0.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_419_1_Uf9.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_219_1_MYh.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_223_1_Qmi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_202_1_Rq4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_225_1_yHf.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_354_1_7VO.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_220_1_Z3Q.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_425_1_uO1.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_140_1_7kH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_416_1_Aqo.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_402_1_SZ3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_284_1_Jb8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_131_1_bWz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_261_1_Dee.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_424_1_7N2.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_426_1_yEd.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_350_1_KNg.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_338_1_Zf8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_328_1_75r.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_358_1_ul3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_319_1_SaU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_132_1_jzh.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_50_2_SJd.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_355_1_Ex2.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_415_1_AVD.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_62_2_s01.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_60_2_BEf.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_57_2_3HU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_93_1_o9Q.root'



)
)
