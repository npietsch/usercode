import FWCore.ParameterSet.Config as cms

process = cms.Process("BtagEff") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('BtagEff.root')
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

#-----------------------------------------------------------------
# Load and configure modules for event weighting
#-----------------------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"
process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#------------------------------------------------------------------------------------------------------------
# Load module to estimate b-tag efficiency and mis-tag rate for c and light quark jets in simulated events
#------------------------------------------------------------------------------------------------------------

process.load("TopAnalysis.TopAnalyzer.BTagEfficiencyAnalyzer_cfi")

process.analyzeBTagEfficiency.jets = "goodJets"
process.analyzeBTagEfficiency.binsPtB     =  0.,10.,20.,30.,40.,50.,60.,80.,140.,250.,500.
process.analyzeBTagEfficiency.binsEtaB    =  0.,0.45,0.9,1.2,1.65,2.1,2.4,3.
process.analyzeBTagEfficiency.binsPtL     =  0.,10.,20.,30.,40.,50.,60.,80.,140.,250.,500.
process.analyzeBTagEfficiency.binsEtaL    =  0.,0.8,1.6,2.4,3.

## Muon RA4b weights
##--------------------------

## TCHEM
process.bTagEffRA4bMuTCHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuTCHEM1.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffRA4bMuTCHEM1.bTagDiscrCut = 3.3
process.bTagEffRA4bMuTCHEM2 = process.bTagEffRA4bMuTCHEM1.clone()
process.bTagEffRA4bMuTCHEM3 = process.bTagEffRA4bMuTCHEM1.clone()
process.bTagEffRA4bMuTCHEM4 = process.bTagEffRA4bMuTCHEM1.clone()

## TCHPM
process.bTagEffRA4bMuTCHPM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuTCHPM1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffRA4bMuTCHPM1.bTagDiscrCut = 1.93
process.bTagEffRA4bMuTCHPM2 = process.bTagEffRA4bMuTCHPM1.clone()
process.bTagEffRA4bMuTCHPM3 = process.bTagEffRA4bMuTCHPM1.clone()
process.bTagEffRA4bMuTCHPM4 = process.bTagEffRA4bMuTCHPM1.clone()

## TCHPT
process.bTagEffRA4bMuTCHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuTCHPT1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffRA4bMuTCHPT1.bTagDiscrCut = 3.41
process.bTagEffRA4bMuTCHPT2 = process.bTagEffRA4bMuTCHPT1.clone()
process.bTagEffRA4bMuTCHPT3 = process.bTagEffRA4bMuTCHPT1.clone()
process.bTagEffRA4bMuTCHPT4 = process.bTagEffRA4bMuTCHPT1.clone()

## SSVHEM
process.bTagEffRA4bMuSSVHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuSSVHEM1.bTagAlgo = "simpleSecondaryVertexHighEffBJetTags"
process.bTagEffRA4bMuSSVHEM1.bTagDiscrCut = 1.74
process.bTagEffRA4bMuSSVHEM2 = process.bTagEffRA4bMuSSVHEM1.clone()
process.bTagEffRA4bMuSSVHEM3 = process.bTagEffRA4bMuSSVHEM1.clone()
process.bTagEffRA4bMuSSVHEM4 = process.bTagEffRA4bMuSSVHEM1.clone()

## SSVHPT
process.bTagEffRA4bMuSSVHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuSSVHPT1.bTagAlgo = "simpleSecondaryVertexHighPurBJetTags"
process.bTagEffRA4bMuSSVHPT1.bTagDiscrCut = 2.0
process.bTagEffRA4bMuSSVHPT2 = process.bTagEffRA4bMuSSVHPT1.clone()
process.bTagEffRA4bMuSSVHPT3 = process.bTagEffRA4bMuSSVHPT1.clone()
process.bTagEffRA4bMuSSVHPT4 = process.bTagEffRA4bMuSSVHPT1.clone()

## Electron RA4b weights
##--------------------------

