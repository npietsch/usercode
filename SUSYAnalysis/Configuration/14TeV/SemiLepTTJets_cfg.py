from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 0.1185 # 0.1181 0.1188
process.weightProducer.NumberEvts = 48903 # 24356 24547
process.weightProducer.Lumi = 300000 ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/SemiLepTTJets_HT700_MET100_14TeV_PAT.root',
    'file:../../../../../../Storage/SemiLepTTJets_HT700_MET100_14TeV_PAT_2.root'
    )
)

