import FWCore.ParameterSet.Config as cms

countGenParticles = cms.EDFilter("PATCandViewCountFilter",
    minNumber = cms.uint32(0),
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("")
)
