import FWCore.ParameterSet.Config as cms

produceTtGenEventJets = cms.EDProducer("JetCollectionProducer",
                                       genEvent = cms.InputTag("genEvt"),
                                       inputJets = cms.InputTag("selectedPatJetsAK5PF")
                                       )
