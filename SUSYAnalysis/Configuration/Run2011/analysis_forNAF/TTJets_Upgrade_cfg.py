from Upgrade_MC_cfg import *

process.GlobalTag.globaltag = cms.string('START42_V13::All')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('TTJets_Upgrade.root')
                                   )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( "file:/afs/naf.desy.de/user/c/costanza/workdir/Synchro/PATupler/CMSSW_4_2_8_patch7/src/SUSYAnalysis/Configuration/Run2011/PATupleTTJets.root")
                            )

