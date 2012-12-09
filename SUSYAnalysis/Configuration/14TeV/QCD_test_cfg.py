from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 146200000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    #'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3127.root',
    'file:/scratch/hh/lustre/cms/user/npietsch/QCD/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV/naf_QCD_3127/QCD_Pythia_14TeV.root'
    )
)
