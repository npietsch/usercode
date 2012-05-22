from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.212 # 1.217 1.211 1.210
process.weightProducer.NumberEvts = 80270 # 26898 26695 26677
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/WJets_HT700_MET100_14TeV_lvjjj_PAT.root',
    'file:../../../../../../Storage/WJets_HT700_MET100_14TeV_lvjjj_PAT_2.root',
    'file:../../../../../../Storage/WJets_HT700_MET100_14TeV_lvjjj_PAT_3.root'
    )
)
