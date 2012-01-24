import FWCore.ParameterSet.Config as cms

process = cms.Process("AnalyzeSystematics") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
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
                                   fileName = cms.string('AnalyzeSystematics.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START42_V13::All')

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_9_1_etL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_99_1_xJ5.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_98_1_t7j.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_97_1_ziv.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_96_1_qKp.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_95_1_x3I.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_94_1_UxC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_93_1_L0X.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_92_1_91X.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_91_1_2Ee.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_90_1_bWe.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_fv3.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_89_1_J6z.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_88_1_fq3.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_87_1_NE7.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_86_1_OG0.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_85_1_VQ6.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_84_1_YNG.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_83_1_sHP.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_82_1_1HH.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_81_1_0Pq.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_80_1_sx2.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_7_1_kzD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_79_1_Mnx.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_78_1_07s.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_77_1_iwz.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_76_1_jkk.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_75_1_jPq.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_74_1_qVd.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_73_1_Yvt.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_72_1_Is6.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_71_1_Giq.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_70_1_X9X.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_6_1_NLd.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_69_1_Rlc.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_68_1_FLe.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_67_1_apg.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_66_1_BuZ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_65_1_lTZ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_64_1_oya.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_63_1_UM7.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_62_1_TGQ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_61_1_ioL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_60_1_Vkb.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_5_1_ZWg.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_59_1_XyX.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_58_1_Esx.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_57_1_UMO.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_56_1_hM5.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_55_1_ZDW.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_54_1_BJq.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_53_1_Zxn.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_52_1_fuL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_51_1_GX3.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_50_1_SUQ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_4_1_HsJ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_49_1_4Hv.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_48_1_LQg.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_47_1_Vou.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_46_1_BRA.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_45_1_XW1.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_44_1_xPh.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_43_1_Uc2.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_42_1_gVs.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_41_1_k5m.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_40_1_A1s.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_A3P.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_39_1_q38.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_38_1_Jkc.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_37_1_WrD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_36_1_ka9.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_35_1_QYg.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_34_1_Htz.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_33_1_RTb.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_32_1_caP.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_31_1_WzT.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_30_1_4lx.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_mtN.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_29_1_JHx.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_28_1_ASY.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_27_1_1Hi.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_26_1_V8b.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_25_1_CRH.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_24_1_fYQ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_23_1_Mag.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_235_1_H7A.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_234_1_SCm.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_233_1_d20.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_232_1_TXE.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_231_1_dkl.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_230_1_vgD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_22_1_iRe.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_229_1_yMc.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_228_1_OcY.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_227_1_wy8.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_226_1_k5Z.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_225_1_GtF.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_224_1_06O.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_223_1_Lu7.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_222_1_SYn.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_221_1_QpM.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_220_1_BLy.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_21_1_d7R.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_219_1_eiV.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_218_1_MZ5.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_217_1_1v5.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_216_1_xTA.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_215_1_DJc.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_214_1_BCe.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_213_1_Qts.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_212_1_Gx3.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_211_1_20a.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_210_1_1nm.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_20_1_5Np.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_209_1_Pec.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_208_1_07t.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_207_2_90E.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_206_1_HE2.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_205_1_XrC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_204_1_jJZ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_203_1_hRM.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_202_1_N8H.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_201_1_T73.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_200_1_q5g.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_5Ad.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_19_1_eft.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_199_1_xOi.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_198_1_K4I.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_197_1_CBl.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_196_1_jKJ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_195_1_fLL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_194_1_keU.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_193_1_C8m.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_192_1_ZMt.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_191_1_jyj.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_190_1_SK6.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_18_1_eiJ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_189_1_Am9.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_188_1_enG.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_187_1_RIC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_186_1_wls.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_185_1_to8.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_184_1_hlw.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_183_1_CF7.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_182_1_vMB.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_181_1_Axz.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_180_1_2h5.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_17_1_Twg.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_179_1_7uc.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_178_1_3gq.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_177_1_G1v.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_176_1_fRC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_175_1_aXk.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_174_1_HMK.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_173_1_oxR.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_172_1_hpJ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_171_1_U8j.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_170_1_nsU.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_16_1_g9J.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_169_1_97E.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_168_1_Phl.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_167_1_WKS.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_166_1_Nbd.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_165_1_2kI.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_164_1_VA2.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_163_1_ILw.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_162_1_3Ek.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_161_1_pmL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_160_1_j5e.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_15_1_0rM.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_159_1_2vE.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_158_1_vfj.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_157_1_4kz.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_156_1_qVp.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_155_1_BAC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_154_1_8zm.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_153_1_1kV.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_152_1_A2d.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_151_1_6e3.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_150_1_uHp.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_14_1_HeT.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_149_1_Bor.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_148_1_mX3.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_147_1_TWB.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_146_1_n0p.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_145_1_mkw.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_144_1_Krm.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_143_1_GBt.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_142_1_ygD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_141_1_phP.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_140_1_Ajv.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_13_1_Z2N.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_139_1_Yf6.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_138_1_ZTK.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_137_1_zBD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_136_1_x0k.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_135_1_Vcq.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_134_1_fC8.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_133_1_aFs.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_132_1_xpv.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_131_1_a63.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_130_1_hBL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_12_1_PMr.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_129_1_viS.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_128_1_nxo.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_127_1_gCh.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_126_1_jjy.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_125_1_QrT.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_124_1_ZvI.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_123_1_ArV.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_122_1_Yo0.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_121_1_XcB.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_120_1_4GC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_11_1_GuD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_119_1_5hH.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_118_1_vmm.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_117_1_t2y.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_116_1_XUz.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_115_1_SxJ.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_114_1_FFL.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_113_1_7lD.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_112_1_J3M.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_111_1_6pN.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_110_1_bnv.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_10_1_hXC.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_109_1_Gtm.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_108_1_9h5.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_107_1_S3g.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_106_1_Q42.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_105_1_lAk.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_104_1_OFr.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_103_1_uOH.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_102_1_LTP.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_101_1_IzM.root',
    '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_100_1_Lza.root'
    )
)

