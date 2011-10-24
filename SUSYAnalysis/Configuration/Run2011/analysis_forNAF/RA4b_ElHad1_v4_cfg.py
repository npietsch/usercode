from BjetsData_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import * 
process.preselectionMuHTData = preselectionMuHTData2 
process.preselectionElHTData = preselectionElHTData2


# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(



)
)
