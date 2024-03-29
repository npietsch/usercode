import FWCore.ParameterSet.Config as cms

scaledJetEnergy = cms.EDProducer("JetEnergy",
                                 inputJets            = cms.InputTag("selectedPatJetsAK5PF"),
                                 inputMETs            = cms.InputTag("patMETsPF"),
                                 scaleFactor          = cms.double(1.0),
                                 scaleFactorB         = cms.double(1.0),
                                 scaleType            = cms.string("abs"), #abs or rel(*eta) or jes:up / jes:down (pt-dependend)
                                 payload              = cms.string("AK5PF"), #jet and constituent type in JetMET convention
                                 jetPTThresholdForMET = cms.double(10.),
                                 maxJetEtaForMET      = cms.double(4.7),                           
                                 jetEMLimitForMET     = cms.double(0.9),                                 
                                 resolutionFactors    = cms.vdouble(1.1, 1.1, 1.1), # list the different JER factors here: (JER1, JER2)
                                 resolutionEtaRanges  = cms.vdouble(0, 1.5, 1.5, 2.0, 2.0, -1),  # list the |eta| ranges for the different JER factors here (etaMin1, etaMax1, etaMin2, etaMax2), etaMax=-1: means |eta|<infinity
                                 doJetSmearing        = cms.bool(True),
                                 JetCorrectionService = cms.string("L2L3ResidualMC"),
                                 L2L3Residual         = cms.bool(True)
                                 )
