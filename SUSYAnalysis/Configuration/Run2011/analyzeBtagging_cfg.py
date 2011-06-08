import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')

# Choose input files
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_9_1_V6M.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_99_1_e1y.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_98_1_dkY.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_97_1_OlA.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_96_1_WNq.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_95_1_CcU.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_94_1_Yf5.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_93_1_pe9.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_92_1_dPG.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_91_1_574.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_90_1_Vy5.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_8_1_hvA.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_89_1_xc7.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_88_1_NSs.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_87_1_WwP.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_86_1_qli.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_85_1_uJX.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_84_1_Vkq.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_83_1_x05.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_82_1_j7U.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_81_1_To6.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_80_1_bly.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_7_1_KR8.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_79_1_9OM.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_78_1_E4P.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_77_1_kXc.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_76_1_lKr.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_75_1_94F.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_74_1_qxz.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_73_1_zIV.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_72_1_Ac9.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_71_1_jJ0.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_70_1_UAL.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_6_1_fUc.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_69_1_NRw.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_68_1_2cd.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_67_1_huj.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_66_1_Ygy.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_65_1_WcU.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_64_1_ts2.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_63_1_sPI.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_62_1_nND.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_61_1_WZ0.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_60_1_5R3.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_5_1_n1F.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_59_1_DEG.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_58_1_PZ3.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_57_1_Ie1.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_56_1_Xm6.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_55_1_36Q.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_54_1_k11.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_53_1_NcT.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_52_1_GSw.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_51_1_qHi.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_50_1_TCB.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_4_1_v1S.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_49_1_X9h.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_48_1_nar.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_47_1_DRD.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_46_1_Ore.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_45_1_yoB.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_44_1_BtU.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_43_1_RJ9.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_42_1_nRC.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_41_1_0yN.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_40_1_iCP.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_3_1_Tdu.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_39_1_8yx.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_38_1_xTs.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_37_1_mMF.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_36_1_5C5.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_35_1_vBb.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_34_1_cxF.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_33_1_50Q.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_32_1_JlV.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_31_1_YOO.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_30_1_cdp.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_2_1_V48.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_29_1_Wp0.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_28_1_4fp.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_27_1_60m.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_26_1_scn.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_25_1_s2X.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_24_1_jJ5.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_23_1_rns.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_22_1_Frx.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_21_1_8Yt.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_20_1_tkI.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_1_1_JWe.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_19_1_WPY.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_18_1_9ts.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_17_1_Srj.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_16_1_2LR.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_15_1_pMB.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_14_1_JxM.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_13_1_aWK.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_130_1_4DL.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_12_1_VPy.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_129_1_RQC.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_128_1_Mez.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_127_1_G90.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_126_1_2p8.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_125_1_PBh.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_124_1_Bdl.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_123_1_3uI.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_122_1_EHX.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_121_1_D1q.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_120_1_dKh.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_11_1_dtg.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_119_1_ZTG.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_118_1_LGa.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_117_1_ZPm.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_116_1_Gmw.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_115_1_frC.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_114_1_doM.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_113_1_Ei5.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_112_1_CSQ.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_111_1_ATu.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_110_1_CTg.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_10_1_Pik.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_109_1_hfi.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_108_1_Cnw.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_107_1_irM.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_106_1_8aB.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_105_1_5LX.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_104_1_Fmu.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_103_1_oSS.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_102_1_Omr.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_101_1_cte.root',
    '/store/user/npietsch/TTJets_TuneD6T_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_100_1_lx8.root'
    )
)

#-------------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
#       - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
#       - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-------------------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

#from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
#process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

#from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
#process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
#process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis2_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#------------------------
# Selection paths
#------------------------

## exactly one good lepton - ttbar signal
process.Signal1l = cms.Path(process.makeObjects *
                            process.makeSUSYGenEvt *
                            process.preselectionSemiLepTTBar *
                            process.LepHadSelection *
                            process.oneGoodLepton *
                            process.oneVetoMuon *
                            process.noVetoElectron *
                            process.fourLooseJets *
                            process.twoMediumJets *
                            process.analyzeSUSYBjets1l_1 *
                            process.HTSelection *
                            process.analyzeSUSYBjets1l_2 *
                            process.metSelection *
                            process.analyzeSUSYBjets1l_3
                            )

##  exactly one good lepton - other ttbar
process.Other1l = cms.Path(process.makeObjects *
                           process.makeSUSYGenEvt *
                           process.preselectionOtherTTBar *
                           process.LepHadSelection *
                           process.oneGoodLepton *
                           process.oneVetoMuon *
                           process.noVetoElectron *
                           process.fourLooseJets *
                           process.twoMediumJets *
                           process.analyzeSUSYBjets1l_4 *
                           process.HTSelection *
                           process.analyzeSUSYBjets1l_5 *
                           process.metSelection *
                           process.analyzeSUSYBjets1l_6
                           )

## at least two good leptons - ttbar signal
process.Signal2l = cms.Path(process.makeObjects *
                            process.makeSUSYGenEvt *
                            process.preselectionFullLepTTBar *
                            process.LepHadSelection *
                            process.twoGoodLeptons *
                            process.twoMediumJets*
                            process.analyzeSUSYBjets2l_1 *
                            process.HTSelection *
                            process.analyzeSUSYBjets2l_2 *
                            process.metSelection *
                            process.analyzeSUSYBjets2l_3
                               )

## at least two good leptons - other ttbar
process.Other2l = cms.Path(process.makeObjects *
                           process.makeSUSYGenEvt *
                           process.preselectionOtherTTBar2 *
                           process.LepHadSelection *
                           process.twoGoodLeptons *
                           process.twoMediumJets*
                           process.analyzeSUSYBjets2l_1 *
                           process.HTSelection *
                           process.analyzeSUSYBjets2l_2 *
                           process.metSelection *
                           process.analyzeSUSYBjets2l_3
                           )
