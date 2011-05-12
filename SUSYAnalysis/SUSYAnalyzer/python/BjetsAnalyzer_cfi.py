import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeBjets = cms.EDAnalyzer("BjetsAnalyzer",
                              met = cms.InputTag("patMETs"),
                              source = cms.InputTag("genParticles"),
                              jets = cms.InputTag("goodJets"),
                              muons = cms.InputTag("goodMuons"),
                              electrons = cms.InputTag("goodElectrons"),
                              looseTrackHighEffBjets = cms.InputTag("selectedPatJets"),
                              mediumTrackHighEffBjets = cms.InputTag("selectedPatJets"),
                              tightTrackHighEffBjets = cms.InputTag("selectedPatJets"),
                              looseTrackHighPurBjets = cms.InputTag("selectedPatJets"),
                              mediumTrackHighPurBjets = cms.InputTag("selectedPatJets"),
                              tightTrackHighPurBjets = cms.InputTag("selectedPatJets"),
                              pvSrc = cms.InputTag("offlinePrimaryVertices")
                             )


