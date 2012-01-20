import FWCore.ParameterSet.Config as cms

produceJetCollection = cms.EDProducer("JetCollectionProducer",
                                      inputJets = cms.InputTag("selectedPatJetsAK5PF")
                                      )
