import FWCore.ParameterSet.Config as cms

PFConsistentMuons = cms.EDProducer("PFConsistentMuonProducer",
                                   muons   = cms.InputTag("selectedPatMuons"),
                                   pfMuons = cms.InputTag("selectedPatMuonsPF")
                                   )
x
