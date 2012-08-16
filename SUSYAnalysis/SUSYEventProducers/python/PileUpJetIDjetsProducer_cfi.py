import FWCore.ParameterSet.Config as cms

PileUpJetID = cms.EDProducer("PileUpJetIDjetsProducer",
                             inputJets       = cms.InputTag("selectedPatJetsAK5PF"),
                             inputMETs       = cms.InputTag("patMETsPF"),
                             discriminator   = cms.InputTag("puJetMvaAK5PF:fullDiscriminant"),
                             flag            = cms.InputTag("puJetMvaAK5PF:fullId"),
                             wp              = cms.InputTag("Tight")
                             )

