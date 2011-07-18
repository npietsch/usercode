from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_QCD_Pt_20_MuEnrichedPt_15_TuneZ2_7TeV_pythia6.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_205_2_o6i.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_343_2_nvy.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_121_2_Abq.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_87_2_TfU.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_167_2_WiD.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_345_2_qDr.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_371_2_qkd.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_248_2_6St.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_326_2_pNt.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_92_2_oNY.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_201_2_giu.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_186_2_gQy.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_219_2_k1I.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_1_2_UBA.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_44_2_D5g.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_79_2_Ge9.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_88_2_7fs.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_247_2_nHI.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_93_2_yXC.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_2_FO1.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_187_2_6ZW.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_129_4_HVE.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_125_4_x8j.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_55_4_ti7.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_61_4_w2X.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_68_4_GOM.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_122_4_faL.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_12_4_8b5.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_195_4_6LD.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_344_2_loI.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_174_3_7r8.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_45_3_XeB.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_41_3_fzy.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_84_3_CvO.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_232_2_VAV.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_46_3_Or7.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_113_2_yqX.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_49_3_nNy.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_85_3_CKi.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_303_3_QTQ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_193_3_CrL.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_33_3_1Vt.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_171_4_Efb.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_183_3_TAq.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_52_3_ZEg.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_9_2_xy3.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_235_2_vla.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_132_3_GnA.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_141_3_Seu.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_355_3_MyQ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_155_3_k6C.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_32_3_3cd.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_199_4_Lro.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_60_4_xhs.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_102_3_y00.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_42_4_sH7.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_278_3_7Kk.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_143_4_MNe.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_200_4_hl4.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_57_3_SuS.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_98_4_zEn.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_140_4_nmp.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_185_3_iVd.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_126_4_1HI.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_89_3_acE.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_3_UFH.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_47_3_p2Z.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_149_3_6u1.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_105_3_2KU.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_11_4_QYF.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_178_4_Y5s.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_22_4_ufY.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_31_3_VCF.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_153_3_8DT.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_172_3_v9t.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_142_3_JcT.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_165_4_6o6.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_196_4_0Fv.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_148_4_ico.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_110_4_Sgg.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_17_4_N9f.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_4_ChE.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_82_4_5Yt.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_76_4_axx.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_173_3_7Z8.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_29_4_aKU.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_51_4_gwX.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_117_4_EXT.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_43_4_zFZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_104_4_0L3.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_176_4_9Ko.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_108_4_aJ1.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_145_4_E37.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_81_4_3ld.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_90_4_xGl.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_194_4_YzC.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_151_4_LWI.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_10_4_Atg.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_50_4_Vcq.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_77_4_aOn.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_21_4_4Il.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_28_4_KWZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_4_vRF.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_83_4_UO3.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_4_QBU.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_100_4_eo5.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_191_4_oz2.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_182_4_17H.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_69_4_hS6.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_39_4_toq.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_120_4_iad.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_101_4_hWe.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_131_4_QBt.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_99_4_CSz.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_136_4_vz3.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_67_4_rtY.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_169_4_NI8.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_156_4_O4Z.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_63_4_VaH.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_64_4_3pC.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_158_4_gPH.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_127_4_OcS.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_135_4_Jr9.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_154_4_L8O.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_128_4_YA1.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_48_4_k18.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_80_4_PRr.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_163_4_cwa.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_14_4_Xv2.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_130_4_GBO.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_54_4_Mwl.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_175_4_Qv1.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_4_XdY.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_150_4_4cJ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_106_4_lQF.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_184_4_MZ6.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_94_4_uHR.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_123_4_wdG.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_109_4_x9l.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_116_4_jcR.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_180_4_uT7.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_159_4_QUI.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_190_4_FA0.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_115_4_14G.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_65_4_9PF.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_157_4_2t3.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_97_4_IXe.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_75_4_fq5.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_18_4_IfY.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_133_4_bBZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_86_4_7Y7.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_181_4_op2.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_103_4_Z3G.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_74_5_UoZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_179_4_45R.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_27_4_yM6.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_62_3_XYY.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_144_4_fqF.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_25_5_NYx.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_35_3_dsf.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_146_3_Nv9.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_166_3_MFk.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_95_3_3H0.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_254_4_ERR.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_307_3_lrn.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_137_4_D2Y.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_160_4_Ysx.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_47_4_uj5.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_297_2_aGm.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_231_2_bWW.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_288_2_xRI.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_331_2_uQH.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_338_2_i5K.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_249_2_NVa.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_138_2_4o8.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_302_2_C5l.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_218_2_KKQ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_377_2_1s7.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_72_2_lxz.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_243_2_s8v.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_354_2_NRZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_376_2_Lpz.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_168_2_Ose.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_188_3_GIR.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_203_2_KF2.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_384_2_2HZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_2_kUu.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_285_2_YSl.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_318_2_Y62.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_217_2_bgv.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_215_2_Oi4.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_397_2_wQe.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_348_2_qIW.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_367_2_ObZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_276_2_Dk6.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_170_2_ezZ.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_282_2_TXo.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_220_2_hJA.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_359_2_RDv.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_330_2_Cer.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_364_2_bpW.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_204_2_1YT.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_295_2_jeU.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_350_2_3zy.root',
'/store/user/fcostanz/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/QCDFlat_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_66_2_o8i.root'




    
)
)
