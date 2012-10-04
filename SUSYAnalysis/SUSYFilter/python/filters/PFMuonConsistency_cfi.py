import FWCore.ParameterSet.Config as cms

pfMuonConsistency = cms.EDFilter("PFMuonConsistency",
                                 muons = cms.InputTag("cleanPatMuons"),
                                 pfMuons = cms.InputTag("patAllMuonsPF")
                                 )