#------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
# - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
# - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-----------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#---------------------------------------------------------------
# Load module for preselection
#----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load module to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Systematics_cff")

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

## load and configure module for PU re-weighting
process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Run2011_bin70.root"

## load and configure module for cross-section and luminosity weighting
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load ("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight           = process.btagEventWeight.clone()
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"

## muon channel default settings
process.btagEventWeightMu                    = process.btagEventWeight.clone()
process.btagEventWeightMu.rootDir            = "RA4bMuTCHEM3"

## create weights for muon selection
process.btagEventWeightMuJER                 = process.btagEventWeightMu.clone()
process.btagEventWeightMuJER.jets            = "smearedGoodJets"

process.btagEventWeightMuBtagSFUp            = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuBtagSFUp.sysVar     = "bTagSFUp"

process.btagEventWeightMuBtagSFDown          = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuBtagSFDown.sysVar   = "bTagSFDown"

process.btagEventWeightMuMistagSFUp          = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuMistagSFUp.sysVar   = "misTagSFUp"

process.btagEventWeightMuMistagSFDown        = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuMistagSFDown.sysVar = "misTagSFDown"

## electron channel default settings
process.btagEventWeightEl                    = process.btagEventWeight.clone()
process.btagEventWeightEl.rootDir            = "RA4bElTCHEM3"

## create weights for electron selection
process.btagEventWeightElJER                 = process.btagEventWeightEl.clone()
process.btagEventWeightElJER.jets            = "smearedGoodJets"

process.btagEventWeightElBtagSFUp            = process.btagEventWeightElJER.clone()
process.btagEventWeightElBtagSFUp.sysVar     = "bTagSFUp"

process.btagEventWeightElBtagSFDown          = process.btagEventWeightElJER.clone()
process.btagEventWeightElBtagSFDown.sysVar   = "bTagSFDown"

process.btagEventWeightElMistagSFUp          = process.btagEventWeightElJER.clone()
process.btagEventWeightElMistagSFUp.sysVar   = "misTagSFUp"

process.btagEventWeightElMistagSFDown        = process.btagEventWeightElJER.clone()
process.btagEventWeightElMistagSFDown.sysVar = "misTagSFDown"

#-----------------------------------------------------------------
# Load and configure module to scale jet energy
#-----------------------------------------------------------------

process.load("SUSYAnalysis.Uncertainties.JetEnergy_cfi")

## define default settings
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"

process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, 1.5, 1.5, 2.0, 2.0, -1)
process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.1, 1.1, 1.1)

