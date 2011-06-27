from BjetsPAT_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_9_1_BBn.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_99_1_mdC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_98_1_KGV.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_97_1_305.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_96_1_ezG.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_95_1_AJ7.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_94_1_2xy.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_93_1_DHw.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_92_1_n8q.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_91_1_kid.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_90_1_J8m.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_8_1_5gn.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_89_1_eqE.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_88_1_7vX.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_87_1_9sV.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_86_1_fav.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_85_1_4Z2.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_84_1_hRT.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_83_1_9YZ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_82_1_3II.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_81_1_GnR.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_80_1_DpL.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_7_1_NSt.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_79_1_Kc3.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_78_1_OrZ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_77_1_lt7.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_76_1_hpQ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_75_1_oCC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_74_1_Ldh.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_73_1_1lW.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_72_1_GNP.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_71_1_cTp.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_70_1_pBi.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_6_1_V63.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_69_1_kFt.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_68_1_xct.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_67_1_wnP.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_66_1_W9O.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_65_1_2L4.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_64_1_DnM.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_63_1_uW1.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_62_1_TFH.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_61_1_1bm.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_60_1_cYC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_5_1_lvX.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_59_1_x6F.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_58_1_OwW.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_57_1_ybB.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_56_1_vkw.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_55_1_b9U.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_54_1_16T.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_53_1_Dgg.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_52_1_DYf.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_51_1_SPx.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_50_1_YC2.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_4_1_U1C.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_49_1_0BZ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_48_1_mBm.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_47_1_YMg.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_46_1_e4N.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_45_1_T2C.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_44_1_BKT.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_43_1_qKN.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_42_1_Mbl.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_41_1_5tt.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_40_1_Aj7.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_3_1_nPB.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_39_1_GK0.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_38_1_dxI.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_37_1_ref.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_36_1_pcQ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_35_1_j7V.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_34_1_hTl.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_33_1_YcG.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_32_1_9mo.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_31_1_0oo.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_30_1_WoZ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_2_1_Q1X.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_29_1_k4r.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_28_1_ONh.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_27_1_49R.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_26_1_LSI.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_25_1_UE9.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_24_1_Uzq.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_23_1_6nY.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_22_1_tXH.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_21_1_Hpd.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_213_1_lKQ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_212_1_91i.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_211_1_6Pc.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_210_1_VyE.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_20_1_Cqp.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_209_1_PMZ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_208_1_KCj.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_207_1_SYl.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_206_1_YcK.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_205_1_ZUG.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_204_1_ak1.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_203_1_CNe.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_202_1_Khs.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_201_1_w8B.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_200_1_SeO.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_1_1_oFq.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_19_1_QjH.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_199_1_m80.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_198_1_tJx.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_197_1_lUU.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_196_1_ft6.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_195_1_DZc.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_194_1_vvj.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_193_1_L9G.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_192_1_HKc.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_191_1_zS1.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_190_1_xhc.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_18_1_YSm.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_189_1_whJ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_188_1_IUM.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_187_1_hcQ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_186_1_TLO.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_185_1_b5y.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_184_1_o9h.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_183_1_RnI.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_182_1_FSD.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_181_1_khd.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_180_1_brL.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_17_1_Plm.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_179_1_bpb.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_178_1_uQV.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_177_1_SkZ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_176_1_I4E.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_175_1_gTk.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_174_1_cC3.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_173_1_bXy.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_172_1_myi.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_171_1_3HN.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_170_1_jur.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_16_1_Zko.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_169_1_wed.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_168_1_Zpv.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_167_1_lPV.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_166_1_kX0.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_165_1_kGp.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_164_1_Dxp.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_163_1_ecB.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_162_1_duu.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_161_1_hpw.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_160_1_47Z.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_15_1_g66.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_159_1_Uaw.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_158_1_ftf.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_157_1_zCI.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_156_1_tk6.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_155_1_XKF.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_154_1_76J.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_153_1_c0l.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_152_1_Wcv.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_151_1_PLm.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_150_1_QvM.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_14_1_Ff1.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_149_1_N63.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_148_1_Xug.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_147_1_COV.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_146_1_6JU.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_145_1_uxJ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_144_1_8Db.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_143_1_5Ci.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_142_1_GTL.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_141_1_ZFz.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_140_1_mcN.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_13_1_cHH.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_139_1_PMi.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_138_1_JHW.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_137_1_HHk.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_136_1_VW1.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_135_1_Hnl.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_134_1_t04.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_133_1_UF7.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_132_1_iYd.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_131_1_r8g.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_130_1_Uwd.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_12_1_FA5.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_129_1_9TC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_128_1_AXP.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_127_1_BkG.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_126_1_d9p.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_125_1_zfx.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_124_1_VWV.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_123_1_6CQ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_122_1_Zkj.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_121_1_bmf.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_120_1_v6S.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_11_1_QRA.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_119_1_9YA.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_118_1_K2s.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_117_1_Exh.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_116_1_INN.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_115_1_Vrj.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_114_1_O1K.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_113_1_iI5.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_112_1_Vwy.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_111_1_8ca.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_110_1_wSs.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_10_1_61K.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_109_1_fmC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_108_1_GHC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_107_1_EcY.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_106_1_7iX.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_105_1_h4U.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_104_1_Ijv.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_103_1_4PJ.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_102_1_ZYC.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_101_1_OT9.root',
        '/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_100_1_kKD.root'
)
)
