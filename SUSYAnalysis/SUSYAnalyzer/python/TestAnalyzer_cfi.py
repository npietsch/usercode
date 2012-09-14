import FWCore.ParameterSet.Config as cms

# module to analyze selected objects
testAnalysis = cms.EDAnalyzer("TestAnalyzer",
                              muons     = cms.InputTag("selectedPatMuons"),
                              electrons = cms.InputTag("selectedPatElectrons"),
                              jets      = cms.InputTag("selectedPatJetsAK5PF")
                              )
