import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSY = cms.EDAnalyzer("SUSYAnalyzer",
                             met = cms.InputTag("patMETs"),
                             source = cms.InputTag("genParticles"),
                             jets = cms.InputTag("selectedPatJets")
                             )


