from BjetsData_cfg import *

process.TriggerWeightProducer.MuonTriggerWeight = True

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_110_1_C96.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_103_1_3om.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_105_1_dJ0.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_42_1_kqw.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_55_1_gvL.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_44_1_nKb.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_25_1_Tu3.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_26_1_8TA.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_79_1_LHQ.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_22_1_4Ca.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_47_1_VpR.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_51_1_uDo.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_8_1_Gl4.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_77_1_Lwx.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_78_1_lab.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_11_1_HGk.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_53_1_vUW.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_45_1_xdR.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_12_1_1d3.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_13_1_zvh.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_16_1_Oaw.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_3_1_lUx.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_5_1_QcP.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_9_1_CH1.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_10_1_pir.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_76_1_eUy.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_54_1_foI.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_18_1_LlF.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_7_1_kXi.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_4_1_vNN.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_75_1_ZQ2.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_46_1_d4Q.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_41_1_VXI.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_90_1_N77.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_2_1_6CX.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_39_1_BLx.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_6_1_zpb.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_89_1_aNB.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_48_1_nU8.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_49_1_Wqj.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_40_1_1VG.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_1_1_Pmb.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_88_1_dCK.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_38_1_GWA.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_50_1_kQr.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_83_1_doD.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_97_1_5zK.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_74_1_zIz.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_72_1_Jbn.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_37_1_Q7U.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_96_1_BPv.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_98_1_AMv.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_87_1_1NS.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_111_1_cNv.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_69_1_STa.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_65_1_sJY.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_73_1_bzw.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_107_1_47B.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_84_1_2CP.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_36_1_6qo.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_66_1_XWf.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_86_1_4ef.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_63_1_N0E.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_59_1_a2D.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_82_1_u2X.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_67_1_iM1.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_108_1_IFW.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_71_1_ZPB.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_61_1_cOz.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_93_1_CbM.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_92_1_YjN.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_101_1_TJZ.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_106_1_9Dn.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_80_1_YOm.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_70_1_IZ0.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_62_1_QeJ.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_100_1_i9O.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_68_1_R0P.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_95_1_xIN.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_81_1_LXr.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_60_1_tIb.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_109_1_mqI.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_99_1_dAs.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_91_1_9fV.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_85_1_QYT.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_28_1_g8t.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_30_1_jsq.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_29_1_kRb.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_94_1_K0M.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_34_1_ibV.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_20_1_Y8D.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_31_1_OTo.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_33_1_yQs.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_21_1_0fi.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_24_1_nP7.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_14_1_yRw.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_23_1_ltj.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_58_1_lSr.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_17_1_IGS.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_57_1_IBM.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_19_1_I8l.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_56_1_W27.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_32_1_47E.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_15_1_69E.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_43_1_0qf.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_104_1_KYk.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_102_1_2Qf.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_35_1_FQO.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_64_1_Onl.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_52_1_t6l.root',
'/store/user/cakir/MuHad/MuHad_Aug05thReReco_New/Summer11_27_1_im4.root'


)
)
