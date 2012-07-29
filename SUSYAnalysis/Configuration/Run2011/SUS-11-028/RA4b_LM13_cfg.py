#-------------------------------------------
# To run on the NAF, type:
# altan
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 16 RA4b_LM13_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM13.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM13.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM13.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

#process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/LM13.root"
#process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/LM13.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_9_1_vsG.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_NQC.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_7_1_dpG.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_6_1_kHi.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_5_1_982.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_4_1_elw.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_jJX.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_rLP.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_AMd.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_16_1_1v0.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_15_1_TY5.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_14_1_Bh6.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_13_1_yXC.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_12_1_HhJ.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_11_1_ldo.root',
    '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_10_1_Uji.root'
    )
)
