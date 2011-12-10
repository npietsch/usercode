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

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#-----------------------------------------------------------------
# Load modules to monitor selection steps
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.RA4Analyzer_cfi")
process.analyzeRA4.jets = "goodJets"
process.analyzeRA4.muons = "goodMuons"
process.analyzeRA4.electrons ="goodElectrons"

process.RA4Preselection = process.analyzeRA4.clone()
process.RA4OneGoodJet = process.analyzeRA4.clone()
process.RA4TwoGoodJets = process.analyzeRA4.clone()
process.RA4ThreeGoodJets = process.analyzeRA4.clone()
process.RA4FourGoodJets = process.analyzeRA4.clone()

process.load("SUSYAnalysis.SUSYAnalyzer.Out_cfi")
process.Out.jets = "goodJets"
process.Out.muons = "goodMuons"
process.Out.electrons ="goodElectrons"

#------------------
# Selection paths
#------------------

process.MuonSelection = cms.Path(process.preselectionMuHTAllData *
                                 process.goodObjects *
                                 process.RA4Preselection *
                                 process.oneGoodJet *
                                 process.RA4OneGoodJet *
                                 process.twoGoodJets *
                                 process.RA4TwoGoodJets *
                                 process.threeGoodJets *
                                 process.RA4ThreeGoodJets *
                                 process.fourGoodJets *
                                 process.RA4FourGoodJets *
                                 process.muonSelection *
                                 process.HTSelection *
                                 process.oneMediumMET *
                                 process.Out
                                 )
