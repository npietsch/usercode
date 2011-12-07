import FWCore.ParameterSet.Config as cms

process = cms.Process("AnalyzeBtags") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('AnalyzeBtags.root')
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

#-----------------------------------------------------------------
# Dummy output module
#-----------------------------------------------------------------
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Summer11.root')
)

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")


from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *

process.highPtJets = selectedPatJets.clone(src = 'goodJets',
                                           cut =
                                           'pt > 240'
                                           )

process.lowPtJets = selectedPatJets.clone(src = 'goodJets',
                                          cut =
                                          'pt < 240'
                                          )

## select events with at least 2 high pt jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
process.twoHighPtJets = countPatJets.clone(src = 'highPtJets',
                                           minNumber = 2
                                           )


#-----------------------------------------------------------------
# Load and configure modules for event weighting
#-----------------------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
#process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"
process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_data2011_upTo178078_bin70.root"

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load ("RecoBTag.PerformanceDB.BTagPerformanceDB1107")

process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

#-----------------------------------------------------------------
# Configure modules for muon channel b-tag event weighting
#-----------------------------------------------------------------

## TCHEM
process.btagEventWeightMuTCHEM3 = process.btagEventWeight.clone()
process.btagEventWeightMuTCHEM3.bTagAlgo= "TCHEM"
process.btagEventWeightMuTCHEM3.rootDir = "RA4bMuTCHEM3"
process.btagEventWeightMuTCHEM3.filename= "../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeightMuTCHEM3.scaleJetEffSF = True
process.btagEventWeightMuTCHEM3.scaleEventEffSF = True

process.btagEventWeightMuTCHEM3highPt = process.btagEventWeightMuTCHEM3.clone()
process.btagEventWeightMuTCHEM3highPt.jets = "highPtJets"

process.btagEventWeightMuTCHEM3lowPt = process.btagEventWeightMuTCHEM3.clone()
process.btagEventWeightMuTCHEM3lowPt.jets = "lowPtJets"

## SSVHEM
process.btagEventWeightMuSSVHEM3 = process.btagEventWeight.clone()
process.btagEventWeightMuSSVHEM3.bTagAlgo= "SSVHEM"
process.btagEventWeightMuSSVHEM3.rootDir = "RA4bMuSSVHEM3"
process.btagEventWeightMuSSVHEM3.filename= "../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeightMuSSVHEM3.scaleJetEffSF = True
process.btagEventWeightMuSSVHEM3.scaleEventEffSF = True

process.btagEventWeightMuSSVHEM3highPt = process.btagEventWeightMuSSVHEM3.clone()
process.btagEventWeightMuSSVHEM3highPt.jets = "highPtJets"

process.btagEventWeightMuSSVHEM3lowPt = process.btagEventWeightMuSSVHEM3.clone()
process.btagEventWeightMuSSVHEM3lowPt.jets = "lowPtJets"

#----------------------------------------------------------------------------------------
# Load and configure modules for analysis of b-tagging in muon channel
#----------------------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

process.analyzeBtags = analyzeBtags.clone()
process.analyzeBtags.useEventWeight = True
process.analyzeBtags.useBtagEventWeight = True

# TCHEM
process.analyzeBtagsMuTCHEM3 = process.analyzeBtags.clone()
process.analyzeBtagsMuTCHEM3.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsMuTCHEM3.BtagJetWeights       = "btagEventWeightMuTCHEM3:RA4bSFJetWeights"
process.analyzeBtagsMuTCHEM3.BtagEventWeights     = "btagEventWeightMuTCHEM3:RA4bSFEventWeights"
process.analyzeBtagsMuTCHEM3.BtagJetWeightsGrid   = "btagEventWeightMuTCHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsMuTCHEM3.BtagEventWeightsGrid = "btagEventWeightMuTCHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsMuTCHEM3.jets                 = "goodJets"

process.analyzeBtagsMuTCHEM3highPt = process.analyzeBtags.clone()
process.analyzeBtagsMuTCHEM3highPt.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsMuTCHEM3highPt.BtagJetWeights       = "btagEventWeightMuTCHEM3highPt:RA4bSFJetWeights"
process.analyzeBtagsMuTCHEM3highPt.BtagEventWeights     = "btagEventWeightMuTCHEM3highPt:RA4bSFEventWeights"
process.analyzeBtagsMuTCHEM3highPt.BtagJetWeightsGrid   = "btagEventWeightMuTCHEM3highPt:RA4bJetWeightsGrid"
process.analyzeBtagsMuTCHEM3highPt.BtagEventWeightsGrid = "btagEventWeightMuTCHEM3highPt:RA4bEventWeightsGrid"
process.analyzeBtagsMuTCHEM3highPt.jets                 = "highPtJets"