process.scaledJetEnergy.jetPTThresholdForMET = 10. ## proposed on Nov 15 in RA4 meeting
process.scaledJetEnergy.maxJetEtaForMET = 4.7      ## proposed on Nov 15 in RA4 meeting

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled up jet energy corrections
process.scaledJetEnergyJECUp = process.scaledJetEnergy.clone()
process.scaledJetEnergyJECUp.scaleType   = "jes:up"

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled down jet energy resolution
process.scaledJetEnergyJECDown = process.scaledJetEnergy.clone()
process.scaledJetEnergyJECDown.scaleType   = "jes:down"

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled up jet energy corrections
process.scaledJetEnergyJERUp = process.scaledJetEnergy.clone()
process.scaledJetEnergyJERUp.resolutionFactors    = cms.vdouble(1.2, 1.25, 1.3)

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled down jet energy corrections
process.scaledJetEnergyJERDown = process.scaledJetEnergy.clone()
process.scaledJetEnergyJERDown.resolutionFactors    = cms.vdouble(1., 0.95, 0.9)

process.L2L3ResidualMC = cms.ESSource(
    'LXXXCorrectionService',
    era = cms.string('Jec11V12'),
    section   = cms.string(''),
    level     = cms.string('L2L3Residual'),
    # the above 3 elements are needed only when the service is initialized from local txt files
    algorithm = cms.string('AK5PF'),
    # the 'algorithm' tag is also the name of the DB payload
    useCondDB = cms.untracked.bool(True)
    )

#-----------------------------------------------------------------
# Load and configure module to scale lepton energy
#-----------------------------------------------------------------

process.load("SUSYAnalysis.Uncertainties.LeptonEnergy_cfi")

process.scaledLeptonEnergy.inputMuons = "goodMuons"
process.scaledLeptonEnergy.inputElectrons = "goodElectrons"
process.scaledLeptonEnergy.inputMETs = "scaledJetEnergy:patMETsPF"

process.scaledLeptonEnergyUp = process.scaledLeptonEnergy.clone()
process.scaledLeptonEnergyUp.scaleFactorMu = 1.01     ## proposed on Nov 15 in RA4 meeting
process.scaledLeptonEnergyUp.scaleFactorEl = 1.025    ## proposed on Nov 15 in RA4 meeting

process.scaledLeptonEnergyDown = process.scaledLeptonEnergy.clone()
process.scaledLeptonEnergyDown.scaleFactorMu = 0.99   ## proposed on Nov 15 in RA4 meeting
process.scaledLeptonEnergyDown.scaleFactorEl = 0.975  ## proposed on Nov 15 in RA4 meeting

#-----------------------------------------------------------------
# Load and configure module to scale unclustered energy
#-----------------------------------------------------------------

process.load("SUSYAnalysis.Uncertainties.UnclusteredEnergy_cfi")

process.scaledUnclusteredEnergyUp = process.unclusteredEnergy.clone()
process.scaledUnclusteredEnergyUp.scaleFactor = 1.1
process.scaledUnclusteredEnergyUp.inputMETs = "scaledJetEnergy:patMETsPF"

process.scaledUnclusteredEnergyDown = process.unclusteredEnergy.clone()
process.scaledUnclusteredEnergyDown.scaleFactor = 0.9
process.scaledUnclusteredEnergyDown.inputMETs = "scaledJetEnergy:patMETsPF"

#-----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SystematicsAnalyzerMu_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SystematicsAnalyzerEl_cff")

#-------------------------------------------------
# Analyzer for cross-check with SUSYAnalyzer
#-------------------------------------------------

process.CrossCheck = process.analyzeSystematicsMu0b.clone()
process.CrossCheck.useBtagEventWeight = False

#--------------------------
# Muon selection paths
#--------------------------

##  muon selection w/o smeared jet energy
process.RA4bMuonSelection = cms.Path(## Object Producer sequences
                                     process.createGoodLeptons *
                                     process.createGoodJets *
                                     process.createGoodMETs *
                                     process.makeSUSYGenEvt *
                                     ## Weight producer sequences
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     process.btagEventWeightMu *
                                     ## Selection sequences
                                     process.preselectionMuHTMC2 *
                                     process.MuHadSelection *
                                     process.muonSelection *
                                     process.jetSelection *
                                     ## Analyzer Sequences
                                     process.CrossCheck *
                                     process.analyzeSystematicsMu0b *
                                     process.analyzeSystematicsMu1b *
                                     process.analyzeSystematicsMu2b *
                                     process.analyzeSystematicsMu3b
                                     )

