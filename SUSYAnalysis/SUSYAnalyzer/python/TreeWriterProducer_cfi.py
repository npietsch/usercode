import FWCore.ParameterSet.Config as cms

# module to analyze selected objects
writeTrees = cms.EDProducer("TreeWriterProducer",
                            muons     = cms.InputTag("selectedPatMuons"),
                            electrons = cms.InputTag("selectedPatElectrons"),
                            jets      = cms.InputTag("selectedPatJetsAK5PF")
                            )
