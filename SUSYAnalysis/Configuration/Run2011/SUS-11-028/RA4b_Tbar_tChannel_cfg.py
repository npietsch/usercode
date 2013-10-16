#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 98 RA4b_Tbar_tChannel_cfg.py
#----------------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 22.65
process.weightProducer.NumberEvts = 1944826 
process.weightProducer.Lumi = 1000 ## Lumi in 1/p

#process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_t_channel_7TeV_powheg_tauola.root"
#process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_t_channel_7TeV_powheg_tauola.root"
#process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_t_channel_7TeV_powheg_tauola.root"

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_SingleTop.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_SingleTop.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_21_1_hS6.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_44_1_a5g.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_96_1_IlF.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_94_1_V8k.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_71_1_SAe.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_92_1_W0H.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_22_1_XHM.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_18_1_UsT.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_10_1_t1d.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_98_1_Gkt.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_31_1_1ft.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_3_1_Wne.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_93_1_lWa.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_16_1_U7N.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_83_1_5ZI.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_15_1_JQE.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_27_1_Md2.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_54_1_lxw.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_6_1_eXS.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_42_1_9Gg.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_20_1_KpT.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_17_1_P7q.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_52_1_Hqd.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_26_1_heJ.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_72_1_5bx.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_30_1_Pae.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_88_1_uvn.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_13_1_olP.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_56_1_WHd.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_57_1_L8V.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_41_1_9an.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_2_1_a7O.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_38_1_ZwR.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_89_1_cMF.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_37_1_xnr.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_4_1_Ktt.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_33_1_xVY.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_36_1_L3k.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_12_1_X39.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_65_1_w1l.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_7_1_tBc.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_14_1_ySm.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_55_1_1Hv.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_68_1_kjD.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_66_1_mYl.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_77_1_xvj.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_48_1_WVh.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_80_1_KCm.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_28_1_RM3.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_79_1_ri6.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_87_1_D6Q.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_11_1_Yke.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_75_1_IgQ.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_51_1_1gg.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_91_1_XL0.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_32_1_wf8.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_49_1_rF6.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_8_1_urw.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_70_1_luk.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_90_1_Mva.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_85_1_RIo.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_64_1_LVi.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_67_1_aZh.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_35_1_lg0.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_29_1_UJZ.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_39_1_Od8.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_62_1_GED.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_9_1_Nvb.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_23_1_WJe.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_59_1_u2n.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_63_1_hRh.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_58_1_ypv.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_76_1_taX.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_47_1_Q29.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_78_1_IVm.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_25_1_Ek1.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_61_1_ore.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_53_1_1Uv.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_81_1_dS8.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_1_1_SuU.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_40_1_d2B.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_60_1_Jkg.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_84_1_hNO.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_74_1_LZf.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_86_1_NuV.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_50_1_f9u.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_46_1_w54.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_73_1_cdW.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_24_1_Vvl.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_69_1_2up.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_34_1_fs8.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_82_1_hvk.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_97_1_m6h.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_43_1_cPE.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_5_1_HNW.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_45_1_hHX.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_95_1_y7d.root',
'/store/user/schettle/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_19_1_kKv.root'
)
)
