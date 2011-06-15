import FWCore.ParameterSet.Config as cms

process = cms.Process("Test") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('Start42_V12::All')

# Choose input file
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:Summer11.root'
    )
)

# Load modules to create SUSY Gen Event
process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

# Load modules for analysis on generator and reco-level
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis2_cff")

# Test selection
process.Test = cms.Path(process.makeObjects *
                        process.makeSUSYGenEvt *
                        process.leptonSelection*
                        process.analyzeSUSYBjets1l_leptonSelection *
                        process.jetSelection*
                        process.analyzeSUSYBjets1l_jetSelection *
                        process.HTSelection *
                        process.analyzeSUSYBjets1l_HTSelection *
                        process.metSelection *
                        process.analyzeSUSYBjets1l_metSelection
                        )
