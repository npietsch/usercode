from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 0.4363
process.weightProducer.NumberEvts = 89997
process.weightProducer.Lumi = 300000 ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../BackgroundSamples/SemiLepTTJetsNew_HT700_MET100_14TeV_PAT_1.root'
    )
)

