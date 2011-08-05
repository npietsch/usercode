import FWCore.ParameterSet.Config as cms

#
# module to make simple event topology analyses
#
analyzeEventTopology = cms.EDAnalyzer("EventTopology",
                                      met = cms.InputTag("patMETsPF"),
                                      jets = cms.InputTag("selectedPatJetsAK5PF"),
                                      mediumJets = cms.InputTag("mediumJets"),
                                      bjets = cms.InputTag("selectedPatJetsAK5PF"),
                                      muons = cms.InputTag("selectedPatMuons"),
                                      electrons = cms.InputTag("selectedPatElectrons"),
                                      pvSrc = cms.InputTag("offlinePrimaryVertices"),
                                      weight = cms.InputTag("eventWeightPU:eventWeightPU"),
                                      RA2weight = cms.InputTag("weightProducer:weight"),
                                      useEventWeight = cms.bool(False)
                                      )
