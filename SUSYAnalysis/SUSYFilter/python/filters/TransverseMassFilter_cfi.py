import FWCore.ParameterSet.Config as cms

filterTransverseMass = cms.EDFilter("TransverseMassFilter",
                                    ## sources
                                    met = cms.InputTag("patMETsPF"),                    
                                    muons = cms.InputTag("selectedPatMuons"),
                                    electrons = cms.InputTag("selectedPatElectrons"),                   
                                    ## cut on HT
                                    Cut   = cms.vdouble(50.,100.)
                                    )


