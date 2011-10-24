import FWCore.ParameterSet.Config as cms

filterMHT = cms.EDFilter("MHTFilter",
    ## sources
    jets = cms.InputTag("selectedPatJets"),
    ## cut on HT
    Cut   = cms.double(60.)
)


