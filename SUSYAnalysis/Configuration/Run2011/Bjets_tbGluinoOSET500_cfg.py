from BjetsAOD_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_tbgluino0j500.1.lhe_7TeV_GEN_FASTSIM.root'
    )
)