## muon selection with smeared jet energy
process.RA4bMuonSelectionJER = cms.Path(## Object Producer sequences
                                        process.scaledJetEnergy *
                                        process.createGoodLeptons *
                                        process.createSmearedGoodJets *
                                        process.createSmearedGoodMETs *
                                        process.makeSUSYGenEvt *
                                        ## Weight producer sequences
                                        process.eventWeightPU *
                                        process.weightProducer *
                                        process.btagEventWeightMuJER *
                                        process.btagEventWeightMuBtagSFUp *
                                        process.btagEventWeightMuBtagSFDown *
                                        process.btagEventWeightMuMistagSFUp *
                                        process.btagEventWeightMuMistagSFDown *
                                        ## Selection sequences
                                        process.preselectionMuHTMC2 *
                                        process.MuHadSelectionJER *
                                        process.muonSelection *
                                        process.jetSelectionJER *
                                        ## Analyzer Sequences for Mu 0 btags
                                        process.analyzeSystematicsMu0bJER *
                                        process.analyzeSystematicsMu0bBtagSFUp *
                                        process.analyzeSystematicsMu0bBtagSFDown *
                                        process.analyzeSystematicsMu0bMistagSFUp *
                                        process.analyzeSystematicsMu0bMistagSFDown *
                                        process.analyzeSystematicsMu0bPUUp *
                                        process.analyzeSystematicsMu0bPUDown *
                                        process.analyzeSystematicsMu0bWUp *
                                        process.analyzeSystematicsMu0bWDown *
                                        ## Analyzer Sequences for Mu 1 btags
                                        process.analyzeSystematicsMu1bJER *
                                        process.analyzeSystematicsMu1bBtagSFUp *
                                        process.analyzeSystematicsMu1bBtagSFDown *
                                        process.analyzeSystematicsMu1bMistagSFUp *
                                        process.analyzeSystematicsMu1bMistagSFDown *
                                        process.analyzeSystematicsMu1bPUUp *
                                        process.analyzeSystematicsMu1bPUDown *
                                        process.analyzeSystematicsMu1bWUp *
                                        process.analyzeSystematicsMu1bWDown *
                                        ## Analyzer Sequences for Mu 2 btags
                                        process.analyzeSystematicsMu2bJER *
                                        process.analyzeSystematicsMu2bBtagSFUp *
                                        process.analyzeSystematicsMu2bBtagSFDown *
                                        process.analyzeSystematicsMu2bMistagSFUp *
                                        process.analyzeSystematicsMu2bMistagSFDown *
                                        process.analyzeSystematicsMu2bPUUp *
                                        process.analyzeSystematicsMu2bPUDown *
                                        process.analyzeSystematicsMu2bWUp *
                                        process.analyzeSystematicsMu2bWDown *
                                        ## Analyzer Sequences for Mu 3 btags
                                        process.analyzeSystematicsMu3bJER *
                                        process.analyzeSystematicsMu3bBtagSFUp *
                                        process.analyzeSystematicsMu3bBtagSFDown *
                                        process.analyzeSystematicsMu3bMistagSFUp *
                                        process.analyzeSystematicsMu3bMistagSFDown *
                                        process.analyzeSystematicsMu3bPUUp *
                                        process.analyzeSystematicsMu3bPUDown *
                                        process.analyzeSystematicsMu3bWUp *
                                        process.analyzeSystematicsMu3bWDown
                                        )

##  muon selection with smeared jet energy and scaled up lepton energy
process.RA4bMuonSelectionLepUp = cms.Path(## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptonsUp *
                                          process.createSmearedGoodJets *
                                          process.scaledLeptonEnergyUp *
                                          process.createGoodMETsLepUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 *
                                          process.MuHadSelectionLepUp *
                                          process.muonSelectionUp *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bLepUp *
                                          process.analyzeSystematicsMu1bLepUp *
                                          process.analyzeSystematicsMu2bLepUp *
                                          process.analyzeSystematicsMu3bLepUp
                                          )

