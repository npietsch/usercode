from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 41.92
process.weightProducer.NumberEvts = 3900171
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_t_channel_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_9_1_7qc.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_8_1_T25.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_80_1_LrK.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_7_4_HNR.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_79_1_jjT.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_78_2_2B3.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_77_1_ckx.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_76_1_Kvf.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_75_3_z2J.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_74_1_gPo.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_73_1_CgS.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_72_1_WHE.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_71_1_gKw.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_70_2_HX9.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_6_2_8y4.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_69_1_Bbz.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_68_2_BIJ.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_67_1_9Er.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_66_4_5oy.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_65_2_o8s.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_64_1_FVR.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_63_2_4RY.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_62_1_sx6.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_61_1_W6a.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_60_1_XcC.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_5_1_Vx1.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_59_2_FmL.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_58_1_GKH.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_57_1_K0t.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_56_1_eAY.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_55_1_Epu.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_54_1_d9Y.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_53_1_st5.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_52_2_GTa.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_51_1_uWh.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_50_3_aF2.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_4_1_t8F.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_49_1_Jeq.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_48_1_lFV.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_47_1_eFr.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_46_1_xQo.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_45_1_DZu.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_44_1_DDQ.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_43_1_YBt.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_42_1_Dn1.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_41_1_SKw.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_40_1_ohR.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_3_2_Fsv.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_39_2_alU.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_38_1_Ebe.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_37_1_uSa.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_36_1_esZ.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_35_1_www.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_34_2_aXA.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_33_1_nHG.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_32_2_RdR.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_31_1_VNo.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_30_1_yil.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_2_2_jRv.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_29_1_75Q.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_28_1_cql.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_27_1_j4u.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_26_1_g81.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_25_1_Bwf.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_24_1_4Iu.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_23_1_tcr.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_22_1_sTr.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_21_1_xLN.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_20_2_Cbm.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_1_1_vPD.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_19_4_HaS.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_18_1_Anl.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_17_1_5Hw.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_16_1_U48.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_15_1_s3x.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_14_1_HtE.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_13_1_FrI.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_12_1_9kp.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_11_2_gjJ.root',
        '/store/user/npietsch/T_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_10_1_DRw.root'
)
)
