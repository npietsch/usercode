import FWCore.ParameterSet.Config as cms

filterHT = cms.EDFilter("HTFilter",
    ## sources
    jets = cms.InputTag("selectedPatJets"),
    ## cut on HT
    Cut   = cms.double(300.),
)

