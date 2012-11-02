from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 1.21 # 1.22 1.20 1.22
process.weightProducer.NumberEvts = 80498 # 26898 26600 27000
process.weightProducer.Lumi = 300000  ##  Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../BackgroundSamples/WJets_HT700_MET100_14TeV_lvjjj_mu_PAT_1.root',
    'file:../../../../../../BackgroundSamples/WJets_HT700_MET100_14TeV_lvjjj_mu_PAT_2.root',
    'file:../../../../../../BackgroundSamples/WJets_HT700_MET100_14TeV_lvjjj_mu_PAT_3.root'
    )
)
