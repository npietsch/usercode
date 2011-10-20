import FWCore.ParameterSet.Config as cms

filterMHT = cms.EDFilter("MHTFilter",
    ## sources
    jets = cms.InputTag("selectedPatJets"),
    ## cut on MHT
    Cut   = cms.double(300.),
)


