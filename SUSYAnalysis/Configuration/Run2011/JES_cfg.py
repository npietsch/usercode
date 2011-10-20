import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000),
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
## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

#from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
#process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

## from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
## process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#getattr(process, pathname).replace(process.selectedPatJets,
#                                   process.scaledJetEnergy * process.selectedPatJets)

## process.selectedPatJets.src = cms.InputTag("scaledJetEnergy", "patJets")
## process.highMETs.src = cms.InputTag("scaledJetEnergy", "patMETs")
## process.scaledJetEnergy.scaleType = "abs" #abs = 1, jes:up, jes:down
## #process.scaledJetEnergy.scaleType = "jes:up" #abs = 1, jes:up, jes:down
## #process.scaledJetEnergy.scaleType = "jes:down" #abs = 1, jes:up, jes:down

## process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, 1.5, 1.5, 2.0, 2.0, -1)

## #process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.0, 0.95, 0.9) # JER down
## process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.1, 1.1, 1.1) # JER standard
## #process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.2, 1.25, 1.3) # JER up

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#-----------------------------------------------------------------
# Scale jet energy
#-----------------------------------------------------------------

process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")

## Configure module to produce collection of jets with scaled energy

## Which jets should be "scaled"?
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.scaleType = "abs" #abs = 1, jes:up, jes:down
process.scaledJetEnergy.scaleType = "jes:up" #abs = 1, jes:up, jes:down
#process.scaledJetEnergy.scaleType = "jes:down" #abs = 1, jes:up, jes:down
#process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, 1.5, 1.5, 2.0, 2.0, -1)
#process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.0, 0.95, 0.9) # JER down
#process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.1, 1.1, 1.1) # JER standard
#process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.2, 1.25, 1.3) # JER up
#process.scaledJetEnergy.scaleFactor = 0.985 # flat offset when using scaleType = "top:*"

process.scaledJetEnergy.payload = "AK5Calo"

## Produce "good jets" from jets with scaled energy
process.goodJets.src="scaledJetEnergy:selectedPatJetsAK5PF"

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")
#process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis2_cff")

#process.load("SUSYAnalysis.SUSYAnalyzer.sequences.EventTopology_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#--------------------------
# muon selection paths
#--------------------------

## no btag
process.Selection1m = cms.Path(#process.printGenParticles *
                               process.scaledJetEnergy *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.eventWeightPU *
                               process.weightProducer *
                               process.analyzeSUSYBjets1m_noCuts *
                               process.preselectionMuHTMC2 *
                               process.MuHadSelection *
                               process.analyzeSUSYBjets1m_preselection *
                               process.RA4MuonCollections *
                               process.RA4MuonSelection *
                               process.muonSelection*
                               process.analyzeSUSYBjets1m_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1m_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1m_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1m_metSelection *
                               process.mTSelection *
                               process.analyzeSUSYBjets1m_mTSelection
                               )
## exactly 1 btag
process.Selection1b1m_2 = cms.Path(process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1m_1
                                   
                                   )
## exactly 2 btags
process.Selection2b1m_2 = cms.Path(process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets2b1m_1
                                   )
## at least 3 btags
process.Selection3b1m_1 = cms.Path(process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1m_1
                                   )

#--------------------------
# electron selection paths
#--------------------------

## no btag
process.Selection1e = cms.Path(process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.eventWeightPU *
                               process.weightProducer *
                               process.analyzeSUSYBjets1e_noCuts *
                               process.preselectionElHTMC2 *
                               process.ElHadSelection *
                               process.analyzeSUSYBjets1e_preselection *
                               process.electronSelection*
                               process.analyzeSUSYBjets1e_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1e_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1e_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1e_metSelection *
                               process.mTSelection *
                               process.analyzeSUSYBjets1e_mTSelection
                               )

## exactly 1 btag
process.Selection1b1e_2 = cms.Path(process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1e_1
                                   )

