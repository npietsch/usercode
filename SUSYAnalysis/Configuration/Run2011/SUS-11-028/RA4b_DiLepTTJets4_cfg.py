#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=12 
# nafJobSplitter.pl 50 RA4b_Fall11_TTJets4_cfg.py
#----------------------------------------------------

from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_TTJetsFall11.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_TTJetsFall11.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_TTJetsFall11.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"

process.preselectionLepHTMC2 = process.preselectionDiLep

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_554_3_ciE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_555_1_DQ4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_556_1_q0z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_557_1_pmO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_558_1_p6d.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_559_1_YGz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_560_1_jNT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_561_1_K3K.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_56_1_aDi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_562_1_GIt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_563_1_PZ1.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_564_3_Tr0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_565_1_O4y.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_566_1_vd9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_567_1_Ixh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_568_1_cNH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_569_1_HBE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_570_1_Vro.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_571_1_qDX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_57_1_Wp3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_572_1_fuv.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_573_1_PhG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_574_1_JYs.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_575_1_ilE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_576_1_K4C.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_577_1_kUj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_578_1_jlh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_579_1_4T1.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_580_1_PHh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_581_1_DZ4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_58_1_ceh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_582_1_NZM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_583_1_3YI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_584_1_YlH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_585_1_yuf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_586_1_oBA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_587_1_SXt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_588_1_vIT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_589_1_KDV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_590_1_k93.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_591_1_BLC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_59_1_eB2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_592_1_Du5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_593_1_kDU.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_594_1_r7I.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_595_1_ylF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_596_1_K3J.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_597_1_FEA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_598_1_iLM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_599_1_TZ8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_600_1_I2C.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_601_1_1by.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_60_1_tPs.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_602_1_ez8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_603_1_8zh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_604_1_nIO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_605_3_7e9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_606_1_IRo.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_607_2_Mc8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_608_1_oh4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_609_1_m26.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_610_1_27Z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_611_1_8uw.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_61_1_m9F.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_612_1_Vjp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_613_1_UZC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_614_2_CH3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_615_1_eb7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_616_2_PJS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_617_1_Op5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_618_1_Cyt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_619_1_eiS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_6_1_iTd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_620_1_Dvg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_621_1_pBM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_62_1_xCs.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_622_2_iSX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_623_2_bye.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_624_1_y3o.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_625_1_Vcb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_626_1_g5b.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_627_1_YNb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_628_2_ykO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_629_1_rX0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_630_2_U4P.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_631_1_rMG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_63_1_Cy7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_632_1_hdl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_633_1_crN.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_634_1_uD3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_635_2_V5d.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_636_1_tbL.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_637_1_lYn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_638_2_D7v.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_639_1_4dj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_640_1_IIb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_641_1_WAT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_64_1_72Z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_642_1_fDZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_643_1_ApK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_644_1_0LF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_645_1_t8Y.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_646_1_H2Q.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_647_1_Ea5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_648_1_7MT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_649_1_wMK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_650_1_sai.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_65_1_0Kj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_651_1_KHj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_652_1_iVf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_653_1_hS9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_654_1_FvZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_655_1_wNu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_656_1_czB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_657_1_dxp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_658_1_Ll9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_659_1_Evh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_660_1_6jy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_661_1_Ch5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_66_1_WB9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_662_1_SFt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_663_1_nlb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_664_1_lMo.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_665_1_aWu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_666_1_Mco.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_667_2_k6I.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_668_1_scp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_669_1_tZB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_670_1_aNS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_671_1_zwi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_67_1_N2V.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_672_1_llQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_673_2_KX1.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_674_1_mdd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_675_1_EWC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_676_1_V08.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_677_1_OJM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_678_1_pPf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_679_2_cGE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_680_1_Ks6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_681_2_DcQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_68_1_SBK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_682_1_6c4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_683_1_GV4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_684_3_vMA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_685_1_SqR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_686_1_Bc2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_687_2_T52.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_688_1_o4Q.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_689_1_Ul7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_690_1_Xav.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_691_1_9Ye.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_69_1_isH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_692_1_Z62.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_693_1_1xG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_694_1_rXt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_695_1_7We.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_696_1_Bx5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_697_1_T7a.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_698_1_K4N.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_699_1_qQZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_700_1_kvd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_701_1_EWy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_70_1_YB6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_702_1_TOp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_703_1_Hli.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_704_1_KrE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_705_1_Bs2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_706_1_mtE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_707_1_J9L.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_708_1_zMD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_709_1_N6m.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_710_1_KK3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_711_1_0qa.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_71_1_1ow.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_712_1_DHk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_713_1_MOw.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_714_1_FCR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_715_1_MIA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_716_1_1hp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_717_1_MEN.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_718_1_Kj5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_719_1_pmz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_7_1_bKh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_720_1_qFR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_721_1_Pur.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_72_1_jCW.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_722_1_vAG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_723_1_puT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_724_1_zX2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_725_1_uQY.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_726_1_8ul.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_727_1_L8S.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_728_1_qBb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_729_1_ZbC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_730_1_n1C.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_731_1_rub.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_73_1_4om.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_732_1_9Hz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_733_1_Tbx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_734_1_LnP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_735_1_00F.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_736_1_T8Y.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_737_1_NDy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_738_1_n75.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_739_1_PLI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_740_1_oEm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_741_1_Znk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_74_1_JnQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_742_1_rf1.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_743_1_aC5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_744_1_YJK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_745_1_Qij.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_746_1_tJ9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_747_1_5ph.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_748_1_dEO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_749_1_nwE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_750_1_uai.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_751_1_8gC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_75_1_Tk5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_752_1_edR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_753_1_ALF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_754_1_N0Z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_755_1_Exg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_756_1_ygp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_757_1_xg2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_758_1_k3p.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_759_1_wxN.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_760_1_VAe.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_761_1_HWX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_76_1_4B6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_762_1_KBZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_763_1_NcB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_764_1_tKM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_765_1_o1U.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_766_1_zR1.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_767_1_fhn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_768_1_ouD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_769_1_5bT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_770_1_0YA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_771_3_qSP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_77_1_rMS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_772_1_zVX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_773_1_jIg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_774_1_BCv.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_775_1_1NQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_776_1_FDi.root'
)
)
