from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.217
process.weightProducer.NumberEvts = 26898
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/ '
    )
)
