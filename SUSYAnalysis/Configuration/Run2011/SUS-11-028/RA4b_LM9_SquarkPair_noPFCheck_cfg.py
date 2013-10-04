#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 31 RA4b_LM9_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 10.82472
process.weightProducer.NumberEvts = 437030 	
process.weightProducer.Lumi = 1000 ## Lumi in 1/p

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM6.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM6.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM6.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"

process.goodMuons = process.vertexSelectedGoodMuons.clone()
process.analyzeRA4Muons.pfMuons = "goodMuons"

process.preselectionMuHTMC2 = process.preselectionSquarkPair
process.preselectionElHTMC2 = process.preselectionSquarkPair
process.preselectionLepHTMC2 = process.preselectionSquarkPair

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_10_2_DWR.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_11_2_bZK.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_12_2_33F.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_1_2_pMS.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_13_2_WxO.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_14_2_Vnk.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_2_UoD.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_2_MKR.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_17_2_GHI.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_18_2_x61.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_2_bKs.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_20_2_2NX.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_21_2_cRh.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_22_2_Tcn.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_2_2_KZW.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_23_2_unu.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_24_2_ihv.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_25_2_29N.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_26_2_umf.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_27_2_kIn.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_28_2_zqm.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_29_2_fEJ.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_30_2_i0C.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_31_2_0ux.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_3_2_275.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_2_yOX.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_2_nQr.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_2_qVT.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_2_wxo.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_8_2_omT.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_9_2_UPY.root',
    )
 )
