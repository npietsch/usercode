import FWCore.ParameterSet.Config as cms

selectedGenParticles = cms.EDFilter("PATgenParticlesSelector",
    src = cms.InputTag("genParticles"),
    cut = cms.string("")
)
