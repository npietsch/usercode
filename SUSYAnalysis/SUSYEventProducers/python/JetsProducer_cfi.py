import FWCore.ParameterSet.Config as cms

produceJets = cms.EDProducer("JetsProducer",
                             inputJets = cms.InputTag("selectedPatJetsAK5PF'")
                             )