##  muon selection with smeared jet energy and scaled down lepton energy
process.RA4bMuonSelectionLepDown = cms.Path(## Object Producer sequences
                                            process.scaledJetEnergy *
                                            process.createGoodLeptonsDown *
                                            process.createSmearedGoodJets *
                                            process.scaledLeptonEnergyDown *
                                            process.createGoodMETsLepDown *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightMuJER *
                                            ## Selection sequences
                                            process.preselectionMuHTMC2 *
                                            process.MuHadSelectionLepDown *
                                            process.muonSelectionDown *
                                            process.jetSelectionJER *
                                            ## Analyzer Sequences
                                            process.analyzeSystematicsMu0bLepDown *
                                            process.analyzeSystematicsMu1bLepDown *
                                            process.analyzeSystematicsMu2bLepDown *
                                            process.analyzeSystematicsMu3bLepDown
                                            )

##  muon selection with smeared jet energy and scaled up unclustered energy
process.RA4bMuonSelectionMETUp = cms.Path(## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.scaledUnclusteredEnergyUp *
                                          process.createGoodMETsMETUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 *
                                          process.MuHadSelectionMETUp *
                                          process.muonSelection *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bMETUp *
                                          process.analyzeSystematicsMu1bMETUp *
                                          process.analyzeSystematicsMu2bMETUp *
                                          process.analyzeSystematicsMu3bMETUp
                                          )

##  muon selection with smeared jet energy and scaled down unclustered energy
process.RA4bMuonSelectionMETDown = cms.Path(## Object Producer sequences
                                            process.scaledJetEnergy *
                                            process.createGoodLeptons *
                                            process.createSmearedGoodJets *
                                            process.scaledUnclusteredEnergyDown *
                                            process.createGoodMETsMETDown *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightMuJER *
                                            ## Selection sequences
                                            process.preselectionMuHTMC2 *
                                            process.MuHadSelectionMETDown *
                                            process.muonSelection *
                                            process.jetSelectionJER *
                                            ## Analyzer Sequences
                                            process.analyzeSystematicsMu0bMETDown *
                                            process.analyzeSystematicsMu1bMETDown *
                                            process.analyzeSystematicsMu2bMETDown *
                                            process.analyzeSystematicsMu3bMETDown
                                            )

##  muon selection with smeared and scaled up jet energy corrections
process.RA4bMuonSelectionJECUp = cms.Path(## Producer sequences
                                          process.scaledJetEnergy *
                                          process.scaledJetEnergyJECUp *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.createGoodJetsJECUp *
                                          process.createGoodMETsJECUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 *
                                          process.MuHadSelectionJECUp *
                                          process.muonSelection *
                                          process.jetSelectionJECUp *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bJECUp *
                                          process.analyzeSystematicsMu1bJECUp *
                                          process.analyzeSystematicsMu2bJECUp *
                                          process.analyzeSystematicsMu3bJECUp
                                          )

##  muon selection with smeared and scaled down jet energy corrections
process.RA4bMuonSelectionJECDown = cms.Path(## Producer sequences
                                            process.scaledJetEnergy *
                                            process.scaledJetEnergyJECDown *
                                            process.createGoodLeptons *
                                            process.createSmearedGoodJets *
                                            process.createGoodJetsJECDown *
                                            process.createGoodMETsJECDown *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightMuJER *
                                            ## Selection sequences
                                            process.preselectionMuHTMC2 *
                                            process.MuHadSelectionJECDown *
                                            process.muonSelection *
                                            process.jetSelectionJECDown *
                                            ## Analyzer Sequences
                                            process.analyzeSystematicsMu0bJECDown *
                                            process.analyzeSystematicsMu1bJECDown *
                                            process.analyzeSystematicsMu2bJECDown *
                                          process.analyzeSystematicsMu3bJECDown
                                          )

##  muon selection with smeared and scaled up jet energy resolution
process.RA4bMuonSelectionJERUp = cms.Path(## Producer sequences
                                          process.scaledJetEnergy *
                                          process.scaledJetEnergyJERUp *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.createGoodJetsJERUp *
                                          process.createGoodMETsJERUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 *
                                          process.MuHadSelectionJERUp *
                                          process.muonSelection *
                                          process.jetSelectionJERUp *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bJERUp *
                                          process.analyzeSystematicsMu1bJERUp *
                                          process.analyzeSystematicsMu2bJERUp *
                                          process.analyzeSystematicsMu3bJERUp
                                          )

