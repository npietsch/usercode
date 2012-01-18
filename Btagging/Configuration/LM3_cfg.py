#-------------------------------------------
# To run on the NAF, type:
#
# export NJS_QUEUE=1 
# nafJobSplitter.pl 31 RA4b_LM3_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 3.438
process.weightProducer.NumberEvts = 440000
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_10_1_7QP.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_11_1_q43.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_12_1_wRZ.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_13_1_5oA.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_14_1_I4X.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_15_1_Ez6.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_16_1_ZYc.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_17_1_bfo.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_18_1_p8z.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_19_1_ohy.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_1_1_y6F.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_20_1_pci.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_21_1_QYj.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_22_1_aY9.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_23_1_7fa.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_24_1_rab.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_25_1_9ob.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_26_2_NQe.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_27_1_SII.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_28_1_c6A.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_29_1_1Er.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_2_1_w6Y.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_30_1_WDh.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_31_1_h42.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_3_1_KvX.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_4_1_iwM.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_5_1_5Ki.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_6_1_9NG.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_7_1_z56.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_8_1_PwW.root',
    '/store/user/fcostanz/LM3_SUSY_sftsht_7TeV-pythia6/LM3_Summer2011_v2/7775abddf4cecee1ba70f412bba59ece/Summer11_9_1_pSy.root'
    )
)
