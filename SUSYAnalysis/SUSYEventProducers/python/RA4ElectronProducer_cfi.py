import FWCore.ParameterSet.Config as cms

produceRA4Electrons = cms.EDProducer("RA4ElectronProducer",
                                     inputElectrons        = cms.InputTag("cleanPatElectrons"),
                                     conversionsInputTag   = cms.InputTag("allConversions"),
                                     beamSpotInputTag      = cms.InputTag("offlineBeamSpot"),
                                     rhoIsoInputTag        = cms.InputTag("kt6PFJetsForIsolation2011", "rho"),
                                     primaryVertexInputTag = cms.InputTag("offlinePrimaryVertices")
                                     )
