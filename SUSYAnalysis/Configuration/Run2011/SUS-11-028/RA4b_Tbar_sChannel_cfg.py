#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 8 RA4b_Tbar_sChannel_cfg.py
#----------------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.44
process.weightProducer.NumberEvts = 137980
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

#process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
#process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
#process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"

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