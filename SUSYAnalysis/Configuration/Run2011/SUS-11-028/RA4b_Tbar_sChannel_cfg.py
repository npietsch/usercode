from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.44
process.weightProducer.NumberEvts = 137980
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/SingleTop.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_5_1_1Kt.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_7Kl.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_6_1_TyY.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_7_1_3Le.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_qhh.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_4_1_rJ6.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_BDi.root',
'/store/user/schettle/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_94x.root'

)
)