process.analyzeBtagsMuTCHEM3lowPt = process.analyzeBtags.clone()
process.analyzeBtagsMuTCHEM3lowPt.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsMuTCHEM3lowPt.BtagJetWeights       = "btagEventWeightMuTCHEM3lowPt:RA4bSFJetWeights"
process.analyzeBtagsMuTCHEM3lowPt.BtagEventWeights     = "btagEventWeightMuTCHEM3lowPt:RA4bSFEventWeights"
process.analyzeBtagsMuTCHEM3lowPt.BtagJetWeightsGrid   = "btagEventWeightMuTCHEM3lowPt:RA4bJetWeightsGrid"
process.analyzeBtagsMuTCHEM3lowPt.BtagEventWeightsGrid = "btagEventWeightMuTCHEM3lowPt:RA4bEventWeightsGrid"
process.analyzeBtagsMuTCHEM3lowPt.jets                 = "lowPtJets"

process.analyzeBtagsMuTCHEM4       = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsMuTCHEM4highPt = process.analyzeBtagsMuTCHEM3highPt.clone()
process.analyzeBtagsMuTCHEM4lowPt  = process.analyzeBtagsMuTCHEM3lowPt.clone()

# clones
process.analyzeBtagsRA4bMuTCHEM3       = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsRA4bMuTCHEM3highPt = process.analyzeBtagsMuTCHEM3highPt.clone()
process.analyzeBtagsRA4bMuTCHEM3lowPt  = process.analyzeBtagsMuTCHEM3lowPt.clone()

process.analyzeBtagsRA4bMuTCHEM4       = process.analyzeBtagsMuTCHEM4.clone()
process.analyzeBtagsRA4bMuTCHEM4highPt = process.analyzeBtagsMuTCHEM4highPt.clone()
process.analyzeBtagsRA4bMuTCHEM4lowPt  = process.analyzeBtagsMuTCHEM4lowPt.clone()

process.analyzeBtagsMuTCHEM3dilep       = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsMuTCHEM3highPtdilep = process.analyzeBtagsMuTCHEM3highPt.clone()
process.analyzeBtagsMuTCHEM3lowPtdilep  = process.analyzeBtagsMuTCHEM3lowPt.clone()

process.analyzeBtagsMuTCHEM4dilep       = process.analyzeBtagsMuTCHEM4.clone()
process.analyzeBtagsMuTCHEM4highPtdilep = process.analyzeBtagsMuTCHEM4highPt.clone()
process.analyzeBtagsMuTCHEM4lowPtdilep  = process.analyzeBtagsMuTCHEM4lowPt.clone()

# for cross-check
process.analyzeBtagsRA4bMuTCHEM3noSF = process.analyzeBtags.clone()
process.analyzeBtagsRA4bMuTCHEM3noSF.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsRA4bMuTCHEM3noSF.BtagJetWeights       = "btagEventWeightMuTCHEM3:RA4bJetWeights"
process.analyzeBtagsRA4bMuTCHEM3noSF.BtagEventWeights     = "btagEventWeightMuTCHEM3:RA4bEventWeights"
process.analyzeBtagsRA4bMuTCHEM3noSF.BtagJetWeightsGrid   = "btagEventWeightMuTCHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsRA4bMuTCHEM3noSF.BtagEventWeightsGrid = "btagEventWeightMuTCHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsRA4bMuTCHEM3noSF.jets                 = "goodJets"

# SSVHEM
process.analyzeBtagsMuSSVHEM3 = process.analyzeBtags.clone()
process.analyzeBtagsMuSSVHEM3.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsMuSSVHEM3.BtagJetWeights       = "btagEventWeightMuSSVHEM3:RA4bSFJetWeights"
process.analyzeBtagsMuSSVHEM3.BtagEventWeights     = "btagEventWeightMuSSVHEM3:RA4bSFEventWeights"
process.analyzeBtagsMuSSVHEM3.BtagJetWeightsGrid   = "btagEventWeightMuSSVHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsMuSSVHEM3.BtagEventWeightsGrid = "btagEventWeightMuSSVHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsMuSSVHEM3.jets                 = "goodJets"

process.analyzeBtagsMuSSVHEM3highPt = process.analyzeBtags.clone()
process.analyzeBtagsMuSSVHEM3highPt.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsMuSSVHEM3highPt.BtagJetWeights       = "btagEventWeightMuSSVHEM3highPt:RA4bSFJetWeights"
process.analyzeBtagsMuSSVHEM3highPt.BtagEventWeights     = "btagEventWeightMuSSVHEM3highPt:RA4bSFEventWeights"
process.analyzeBtagsMuSSVHEM3highPt.BtagJetWeightsGrid   = "btagEventWeightMuSSVHEM3highPt:RA4bJetWeightsGrid"
process.analyzeBtagsMuSSVHEM3highPt.BtagEventWeightsGrid = "btagEventWeightMuSSVHEM3highPt:RA4bEventWeightsGrid"
process.analyzeBtagsMuSSVHEM3highPt.jets                 = "highPtJets"

