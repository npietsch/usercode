from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 3.19
process.weightProducer.NumberEvts = 259971
process.weightProducer.Lumi = 2000  ## Lumi in 1/pb

## PU histogram has to be updated
process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"


# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_10_1_zy2.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_11_1_0Bh.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_12_1_hC0.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_13_1_7Al.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_14_1_PN4.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_1_1_Nv0.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_2_1_KTx.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_3_1_Q2I.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_4_1_Ww5.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_5_1_AMr.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_6_1_fme.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_7_1_49q.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_8_1_bHv.root',
'/store/user/schettle/T_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/d81d81f7c5973c60c0add93b95511b5f/Summer11_9_1_S44.root'
)
)