## TCHEM
process.bTagEffRA4bElTCHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElTCHEM1.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffRA4bElTCHEM1.bTagDiscrCut = 3.3
process.bTagEffRA4bElTCHEM2 = process.bTagEffRA4bElTCHEM1.clone()
process.bTagEffRA4bElTCHEM3 = process.bTagEffRA4bElTCHEM1.clone()
process.bTagEffRA4bElTCHEM4 = process.bTagEffRA4bElTCHEM1.clone()

## TCHPM
process.bTagEffRA4bElTCHPM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElTCHPM1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffRA4bElTCHPM1.bTagDiscrCut = 1.93
process.bTagEffRA4bElTCHPM2 = process.bTagEffRA4bElTCHPM1.clone()
process.bTagEffRA4bElTCHPM3 = process.bTagEffRA4bElTCHPM1.clone()
process.bTagEffRA4bElTCHPM4 = process.bTagEffRA4bElTCHPM1.clone()

## TCHPT
process.bTagEffRA4bElTCHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElTCHPT1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffRA4bElTCHPT1.bTagDiscrCut = 3.41
process.bTagEffRA4bElTCHPT2 = process.bTagEffRA4bElTCHPT1.clone()
process.bTagEffRA4bElTCHPT3 = process.bTagEffRA4bElTCHPT1.clone()
process.bTagEffRA4bElTCHPT4 = process.bTagEffRA4bElTCHPT1.clone()

## SSVHEM
process.bTagEffRA4bElSSVHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElSSVHEM1.bTagAlgo = "simpleSecondaryVertexHighEffBJetTags"
process.bTagEffRA4bElSSVHEM1.bTagDiscrCut = 1.74
process.bTagEffRA4bElSSVHEM2 = process.bTagEffRA4bElSSVHEM1.clone()
process.bTagEffRA4bElSSVHEM3 = process.bTagEffRA4bElSSVHEM1.clone()
process.bTagEffRA4bElSSVHEM4 = process.bTagEffRA4bElSSVHEM1.clone()

## SSVHPT
process.bTagEffRA4bElSSVHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElSSVHPT1.bTagAlgo = "simpleSecondaryVertexHighPurBJetTags"
process.bTagEffRA4bElSSVHPT1.bTagDiscrCut = 2.0
process.bTagEffRA4bElSSVHPT2 = process.bTagEffRA4bElSSVHPT1.clone()
process.bTagEffRA4bElSSVHPT3 = process.bTagEffRA4bElSSVHPT1.clone()
process.bTagEffRA4bElSSVHPT4 = process.bTagEffRA4bElSSVHPT1.clone()

## Muon Dilep weights
##--------------------------

## TCHEM
process.bTagEffDilepMuTCHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepMuTCHEM1.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffDilepMuTCHEM1.bTagDiscrCut = 3.3
process.bTagEffDilepMuTCHEM2 = process.bTagEffDilepMuTCHEM1.clone()
process.bTagEffDilepMuTCHEM3 = process.bTagEffDilepMuTCHEM1.clone()
process.bTagEffDilepMuTCHEM4 = process.bTagEffDilepMuTCHEM1.clone()

## TCHPM
process.bTagEffDilepMuTCHPM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepMuTCHPM1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffDilepMuTCHPM1.bTagDiscrCut = 1.93
process.bTagEffDilepMuTCHPM2 = process.bTagEffDilepMuTCHPM1.clone()
process.bTagEffDilepMuTCHPM3 = process.bTagEffDilepMuTCHPM1.clone()
process.bTagEffDilepMuTCHPM4 = process.bTagEffDilepMuTCHPM1.clone()

## TCHPT
process.bTagEffDilepMuTCHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepMuTCHPT1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffDilepMuTCHPT1.bTagDiscrCut = 3.41
process.bTagEffDilepMuTCHPT2 = process.bTagEffDilepMuTCHPT1.clone()
process.bTagEffDilepMuTCHPT3 = process.bTagEffDilepMuTCHPT1.clone()
process.bTagEffDilepMuTCHPT4 = process.bTagEffDilepMuTCHPT1.clone()