process.analyzeBtagsMuSSVHEM3lowPt = process.analyzeBtags.clone()
process.analyzeBtagsMuSSVHEM3lowPt.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsMuSSVHEM3lowPt.BtagJetWeights       = "btagEventWeightMuSSVHEM3lowPt:RA4bSFJetWeights"
process.analyzeBtagsMuSSVHEM3lowPt.BtagEventWeights     = "btagEventWeightMuSSVHEM3lowPt:RA4bSFEventWeights"
process.analyzeBtagsMuSSVHEM3lowPt.BtagJetWeightsGrid   = "btagEventWeightMuSSVHEM3lowPt:RA4bJetWeightsGrid"
process.analyzeBtagsMuSSVHEM3lowPt.BtagEventWeightsGrid = "btagEventWeightMuSSVHEM3lowPt:RA4bEventWeightsGrid"
process.analyzeBtagsMuSSVHEM3lowPt.jets                 = "lowPtJets"

process.analyzeBtagsMuSSVHEM4       = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsMuSSVHEM4highPt = process.analyzeBtagsMuSSVHEM3highPt.clone()
process.analyzeBtagsMuSSVHEM4lowPt  = process.analyzeBtagsMuSSVHEM3lowPt.clone()

# clones
process.analyzeBtagsRA4bMuSSVHEM3       = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsRA4bMuSSVHEM3highPt = process.analyzeBtagsMuSSVHEM3highPt.clone()
process.analyzeBtagsRA4bMuSSVHEM3lowPt  = process.analyzeBtagsMuSSVHEM3lowPt.clone()

process.analyzeBtagsRA4bMuSSVHEM4       = process.analyzeBtagsMuSSVHEM4.clone()
process.analyzeBtagsRA4bMuSSVHEM4highPt = process.analyzeBtagsMuSSVHEM4highPt.clone()
process.analyzeBtagsRA4bMuSSVHEM4lowPt  = process.analyzeBtagsMuSSVHEM4lowPt.clone()

process.analyzeBtagsMuSSVHEM3dilep       = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsMuSSVHEM3highPtdilep = process.analyzeBtagsMuSSVHEM3highPt.clone()
process.analyzeBtagsMuSSVHEM3lowPtdilep  = process.analyzeBtagsMuSSVHEM3lowPt.clone()

process.analyzeBtagsMuSSVHEM4dilep       = process.analyzeBtagsMuSSVHEM4.clone()
process.analyzeBtagsMuSSVHEM4highPtdilep = process.analyzeBtagsMuSSVHEM4highPt.clone()
process.analyzeBtagsMuSSVHEM4lowPtdilep  = process.analyzeBtagsMuSSVHEM4lowPt.clone()

# for cross-check
process.analyzeBtagsRA4bMuSSVHEM3noSF = process.analyzeBtags.clone()
process.analyzeBtagsRA4bMuSSVHEM3noSF.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsRA4bMuSSVHEM3noSF.BtagJetWeights       = "btagEventWeightMuSSVHEM3:RA4bJetWeights"
process.analyzeBtagsRA4bMuSSVHEM3noSF.BtagEventWeights     = "btagEventWeightMuSSVHEM3:RA4bEventWeights"
process.analyzeBtagsRA4bMuSSVHEM3noSF.BtagJetWeightsGrid   = "btagEventWeightMuSSVHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsRA4bMuSSVHEM3noSF.BtagEventWeightsGrid = "btagEventWeightMuSSVHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsRA4bMuSSVHEM3noSF.jets                 = "goodJets"

#--------------------------
# Muon selection paths
#--------------------------


## Standard RA4b selection
##-------------------------
process.analyzeBtags_RA4bMu = cms.Path(# Standard RA4b preselection
                                       process.preselectionMuHTMC2 *
                                       process.eventWeightPU *
                                       process.weightProducer *
                                       process.makeObjects *
                                       # match different triggers
                                       process.MuHadSelection *
                                       # produce btag event weights
                                       process.btagEventWeightMuSSVHEM3 *
                                       process.btagEventWeightMuTCHEM3 *
                                       # muon selection
                                       process.muonSelection*
                                       # jet selection
                                       process.jetSelection*
                                       # analyze btags
                                       process.analyzeBtagsRA4bMuTCHEM3 *
                                       process.analyzeBtagsRA4bMuSSVHEM3 *
                                       process.analyzeBtagsRA4bMuTCHEM3noSF *
                                       process.analyzeBtagsRA4bMuSSVHEM3noSF *
                                       # additinal cut
                                       process.oneNoSignalMET *
                                       # analyze btags
                                       process.analyzeBtagsRA4bMuTCHEM4 *
                                       process.analyzeBtagsRA4bMuSSVHEM4
                                       )


