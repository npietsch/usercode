#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 218 RA4b_QCD1_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 2.213E+10
process.weightProducer.NumberEvts = 10715600
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

#process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/MC_PUDist_Summer11_QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6.root"
#process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/MC_PUDist_Summer11_QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6.root"
#process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/MC_PUDist_Summer11_QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6.root"

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_QCD.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_QCD.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_QCD.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

#process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/QCD.root"
#process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/QCD.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_184_1_4Rg.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_311_1_SFv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_167_1_s1R.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_190_1_xNB.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_306_1_mMy.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_8_1_w2f.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_393_1_L6a.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_165_1_smW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_202_1_N0b.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_292_1_7Z3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_357_1_9od.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_318_1_zY2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_295_1_Rj1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_181_1_fkZ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_208_1_6bm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_361_1_SzH.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_117_0_3T0.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_172_1_Yi5.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_170_1_hmP.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_328_1_EbF.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_149_1_E7B.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_158_1_z8q.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_320_1_ESz.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_22_1_r3i.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_445_1_6l8.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_342_1_Tqw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_171_1_qhZ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_140_1_fCX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_360_1_9r1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_205_1_76o.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_310_1_DKe.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_338_1_7s1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_185_1_i5i.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_334_1_4Un.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_309_1_kmS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_351_1_87w.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_135_1_ZKR.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_380_1_p1G.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_303_1_BvR.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_429_1_rx1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_61_0_MbW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_340_1_8k7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_438_1_zGA.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_211_1_YXM.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_214_0_mGZ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_221_0_Q3M.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_301_1_a7C.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_198_1_Trp.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_207_1_2rT.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_443_1_Rsl.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_63_0_nL0.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_186_1_KH4.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_385_1_c39.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_188_1_Qe2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_307_1_VnU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_13_1_aZW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_2_1_wD4.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_23_1_toc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_440_1_hgo.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_366_0_ve8.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_324_1_eJY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_134_1_PDI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_421_1_bIQ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_364_0_muc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_288_1_opb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_136_1_1zc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_144_1_8e6.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_294_1_IL1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_333_1_C8H.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_212_0_0xf.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_6_1_eQh.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_369_0_p3a.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_399_1_iFj.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_435_1_TXC.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_179_1_yRC.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_329_1_xa2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_130_0_7xh.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_193_1_CGI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_347_1_fTA.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_189_1_8CH.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_201_1_Suy.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_176_1_uD2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_153_1_Kaq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_431_1_SC4.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_59_0_PqL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_187_1_QAr.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_376_0_CHk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_137_1_96T.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_426_1_Nlp.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_243_0_hSA.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_178_1_2Jh.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_341_1_3Rn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_139_1_gOv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_365_0_RmB.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_150_1_c0T.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_19_1_Xvq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_168_1_LDf.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_355_1_GDw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_197_1_Ttg.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_129_0_UHO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_332_1_oW7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_191_1_yAv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_28_0_EXb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_85_0_P62.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_209_1_WgU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_44_0_dgJ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_77_0_sKt.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_266_0_axT.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_40_0_OHY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_86_0_kTk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_110_0_Z9r.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_281_0_u6x.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_273_0_l9K.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_371_0_jTS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_98_0_thw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_199_1_Pdu.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_282_0_NMb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_397_1_S70.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_381_1_3gH.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_400_1_al5.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_395_1_i5i.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_196_1_d85.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_331_1_ykV.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_415_1_9pQ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_436_1_mlB.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_401_1_vtv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_94_0_3td.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_370_0_g9j.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_29_0_ygU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_283_0_2Rm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_218_0_bUG.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_368_0_ARs.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_227_0_PjL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_65_0_Dlm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_120_0_Ue3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_419_1_Kzx.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_78_0_8cX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_81_0_1i8.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_32_0_9sE.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_112_0_788.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_105_0_jnb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_348_1_Anr.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_275_0_PiG.root',
 '/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_432_1_jBB.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_159_1_QHe.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_11_1_eQI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_319_1_ejm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_21_1_TEI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_157_1_F8E.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_358_1_NL0.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_404_1_bmW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_321_1_7FU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_133_1_rHf.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_220_0_Ovk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_308_1_ugd.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_349_1_Ltp.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_177_1_vot.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_442_1_vlb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_92_0_x6o.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_152_1_Lkq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_97_0_PuI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_147_1_qJR.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_210_1_UQN.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_148_1_aj9.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_166_1_Mri.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_17_1_rI2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_9_1_BS1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_305_1_f5M.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_5_1_NlB.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_299_1_1hb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_175_1_tSS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_323_1_Ltp.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_297_1_5nb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_352_1_vf6.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_4_1_kdL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_386_1_cWl.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_345_1_1Yi.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_3_1_WrX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_108_0_Ytm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_293_1_QzQ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_290_1_9lX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_373_0_JUV.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_204_1_giw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_296_1_1Oi.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_391_1_NTd.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_359_1_mLc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_174_1_jzE.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_433_1_jkh.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_284_0_1cM.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_291_1_RAn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_192_1_l3S.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_246_0_fBG.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_316_1_0JI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_382_1_odL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_183_1_Kzq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_350_1_ZMh.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_200_1_P01.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_203_1_5tX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_132_1_eyR.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_444_1_0b0.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_173_1_Str.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_285_0_Oc1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_128_0_NnF.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_30_0_T88.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_160_1_U87.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_138_1_TpD.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_249_0_sTv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_261_0_ZlF.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_253_0_cIO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_289_1_Ndn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_96_0_4qC.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_387_1_iJg.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_156_1_3cO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_88_0_wQa.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_312_1_Cjc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_180_1_fPQ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_326_1_E8i.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_102_0_clA.root'   
)
)