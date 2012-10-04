import FWCore.ParameterSet.Config as cms

vertexSelectedElectrons = cms.EDProducer("VertexSelectedElectronProducer",
                                         src           = cms.InputTag("cleanPatElectrons"),
                                         primaryVertex = cms.InputTag("offlinePrimaryVertices"),
                                         dxyCut        = cms.bool(False),
                                         dzCut         = cms.bool(False),                                   
                                         dxyCutValue   = cms.double(0.04),
                                         dzCutValue    = cms.double(0.2)                                 
                                         )
