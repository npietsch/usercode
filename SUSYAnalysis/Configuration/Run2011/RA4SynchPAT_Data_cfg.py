import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000),
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
process.GlobalTag.globaltag = cms.string('GR_R_42_V19::All')

## load modules for preselection
process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

## load modules to create objects and filter events on reco level
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#------------------
# Selection paths
#------------------

process.MuonSelection = cms.Path(process.preselectionMuSynchData *
                                 process.goodObjects *
                                 process.oneGoodJet *
                                 process.twoGoodJets *
                                 process.threeGoodJets *
                                 process.fourGoodJets *
                                 process.muonSelection *
                                 process.HTSelection *
                                 process.oneMediumMET *
                                 )

process.ElectronSelection = cms.Path(process.preselectionElSynchData *
                                     process.goodObjects *
                                     process.oneGoodJet *
                                     process.twoGoodJets *
                                     process.threeGoodJets *
                                     process.fourGoodJets *
                                     process.electronSelection *
                                     process.HTSelection *
                                     process.oneMediumMET *
                                     )

