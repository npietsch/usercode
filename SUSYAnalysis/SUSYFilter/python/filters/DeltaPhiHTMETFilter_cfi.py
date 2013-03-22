import FWCore.ParameterSet.Config as cms

filterDeltaPhiHTMET = cms.EDFilter("DeltaPhiHTMETFilter",
                                   ## sources
                                   jets = cms.InputTag("selectedPatJetsAK5PF"),
                                   mets = cms.InputTag("patMETsPF"),
                                   Cut  = cms.vdouble(0,0.5)
                                   )
