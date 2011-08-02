import FWCore.ParameterSet.Config as cms

pfMuonConsistency = cms.EDFilter("PFMuonConsistency",
                                 muons = cms.InputTag("selectedPatMuons"),
                                 pfMuons = cms.InputTag("selectedPatMuonsPF")
                                 )


