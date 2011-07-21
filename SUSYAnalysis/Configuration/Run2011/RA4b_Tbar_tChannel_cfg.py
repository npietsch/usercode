from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 22.65
process.weightProducer.NumberEvts = 1944826 
process.weightProducer.Lumi = 1000  ## Lumi in 1/p

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleAntiTop_TuneZ2_t_channel_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
            '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_9_1_8PX.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_98_1_S4F.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_97_1_Fq2.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_96_1_eSo.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_95_1_UjR.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_94_1_n71.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_93_1_hKT.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_92_1_5CL.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_91_1_NUX.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_90_1_IQ2.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_8_1_4wb.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_89_1_4hV.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_88_1_A0H.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_87_1_ehD.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_86_1_0qv.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_85_1_gtJ.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_84_1_i0O.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_83_1_622.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_82_1_Ww0.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_81_1_Kg9.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_80_1_h32.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_7_1_nnE.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_79_1_uOT.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_78_1_DKR.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_77_1_YNF.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_76_1_9pe.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_75_1_WZx.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_74_1_uD8.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_73_1_lOa.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_72_1_hoV.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_71_1_clX.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_70_1_2Cc.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_6_1_3p0.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_69_1_SBD.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_68_1_OLk.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_67_1_lKg.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_66_1_nYY.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_65_1_vkC.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_64_1_HQo.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_63_1_tDs.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_62_1_1Xk.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_61_1_vP6.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_60_1_aV1.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_5_1_P5x.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_59_1_Eor.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_58_1_rwd.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_57_1_Blc.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_56_1_FRG.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_55_1_fZd.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_54_1_3j8.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_53_1_EHC.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_52_1_n1X.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_51_1_Zrk.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_50_1_Ekj.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_4_1_B3v.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_49_1_oVa.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_48_1_cvu.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_47_1_75z.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_46_1_4mf.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_45_1_EWk.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_44_1_ChG.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_43_1_Z3A.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_42_1_XRu.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_41_1_Q6p.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_40_1_VSV.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_3_1_8wi.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_39_1_Yhf.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_38_1_5IF.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_37_1_o6P.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_36_1_H9n.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_35_1_P8x.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_34_1_ku4.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_33_1_PVE.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_32_1_Aww.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_31_1_W8r.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_30_1_Dqo.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_2_1_ecS.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_29_1_jtB.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_28_1_bGq.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_27_1_QAA.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_26_1_H8k.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_25_1_31c.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_24_1_pm3.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_23_1_U3x.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_22_1_ulc.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_21_1_9HR.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_20_1_Qpf.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_1_1_Ele.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_19_1_dWk.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_18_1_mDN.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_17_1_WLy.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_16_1_Mg5.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_15_1_SK6.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_14_1_7fG.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_13_1_knZ.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_12_1_qxT.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_11_1_9ck.root',
        '/store/user/npietsch/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/PAT/d33b50267c88e620c112aadc5d05059b/Summer11_10_1_6dC.root'
)
)
