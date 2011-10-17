from BjetsData_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_99_1_LM1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_98_1_2OZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_97_1_ssP.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_96_1_SdN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_95_1_Nkm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_94_2_Xwj.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_93_1_gS1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_92_1_0P3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_91_1_1RS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_90_1_0t5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_9_1_tCK.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_89_1_AxD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_88_1_6P3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_87_1_jYb.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_86_1_5pl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_85_1_EC1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_84_1_3eZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_83_1_xhJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_82_1_yB3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_81_1_P7o.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_80_1_aXz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_8_1_gXl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_79_1_b1G.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_78_1_7wF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_77_1_wCh.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_76_1_kKH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_75_1_wyZ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_74_1_gKz.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_73_1_3WD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_72_1_aYU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_71_1_rzq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_70_1_DWN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_7_1_nL4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_69_1_wLG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_68_1_JtY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_67_1_jIM.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_66_1_WA2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_65_1_2QG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_64_1_Gf2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_63_1_Ped.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_62_1_JGN.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_61_1_SA4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_60_1_JsS.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_6_1_WpH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_59_1_Gk3.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_30_1_CfY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_58_1_cTp.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_57_1_ial.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_56_1_cPD.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_55_1_ZXJ.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_54_1_1Bo.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_53_1_4YA.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_52_1_mkH.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_51_1_nN1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_50_1_Ea4.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_5_1_Brl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_49_1_EfG.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_48_1_wj5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_47_1_VFv.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_46_1_XgW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_45_1_zBt.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_44_1_Rwl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_43_1_FKw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_42_1_S2h.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_41_1_gXu.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_40_1_qPw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_4_1_6JR.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_39_1_wNl.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_38_1_IPU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_37_1_pGU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_36_1_EfF.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_35_1_KGV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_34_1_HxV.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_33_1_icU.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_32_1_58T.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_31_1_JfB.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_3_1_M1P.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_29_1_a97.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_28_1_U8x.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_27_1_8bg.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_26_1_c5Z.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_25_1_Pzm.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_24_1_Tn5.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_23_1_hbe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_22_1_Aht.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_21_1_CwL.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_20_1_zQY.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_2_1_vAw.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_19_1_uhW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_18_1_hWq.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_17_1_6DC.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_16_1_06K.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_15_1_LmW.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_14_1_p0D.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_13_1_43C.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_12_1_2f1.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_11_1_D2A.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_102_1_NE2.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_101_1_H7v.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_100_1_1mI.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_10_1_TRe.root',
'/store/user/fcostanz/ElectronHad/ElectronHad_ReReco05Aug/3a40145936c3805b27cefb801160c593//Summer11_1_1_PEk.root'

)
)
