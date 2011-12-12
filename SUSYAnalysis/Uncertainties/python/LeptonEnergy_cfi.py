import FWCore.ParameterSet.Config as cms

scaledJetEnergy = cms.EDProducer("JetEnergy",
    inputMuons              = cms.InputTag("selectedPatMuons'"),
    inputElectrons          = cms.InputTag("selectedPatElectrons"),                   
    inputMETs               = cms.InputTag("patMETsPF"),
    scaleType               = cms.string("abs"),                        
    scaleFactor             = cms.double(1.0),
    leptonPTThresholdForMET = cms.double(20.)                                
)
