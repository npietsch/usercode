import FWCore.ParameterSet.Config as cms

scaledLeptonEnergy = cms.EDProducer("LeptonEnergy",
    inputMuons              = cms.InputTag("selectedPatMuons"),
    inputElectrons          = cms.InputTag("selectedPatElectrons"),
    inputMETs               = cms.InputTag("patMETsPF"),
    scaleFactorMu           = cms.double(1.0),
    scaleFactorEl           = cms.double(1.0),
    leptonPTThresholdForMET = cms.double(20.)                                
)
