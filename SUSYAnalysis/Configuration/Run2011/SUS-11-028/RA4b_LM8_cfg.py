#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 3 RA4b_LM8_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.eventWeightPU.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM8.root"
process.eventWeightPU.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUUp.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM8.root"
process.eventWeightPUUp.MCSampleHistoName   = cms.string("pileup")

process.eventWeightPUDown.MCSampleFile = "SUSYAnalysis/SUSYUtils/data/PU_LM8.root"
process.eventWeightPUDown.MCSampleHistoName   = cms.string("pileup")

#process.btagEventWeightMuJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/LM8.root"
#process.btagEventWeightElJER.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/LM8.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_mpc.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_w8m.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_sKN.root'
    )
)