##  muon selection with smeared and scaled down jet energy resolution
process.RA4bMuonSelectionJERDown = cms.Path(## Producer sequences
                                            process.scaledJetEnergy *
                                            process.scaledJetEnergyJERDown *
                                            process.createGoodLeptons *
                                            process.createSmearedGoodJets *
                                            process.createGoodJetsJERDown *
                                            process.createGoodMETsJERDown *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightMuJER *
                                            ## Selection sequences
                                            process.preselectionMuHTMC2 *
                                            process.MuHadSelectionJERDown *
                                            process.muonSelection *
                                            process.jetSelectionJERDown *
                                            ## Analyzer Sequences
                                            process.analyzeSystematicsMu0bJERDown *
                                            process.analyzeSystematicsMu1bJERDown *
                                            process.analyzeSystematicsMu2bJERDown *
                                            process.analyzeSystematicsMu3bJERDown 
                                            )


#--------------------------
# Electron selection paths
#--------------------------

##  electron selection w/o smeared jet energy
process.RA4bElectronSelection = cms.Path(## Object Producer sequences
                                         process.createGoodLeptons *
                                         process.createGoodJets *
                                         process.createGoodMETs *
                                         process.makeSUSYGenEvt *
                                         ## Weight producer sequences
                                         process.eventWeightPU *
                                         process.weightProducer *
                                         process.btagEventWeightEl *
                                         ## Selection sequences
                                         process.preselectionElHTMC2 *
                                         process.ElHadSelection *
                                         process.electronSelection *
                                         process.jetSelection *
                                         ## Analyzer Sequences
                                         process.analyzeSystematicsEl0b *
                                         process.analyzeSystematicsEl1b *
                                         process.analyzeSystematicsEl2b *
                                         process.analyzeSystematicsEl3b
                                         )

## electron selection with smeared jet energy
process.RA4bElectronSelectionJER = cms.Path(## Object Producer sequences
                                            process.scaledJetEnergy *
                                            process.createGoodLeptons *
                                            process.createSmearedGoodJets *
                                            process.createSmearedGoodMETs *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightElJER *
                                            process.btagEventWeightElBtagSFUp *
                                            process.btagEventWeightElBtagSFDown *
                                            process.btagEventWeightElMistagSFUp *
                                            process.btagEventWeightElMistagSFDown *
                                            ## Selection sequences
                                            process.preselectionElHTMC2 *
                                            process.ElHadSelectionJER *
                                            process.electronSelection *
                                            process.jetSelectionJER *
                                            ## Analyzer Sequences for El 0 btags
                                            process.analyzeSystematicsEl0bJER *
                                            process.analyzeSystematicsEl0bBtagSFUp *
                                            process.analyzeSystematicsEl0bBtagSFDown *
                                            process.analyzeSystematicsEl0bMistagSFUp *
                                            process.analyzeSystematicsEl0bMistagSFDown *
                                            process.analyzeSystematicsEl0bPUUp *
                                            process.analyzeSystematicsEl0bPUDown *
                                            process.analyzeSystematicsEl0bWUp *
                                            process.analyzeSystematicsEl0bWDown *
                                            ## Analyzer Sequences for El 1 btags
                                            process.analyzeSystematicsEl1bJER *
                                            process.analyzeSystematicsEl1bBtagSFUp *
                                            process.analyzeSystematicsEl1bBtagSFDown *
                                            process.analyzeSystematicsEl1bMistagSFUp *
                                            process.analyzeSystematicsEl1bMistagSFDown *
                                            process.analyzeSystematicsEl1bPUUp *
                                            process.analyzeSystematicsEl1bPUDown *
                                            process.analyzeSystematicsEl1bWUp *
                                            process.analyzeSystematicsEl1bWDown *
                                            ## Analyzer Sequences for El 2 btags
                                            process.analyzeSystematicsEl2bJER *
                                            process.analyzeSystematicsEl2bBtagSFUp *
                                            process.analyzeSystematicsEl2bBtagSFDown *
                                            process.analyzeSystematicsEl2bMistagSFUp *
                                            process.analyzeSystematicsEl2bMistagSFDown *
                                            process.analyzeSystematicsEl2bPUUp *
                                            process.analyzeSystematicsEl2bPUDown *
                                            process.analyzeSystematicsEl2bWUp *
                                            process.analyzeSystematicsEl2bWDown *
                                            ## Analyzer Sequences for El 3 btags
                                            process.analyzeSystematicsEl3bJER *
                                            process.analyzeSystematicsEl3bBtagSFUp *
                                            process.analyzeSystematicsEl3bBtagSFDown *
                                            process.analyzeSystematicsEl3bMistagSFUp *
                                            process.analyzeSystematicsEl3bMistagSFDown *
                                            process.analyzeSystematicsEl3bPUUp *
                                            process.analyzeSystematicsEl3bPUDown *
                                            process.analyzeSystematicsEl3bWUp *
                                            process.analyzeSystematicsEl3bWDown
                                            )

