import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSY = cms.EDAnalyzer("SUSYAnalyzer",
                             met = cms.InputTag("patMETs"),
                             source = cms.InputTag("genParticles"),
                             jets = cms.InputTag("selectedPatJets"),
                             muons = cms.InputTag("selectedPatMuons"),
                             electrons = cms.InputTag("selectedPatMuons")
                             )


