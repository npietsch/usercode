from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHT

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'file:PAT.root'
    '/store/user/npietsch/Spring10/DYJetsToLLD6TM50/Spring11MC_17_1_Gbj.root'
    )
)
