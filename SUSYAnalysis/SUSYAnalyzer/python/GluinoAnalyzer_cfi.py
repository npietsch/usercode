import FWCore.ParameterSet.Config as cms

#
# module to study systematics
#
analyzeGluino = cms.EDAnalyzer("GluinoAnalyzer",
                               jets = cms.InputTag("selectedPatJetsAK5PF"),
                               looseJets = cms.InputTag("looseJets"),
                               bjets = cms.InputTag("mediumTrackHighEffBjets"),
                               muons = cms.InputTag("goodMuons"),
                               electrons = cms.InputTag("goodElectrons"),
                               met = cms.InputTag("patMETsPF"),
                               susyGenEvent = cms.InputTag("SUSYGenEvt"),
                               PVSrc = cms.InputTag("offlinePrimaryVertices"),
                               PUInfo = cms.InputTag("addPileupInfo")
                               )

