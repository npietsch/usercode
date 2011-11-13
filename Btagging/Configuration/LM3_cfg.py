#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 8 RA4b_LM3_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 3.438
process.weightProducer.NumberEvts = 36475
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_1fH.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_7_1_ZI8.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_6_1_flK.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_5_1_T0Q.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_4_1_Zqi.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_qPF.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_Gan.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_CIB.root'
    )
)
