import FWCore.ParameterSet.Config as cms

filterDeltaPhi = cms.EDFilter("DeltaPhiFilter",
                              ## sources
                              jets = cms.InputTag("selectedPatJetsAK5PF"),
                              mets = cms.InputTag("patMETsPF"),
                              Jet  = cms.int32(0),
                              Cut  = cms.double(0.5)
                              )