##  electron selection with smeared jet energy and scaled up lepton energy
process.RA4bElectronSelectionLepUp = cms.Path(## Object Producer sequences
                                              process.scaledJetEnergy *
                                              process.createGoodLeptonsUp *
                                              process.createSmearedGoodJets *
                                              process.scaledLeptonEnergyUp *
                                              process.createGoodMETsLepUp *
                                              process.makeSUSYGenEvt *
                                              ## Weight producer sequences
                                              process.eventWeightPU *
                                              process.weightProducer *
                                              process.btagEventWeightElJER *
                                              ## Selection sequences
                                              process.preselectionElHTMC2 *
                                              process.ElHadSelectionLepUp *
                                              process.electronSelectionUp *
                                              process.jetSelectionJER *
                                              ## Analyzer Sequences
                                              process.analyzeSystematicsEl0bLepUp *
                                              process.analyzeSystematicsEl1bLepUp *
                                              process.analyzeSystematicsEl2bLepUp *
                                              process.analyzeSystematicsEl3bLepUp
                                              )

##  electron selection with smeared jet energy and scaled down lepton energy
process.RA4bElectronSelectionLepDown = cms.Path(## Object Producer sequences
                                               process.scaledJetEnergy *
                                               process.createGoodLeptonsDown *
                                               process.createSmearedGoodJets *
                                               process.scaledLeptonEnergyDown *
                                               process.createGoodMETsLepDown *
                                               process.makeSUSYGenEvt *
                                               ## Weight producer sequences
                                               process.eventWeightPU *
                                               process.weightProducer *
                                               process.btagEventWeightElJER *
                                               ## Selection sequences
                                               process.preselectionElHTMC2 *
                                               process.ElHadSelectionLepDown *
                                               process.electronSelectionDown *
                                               process.jetSelectionJER *
                                               ## Analyzer Sequences
                                               process.analyzeSystematicsEl0bLepDown *
                                               process.analyzeSystematicsEl1bLepDown *
                                               process.analyzeSystematicsEl2bLepDown *
                                               process.analyzeSystematicsEl3bLepDown
                                               )

##  electron selection with smeared jet energy and scaled up unclustered energy
process.RA4bElectronSelectionMETUp = cms.Path(## Object Producer sequences
                                              process.scaledJetEnergy *
                                              process.createGoodLeptons *
                                              process.createSmearedGoodJets *
                                              process.scaledUnclusteredEnergyUp *
                                              process.createGoodMETsMETUp *
                                              process.makeSUSYGenEvt *
                                              ## Weight producer sequences
                                              process.eventWeightPU *
                                              process.weightProducer *
                                              process.btagEventWeightElJER *
                                              ## Selection sequences
                                              process.preselectionElHTMC2 *
                                              process.ElHadSelectionMETUp *
                                              process.electronSelection *
                                              process.jetSelectionJER *
                                              ## Analyzer Sequences
                                              process.analyzeSystematicsEl0bMETUp *
                                              process.analyzeSystematicsEl1bMETUp *
                                              process.analyzeSystematicsEl2bMETUp *
                                              process.analyzeSystematicsEl3bMETUp
                                              )

##  electron selection with smeared jet energy and scaled down unclustered energy
process.RA4bElectronSelectionMETDown = cms.Path(## Object Producer sequences
                                                process.scaledJetEnergy *
                                                process.createGoodLeptons *
                                                process.createSmearedGoodJets *
                                                process.scaledUnclusteredEnergyDown *
                                                process.createGoodMETsMETDown *
                                                process.makeSUSYGenEvt *
                                                ## Weight producer sequences
                                                process.eventWeightPU *
                                                process.weightProducer *
                                                process.btagEventWeightElJER *
                                                ## Selection sequences
                                                process.preselectionElHTMC2 *
                                                process.ElHadSelectionMETDown *
                                                process.electronSelection *
                                                process.jetSelectionJER *
                                                ## Analyzer Sequences
                                                process.analyzeSystematicsEl0bMETDown *
                                                process.analyzeSystematicsEl1bMETDown *
                                                process.analyzeSystematicsEl2bMETDown *
                                                process.analyzeSystematicsEl3bMETDown
                                                )

