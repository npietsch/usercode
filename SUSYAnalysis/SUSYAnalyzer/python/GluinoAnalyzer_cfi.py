import FWCore.ParameterSet.Config as cms

#
# module to study systematics
#
analyzeGluino = cms.EDAnalyzer("GluinoAnalyzer",
                               jets = cms.InputTag("patMETsPF"),
                               looseJets = cms.InputTag("looseJets"),
                               bjets = cms.InputTag("mediumTrackHighEffBjets"),
                               muons = cms.InputTag("goodMuons"),
                               electrons = cms.InputTag("goodElectrons"),
                               vetoMuons = cms.InputTag("vetoMuons"),
                               vetoElectrons = cms.InputTag("vetoElectrons"),
                               met = cms.InputTag("patMETsPF"),
                               susyGenEvent = cms.InputTag("SUSYGenEvt"),
                               PVSrc = cms.InputTag("offlinePrimaryVertices"),
                               PUInfo = cms.InputTag("addPileupInfo"),
                               RA2Weight = cms.InputTag("weightProducer:weight")
                               )

