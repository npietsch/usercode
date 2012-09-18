import FWCore.ParameterSet.Config as cms

trackingFailure = cms.EDFilter(
  "TrackingFailure",
  JetSource = cms.InputTag('selectedPatJetsAK5PF'),
  TrackSource = cms.InputTag('generalTracks'),
  VertexSource = cms.InputTag('goodVertices'),
  DzTrVtxMax = cms.double(1),
  DxyTrVtxMax = cms.double(0.2),
  MinSumPtOverHT = cms.double(0.10)
)