##  electron selection with smeared and scaled up jet energy corrections
process.RA4bElectronSelectionJECUp = cms.Path(## Producer sequences
                                              process.scaledJetEnergy *
                                              process.scaledJetEnergyJECUp *
                                              process.createGoodLeptons *
                                              process.createSmearedGoodJets *
                                              process.createGoodJetsJECUp *
                                              process.createGoodMETsJECUp *
                                              process.makeSUSYGenEvt *
                                              ## Weight producer sequences
                                              process.eventWeightPU *
                                              process.weightProducer *
                                              process.btagEventWeightElJER *
                                              ## Selection sequences
                                              process.preselectionElHTMC2 *
                                              process.ElHadSelectionJECUp *
                                              process.electronSelection *
                                              process.jetSelectionJECUp *
                                              ## Analyzer Sequences
                                              process.analyzeSystematicsEl0bJECUp *
                                              process.analyzeSystematicsEl1bJECUp *
                                              process.analyzeSystematicsEl2bJECUp *
                                              process.analyzeSystematicsEl3bJECUp
                                              )

##  electron selection with smeared and scaled down jet energy corrections
process.RA4bElectronSelectionJECDown = cms.Path(## Producer sequences
                                                process.scaledJetEnergy *
                                                process.scaledJetEnergyJECDown *
                                                process.createGoodLeptons *
                                                process.createSmearedGoodJets *
                                                process.createGoodJetsJECDown *
                                                process.createGoodMETsJECDown *
                                                process.makeSUSYGenEvt *
                                                ## Weight producer sequences
                                                process.eventWeightPU *
                                                process.weightProducer *
                                                process.btagEventWeightElJER *
                                                ## Selection sequences
                                                process.preselectionElHTMC2 *
                                                process.ElHadSelectionJECDown *
                                                process.electronSelection *
                                                process.jetSelectionJECDown *
                                                ## Analyzer Sequences
                                                process.analyzeSystematicsEl0bJECDown *
                                                process.analyzeSystematicsEl1bJECDown *
                                                process.analyzeSystematicsEl2bJECDown *
                                                process.analyzeSystematicsEl3bJECDown
                                                )

##  electron selection with smeared and scaled up jet energy resolution
process.RA4bElectronSelectionJERUp = cms.Path(## Producer sequences
                                              process.scaledJetEnergy *
                                              process.scaledJetEnergyJERUp *
                                              process.createGoodLeptons *
                                              process.createSmearedGoodJets *
                                              process.createGoodJetsJERUp *
                                              process.createGoodMETsJERUp *
                                              process.makeSUSYGenEvt *
                                              ## Weight producer sequences
                                              process.eventWeightPU *
                                              process.weightProducer *
                                              process.btagEventWeightElJER *
                                              ## Selection sequences
                                              process.preselectionElHTMC2 *
                                              process.ElHadSelectionJERUp *
                                              process.electronSelection *
                                              process.jetSelectionJERUp *
                                              ## Analyzer Sequences
                                              process.analyzeSystematicsEl0bJERUp *
                                              process.analyzeSystematicsEl1bJERUp *
                                              process.analyzeSystematicsEl2bJERUp *
                                              process.analyzeSystematicsEl3bJERUp
                                              )

##  electron selection with smeared and scaled down jet energy resolution
process.RA4bElectronSelectionJERDown = cms.Path(## Producer sequences
                                                process.scaledJetEnergy *
                                                process.scaledJetEnergyJERDown *
                                                process.createGoodLeptons *
                                                process.createSmearedGoodJets *
                                                process.createGoodJetsJERDown *
                                                process.createGoodMETsJERDown *
                                                process.makeSUSYGenEvt *
                                                ## Weight producer sequences
                                                process.eventWeightPU *
                                                process.weightProducer *
                                                process.btagEventWeightElJER *
                                                ## Selection sequences
                                                process.preselectionElHTMC2 *
                                                process.ElHadSelectionJERDown *
                                                process.electronSelection *
                                                process.jetSelectionJERDown *
                                                ## Analyzer Sequences
                                                process.analyzeSystematicsEl0bJERDown *
                                                process.analyzeSystematicsEl1bJERDown *
                                                process.analyzeSystematicsEl2bJERDown *
                                                process.analyzeSystematicsEl3bJERDown 
                                                )
