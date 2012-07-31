#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 37 RA4b_Top_tW_cfg.py
#----------------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 7.87
process.weightProducer.NumberEvts = 814390
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

#process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_tW_channel_DR_7TeV_powheg_tauola.root"
#process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_tW_channel_DR_7TeV_powheg_tauola.root"
#process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_tW_channel_DR_7TeV_powheg_tauola.root"

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/SingleTop.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/SingleTop.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_fLf.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_VZ0.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_4_1_cpS.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_xe8.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_9_1_Ofn.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_11_1_vUn.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_10_1_y4M.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_14_1_DN9.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_12_1_Ir7.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_16_1_Vkl.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_31_1_m7k.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_13_1_LPF.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_5_1_v5G.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_18_1_6sk.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_17_1_ppX.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_19_1_zDZ.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_27_1_hVZ.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_21_1_Mm7.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_6_1_1LW.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_28_1_5rp.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_15_1_F3c.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_20_1_ZZy.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_23_1_Qco.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_22_1_gx5.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_33_1_K4A.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_32_1_Cw6.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_36_1_Y5j.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_24_1_sbP.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_29_1_NSp.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_26_1_1CP.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_39_1_bdm.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_38_1_ZW2.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_naP.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_35_1_OH6.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_30_1_4ar.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_42_1_HkD.root',
'/store/user/schettle/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_7_1_2ds.root'
)
)
