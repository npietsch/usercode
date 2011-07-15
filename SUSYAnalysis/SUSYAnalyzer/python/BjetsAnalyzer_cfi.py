import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeBjets = cms.EDAnalyzer("BjetsAnalyzer",
                              met = cms.InputTag("patMETsPF"),
                              source = cms.InputTag("genParticles"),
                              jets = cms.InputTag("goodJets"),
                              muons = cms.InputTag("goodMuons"),
                              electrons = cms.InputTag("goodElectrons"),
                              looseTrackHighEffBjets = cms.InputTag("selectedPatJetsAK5PF"),
                              mediumTrackHighEffBjets = cms.InputTag("selectedPatJetsAK5PF"),
                              tightTrackHighEffBjets = cms.InputTag("selectedPatJetsAK5PF"),
                              looseTrackHighPurBjets = cms.InputTag("selectedPatJetsAK5PF"),
                              mediumTrackHighPurBjets = cms.InputTag("selectedPatJetsAK5PF"),
                              tightTrackHighPurBjets = cms.InputTag("selectedPatJetsAK5PF"),
                              pvSrc = cms.InputTag("offlinePrimaryVertices"),
                              weight = cms.InputTag("eventWeightPU:eventWeightPU"),
                              useEventWeight = cms.bool(True)
                             )