## RA4b selection with cut on two high pt jets in and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_RA4b = cms.Path(# Standard RA4b preselection
                                     process.preselectionMuHTMC2 *
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     process.makeObjects *
                                     # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                     process.highPtJets *
                                     process.lowPtJets *
                                     # additinal cut
                                     process.twoHighPtJets *
                                     # match different triggers
                                     process.MuHadSelection *
                                     # produce btag event weights
                                     process.btagEventWeightMuSSVHEM3 *
                                     process.btagEventWeightMuTCHEM3 *
                                     process.btagEventWeightMuSSVHEM3lowPt *
                                     process.btagEventWeightMuTCHEM3lowPt *
                                     process.btagEventWeightMuSSVHEM3highPt *
                                     process.btagEventWeightMuTCHEM3highPt *
                                     # muon selection
                                     process.muonSelection*
                                     # jet selection
                                     process.jetSelection*
                                     # analyze btags
                                     process.analyzeBtagsMuTCHEM3 *
                                     process.analyzeBtagsMuSSVHEM3*
                                     process.analyzeBtagsMuTCHEM3lowPt *
                                     process.analyzeBtagsMuSSVHEM3lowPt *
                                     process.analyzeBtagsMuTCHEM3highPt *
                                     process.analyzeBtagsMuSSVHEM3highPt *
                                     # additinal cut
                                     process.oneNoSignalMET *
                                     # analyze btags
                                     process.analyzeBtagsMuTCHEM4 *
                                     process.analyzeBtagsMuSSVHEM4*
                                     process.analyzeBtagsMuTCHEM4lowPt *
                                     process.analyzeBtagsMuSSVHEM4lowPt *
                                     process.analyzeBtagsMuTCHEM4highPt *
                                     process.analyzeBtagsMuSSVHEM4highPt
                                     )

## Incl. RA4b selection with cut on two high pt jets and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_diLep = cms.Path(# Standard RA4b preselection
                                      process.preselectionMuHTMC2 *
                                      process.eventWeightPU *
                                      process.weightProducer *
                                      process.makeObjects *
                                      # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                      process.highPtJets *
                                      process.lowPtJets *
                                      ## additional cut
                                      process.twoHighPtJets *
                                      # match different triggers
                                      process.MuHadSelection *
                                      # produce btag event weights
                                      process.btagEventWeightMuSSVHEM3 *
                                      process.btagEventWeightMuTCHEM3 *
                                      process.btagEventWeightMuSSVHEM3lowPt *
                                      process.btagEventWeightMuTCHEM3lowPt *
                                      process.btagEventWeightMuSSVHEM3highPt *
                                      process.btagEventWeightMuTCHEM3highPt *
                                      # muon selection
                                      process.oneGoodMuon *
                                      # jet selection
                                      process.twoGoodJets*
                                      # analyze btags
                                      process.analyzeBtagsMuTCHEM3dilep *
                                      process.analyzeBtagsMuSSVHEM3dilep*
                                      process.analyzeBtagsMuTCHEM3lowPtdilep *
                                      process.analyzeBtagsMuSSVHEM3lowPtdilep *
                                      process.analyzeBtagsMuTCHEM3highPtdilep *
                                      process.analyzeBtagsMuSSVHEM3highPtdilep *
                                      # additinal cut
                                      process.oneNoSignalMET*
                                      # analyze btags
                                      process.analyzeBtagsMuTCHEM4dilep *
                                      process.analyzeBtagsMuSSVHEM4dilep*
                                      process.analyzeBtagsMuTCHEM4lowPtdilep *
                                      process.analyzeBtagsMuSSVHEM4lowPtdilep *
                                      process.analyzeBtagsMuTCHEM4highPtdilep *
                                      process.analyzeBtagsMuSSVHEM4highPtdilep
                                      )

#-----------------------------------------------------------------
# Configure modules for electron channel b-tag event weighting
#-----------------------------------------------------------------

## TCHEM
process.btagEventWeightElTCHEM3 = process.btagEventWeight.clone()
process.btagEventWeightElTCHEM3.bTagAlgo= "TCHEM"
process.btagEventWeightElTCHEM3.rootDir = "RA4bElTCHEM3"
process.btagEventWeightElTCHEM3.filename= "../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeightElTCHEM3.scaleJetEffSF = True
process.btagEventWeightElTCHEM3.scaleEventEffSF = True

process.btagEventWeightElTCHEM3highPt = process.btagEventWeightElTCHEM3.clone()
process.btagEventWeightElTCHEM3highPt.jets = "highPtJets"

