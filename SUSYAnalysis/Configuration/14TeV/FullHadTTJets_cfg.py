from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 0.9664
process.weightProducer.NumberEvts = 27192
process.weightProducer.Lumi = 300000

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/FullHadTTJets_HT700_14TeV_PAT.root'
    )
)

