from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 7.87
process.weightProducer.NumberEvts = 787629
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_tW_channel_DR_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_9_1_ehU.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_8_1_Hhj.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_7_1_wwZ.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_6_1_y9w.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_5_1_0i6.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_4_1_fQW.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_3_1_kRd.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_2_1_PvW.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_1_1_uUQ.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_17_1_yPp.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_16_1_3cO.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_15_1_47O.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_14_1_Hv4.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_13_1_w5y.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_12_1_b5X.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_11_1_KBV.root',
        '/store/user/npietsch/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_10_1_TVN.root'
)
)
