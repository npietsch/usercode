from BjetsData_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_94_2_GcM.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_107_2_oB7.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_105_2_Mu9.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_65_2_9rW.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_96_2_yz4.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_106_2_VB2.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_82_2_nzm.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_61_2_JFa.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_81_2_1TX.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_101_2_oIw.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_66_2_U0N.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_85_2_F7y.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_63_2_GDX.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_69_2_reQ.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_102_2_Wlw.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_67_2_CP8.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_83_2_D66.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_87_2_5kW.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_109_2_TM5.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_41_2_5OQ.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_72_2_enz.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_68_2_QAp.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_92_2_kOb.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_74_2_hdR.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_70_2_LGL.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_73_2_PUw.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_39_2_EFy.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_90_2_6FC.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_100_2_j9H.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_91_2_OC3.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_51_2_WX9.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_103_2_mrO.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_84_2_Qqx.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_110_2_jMk.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_64_2_P4p.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_13_2_qDI.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_89_2_1vG.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_88_2_HaW.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_97_2_4GE.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_40_2_4Vj.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_93_2_qey.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_60_2_WJT.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_12_2_sxk.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_53_2_qRz.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_54_2_jwP.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_42_2_cDt.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_4_2_pSc.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_48_2_Z6V.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_55_2_s1b.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_47_2_Z05.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_44_2_qcn.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_11_2_Q7m.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_71_2_4AJ.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_22_2_40N.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_43_2_KsW.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_19_2_G58.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_9_2_Dz4.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_14_2_Z2O.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_52_2_8pf.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_108_2_WCJ.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_78_2_P6V.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_21_2_2M9.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_16_2_CYT.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_17_2_3HO.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_10_2_pIC.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_15_2_zsa.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_23_2_obI.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_30_2_bwd.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_38_2_cYb.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_59_2_fND.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_29_2_1Ep.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_80_2_0HE.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_99_2_MPo.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_45_2_4ue.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_25_2_Mhg.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_35_2_n8b.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_75_2_KX7.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_20_2_kVy.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_7_2_uVY.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_56_2_vvf.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_2_2_HX1.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_18_2_iHz.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_1_2_EbI.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_98_2_0St.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_3_2_OAD.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_6_2_KTZ.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_26_2_6k0.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_36_2_afv.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_24_2_oA8.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_34_2_kmE.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_50_2_J25.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_76_2_U9q.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_77_2_xLt.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_32_2_tMm.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_57_2_ovC.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_37_2_mjt.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_33_2_6IV.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_79_2_ZOq.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_49_2_WW8.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_46_2_18E.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_28_2_ibE.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_31_2_zyP.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_5_2_7Yk.root',
'/store/user/cakir/MuHad/MuHad_05Aug2011/3a40145936c3805b27cefb801160c593/Summer11_27_2_D4u.root'
)
)