process.btagEventWeightElTCHEM3lowPt = process.btagEventWeightElTCHEM3.clone()
process.btagEventWeightElTCHEM3lowPt.jets = "lowPtJets"

## SSVHEM
process.btagEventWeightElSSVHEM3 = process.btagEventWeight.clone()
process.btagEventWeightElSSVHEM3.bTagAlgo= "SSVHEM"
process.btagEventWeightElSSVHEM3.rootDir = "RA4bElSSVHEM3"
process.btagEventWeightElSSVHEM3.filename= "../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeightElSSVHEM3.scaleJetEffSF = True
process.btagEventWeightElSSVHEM3.scaleEventEffSF = True

process.btagEventWeightElSSVHEM3highPt = process.btagEventWeightElSSVHEM3.clone()
process.btagEventWeightElSSVHEM3highPt.jets = "highPtJets"

process.btagEventWeightElSSVHEM3lowPt = process.btagEventWeightElSSVHEM3.clone()
process.btagEventWeightElSSVHEM3lowPt.jets = "lowPtJets"

#----------------------------------------------------------------------------------------
# Load and configure modules for analysis of b-tagging in electron channel
#----------------------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

process.analyzeBtags = analyzeBtags.clone()
process.analyzeBtags.useEventWeight = True
process.analyzeBtags.useBtagEventWeight = True

# TCHEM
process.analyzeBtagsElTCHEM3 = process.analyzeBtags.clone()
process.analyzeBtagsElTCHEM3.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsElTCHEM3.BtagJetWeights       = "btagEventWeightElTCHEM3:RA4bSFJetWeights"
process.analyzeBtagsElTCHEM3.BtagEventWeights     = "btagEventWeightElTCHEM3:RA4bSFEventWeights"
process.analyzeBtagsElTCHEM3.BtagJetWeightsGrid   = "btagEventWeightElTCHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsElTCHEM3.BtagEventWeightsGrid = "btagEventWeightElTCHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsElTCHEM3.jets                 = "goodJets"

process.analyzeBtagsElTCHEM3highPt = process.analyzeBtags.clone()
process.analyzeBtagsElTCHEM3highPt.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsElTCHEM3highPt.BtagJetWeights       = "btagEventWeightElTCHEM3highPt:RA4bSFJetWeights"
process.analyzeBtagsElTCHEM3highPt.BtagEventWeights     = "btagEventWeightElTCHEM3highPt:RA4bSFEventWeights"
process.analyzeBtagsElTCHEM3highPt.BtagJetWeightsGrid   = "btagEventWeightElTCHEM3highPt:RA4bJetWeightsGrid"
process.analyzeBtagsElTCHEM3highPt.BtagEventWeightsGrid = "btagEventWeightElTCHEM3highPt:RA4bEventWeightsGrid"
process.analyzeBtagsElTCHEM3highPt.jets                 = "highPtJets"

process.analyzeBtagsElTCHEM3lowPt = process.analyzeBtags.clone()
process.analyzeBtagsElTCHEM3lowPt.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsElTCHEM3lowPt.BtagJetWeights       = "btagEventWeightElTCHEM3lowPt:RA4bSFJetWeights"
process.analyzeBtagsElTCHEM3lowPt.BtagEventWeights     = "btagEventWeightElTCHEM3lowPt:RA4bSFEventWeights"
process.analyzeBtagsElTCHEM3lowPt.BtagJetWeightsGrid   = "btagEventWeightElTCHEM3lowPt:RA4bJetWeightsGrid"
process.analyzeBtagsElTCHEM3lowPt.BtagEventWeightsGrid = "btagEventWeightElTCHEM3lowPt:RA4bEventWeightsGrid"
process.analyzeBtagsElTCHEM3lowPt.jets                 = "lowPtJets"

process.analyzeBtagsElTCHEM4       = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElTCHEM4highPt = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsElTCHEM4lowPt  = process.analyzeBtagsElTCHEM3lowPt.clone()

# clones
process.analyzeBtagsRA4bElTCHEM3       = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsRA4bElTCHEM3highPt = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsRA4bElTCHEM3lowPt  = process.analyzeBtagsElTCHEM3lowPt.clone()

process.analyzeBtagsRA4bElTCHEM4       = process.analyzeBtagsElTCHEM4.clone()
process.analyzeBtagsRA4bElTCHEM4highPt = process.analyzeBtagsElTCHEM4highPt.clone()
process.analyzeBtagsRA4bElTCHEM4lowPt  = process.analyzeBtagsElTCHEM4lowPt.clone()

process.analyzeBtagsElTCHEM3dilep       = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElTCHEM3highPtdilep = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsElTCHEM3lowPtdilep  = process.analyzeBtagsElTCHEM3lowPt.clone()

