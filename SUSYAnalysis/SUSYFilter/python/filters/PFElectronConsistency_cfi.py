import FWCore.ParameterSet.Config as cms

pfElectronConsistency = cms.EDFilter("PFElectronConsistency",
                                 electrons = cms.InputTag("cleanPatElectrons"),
                                 pfCandidates = cms.InputTag("particleFlow")
                                 )


