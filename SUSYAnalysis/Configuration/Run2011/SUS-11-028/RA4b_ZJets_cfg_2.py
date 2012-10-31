#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 227 RA4b_ZJets_cfg_2.py
#----------------------------------------------------

from BjetsPAT_cfg import *

#process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_DYJetsToLL_TuneZ2_M_50_7TeV_madgraph_tauola.root"
#process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_DYJetsToLL_TuneZ2_M_50_7TeV_madgraph_tauola.root"
#process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_DYJetsToLL_TuneZ2_M_50_7TeV_madgraph_tauola.root"

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_ZJets.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_ZJets.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_ZJets.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_WJetsHT.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_WJetsHT.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_314_2_f45.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_254_1_PlU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_398_1_HP3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_141_1_xHB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_279_1_lv4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_36_2_obT.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_194_1_S30.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_260_1_erf.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_94_1_Yhl.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_273_1_TFM.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_397_1_piO.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_214_1_i1h.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_283_1_BGG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_274_1_qDp.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_84_1_HRH.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_418_1_9mi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_257_1_U7Z.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_405_1_p2z.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_346_1_juu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_258_1_GI4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_148_1_d6P.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_414_1_koE.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_340_1_a4U.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_256_1_IPe.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_189_1_vCk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_33_2_1eL.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_410_1_z9C.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_275_1_JEM.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_116_2_YMn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_321_1_Ln6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_127_1_426.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_235_1_BlR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_137_1_3o9.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_89_1_0i3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_411_1_W5c.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_41_2_pol.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_270_1_IhQ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_64_1_fmJ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_49_2_IBy.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_267_1_FgI.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_199_1_68X.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_396_1_ZRZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_349_1_qCC.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_353_1_CmK.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_323_1_xgd.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_152_1_j2P.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_341_1_zUk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_269_1_0zg.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_359_1_wtr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_277_1_2Wc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_80_1_PCU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_239_1_TDw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_65_1_n2l.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_400_1_K0G.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_251_1_lAQ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_417_1_T8E.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_142_1_XNw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_324_1_ioQ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_318_1_6nv.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_360_1_ywY.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_395_1_Kkk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_413_1_zE8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_81_1_4Pl.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_329_1_idR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_421_1_eq8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_134_1_jht.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_352_1_oBI.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_72_1_Zj6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_361_1_EfO.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_241_1_v4T.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_55_2_NNA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_68_1_7uR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_95_1_p15.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_193_1_UJu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_46_2_itn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_356_1_ENw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_43_2_jAI.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_420_1_yz4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_153_1_w5r.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_73_1_CeR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_320_1_JdF.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_79_1_FXE.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_252_1_O8x.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_327_1_WOc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_44_2_mUc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_403_1_MJA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_233_1_GNr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_82_1_cW6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_66_1_hhj.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_37_2_8Dj.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_52_2_zN8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_139_1_Xo8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_357_1_J8k.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_401_1_gZb.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_59_2_02M.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_78_1_WyE.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_317_1_4nR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_423_1_PSC.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_88_1_cI4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_243_1_ARb.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_67_1_BeX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_69_1_ijs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_51_2_7W3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_345_1_rUM.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_75_1_SAz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_147_1_Wxt.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_409_1_okU.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_92_1_ZDb.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_86_1_gA9.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_278_1_DLJ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_71_1_sGZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_339_1_jie.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_53_2_diu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_253_1_fIo.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_90_1_gsR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_209_1_cgh.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_227_1_f1J.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_232_1_FYC.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_229_1_XJS.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_200_1_1E5.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_348_1_jxe.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_236_1_lBb.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_204_1_H9M.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_326_1_hg8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_255_1_atk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_136_1_HCs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_128_1_Jns.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_336_1_M6F.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_242_1_pYe.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_143_1_1pZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_48_2_tW4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_230_1_Ekn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_138_1_j88.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_129_1_IGB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_362_1_xg0.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_151_1_lA4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_331_1_C9a.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_332_1_JzT.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_85_1_tbi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_196_1_m7R.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_91_1_7VA.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_144_1_NuZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_280_1_HYg.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_342_1_Yl8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_126_1_olM.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_42_2_DS4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_201_1_5bs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_412_1_He3.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_192_1_ajp.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_237_1_upW.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_330_1_qU7.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_215_1_i8y.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_191_1_XPP.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_76_1_aZj.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_110_2_hJ7.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_149_1_DFG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_54_2_IBY.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_216_1_xUR.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_47_2_8Xn.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_198_1_Xkx.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_344_1_2fu.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_245_1_PIG.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_207_1_KM4.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_125_1_Os5.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_333_1_afB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_422_1_m56.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_234_1_zMi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_35_2_Zpe.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_271_1_8SX.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_195_1_Sfc.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_130_1_VNY.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_154_1_XI0.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_347_1_e9p.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_211_1_quZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_150_1_sk6.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_217_1_xXm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_190_1_QCB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_264_1_Fxq.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_276_1_kWm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_335_1_9WK.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_325_1_B4h.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_281_1_38h.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_77_1_3l9.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_145_1_Ryw.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_351_1_Qwv.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_45_2_IGC.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_343_1_OyZ.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_334_1_OLr.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_262_1_sDo.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_228_1_ICY.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_337_1_x9O.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_197_1_Nhs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_156_1_SxB.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_146_1_dLi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_407_1_5hN.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_404_1_NDP.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_259_1_3Zg.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_406_1_ZpC.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_266_1_QK8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_205_1_NOm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_222_1_xop.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_231_1_Z25.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_322_1_jKm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_224_1_DK5.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_210_1_b4E.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_135_1_8zm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_83_1_H0p.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_40_2_PFi.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_155_1_eVK.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_74_1_XOx.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_218_1_uvm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_87_1_SGb.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_282_1_e0M.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_133_1_LFz.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_221_1_zwP.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_56_2_7m8.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_399_1_eQF.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_263_1_uvm.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_208_1_GOs.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_244_1_2af.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_206_1_4pe.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_39_2_JPk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_248_1_O1i.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_109_2_A72.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_212_1_Lsk.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_213_1_LTg.root',
'/store/user/schettle/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_250_1_lKh.root'
)
)
