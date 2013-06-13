import FWCore.ParameterSet.Config as cms

#
# module to combine the persistent genParticles
# from the top decay and top mothers
#
SUSYGenEvt = cms.EDProducer("SUSYGenEventReco",
    Generation = cms.int32(2),            
    src  = cms.InputTag("genParticles"),
    init = cms.InputTag("SUSYInitSubset:genParticles"),
    sparticles = cms.InputTag("SUSYInitSubset")                      
)


