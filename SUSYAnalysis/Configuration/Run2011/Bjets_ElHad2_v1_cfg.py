from BjetsData_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_281_3_5Z2.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_282_3_wGq.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_283_3_KWM.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_284_3_FSC.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_285_3_Fg5.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_286_3_hpK.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_287_3_hej.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_288_3_b8V.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_289_3_D2U.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_28_3_Y8p.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_290_3_H4q.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_291_3_vuY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_292_3_WBS.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_293_3_TYZ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_294_3_ZrI.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_295_3_UKB.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_296_3_jx4.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_297_3_NnY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_298_3_COf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_299_3_6JQ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_29_3_F5Y.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_2_3_H5T.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_30_3_NWx.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_31_3_Vz4.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_32_3_dLd.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_33_3_ZPu.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_34_3_mnv.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_35_3_a2W.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_36_3_lhx.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_37_3_2Rj.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_38_3_3uU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_39_3_PHU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_3_3_fss.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_40_3_tUp.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_41_3_MLl.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_42_3_su9.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_43_3_XBr.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_44_3_3mu.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_45_3_2vT.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_46_3_scN.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_47_3_JQU.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_48_3_H4J.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_49_3_4re.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_4_3_bzu.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_50_3_bbz.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_51_3_Xls.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_52_3_r8g.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_53_3_Pdk.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_54_3_rnk.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_55_3_RUY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_56_3_VXf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_57_3_Non.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_58_3_qHa.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_59_3_FRQ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_5_3_Qvh.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_60_3_QX8.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_61_3_1Ek.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_62_3_N94.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_63_3_bss.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_64_3_fB7.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_65_3_Q48.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_66_3_fZz.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_67_3_xUn.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_68_3_yOe.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_69_3_HT9.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_6_3_c9C.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_70_3_dCK.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_71_3_G05.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_72_3_6o7.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_73_3_lSR.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_74_3_yzd.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_75_3_Row.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_76_3_p6X.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_77_3_5qA.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_78_3_MUY.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_79_3_s6h.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_7_3_aId.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_80_3_7BO.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_81_3_PRC.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_82_3_XtK.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_83_3_0eW.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_84_3_k5T.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_85_3_fpF.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_86_3_vAw.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_87_3_xJ6.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_88_3_hPs.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_89_3_tn0.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_8_3_ej8.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_90_3_SnG.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_91_3_das.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_92_3_wA3.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_93_3_Si1.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_94_3_v8z.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_95_3_NHC.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_96_5_3C5.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_97_3_boT.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_98_3_yBf.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_99_3_wkQ.root',
'/store/user/cakir/ElectronHad/PATL1_Data2011_ElectronHadv1_ReReco_163869/5452c323c9105893e3e2aa2b5ad2dfcb/Summer11_9_3_8Xs.root'
)
)