from BjetsPAT_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_284_1_KdI.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_285_1_VNr.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_286_1_my0.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_287_1_VGD.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_288_1_cwr.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_289_1_srB.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_28_1_ala.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_290_1_abJ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_291_1_kPj.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_292_1_WcJ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_293_1_1va.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_294_1_A98.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_295_1_xXt.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_296_1_XSr.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_297_1_fHa.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_298_1_1x0.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_299_1_OIm.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_29_1_nZD.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_2_1_0U6.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_30_1_OSh.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_31_1_Zbq.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_32_1_s3G.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_33_1_hAc.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_34_1_8Oy.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_35_1_zVt.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_36_1_dJQ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_37_1_6TB.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_38_1_EsF.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_39_1_U9x.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_3_1_JkK.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_40_1_I5K.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_41_1_onJ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_42_1_OF8.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_43_1_cay.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_44_1_i7A.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_45_1_2WU.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_46_1_pN0.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_47_1_6h9.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_48_1_La0.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_49_1_mVF.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_4_1_pz2.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_50_1_cRG.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_51_1_hiK.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_52_1_wNV.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_53_1_j7W.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_54_1_nNs.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_55_1_JeF.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_56_1_gPh.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_57_1_XZo.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_58_1_cSE.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_5_1_Id6.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_60_1_8SP.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_61_1_Jh2.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_62_1_BBN.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_63_1_nGN.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_64_1_sSw.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_65_1_msP.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_66_1_p1W.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_67_1_DxX.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_68_1_3zZ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_69_1_Fm3.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_6_1_pL6.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_70_1_PN1.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_71_1_h74.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_72_1_wAr.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_73_1_YAm.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_74_1_ehh.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_75_1_2ix.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_76_1_2ny.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_77_1_n2K.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_78_1_pUZ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_79_1_vMG.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_7_1_e39.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_80_1_49C.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_81_1_FSb.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_82_1_4v1.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_83_1_Wqm.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_84_1_IOe.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_85_1_LjX.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_86_1_Jd5.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_87_1_LLS.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_88_1_1zV.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_89_1_1qt.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_8_1_nLu.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_90_1_3sA.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_91_1_8WT.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_92_1_QRe.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_93_1_u2V.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_94_1_4KU.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_95_1_I2t.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_96_1_3IJ.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_97_1_BT0.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_98_1_FP8.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_99_1_hhN.root',
'/store/user/npietsch/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_9_1_HHj.root'
)
)