process.analyzeBtagsElTCHEM4dilep       = process.analyzeBtagsElTCHEM4.clone()
process.analyzeBtagsElTCHEM4highPtdilep = process.analyzeBtagsElTCHEM4highPt.clone()
process.analyzeBtagsElTCHEM4lowPtdilep  = process.analyzeBtagsElTCHEM4lowPt.clone()

process.analyzeBtagsElElTCHEM3dilep       = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElElTCHEM3highPtdilep = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsElElTCHEM3lowPtdilep  = process.analyzeBtagsElTCHEM3lowPt.clone()

process.analyzeBtagsElElTCHEM4dilep       = process.analyzeBtagsElTCHEM4.clone()
process.analyzeBtagsElElTCHEM4highPtdilep = process.analyzeBtagsElTCHEM4highPt.clone()
process.analyzeBtagsElElTCHEM4lowPtdilep  = process.analyzeBtagsElTCHEM4lowPt.clone()

# for cross-check
process.analyzeBtagsRA4bElTCHEM3noSF = process.analyzeBtags.clone()
process.analyzeBtagsRA4bElTCHEM3noSF.bjets                = "mediumTrackHighEffBjets"
process.analyzeBtagsRA4bElTCHEM3noSF.BtagJetWeights       = "btagEventWeightElTCHEM3:RA4bJetWeights"
process.analyzeBtagsRA4bElTCHEM3noSF.BtagEventWeights     = "btagEventWeightElTCHEM3:RA4bEventWeights"
process.analyzeBtagsRA4bElTCHEM3noSF.BtagJetWeightsGrid   = "btagEventWeightElTCHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsRA4bElTCHEM3noSF.BtagEventWeightsGrid = "btagEventWeightElTCHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsRA4bElTCHEM3noSF.jets                 = "goodJets"

# SSVHEM
process.analyzeBtagsElSSVHEM3 = process.analyzeBtags.clone()
process.analyzeBtagsElSSVHEM3.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsElSSVHEM3.BtagJetWeights       = "btagEventWeightElSSVHEM3:RA4bSFJetWeights"
process.analyzeBtagsElSSVHEM3.BtagEventWeights     = "btagEventWeightElSSVHEM3:RA4bSFEventWeights"
process.analyzeBtagsElSSVHEM3.BtagJetWeightsGrid   = "btagEventWeightElSSVHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsElSSVHEM3.BtagEventWeightsGrid = "btagEventWeightElSSVHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsElSSVHEM3.jets                 = "goodJets"

process.analyzeBtagsElSSVHEM3highPt = process.analyzeBtags.clone()
process.analyzeBtagsElSSVHEM3highPt.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsElSSVHEM3highPt.BtagJetWeights       = "btagEventWeightElSSVHEM3highPt:RA4bSFJetWeights"
process.analyzeBtagsElSSVHEM3highPt.BtagEventWeights     = "btagEventWeightElSSVHEM3highPt:RA4bSFEventWeights"
process.analyzeBtagsElSSVHEM3highPt.BtagJetWeightsGrid   = "btagEventWeightElSSVHEM3highPt:RA4bJetWeightsGrid"
process.analyzeBtagsElSSVHEM3highPt.BtagEventWeightsGrid = "btagE"TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"ventWeightElSSVHEM3highPt:RA4bEventWeightsGrid"
process.analyzeBtagsElSSVHEM3highPt.jets                 = "highPtJets"

process.analyzeBtagsElSSVHEM3lowPt = process.analyzeBtags.clone()
process.analyzeBtagsElSSVHEM3lowPt.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsElSSVHEM3lowPt.BtagJetWeights       = "btagEventWeightElSSVHEM3lowPt:RA4bSFJetWeights"
process.analyzeBtagsElSSVHEM3lowPt.BtagEventWeights     = "btagEventWeightElSSVHEM3lowPt:RA4bSFEventWeights"
process.analyzeBtagsElSSVHEM3lowPt.BtagJetWeightsGrid   = "btagEventWeightElSSVHEM3lowPt:RA4bJetWeightsGrid"
process.analyzeBtagsElSSVHEM3lowPt.BtagEventWeightsGrid = "btagEventWeightElSSVHEM3lowPt:RA4bEventWeightsGrid"
process.analyzeBtagsElSSVHEM3lowPt.jets                 = "lowPtJets"

process.analyzeBtagsElSSVHEM4       = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElSSVHEM4highPt = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsElSSVHEM4lowPt  = process.analyzeBtagsElSSVHEM3lowPt.clone()

# clones"TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"
process.analyzeBtagsRA4bElSSVHEM3       = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsRA4bElSSVHEM3highPt = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsRA4bElSSVHEM3lowPt  = process.analyzeBtagsElSSVHEM3lowPt.clone()

