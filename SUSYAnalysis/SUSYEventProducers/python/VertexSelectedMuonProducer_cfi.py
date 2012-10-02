import FWCore.ParameterSet.Config as cms

vertexSelectedMuons = cms.EDProducer("MuonVertexDistanceSelector",
  src           = cms.InputTag("selectedPatMuons"),
  primaryVertex = cms.InputTag("offlinePrimaryVertices"),
  cutValue      = cms.double(1.),

  dxy_cut       = cms.bool(False),
  dxy           = cms.double(0.02)                                   
)
