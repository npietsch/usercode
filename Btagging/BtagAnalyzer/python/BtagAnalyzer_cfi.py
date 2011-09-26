import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeBtags = cms.EDAnalyzer("BtagAnalyzer",
                              met = cms.InputTag("patMETsPF"),
                              jets = cms.InputTag("selectedPatJetsAK5PF"),
                              bjets = cms.InputTag("mediumTrackHighEffBjets"),
                              matchedLightJets = cms.InputTag("matchedLightJets"),
                              matchedBJets = cms.InputTag("matchedBJets"),
                              muons = cms.InputTag("selectedPatMuons"),
                              electrons = cms.InputTag("selectedPatElectrons"),
                              pvSrc = cms.InputTag("offlinePrimaryVertices"),
                              weight = cms.InputTag("eventWeightPU:eventWeightPU"),
                              PUInfo = cms.InputTag("addPileupInfo"),
                              RA2weight = cms.InputTag("weightProducer:weight"),
                              useEventWeight = cms.bool(False)
                              )
                
