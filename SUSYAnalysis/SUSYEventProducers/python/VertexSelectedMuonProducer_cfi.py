import FWCore.ParameterSet.Config as cms

vertexSelectedMuons = cms.EDProducer("VertexSelectedMuonProducer",
                                     src           = cms.InputTag("cleanPatMuons"),
                                     primaryVertex = cms.InputTag("offlinePrimaryVertices"),
                                     dxyCut        = cms.bool(True),
                                     dzCut         = cms.bool(True),                                   
                                     dxyCutValue   = cms.double(0.2),
                                     dzCutValue    = cms.double(0.5)                                 
                                     )
