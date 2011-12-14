import FWCore.ParameterSet.Config as cms

TriggerWeightProducer = cms.EDProducer('TriggerWeightProducer',
                                       inputMETs             = cms.InputTag("patMETsPF"),
                                       MuonTriggerWeight     = cms.bool(False),
                                       ElectronTriggerWeight = cms.bool(False)                    
)


