import FWCore.ParameterSet.Config as cms

SUSYInitSubset = cms.EDProducer("SUSYInitSubset",
    src = cms.InputTag("genParticles")
)


