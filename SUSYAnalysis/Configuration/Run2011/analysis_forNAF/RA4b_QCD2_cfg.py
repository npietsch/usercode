#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 16 RA4b_LM13_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 2.213E+10
process.weightProducer.NumberEvts = 10715600
process.weightProducer.Lumi = 1000 ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/MC_PUDist_Summer11_QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6.root"
process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/MC_PUDist_Summer11_QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6.root"
process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/MC_PUDist_Summer11_QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_131_0_a0h.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_36_0_iIT.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_49_0_21Q.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_37_0_BIX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_287_0_gDW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_363_0_Ted.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_60_0_8ev.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_425_1_XIe.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_427_1_gET.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_346_1_98V.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_225_0_yM0.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_276_0_I9l.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_93_0_XYT.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_52_0_E5p.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_103_0_6Ch.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_406_1_riW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_83_0_4dt.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_392_1_Vge.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_375_0_Wub.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_104_0_rwr.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_43_0_AEi.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_91_0_XNI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_45_0_AVN.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_240_0_x1Z.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_126_0_S31.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_73_0_y1j.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_26_0_oov.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_258_0_n4O.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_82_0_N6A.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_362_1_o3t.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_447_1_pBw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_50_0_sQ1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_271_0_Dvz.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_223_0_qus.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_90_0_J47.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_410_1_HjY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_39_0_bXd.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_68_0_4lI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_75_0_keU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_267_0_c2G.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_71_0_X41.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_79_0_CHW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_48_0_ZBk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_113_0_XMk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_402_1_cms.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_27_0_bDM.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_226_0_SnX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_417_1_Y4g.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_237_0_gbv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_420_1_hSg.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_99_0_8lU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_238_0_iwA.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_229_0_gYr.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_80_0_hUO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_57_0_CL3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_111_0_nTS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_122_0_y90.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_277_0_525.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_272_0_e6w.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_228_0_pps.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_241_0_205.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_251_0_LYw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_230_0_lGv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_51_0_iwx.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_378_0_XFK.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_42_0_5Vv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_235_0_K9Z.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_100_0_wkb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_58_0_xeI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_215_0_eiv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_33_0_7f5.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_256_0_H8J.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_41_0_Cs2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_64_0_Tqc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_53_0_9cM.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_280_0_K1v.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_411_1_7fO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_250_0_13s.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_12_1_uNb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_109_0_oY7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_217_0_hLq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_236_0_tFd.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_35_0_z7i.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_72_0_4pF.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_124_0_cSk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_213_0_xn1.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_264_0_WNx.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_47_0_kCY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_219_0_JJr.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_286_0_FNy.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_74_0_fTL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_115_0_eWb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_389_1_kDg.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_263_0_v75.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_408_1_P9r.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_374_0_GnL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_14_1_GZs.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_259_0_TmL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_262_0_AHr.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_274_0_U5K.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_106_0_bpP.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_62_0_2E7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_279_0_9NY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_24_1_66S.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_84_0_a9j.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_247_0_Yiw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_127_0_Bvx.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_407_1_oLY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_377_0_YXq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_70_0_BF4.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_379_0_BMF.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_222_0_zeu.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_118_0_2FU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_46_0_OfX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_248_0_Fah.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_394_1_Bab.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_372_0_NqW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_69_0_bwM.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_428_1_mxz.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_260_0_zza.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_418_1_aAJ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_409_1_I0c.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_430_1_jUY.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_231_0_Mqt.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_31_0_EuP.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_265_0_EgI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_384_1_4aH.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_89_0_kAm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_414_1_9we.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_255_0_lH9.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_56_0_bxH.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_242_0_Aq8.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_25_0_dj9.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_233_0_XG3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_114_0_JZI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_343_1_5Px.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_7_1_Eri.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_416_1_S4L.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_403_1_PON.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_101_0_gof.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_269_0_iQ2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_270_0_lYw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_245_0_dVc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_325_1_tYw.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_405_1_6aO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_67_0_U8W.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_76_0_NFT.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_116_0_95m.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_254_0_X5i.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_154_1_ZuJ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_216_0_H7v.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_194_1_fNJ.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_423_1_NVS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_224_0_y2t.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_244_0_XfP.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_422_1_Sbt.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_15_1_mK3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_66_0_Nfp.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_396_1_ari.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_125_0_Hmt.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_413_1_4lv.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_232_0_csG.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_123_0_z1Q.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_339_1_LQs.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_145_1_Fg9.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_335_1_Yy7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_146_1_ICP.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_87_0_SSq.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_34_0_pHc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_441_1_u1l.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_344_1_v9b.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_121_0_esu.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_234_0_dGU.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_195_1_dpa.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_367_0_mdn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_18_1_xG6.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_439_1_N67.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_257_0_WZj.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_383_1_3jS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_424_1_ieL.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_304_1_hnX.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_336_1_1LI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_107_0_eUb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_314_1_LJF.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_155_1_Yvt.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_448_1_MFl.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_164_1_ihT.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_446_1_xFm.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_390_1_hFI.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_239_0_QCO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_16_1_LKS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_95_0_P1F.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_38_0_pQz.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_182_1_9jo.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_412_1_zQe.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_337_1_Ty2.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_151_1_si7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_449_1_nOb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_322_1_eFu.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_169_1_vF5.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_1_1_GKj.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_317_1_mca.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_119_0_7nG.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_54_0_Ei3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_20_1_6Sn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_206_1_d0X.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_356_1_Usi.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_142_1_v3d.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_10_1_Pec.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_315_1_DFl.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_388_1_9Pc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_298_1_nIS.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_55_0_LOD.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_398_1_C0T.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_330_1_WQ3.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_278_0_vum.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_353_1_zMn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_434_1_kGu.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_302_1_tSf.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_268_0_7RO.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_141_1_H08.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_143_1_xW7.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_163_1_C5y.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_252_0_kbk.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_354_1_PfP.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_437_1_sdc.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_300_1_qVW.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_313_1_019.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_161_1_hsn.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_162_1_uSb.root',
'/store/user/dhorton/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/SUSYPAT2/d81d81f7c5973c60c0add93b95511b5f/Summer11_327_1_DHG.root'
    

  )
)
