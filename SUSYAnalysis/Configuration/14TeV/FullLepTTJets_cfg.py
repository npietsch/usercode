from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 7106
process.weightProducer.NumberEvts = 25000
process.weightProducer.Lumi = 300  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/ '
    )
)
