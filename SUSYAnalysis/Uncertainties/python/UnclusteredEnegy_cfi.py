import FWCore.ParameterSet.Config as cms

scaledMET = cms.EDProducer("UnclusteredMETScale",
    inputJets            = cms.InputTag("selectedpatJetsAK5PF"),
    inputMETs            = cms.InputTag("patMETsPF"),
    scaleFactor          = cms.double(1.0)
)
