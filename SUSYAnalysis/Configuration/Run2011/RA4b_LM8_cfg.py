#-------------------------------------------
# To run on the NAF, type:
#
# xport NJS_QUEUE=1 
# nafJobSplitter.pl 3 RA4b_LM8_cfg.py
#-------------------------------------------

from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC2
process.preselection2 = preselectionElHTMC2

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_3_1_mpc.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_2_1_w8m.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_1_1_sKN.root'
    )
)
