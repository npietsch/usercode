from Ruediger_cfg import *

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 0.054
process.weightProducer.NumberEvts = 100000
process.weightProducer.Lumi = 300000

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../SignalSamples/MSSM_14TeV_herwigpp_cff_py_GEN_FASTSIM_HLT_PointD1_PAT_1.root',
    'file:../../../../../../SignalSamples/MSSM_14TeV_herwigpp_cff_py_GEN_FASTSIM_HLT_PointD1_PAT_2.root'
    )
)

