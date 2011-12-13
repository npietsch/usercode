import FWCore.ParameterSet.Config as cms

TriggerWeightProducer = cms.EDProducer('TriggerWeightProducer',
    inputMETs            = cms.InputTag("patMETsPF"),
    sig                  = cms.double(1.0),
    eps                  = cms.double(1.0),
    triggerWeight        = cms.bool(False),
    threshold            = cms.double(40.)                      
)


