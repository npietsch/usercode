import FWCore.ParameterSet.Config as cms

unclusteredEnergy = cms.EDProducer("UnclusteredEnergy",
    inputJets            = cms.InputTag("selectedPatJetsAK5PF"),
    inputMETs            = cms.InputTag("patMETsPF"),
    jetPTThresholdForMET = cms.double(10.),
    maxJetEtaForMET      = cms.double(4.7),                       
    scaleFactor          = cms.double(1.0)
)
