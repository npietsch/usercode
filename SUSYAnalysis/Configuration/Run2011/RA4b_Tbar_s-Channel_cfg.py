from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.44
process.weightProducer.NumberEvts = 137980
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_s_channel_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
            '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_8_1_u5r.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_7_1_gST.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_6_1_IlY.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_5_1_V6m.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_4_1_5xj.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_3_1_vP7.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_2_1_OoV.root',
        '/store/user/npietsch/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_1_2_mhx.root'

)
)
