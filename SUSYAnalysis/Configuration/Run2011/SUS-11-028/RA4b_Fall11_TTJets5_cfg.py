#----------------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=12 
# nafJobSplitter.pl 50 RA4b_Fall11_TTJets5_cfg.py
#----------------------------------------------------

from TTJets_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_TTJetsFall11.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_TTJetsFall11.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_TTJetsFall11.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_777_1_0TT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_778_1_u2s.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_779_1_Wy8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_780_1_XNf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_781_1_eZ3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_78_1_Q7E.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_782_1_BYV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_783_1_LB6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_784_1_B2J.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_785_1_sue.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_786_1_OCH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_787_1_7Rv.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_788_1_QWu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_789_1_3Yt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_790_1_e6b.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_791_1_X2n.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_79_1_dyj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_792_1_V2c.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_793_1_QL1.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_794_1_Lav.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_795_1_xq9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_796_1_MR9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_797_1_QRa.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_798_1_h9a.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_799_1_Fvq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_800_1_hgn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_801_1_YE7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_80_1_7dz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_802_1_dlf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_803_1_a0E.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_804_1_VeF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_805_1_Q3o.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_806_1_lWA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_807_2_4tg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_808_1_Fok.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_809_1_1OH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_810_1_kw3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_811_1_hrA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_81_1_8qQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_812_1_KLJ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_813_1_9bZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_814_2_u8z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_815_2_Z4Y.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_816_1_Y1q.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_817_1_PqB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_818_1_qE5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_8_1_b3t.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_820_1_054.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_821_1_aIn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_82_1_vvl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_822_1_vYZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_823_1_hAM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_824_1_ISG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_825_1_G7v.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_826_1_xHd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_827_1_8a7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_828_1_0F0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_829_1_Y77.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_830_1_Mwa.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_83_1_1nf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_831_3_AKs.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_832_1_c53.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_833_1_7RE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_834_1_lx3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_835_1_dwi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_836_2_SZm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_837_1_JUd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_838_1_1dI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_839_1_O3k.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_840_1_rNh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_841_1_f3f.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_84_1_wuM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_842_1_49d.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_843_1_MTg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_844_1_n9S.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_845_1_AUQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_846_3_WBh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_847_1_oV8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_848_1_vHW.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_849_1_zs3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_850_1_IHP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_851_1_XRB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_85_1_NQx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_852_1_2rT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_853_1_9vS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_854_1_hp5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_855_1_vuT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_856_1_I4t.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_857_1_64M.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_858_1_hmQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_859_1_Mzi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_860_1_Tae.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_861_1_cvR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_86_1_9ii.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_862_1_nZy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_863_1_TPH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_864_1_2WF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_865_1_WJ4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_866_1_LQ7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_867_1_QgG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_868_1_QAn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_869_1_QqH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_870_1_ngZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_871_1_NaO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_87_1_7pW.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_872_1_6ao.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_873_1_uBx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_874_1_76D.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_875_1_DZM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_876_1_0IT.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_877_1_W1a.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_878_1_mZG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_879_1_AT4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_880_1_BH6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_881_1_w1Z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_88_1_6eW.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_882_1_IdV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_883_1_QZm.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_884_1_u2E.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_885_1_7as.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_886_1_EbF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_887_1_waH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_888_1_2aS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_889_1_FQ5.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_890_1_5qx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_891_1_acq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_89_2_145.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_892_1_SA4.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_893_1_NVd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_894_1_JDg.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_895_1_emI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_896_1_C4M.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_897_1_EFp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_898_1_Gmj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_899_1_Jb2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_900_1_akO.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_901_3_BoV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_90_1_qDS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_902_1_cKi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_903_1_ThZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_904_1_5u2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_905_1_nVD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_906_1_z9l.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_907_1_z8d.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_908_1_e5B.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_909_1_JXB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_910_1_044.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_911_2_Xtn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_91_1_GXi.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_912_1_fML.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_913_1_fTS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_914_1_lgK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_915_1_kS0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_916_1_LUb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_917_1_O0h.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_918_1_m63.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_919_1_xCB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_9_1_HJK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_920_1_Jz8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_921_3_wS7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_92_1_RkZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_922_1_mnC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_923_1_K3p.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_924_1_O1i.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_925_1_Sle.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_926_1_GmF.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_927_1_Lgl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_928_1_F3o.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_929_1_bpQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_930_1_04u.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_931_1_JnE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_93_1_9vH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_932_1_uCI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_933_1_24W.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_934_3_1JD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_935_1_jZe.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_936_1_bN2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_937_1_yw6.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_938_1_h43.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_939_1_VRv.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_940_2_lxy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_941_2_IRd.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_94_1_vJM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_942_3_j3E.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_943_1_uHM.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_944_1_X4Z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_945_1_mIq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_946_2_nXs.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_947_1_bTV.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_948_1_Q8m.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_949_2_Vd7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_950_2_IzW.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_951_2_vns.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_95_1_59R.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_952_1_8Of.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_953_1_BtX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_954_1_8YP.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_955_1_8KQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_956_1_2RD.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_957_1_QMA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_958_1_XEb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_959_1_1kp.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_960_1_zf9.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_961_1_0lS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_96_1_SXx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_962_3_zCl.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_963_1_5St.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_964_1_QUr.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_965_1_K2n.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_966_3_0xX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_967_1_Tmt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_968_1_4bk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_969_1_PUI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_970_1_JoK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_971_1_KSa.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_97_1_9OB.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_972_1_CqL.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_973_1_Fb7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_974_1_wWb.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_975_1_Yjt.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_976_1_edI.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_977_1_7ng.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_978_1_AHy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_979_1_szC.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_980_1_U9d.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_981_1_1Nj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_98_1_N9B.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_982_1_WZ7.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_983_1_oeE.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_984_1_9nY.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_985_1_Loc.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_986_2_RT0.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_987_1_XSK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_988_1_lzf.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_989_1_CON.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_990_1_1yu.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_991_1_m8K.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_99_1_yEK.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_992_1_Lsh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_993_1_icS.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_994_1_pcn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_995_1_mdQ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_996_1_z1Z.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_997_1_vYA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_998_1_KSh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_999_1_wSL.root'
)
)
