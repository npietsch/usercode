from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 3.1955 # 3.198 3.193
process.weightProducer.NumberEvts = 179992 # 89996 89996
process.weightProducer.Lumi = 300000

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../BackgroundSamples/FullHadTTJetsNew_HT700_14TeV_PAT_1.root',
    'file:../../../../../../BackgroundSamples/FullHadTTJetsNew_HT700_14TeV_PAT_2.root'
    )
)

