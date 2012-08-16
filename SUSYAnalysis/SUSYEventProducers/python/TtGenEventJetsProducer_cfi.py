import FWCore.ParameterSet.Config as cms

produceTtGenEventJets = cms.EDProducer("TtGenEventJetsProducer",
                                       genEvent = cms.InputTag("genEvt"),
                                       inputRecoJets = cms.InputTag("selectedPatJetsAK5PF"),
                                       inputGenJets = cms.InputTag("selectedPatJetsAK5PF:genJets"),
                                       )
