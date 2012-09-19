import FWCore.ParameterSet.Config as cms

produceRA4Electrons = cms.EDProducer("RA4ElectronProducer",
                                     inputElectrons = cms.InputTag("selectedPatElectrons")
                                     )
