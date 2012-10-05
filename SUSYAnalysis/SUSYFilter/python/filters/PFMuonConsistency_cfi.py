import FWCore.ParameterSet.Config as cms

pfMuonConsistency = cms.EDFilter("PFMuonConsistency",
                                 muons = cms.InputTag("cleanPatMuons"),
                                 pfCandidates = cms.InputTag("particleFlow")
                                 )


