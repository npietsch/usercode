from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
    '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_9_1_jW6.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_99_1_RF3.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_98_1_tWX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_97_1_Rjn.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_95_1_6Uk.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_94_1_KlG.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_93_1_F0f.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_92_1_WfY.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_91_1_B6s.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_90_1_OY2.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_8_1_eYV.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_89_1_G9O.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_88_1_aL6.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_87_1_R3e.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_86_1_rxf.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_85_1_H4m.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_84_1_n33.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_83_1_Bq5.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_82_1_LJI.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_81_1_m7Z.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_80_1_Gim.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_7_1_5Tb.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_79_1_w2E.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_78_1_S6K.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_77_1_iwn.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_76_1_ljF.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_75_1_EgK.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_74_1_01e.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_73_1_fyk.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_72_1_QCN.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_71_1_EsG.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_70_1_j8t.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_6_1_1Qm.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_69_1_Ltf.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_68_1_yhN.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_66_1_N5C.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_65_1_MuY.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_64_1_4EU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_63_1_xPW.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_62_1_TM7.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_61_1_LRu.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_60_1_JQd.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_5_1_USO.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_59_1_ngp.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_58_1_fcd.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_57_1_F9D.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_56_1_kDD.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_55_1_Efl.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_54_1_Pag.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_53_1_baX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_52_1_O6y.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_51_1_Vwd.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_50_1_5Rz.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_4_1_CdA.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_49_1_gja.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_48_1_myr.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_47_1_oFG.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_46_1_0Kf.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_45_1_zS7.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_44_1_D19.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_43_1_zl8.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_42_1_Wjd.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_41_1_TX7.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_40_1_1Bq.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_3_1_oRk.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_39_1_V56.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_38_1_6xK.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_37_1_ieD.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_36_1_1QQ.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_35_1_G3r.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_34_1_Oz1.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_33_1_Sw3.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_32_1_yeP.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_31_1_ZqW.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_2_1_puB.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_29_1_pWg.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_28_1_p5x.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_27_1_OKn.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_25_1_hIJ.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_24_1_Z3F.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_240_1_Do3.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_23_1_6VG.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_237_1_ps2.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_234_1_xgh.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_233_1_zTa.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_232_1_Rzk.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_230_1_WK8.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_22_1_C0v.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_229_1_DpT.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_228_1_cmS.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_226_1_3fp.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_225_1_vgF.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_224_1_Giv.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_223_1_1eX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_221_1_dGl.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_220_1_4Rg.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_21_1_0DK.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_219_1_82y.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_218_1_6om.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_217_1_8Fi.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_216_1_RBD.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_215_1_498.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_214_1_YMJ.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_213_1_HOy.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_212_1_LDs.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_211_1_Ocz.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_210_1_m0m.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_20_1_Ukg.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_209_1_AZs.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_208_1_xtU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_207_1_36Y.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_206_1_pzk.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_205_1_fDQ.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_204_1_wAa.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_203_1_HOm.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_202_1_qga.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_201_1_Fz0.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_200_1_WO5.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_1_1_qoW.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_19_1_V8S.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_199_1_F7e.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_198_1_VCV.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_197_1_G3g.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_196_1_ooU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_195_1_NuN.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_194_1_bxX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_193_1_jfh.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_192_1_h2O.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_191_1_QLO.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_190_1_8Ij.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_18_1_1dr.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_189_1_FeI.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_188_1_ZTR.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_187_1_3zX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_186_1_msa.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_185_1_pbu.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_183_1_whU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_182_1_8jR.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_181_1_74x.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_180_1_kew.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_17_1_ugI.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_179_1_62T.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_178_1_r1f.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_177_1_zpe.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_175_1_NZU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_174_1_RTS.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_173_1_tUV.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_172_1_nyj.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_171_1_y2w.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_170_1_E1a.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_16_1_08V.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_169_1_oib.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_166_1_BHl.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_165_1_Rdt.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_164_1_Ee5.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_163_1_T8j.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_162_1_z3E.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_161_1_ikh.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_160_1_4tC.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_15_1_PVU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_159_1_znw.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_157_1_v8a.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_156_1_Lc8.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_155_1_CKc.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_154_1_apn.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_153_1_0gi.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_152_1_LJy.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_151_1_pAE.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_150_1_gYX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_14_1_f4q.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_149_1_eRs.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_148_1_ukn.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_146_1_M2w.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_145_1_1w0.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_144_1_qxJ.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_143_1_vKp.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_142_1_R4a.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_141_1_t2H.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_140_1_m6X.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_13_1_4gp.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_139_1_N98.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_138_1_aqq.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_137_1_nx1.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_136_1_iIo.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_135_1_EdP.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_134_1_rUJ.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_132_1_5gO.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_131_1_TPU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_130_1_CWC.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_12_1_N3h.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_129_1_4NX.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_128_1_aca.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_126_1_MRl.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_125_1_TSg.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_123_1_znr.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_122_1_uGh.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_121_1_DdE.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_120_1_phL.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_11_1_8zM.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_119_1_W64.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_118_1_z39.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_117_1_wc7.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_116_1_Xky.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_115_1_JvI.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_114_1_alI.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_112_1_ZCu.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_111_1_Vyy.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_110_1_FLt.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_10_1_Tqh.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_108_1_DBB.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_107_1_3HK.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_106_1_DGH.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_105_1_wDE.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_104_1_w7z.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_103_1_hMm.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_102_1_QbU.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_101_1_71J.root',
        '/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_100_1_rv1.root'
)
)
