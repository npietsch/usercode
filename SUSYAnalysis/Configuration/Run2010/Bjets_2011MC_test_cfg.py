from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHT

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:Spring11.root'
    )
)
