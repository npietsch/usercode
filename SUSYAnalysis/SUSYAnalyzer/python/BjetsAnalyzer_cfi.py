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
                              bjets = cms.InputTag("selectedPatJets"),
                             )


