import FWCore.ParameterSet.Config as cms

filterYmet = cms.EDFilter("YmetFilter",
                          ## sources
                          jets = cms.InputTag("selectedPatJetsAK5PF"),
                          mets = cms.InputTag("patMETsPF"),
                          ## cut on Ymet
                          Cut   = cms.double(0.),
                          )


