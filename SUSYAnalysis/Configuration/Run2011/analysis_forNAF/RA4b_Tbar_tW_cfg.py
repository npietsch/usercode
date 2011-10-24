from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.44
process.weightProducer.NumberEvts = 787629
process.weightProducer.Lumi = 3000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_tW_channel_DR_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_29_1_2ko.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_32_1_yno.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_33_1_MsW.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_36_1_leB.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_10_1_9EY.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_30_1_M4C.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_39_1_1ar.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_22_1_FE3.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_34_1_yhy.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_38_1_Z6K.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_35_1_9RC.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_37_1_ONZ.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_31_1_E0B.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_40_1_a7F.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_21_1_Tra.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_RcA.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_cg4.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_6_1_TvO.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_4_1_pGa.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_7_1_NRZ.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_Vtw.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_5_1_Fdr.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_11_1_Rde.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_12_1_oUL.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_15_1_qgW.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_14_1_q4h.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_13_1_p9B.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_19_1_MJr.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_17_1_p0R.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_25_1_EH6.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_9_1_ref.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_18_1_Kzy.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_16_1_fBh.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_41_1_25x.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_20_1_Upe.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_24_1_rJO.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_23_1_5lQ.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_27_1_iR0.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_MQD.root',
'/store/user/schettle/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_28_1_BAL.root'

)
)
