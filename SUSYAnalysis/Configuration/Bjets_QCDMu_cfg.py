from BjetsQCDPat_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_9_1_mFa.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_99_2_J3H.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_98_1_NkE.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_97_2_oQw.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_96_1_rho.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_95_1_N3b.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_94_1_PIq.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_93_1_tDA.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_92_1_ikc.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_91_1_d8J.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_90_1_mVI.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_8_1_e0u.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_89_1_b5Y.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_88_1_SAf.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_87_1_4Dx.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_86_1_3Wt.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_85_2_7Ue.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_84_1_rVr.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_83_1_OMw.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_82_1_3RA.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_81_1_U1r.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_80_1_lNt.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_7_1_xRR.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_79_1_Sdj.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_78_1_HEO.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_77_1_ms9.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_76_1_DJ5.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_75_1_JqM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_74_1_89V.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_73_1_24l.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_72_1_izY.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_71_1_Zjl.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_70_1_ePR.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_6_1_d71.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_69_1_vyw.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_68_1_3XE.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_67_1_roc.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_66_1_3N2.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_65_1_4eT.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_64_1_xlr.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_63_1_20M.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_62_1_6Xh.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_61_1_Fkl.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_60_1_4Fx.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_5_1_YGz.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_59_1_SWp.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_58_1_Bkg.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_57_1_c8w.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_56_1_8Qi.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_55_1_0Ld.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_54_1_d8g.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_53_1_uHr.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_52_1_0zV.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_51_1_fLK.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_50_1_LZF.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_4_1_C29.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_49_1_tYM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_48_1_Uk8.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_47_1_Bz7.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_46_1_V8p.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_45_1_Br0.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_44_1_apN.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_43_1_Gs7.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_42_1_aCe.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_41_1_eh8.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_40_1_nGl.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_3_1_tUc.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_39_1_Bwc.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_38_1_MMA.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_37_1_dzp.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_36_1_LHa.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_35_1_63u.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_34_1_UNG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_33_2_OGN.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_32_2_4uC.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_31_1_Qvr.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_30_1_xO4.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_2_1_a7U.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_29_2_2eK.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_298_1_oGH.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_297_1_QOg.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_296_1_ybC.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_295_1_Y2e.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_294_1_e2u.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_293_1_bga.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_292_1_AlT.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_291_2_yBN.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_290_1_GZR.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_28_1_hHf.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_289_1_WLX.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_288_1_LgW.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_287_1_BB5.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_286_2_4d5.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_285_1_0Tu.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_284_1_jY7.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_283_1_tfd.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_282_1_bjP.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_281_2_Qyt.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_280_1_azM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_27_1_Yqm.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_279_1_pJV.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_278_1_jOZ.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_277_1_UaL.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_276_1_l4y.root',
        '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_275_1_Bhw.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_274_1_JhG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_273_1_YSN.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_272_1_yfT.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_271_1_ASG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_270_1_MEu.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_26_1_zyV.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_269_1_xr8.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_268_1_kO0.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_267_1_LJG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_266_1_FRY.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_265_1_IV0.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_264_1_KU5.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_263_2_nuw.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_262_1_TQl.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_261_1_5Nu.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_260_1_9RX.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_25_1_0Pa.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_259_1_QcD.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_258_1_nvx.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_257_1_xsZ.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_256_1_Us6.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_255_1_5hI.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_254_2_usu.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_253_1_O96.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_252_1_4ou.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_251_1_xur.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_250_1_fLs.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_24_1_CvU.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_249_1_cyB.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_248_2_Doj.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_247_1_PlG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_246_1_Awq.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_245_1_zFS.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_244_1_yR6.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_243_1_haU.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_242_1_O7x.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_241_1_p9Z.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_240_1_3gp.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_23_1_kzn.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_239_1_i4H.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_238_1_zWf.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_237_1_MKM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_236_1_8xs.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_235_1_m0V.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_234_1_tkk.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_233_1_mXM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_232_1_cZz.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_231_1_jDy.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_230_1_ONB.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_22_1_oMO.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_229_1_lv5.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_228_1_V53.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_227_1_77m.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_226_1_g0V.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_225_1_yTP.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_224_1_2cm.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_223_1_NtA.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_222_1_rB7.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_221_1_GcX.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_220_1_FVD.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_21_1_T86.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_219_1_PlW.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_218_1_wA9.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_217_1_SHJ.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_216_1_Jsz.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_215_1_OcK.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_214_1_5Bm.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_213_1_SCG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_212_1_ReM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_211_1_sDM.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_210_1_5ME.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_20_1_MJz.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_209_1_b0I.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_208_1_YYe.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_207_1_T1B.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_206_1_xQ6.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_205_1_Xnc.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_204_1_1QT.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_203_1_eMh.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_202_2_daN.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_201_1_AIG.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_200_1_3Rq.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_1_1_ltB.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_19_2_idc.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_199_1_NLR.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_198_1_Rrm.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_197_1_Shy.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_196_1_I8Y.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_195_1_yGk.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_194_1_OhO.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_193_1_EPE.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_192_1_tFu.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_191_1_lNx.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_190_1_a0l.root',
    '/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_18_1_5UW.root'
    )
)
