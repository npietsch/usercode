import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
Out = cms.EDAnalyzer("Out",
                     met = cms.InputTag("patMETsPF"),
                     jets = cms.InputTag("selectedPatJetsAK5PF"),
                     muons = cms.InputTag("selectedPatMuons"),
                     electrons = cms.InputTag("selectedPatElectrons")
                     )

