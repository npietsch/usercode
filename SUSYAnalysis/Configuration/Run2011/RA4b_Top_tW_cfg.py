from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 7.87
process.weightProducer.NumberEvts = 814390
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_tW_channel_DR_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_9_1_pzu.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_8_1_JOn.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_7_1_Hpl.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_6_1_2NY.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_5_1_0li.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_4_1_i7l.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_42_1_pRq.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_41_1_bHC.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_40_1_InA.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_3_1_IfG.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_39_1_aXt.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_38_1_Yee.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_37_1_Utk.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_36_1_nQb.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_35_1_5Ma.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_34_1_LCL.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_33_1_wq9.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_32_1_ptf.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_31_1_NLH.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_30_1_L20.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_2_1_7wk.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_29_1_VrF.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_28_1_hhQ.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_27_1_mza.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_26_1_MSO.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_25_1_uen.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_24_1_bVi.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_23_1_Mmh.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_22_1_x9r.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_21_1_JT3.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_20_1_z1W.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_1_1_YX1.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_19_1_VK6.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_18_1_osG.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_17_1_Aps.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_16_1_oDO.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_15_1_X21.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_14_1_XB9.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_13_1_p8y.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_12_1_bll.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_11_1_mki.root',
        '/store/user/npietsch/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_10_1_AnF.root'
)
)
