import FWCore.ParameterSet.Config as cms

SUSYEvt = cms.EDProducer("SUSYEventProducer",
                         test = cms.int32(2),
                         muons = cms.InputTag("selectedPatMuons"),
                         electrons = cms.InputTag("selectedPatElectrons"),
                         jets = cms.InputTag("selectedPatJetsAK5PF"),
                         mets = cms.InputTag("patMETsPF")
                         )
