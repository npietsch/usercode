#-------------------------------------------------
# To run on the NAF, type:
# altan
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 32 RA4b_LM13_noPFCheck_cfg.py
#-------------------------------------------------

from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM13.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM13.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM13.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"
process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"

process.muonSelection = cms.Sequence(process.oneGoodMuon *
                                     process.exactlyOneGoodMuon *
                                     ##process.pfMuonConsistency *
                                     process.noGoodElectron *
                                     process.exactlyOneVetoMuon *
                                     process.noVetoElectron
                                     )

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_10_2_fsC.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_11_1_EV5.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_1_1_aih.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_12_1_HZg.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_13_2_sU4.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_14_1_eyI.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_1_9Qj.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_1_CCX.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_17_2_RhV.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_18_1_plL.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_1_5WU.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_20_2_jzB.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_21_1_WmO.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_22_1_xWT.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_2_2_k1C.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_23_2_IOk.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_24_2_5Fq.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_25_2_j27.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_26_1_Ro4.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_27_2_vqi.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_28_2_FDh.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_29_1_WR0.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_30_1_Bmo.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_31_2_kcr.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_3_1_eOl.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_32_2_AjO.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_1_3GT.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_2_3jm.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_1_8uC.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_2_Xat.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_8_1_A5V.root',
    '/store/user/fcostanz/LM13_SUSY_sftsht_7TeV-pythia6/LM13_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_9_2_xfv.root'
    )
)
