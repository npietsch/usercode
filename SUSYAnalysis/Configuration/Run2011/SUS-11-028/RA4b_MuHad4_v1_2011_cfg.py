from BjetsData_cfg import *

process.TriggerWeightProducer.MuonTriggerWeight = True

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_699_1_Lou.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_394_1_0yF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_245_1_YU3.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_746_1_5ha.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_244_1_FyE.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_56_1_qj7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_566_1_N9p.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_572_1_k2m.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_500_1_Nhy.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_323_1_F4r.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_215_1_Rcw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_447_1_dX1.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_603_1_H0R.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_165_1_7Le.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_518_1_j5o.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_748_1_sPC.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_240_1_kps.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_359_1_rwf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_395_1_xz7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_706_1_zAs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_31_0_S4F.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_551_0_GBv.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_35_1_vVR.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_567_1_BZs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_116_1_lPq.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_396_1_ObS.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_226_1_Rdw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_156_1_6CK.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_197_1_lE4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_623_1_AsS.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_103_1_KHe.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_335_1_AQV.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_332_1_ppr.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_638_1_VyH.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_178_1_blH.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_284_0_xfK.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_140_1_PDs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_213_1_0Vu.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_590_1_5x7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_272_1_JTB.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_451_1_VP3.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_238_1_4G4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_322_1_v26.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_392_1_LQV.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_355_1_e0A.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_239_1_ph5.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_36_1_KmT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_334_1_A0G.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_360_1_5NP.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_362_1_7i6.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_387_1_CB0.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_24_1_MsJ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_356_1_Occ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_37_1_4As.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_138_1_3tb.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_621_1_Kl7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_605_1_r3A.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_126_1_KhW.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_593_1_SPg.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_72_1_tsf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_680_1_WcS.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_29_1_DDo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_50_0_UjC.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_10_1_vNO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_6_1_eBj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_591_1_LsR.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_594_1_K7L.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_28_1_5BY.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_9_1_Q1E.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_255_1_BgM.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_135_1_ttk.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_11_1_2sN.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_69_1_jrj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_391_1_6MG.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_545_0_EMZ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_263_1_XG4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_735_1_9D3.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_546_0_t4B.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_448_1_Orp.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_397_1_dMO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_471_0_IZB.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_508_1_IUF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_670_1_148.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_801_1_KSH.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_155_1_9Bg.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_708_1_gAU.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_531_1_veb.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_548_0_C0C.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_223_1_AoK.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_747_1_OUQ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_799_1_Ifb.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_710_1_BLu.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_8_1_Cl7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_222_1_vXd.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_665_1_wcw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_320_1_Rsf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_678_1_bgP.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_264_1_Ogg.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_289_0_5pp.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_4_1_NoT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_34_1_aZw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_516_1_4W4.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_276_1_uJT.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_501_0_Q61.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_529_1_OL6.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_619_1_Y6l.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_225_1_Abi.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_25_0_mh6.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_393_1_WTe.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_137_1_jQj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_702_1_0iw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_515_1_4rj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_767_1_sUO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_13_1_05V.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_162_1_20N.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_745_1_Boh.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_357_1_nEa.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_286_0_kVA.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_252_1_PTo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_424_1_FLw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_49_0_wUJ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_644_0_2dF.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_547_0_FDt.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_73_0_p7Y.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_694_1_Ncm.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_800_1_7Dp.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_728_1_6Ib.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_606_1_YJy.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_498_1_aaG.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_44_1_6oP.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_543_0_cHo.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_667_1_PoD.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_191_2_9wq.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_761_1_Xh9.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_40_0_Nue.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_707_1_AL8.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_655_0_K8Z.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_653_1_ntj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_5_1_gbW.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_45_1_Y3M.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_97_1_o5D.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_758_1_7aV.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_477_1_kzx.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_247_1_5Qa.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_3_1_bWf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_224_1_57C.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_166_1_XAe.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_610_1_bRr.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_489_1_OVC.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_782_1_H1D.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_512_1_In2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_438_0_tQ7.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_472_0_ypL.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_564_1_D38.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_180_1_h0J.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_461_1_UXM.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_192_1_Kpp.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_390_1_Alz.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_679_1_Dlj.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_190_1_DRD.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_563_1_pzD.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_185_1_N8l.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_38_1_3y1.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_177_1_MaV.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_584_1_Q7N.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_15_1_ddO.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_474_0_S8z.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_495_1_DMG.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_705_1_GT1.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_484_1_q5B.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_556_1_a47.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_602_1_wov.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_752_1_Qmw.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_42_0_wDI.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_96_1_uEg.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_676_1_HcG.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_757_1_g7G.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_711_1_Nlb.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_756_1_YTI.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_588_1_Q6c.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_459_1_U4M.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_635_1_Ml2.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_580_1_749.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_631_0_2rI.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_661_1_WqQ.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_554_1_hE6.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_607_1_TrH.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_709_1_3Wf.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_14_1_wfm.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_496_1_up8.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_181_1_kmy.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_583_1_Cnu.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_432_0_qFs.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_612_1_rZU.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_669_1_2Vm.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_608_1_JW0.root',
'/store/user/cakir/Summer11/MuHad_2011B/Summer11_478_1_rAL.root'


)
)