process.analyzeBtagsRA4bElSSVHEM4       = process.analyzeBtagsElSSVHEM4.clone()
process.analyzeBtagsRA4bElSSVHEM4highPt = process.analyzeBtagsElSSVHEM4highPt.clone()
process.analyzeBtagsRA4bElSSVHEM4lowPt  = process.analyzeBtagsElSSVHEM4lowPt.clone()

process.analyzeBtagsElSSVHEM3dilep       = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElSSVHEM3highPtdilep = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsElSSVHEM3lowPtdilep  = process.analyzeBtagsElSSVHEM3lowPt.clone()

process.analyzeBtagsElSSVHEM4dilep       = process.analyzeBtagsElSSVHEM4.clone()
process.analyzeBtagsElSSVHEM4highPtdilep = process.analyzeBtagsElSSVHEM4highPt.clone()
process.analyzeBtagsElSSVHEM4lowPtdilep  = process.analyzeBtagsElSSVHEM4lowPt.clone()

process.analyzeBtagsElElSSVHEM3dilep       = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElElSSVHEM3highPtdilep = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsElElSSVHEM3lowPtdilep  = process.analyzeBtagsElSSVHEM3lowPt.clone()

process.analyzeBtagsElElSSVHEM4dilep       = process.analyzeBtagsElSSVHEM4.clone()
process.analyzeBtagsElElSSVHEM4highPtdilep = process.analyzeBtagsElSSVHEM4highPt.clone()
process.analyzeBtagsElElSSVHEM4lowPtdilep  = process.analyzeBtagsElSSVHEM4lowPt.clone()

# for cross-check
process.analyzeBtagsRA4bElSSVHEM3noSF = process.analyzeBtags.clone()
process.analyzeBtagsRA4bElSSVHEM3noSF.bjets                = "mediumSSVHighEffBjets"
process.analyzeBtagsRA4bElSSVHEM3noSF.BtagJetWeights       = "btagEventWeightElSSVHEM3:RA4bJetWeights"
process.analyzeBtagsRA4bElSSVHEM3noSF.BtagEventWeights     = "btagEventWeightElSSVHEM3:RA4bEventWeights"
process.analyzeBtagsRA4bElSSVHEM3noSF.BtagJetWeightsGrid   = "btagEventWeightElSSVHEM3:RA4bJetWeightsGrid"
process.analyzeBtagsRA4bElSSVHEM3noSF.BtagEventWeightsGrid = "btagEventWeightElSSVHEM3:RA4bEventWeightsGrid"
process.analyzeBtagsRA4bElSSVHEM3noSF.jets                 = "goodJets"

#--------------------------
# Electron selection paths
#--------------------------


## Standard RA4b selection
##-------------------------
process.analyzeBtags_RA4bEl = cms.Path(# Standard RA4b preselection
                                       process.preselectionElHTMC2 *
                                       process.eventWeightPU *
                                       process.weightProducer *
                                       process.makeObjects *
                                       # match different triggers
                                       process.ElHadSelection *
                                       # produce btag event weights
                                       process.btagEventWeightElSSVHEM3 *
                                       process.btagEventWeightElTCHEM3 *
                                       # muon selection
                                       process.electronSelection*
                                       # jet selection
                                       process.jetSelection*
                                       # analyze btags
                                       process.analyzeBtagsRA4bElTCHEM3 *
                                       process.analyzeBtagsRA4bElSSVHEM3*
                                       process.analyzeBtagsRA4bElTCHEM3noSF *
                                       process.analyzeBtagsRA4bElSSVHEM3noSF *
                                       # additinal cut
                                       process.oneNoSignalMET *
                                       # analyze btags
                                       process.analyzeBtagsRA4bElTCHEM4 *
                                       process.analyzeBtagsRA4bElSSVHEM4
                                       )


## RA4b selection with cut on two high pt jets in and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_RA4b2 = cms.Path(# Standard RA4b preselectio"TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"n
                                      process.preselectionElHTMC2 *
                                      process.eventWeightPU *
                                      process.weightProducer *
                                      process.makeObjects *
                                      # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                      process.highPtJets *
                                      process.lowPtJets *
                                      # additinal cut
                                      process.twoHighPtJets *
                                      # match different triggers"TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"
                                      process.ElHadSelection *
                                      # produce btag event weights
                                      process.btagEventWeightElSSVHEM3 *
                                      process.btagEventWeightElTCHEM3 *
                                      process.btagEventWeightElSSVHEM3lowPt *
                                      process.btagEventWeightElTCHEM3lowPt *
                                      process.btagEventWeightElSSVHEM3highPt *
                                      process.btagEventWeightElTCHEM3highPt *
                                      # electron selection
                                      process.electronSelection *
                                      # jet selection
                                      process.jetSelection *
                                      # analyze btags
                                      process.analyzeBtagsElTCHEM3 *
                                      process.analyzeBtagsElSSVHEM3*
                                      process.analyzeBtagsElTCHEM3lowPt *
                                      process.analyzeBtagsElSSVHEM3lowPt *
                                      process.analyzeBtagsElTCHEM3highPt *
                                      process.analyzeBtagsElSSVHEM3highPt *
                                      # additinal cut
                                      process.oneNoSignalMET *
                                      # analyze btags
                                      process.analyzeBtagsElTCHEM4 *
                                      process.analyzeBtagsElSSVHEM4*
                                      process.analyzeBtagsElTCHEM4lowPt *
                                      process.analyzeBtagsElSSVHEM4lowPt *
                                      process.analyzeBtagsElTCHEM4highPt *
                                      process.analyzeBtagsElSSVHEM4highPt
                                      )

