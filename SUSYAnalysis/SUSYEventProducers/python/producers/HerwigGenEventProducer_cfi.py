import FWCore.ParameterSet.Config as cms


HerwigGenEvent = cms.EDProducer("HerwigGenEventProducer",          
                                src  = cms.InputTag("genParticles")                    
)


