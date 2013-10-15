#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 14 RA4b_Top_sChannel_cfg.py
#----------------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 3.19
process.weightProducer.NumberEvts = 259971
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

#process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
#process.eventWeightPUUp.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"
#process.eventWeightPUDown.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop_new.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop_new.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_SingleTop_new.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_SingleTop.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_SingleTop.root"

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