## SSVHEM
process.bTagEffDilepMuSSVHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepMuSSVHEM1.bTagAlgo = "simpleSecondaryVertexHighEffBJetTags"
process.bTagEffDilepMuSSVHEM1.bTagDiscrCut = 1.74
process.bTagEffDilepMuSSVHEM2 = process.bTagEffDilepMuSSVHEM1.clone()
process.bTagEffDilepMuSSVHEM3 = process.bTagEffDilepMuSSVHEM1.clone()
process.bTagEffDilepMuSSVHEM4 = process.bTagEffDilepMuSSVHEM1.clone()

## SSVHPT
process.bTagEffDilepMuSSVHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepMuSSVHPT1.bTagAlgo = "simpleSecondaryVertexHighPurBJetTags"
process.bTagEffDilepMuSSVHPT1.bTagDiscrCut = 2.0
process.bTagEffDilepMuSSVHPT2 = process.bTagEffDilepMuSSVHPT1.clone()
process.bTagEffDilepMuSSVHPT3 = process.bTagEffDilepMuSSVHPT1.clone()
process.bTagEffDilepMuSSVHPT4 = process.bTagEffDilepMuSSVHPT1.clone()

## Electron Dilep weights
##----------------------------

## TCHEM
process.bTagEffDilepElTCHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepElTCHEM1.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffDilepElTCHEM1.bTagDiscrCut = 3.3
process.bTagEffDilepElTCHEM2 = process.bTagEffDilepElTCHEM1.clone()
process.bTagEffDilepElTCHEM3 = process.bTagEffDilepElTCHEM1.clone()
process.bTagEffDilepElTCHEM4 = process.bTagEffDilepElTCHEM1.clone()

## TCHPM
process.bTagEffDilepElTCHPM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepElTCHPM1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffDilepElTCHPM1.bTagDiscrCut = 1.93
process.bTagEffDilepElTCHPM2 = process.bTagEffDilepElTCHPM1.clone()
process.bTagEffDilepElTCHPM3 = process.bTagEffDilepElTCHPM1.clone()
process.bTagEffDilepElTCHPM4 = process.bTagEffDilepElTCHPM1.clone()

## TCHPT
process.bTagEffDilepElTCHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepElTCHPT1.bTagAlgo = "trackCountingHighPurBJetTags"
process.bTagEffDilepElTCHPT1.bTagDiscrCut = 3.41
process.bTagEffDilepElTCHPT2 = process.bTagEffDilepElTCHPT1.clone()
process.bTagEffDilepElTCHPT3 = process.bTagEffDilepElTCHPT1.clone()
process.bTagEffDilepElTCHPT4 = process.bTagEffDilepElTCHPT1.clone()

## SSVHEM
process.bTagEffDilepElSSVHEM1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepElSSVHEM1.bTagAlgo = "simpleSecondaryVertexHighEffBJetTags"
process.bTagEffDilepElSSVHEM1.bTagDiscrCut = 1.74
process.bTagEffDilepElSSVHEM2 = process.bTagEffDilepElSSVHEM1.clone()
process.bTagEffDilepElSSVHEM3 = process.bTagEffDilepElSSVHEM1.clone()
process.bTagEffDilepElSSVHEM4 = process.bTagEffDilepElSSVHEM1.clone()

## SSVHPT
process.bTagEffDilepElSSVHPT1 = process.analyzeBTagEfficiency.clone()
process.bTagEffDilepElSSVHPT1.bTagAlgo = "simpleSecondaryVertexHighPurBJetTags"
process.bTagEffDilepElSSVHPT1.bTagDiscrCut = 2.0
process.bTagEffDilepElSSVHPT2 = process.bTagEffDilepElSSVHPT1.clone()
process.bTagEffDilepElSSVHPT3 = process.bTagEffDilepElSSVHPT1.clone()
process.bTagEffDilepElSSVHPT4 = process.bTagEffDilepElSSVHPT1.clone()