## exactly 2 btags
process.Selection2b1e_2 = cms.Path(process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets2b1e_1
                                   )

## at least 3 btags
process.Selection3b1e_1 = cms.Path(process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection *
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1e_1
                                   )

## #--------------------------
## # two lepton selection
## #--------------------------

## ## no btag
## process.Selection2l = cms.Path(process.makeObjects *
##                                process.makeSUSYGenEvt *
##                                process.eventWeightPU *
##                                process.analyzeSUSYBjets2l_noCuts *
##                                process.preselectionLepHTMC *
##                                process.LepHadSelection *
##                                process.analyzeSUSYBjets2l_preselection *
##                                process.twoGoodLeptons *
##                                process.analyzeSUSYBjets2l_leptonSelection *
##                                process.jetSelection*
##                                process.analyzeSUSYBjets2l_jetSelection *
##                                process.HTSelection *
##                                process.analyzeSUSYBjets2l_HTSelection *
##                                process.metSelection *
##                                process.analyzeSUSYBjets2l_metSelection *
##                                process.analyzeEventTopology2l_3
##                                )

## #--------------------------
## # combined selection paths
## #--------------------------

## ## no btag
## process.Selection1l = cms.Path(process.makeObjects *
##                                process.makeSUSYGenEvt *
##                                process.eventWeightPU *
##                                process.analyzeSUSYBjets1l_noCuts *
##                                process.preselectionLepHTMC *
##                                process.LepHadSelection *
##                                process.analyzeSUSYBjets1l_preselection *
##                                process.leptonSelection*
##                                process.analyzeSUSYBjets1l_leptonSelection *
##                                process.jetSelection*
##                                process.analyzeSUSYBjets1l_jetSelection *
##                                process.HTSelection *
##                                process.analyzeSUSYBjets1l_HTSelection *
##                                process.metSelection *
##                                process.analyzeSUSYBjets1l_metSelection *
##                                process.analyzeEventTopology1l_3
##                                )
## ## exactly 1 btag
## process.Selection1b1l_2 = cms.Path(process.makeObjects *
##                                    process.makeSUSYGenEvt *
##                                    process.eventWeightPU *
##                                    process.preselectionLepHTMC *
##                                    process.LepHadSelection *
##                                    process.leptonSelection*
##                                    process.jetSelection *
##                                    process.exactlyOneMediumTrackHighEffBjet *
##                                    process.analyzeSUSYBjets1b1l_4 *
##                                    process.HTSelection *
##                                    process.analyzeSUSYBjets1b1l_5 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets1b1l_6 *
##                                    process.analyzeEventTopology1b1l_6
##                                    )
## ## exactly 2 btags
## process.Selection2b1l_2 = cms.Path(process.makeObjects *
##                                    process.makeSUSYGenEvt *
##                                    process.eventWeightPU *
##                                    process.preselectionLepHTMC *
##                                    process.LepHadSelection *
##                                    process.leptonSelection*
##                                    process.jetSelection *
##                                    process.exactlyTwoMediumTrackHighEffBjets *
##                                    process.analyzeSUSYBjets2b1l_4 *
##                                    process.HTSelection *
##                                    process.analyzeSUSYBjets2b1l_5 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets2b1l_6 *
##                                    process.analyzeEventTopology2b1l_6
##                                    )
## ## at least 3 btags
## process.Selection3b1l_1 = cms.Path(process.makeObjects *
##                                    process.makeSUSYGenEvt *
##                                    process.eventWeightPU *
##                                    process.preselectionLepHTMC *
##                                    process.LepHadSelection *
##                                    process.leptonSelection *
##                                    process.jetSelection *
##                                    process.threeMediumTrackHighEffBjets *
##                                    process.analyzeSUSYBjets3b1l_1 *
##                                    process.HTSelection *
##                                    process.analyzeSUSYBjets3b1l_2 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets3b1l_3 *
##                                    process.analyzeEventTopology3b1l_3
##                                    )

