import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSY = cms.EDAnalyzer("SUSYAnalyzer",
                             met = cms.InputTag("patMETs"),
                             jets = cms.InputTag("selectedPatJets"),
                             muons = cms.InputTag("selectedPatMuons"),
                             electrons = cms.InputTag("selectedPatElectrons"),
                             pvSrc = cms.InputTag("offlinePrimaryVertices")
                             )
