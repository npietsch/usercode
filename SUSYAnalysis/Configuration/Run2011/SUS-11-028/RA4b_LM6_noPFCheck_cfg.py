#-------------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 27 RA4b_LM6_noPFCheck_cfg.py
#-------------------------------------------------

from BjetsPAT_cfg import *

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

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_10_1_mdH.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_11_2_laJ.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_12_2_sGz.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_1_2_sP3.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_13_2_J7B.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_14_2_jtx.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_1_v3D.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_2_Aeq.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_17_2_d4H.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_18_2_9mA.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_3_Yd1.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_20_1_tjT.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_21_2_5TC.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_22_2_gCT.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_2_2_Oyg.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_23_2_DJr.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_24_1_iiS.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_25_2_Eys.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_26_1_FZa.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_27_1_ptf.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_3_1_vTI.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_2_nxZ.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_2_tjn.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_1_idr.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_2_SAx.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_8_1_5Dw.root',
    '/store/user/fcostanz/LM6_SUSY_sftsht_7TeV-pythia6/LM6_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_9_2_4rf.root'
    )
)