## Incl. RA4b selection with cut on two high pt jets and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_diLep2 = cms.Path(# Standard RA4b preselection
                                       process.preselectionElHTMC2 *
                                       process.eventWeightPU *
                                       process.weightProducer *
                                       process.makeObjects *
                                       # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                       process.highPtJets *
                                       process.lowPtJets *
                                       ## additional cut
                                       process.twoHighPtJets *
                                       # match different triggers
                                       process.ElHadSelection *
                                       # produce btag event weights
                                       process.btagEventWeightElSSVHEM3 *
                                       process.btagEventWeightElTCHEM3 *
                                       process.btagEventWeightElSSVHEM3lowPt *
                                       process.btagEventWeightElTCHEM3lowPt *
                                       process.btagEventWeightElSSVHEM3highPt *
                                       process.btagEventWeightElTCHEM3highPt *
                                       # electron selection
                                       process.oneGoodElectron *
                                       # jet selection
                                       process.twoGoodJets*
                                       # analyze btags
                                       process.analyzeBtagsElTCHEM3dilep *
                                       process.analyzeBtagsElSSVHEM3dilep*
                                       process.analyzeBtagsElTCHEM3lowPtdilep *
                                       process.analyzeBtagsElSSVHEM3lowPtdilep *
                                       process.analyzeBtagsElTCHEM3highPtdilep *
                                       process.analyzeBtagsElSSVHEM3highPtdilep *
                                       # additinal cut
                                       process.oneNoSignalMET*
                                       # analyze btags
                                       process.analyzeBtagsElTCHEM4dilep *
                                       process.analyzeBtagsElSSVHEM4dilep*
                                       process.analyzeBtagsElTCHEM4lowPtdilep *
                                       process.analyzeBtagsElSSVHEM4lowPtdilep *
                                       process.analyzeBtagsElTCHEM4highPtdilep *
                                       process.analyzeBtagsElSSVHEM4highPtdilep
                                       )

## Incl. RA4b electron selection with cut on two high pt jets and MET < 300 in addition
##-------------------------------------------------------------------------------------------
process.analyzeBtags_elel = cms.Path(# Standard RA4b preselection
                                     process.preselectionElHTMC2 *
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     process.makeObjects *
                                     # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                     process.highPtJets *
                                     process.lowPtJets *
                                     ## additional cut
                                     process.twoHighPtJets *
                                     # match different triggers
                                     process.ElHadSelection *
                                     # produce btag event weights
                                     process.btagEventWeightElSSVHEM3 *
                                     process.btagEventWeightElTCHEM3 *
                                     process.btagEventWeightElSSVHEM3lowPt *
                                     process.btagEventWeightElTCHEM3lowPt *
                                     process.btagEventWeightElSSVHEM3highPt *
                                     process.btagEventWeightElTCHEM3highPt *
                                     # electron selection
                                     process.oneGoodElectron *
                                     process.noGoodMuon *
                                     # jet selection
                                     process.twoGoodJets*
                                     # analyze btags
                                     process.analyzeBtagsElElTCHEM3dilep *
                                     process.analyzeBtagsElElSSVHEM3dilep*
                                     process.analyzeBtagsElElTCHEM3lowPtdilep *
                                     process.analyzeBtagsElElSSVHEM3lowPtdilep *
                                     process.analyzeBtagsElElTCHEM3highPtdilep *
                                     process.analyzeBtagsElElSSVHEM3highPtdilep *
                                     # additinal cut
                                     process.oneNoSignalMET*
                                     # analyze btags
                                     process.analyzeBtagsElElTCHEM4dilep *
                                     process.analyzeBtagsElElSSVHEM4dilep*
                                     process.analyzeBtagsElElTCHEM4lowPtdilep *
                                     process.analyzeBtagsElElSSVHEM4lowPtdilep *
                                     process.analyzeBtagsElElTCHEM4highPtdilep *
                                     process.analyzeBtagsElElSSVHEM4highPtdilep
                                     )