#-----------------------------------------------------------------
# selection paths
#-----------------------------------------------------------------


## calculate weights for RA4b selection
##------------------------------------------

process.BtagEfficiencies_Muon = cms.Path(# preselection
                                         process.preselectionMuHTMC2 *
                                         process.makeObjects *
                                         process.eventWeightPU *
                                         process.weightProducer *
                                         # match different triggers
                                         process.MuHadSelection *
                                         # estimate btag eff
                                         process.bTagEffRA4bMuTCHEM1 *
                                         process.bTagEffRA4bMuTCHPM1 *
                                         process.bTagEffRA4bMuTCHPT1 *
                                         process.bTagEffRA4bMuSSVHEM1 *
                                         process.bTagEffRA4bMuSSVHPT1 *
                                         # muon selection
                                         process.muonSelection *
                                         # etsimate btag eff
                                         process.bTagEffRA4bMuTCHEM2 *
                                         process.bTagEffRA4bMuTCHPM2 *
                                         process.bTagEffRA4bMuTCHPT2 *
                                         process.bTagEffRA4bMuSSVHEM2 *
                                         process.bTagEffRA4bMuSSVHPT2 *
                                         # jet selection
                                         process.jetSelection*
                                         #estimate btagg eff 
                                         process.bTagEffRA4bMuTCHEM3 *
                                         process.bTagEffRA4bMuTCHPM3 *
                                         process.bTagEffRA4bMuTCHPT3 *
                                         process.bTagEffRA4bMuSSVHEM3 *
                                         process.bTagEffRA4bMuSSVHPT3 *
                                         # additinal cut
                                         process.oneNoSignalMET *
                                         # estimate btagg eff 
                                         process.bTagEffRA4bMuTCHEM4 *
                                         process.bTagEffRA4bMuTCHPM4 *
                                         process.bTagEffRA4bMuTCHPT4 *
                                         process.bTagEffRA4bMuSSVHEM4 *
                                         process.bTagEffRA4bMuSSVHPT4
                                         )

process.BtagEfficiencies_Electron = cms.Path(# preselection
                                             process.preselectionMuHTMC2 *
                                             process.makeObjects *
                                             process.eventWeightPU *
                                             process.weightProducer *
                                             process.MuHadSelection *
                                             # estimate btag eff
                                             process.bTagEffRA4bElTCHEM1 *
                                             process.bTagEffRA4bElTCHPM1 *
                                             process.bTagEffRA4bElTCHPT1 *
                                             process.bTagEffRA4bElSSVHEM1 *
                                             process.bTagEffRA4bElSSVHPT1 *
                                             # electron selection
                                             process.electronSelection *
                                             # etsimate btag eff
                                             process.bTagEffRA4bElTCHEM2 *
                                             process.bTagEffRA4bElTCHPM2 *
                                             process.bTagEffRA4bElTCHPT2 *
                                             process.bTagEffRA4bElSSVHEM2 *
                                             process.bTagEffRA4bElSSVHPT2 *
                                             #jet selection
                                             process.jetSelection*
                                             #estimate btagg eff 
                                             process.bTagEffRA4bElTCHEM3 *
                                             process.bTagEffRA4bElTCHPM3 *
                                             process.bTagEffRA4bElTCHPT3 *
                                             process.bTagEffRA4bElSSVHEM3 *
                                             process.bTagEffRA4bElSSVHPT3 *
                                             # additinal cut
                                             process.oneNoSignalMET *
                                             # estimate btagg eff 
                                             process.bTagEffRA4bElTCHEM4 *
                                             process.bTagEffRA4bElTCHPM4 *
                                             process.bTagEffRA4bElTCHPT4 *
                                             process.bTagEffRA4bElSSVHEM4 *
                                             process.bTagEffRA4bElSSVHPT4
                                             )

## calculate weights for dilep selection
##------------------------------------------

