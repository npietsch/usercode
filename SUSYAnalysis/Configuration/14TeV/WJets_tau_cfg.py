from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS =  1.212 # 1.212 1.224 1.220
process.weightProducer.NumberEvts = 80807 # 26783 27038 26986
process.weightProducer.Lumi = 300000  ##  Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../BackgroundSamples/WJets_HT700_MET100_14TeV_lvjjj_tau_PAT_1.root',
    'file:../../../../../../BackgroundSamples/WJets_HT700_MET100_14TeV_lvjjj_tau_PAT_2.root',
    'file:../../../../../../BackgroundSamples/WJets_HT700_MET100_14TeV_lvjjj_tau_PAT_3.root'
    )
)
