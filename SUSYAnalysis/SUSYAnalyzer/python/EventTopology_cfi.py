import FWCore.ParameterSet.Config as cms

#
# module to make simple event topology analyses
#
analyzeEventTopology = cms.EDAnalyzer("EventTopology",
                                      met = cms.InputTag("patMETs"),
                                      jets = cms.InputTag("selectedPatJets"),
                                      bjets = cms.InputTag("selectedPatJets"),
                                      muons = cms.InputTag("selectedPatMuons"),
                                      electrons = cms.InputTag("selectedPatElectrons"),
                                      pvSrc = cms.InputTag("offlinePrimaryVertices")
                                      )