process.BtagEfficiencies_Muon2 = cms.Path(# preselection
                                          process.preselectionMuHTMC2 *
                                          process.makeObjects *
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.MuHadSelection *
                                          # estimate btag eff
                                          process.bTagEffDilepMuTCHEM1 *
                                          process.bTagEffDilepMuTCHPM1 *
                                          process.bTagEffDilepMuTCHPT1 *
                                          process.bTagEffDilepMuSSVHEM1 *
                                          process.bTagEffDilepMuSSVHPT1 *
                                          # muon selection
                                          process.oneGoodMuon*
                                          # etsimate btag eff
                                          process.bTagEffDilepMuTCHEM2 *
                                          process.bTagEffDilepMuTCHPM2 *
                                          process.bTagEffDilepMuTCHPT2 *
                                          process.bTagEffDilepMuSSVHEM2 *
                                          process.bTagEffDilepMuSSVHPT2 *
                                          #jet selection
                                          process.twoGoodJets *
                                          #estimate btagg eff 
                                          process.bTagEffDilepMuTCHEM3 *
                                          process.bTagEffDilepMuTCHPM3 *
                                          process.bTagEffDilepMuTCHPT3 *
                                          process.bTagEffDilepMuSSVHEM3 *
                                          process.bTagEffDilepMuSSVHPT3 *
                                          # additinal cut
                                          process.oneNoSignalMET *
                                          # estimate btagg eff 
                                          process.bTagEffDilepMuTCHEM4 *
                                          process.bTagEffDilepMuTCHPM4 *
                                          process.bTagEffDilepMuTCHPT4 *
                                          process.bTagEffDilepMuSSVHEM4 *
                                          process.bTagEffDilepMuSSVHPT4
                                          )

process.BtagEfficiencies_Electron2 = cms.Path(# preselection
                                              process.preselectionMuHTMC2 *
                                              process.makeObjects *
                                              process.eventWeightPU *
                                              process.weightProducer *
                                              process.MuHadSelection *
                                              # estimate btag eff
                                              process.bTagEffDilepElTCHEM1 *
                                              process.bTagEffDilepElTCHPM1 *
                                              process.bTagEffDilepElTCHPT1 *
                                              process.bTagEffDilepElSSVHEM1 *
                                              process.bTagEffDilepElSSVHPT1 *
                                              # muon selection
                                              process.oneGoodElectron *
                                              # etsimate btag eff
                                              process.bTagEffDilepElTCHEM2 *
                                              process.bTagEffDilepElTCHPM2 *
                                              process.bTagEffDilepElTCHPT2 *
                                              process.bTagEffDilepElSSVHEM2 *
                                              process.bTagEffDilepElSSVHPT2 *
                                              #jet selection
                                              process.twoGoodJets *
                                              #estimate btagg eff 
                                              process.bTagEffDilepElTCHEM3 *
                                              process.bTagEffDilepElTCHPM3 *
                                              process.bTagEffDilepElTCHPT3 *
                                              process.bTagEffDilepElSSVHEM3 *
                                              process.bTagEffDilepElSSVHPT3 *
                                              # additinal cut
                                              process.oneNoSignalMET *
                                              # estimate btagg eff 
                                              process.bTagEffDilepElTCHEM4 *
                                              process.bTagEffDilepElTCHPM4 *
                                              process.bTagEffDilepElTCHPT4 *
                                              process.bTagEffDilepElSSVHEM4 *
                                              process.bTagEffDilepElSSVHPT4
                                              )

## Incl. RA4b electron selection with cut on two high pt jets and MET < 300 in addition
##-------------------------------------------------------------------------------------------
process.analyzeBtags_elel = cms.Path(# Standard RA4b preselection
                                     process.preselectionElHTAllData *
                                     process.makeObjects *
                                     # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                     process.highPtJets *
                                     process.lowPtJets *
                                     ## additional cut
                                     process.twoHighPtJets *
                                     # match different triggers
                                     process.ElHadSelection *
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
