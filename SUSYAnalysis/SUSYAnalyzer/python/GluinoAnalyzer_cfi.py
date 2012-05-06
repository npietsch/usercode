import FWCore.ParameterSet.Config as cms

#
# module to study systematics
#
analyzeGluino = cms.EDAnalyzer("GluinoAnalyzer",
                               ## collections of RA4b objects
                               jets = cms.InputTag("selectedPatJetsAK5PF"),
                               bjets = cms.InputTag("mediumTrackHighEffBjets"),
                               muons = cms.InputTag("goodMuons"),
                               electrons = cms.InputTag("goodElectrons"),
                               met = cms.InputTag("patMETsPF"),
                               ## SUSGenEvent
                               susyGenEvent = cms.InputTag("SUSYGenEvt"),
                               ## for event weighting
                               PVSrc = cms.InputTag("offlinePrimaryVertices"),
                               PUInfo = cms.InputTag("addPileupInfo"),
                               PUWeight = cms.InputTag("eventWeightPU:eventWeightPU"),
                               RA2Weight = cms.InputTag("weightProducer:weight"),
                               useEventWeight = cms.bool(False)
                               )

