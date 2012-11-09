#-------------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 32 RA4b_LM8_noPFCheck_cfg.py
#-------------------------------------------------

from TTJets_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM8.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM8.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM8.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"

process.goodMuons = process.vertexSelectedGoodMuons.clone()

process.preselectionMuHTMC2  = process.preselectionSquarkPair
process.preselectionElHTMC2  = process.preselectionSquarkPair
process.preselectionLepHTMC2 = process.preselectionSquarkPair

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_10_1_TPM.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_11_2_PFG.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_1_1_KVF.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_12_1_IgG.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_13_1_ayU.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_14_2_oLM.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_1_TVD.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_1_lGz.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_17_1_ADq.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_18_1_JVs.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_1_z6P.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_20_1_abo.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_21_2_ptK.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_2_1_anT.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_22_1_Ccg.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_23_1_GRT.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_24_1_OaD.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_25_1_02d.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_26_2_omR.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_27_2_ujG.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_28_1_Mpm.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_29_2_KVw.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_30_1_Fao.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_31_1_kZI.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_3_1_zuF.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_32_1_Mz8.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_2_e3a.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_2_aeX.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_2_XCp.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_1_qAr.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_8_2_4TB.root',
    '/store/user/fcostanz/LM8_SUSY_sftsht_7TeV-pythia6/LM8_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_9_1_Wyl.root'
    )
)
