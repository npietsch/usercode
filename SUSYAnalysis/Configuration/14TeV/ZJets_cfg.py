from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 0.5246 # 0.5231 0.5255 0.5252
process.weightProducer.NumberEvts = 71779 # 23863 23968 23948
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode=cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../BackgroundSamples/Zvv_HT700_MET100_14TeV_vvjjj_PAT_1.root',
    'file:../../../../../../BackgroundSamples/Zvv_HT700_MET100_14TeV_vvjjj_PAT_2.root',
    'file:../../../../../../BackgroundSamples/Zvv_HT700_MET100_14TeV_vvjjj_PAT_3.root'
    )
)
