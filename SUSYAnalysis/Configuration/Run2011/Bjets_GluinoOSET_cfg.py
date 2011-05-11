from BjetsAOD_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j400.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j450.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j500.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j550.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j600.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j650.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j700.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j750.1.lhe_7TeV_GEN_FASTSIM.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/job1_gluino0j800.1.lhe_7TeV_GEN_FASTSIM.root'
    )
)
