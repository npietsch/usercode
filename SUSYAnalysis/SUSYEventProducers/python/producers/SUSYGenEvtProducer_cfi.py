import FWCore.ParameterSet.Config as cms

#
# module to combine the persistent genParticles
# from the top decay and top mothers
#
SUSYGenEvt = cms.EDProducer("SUSYGenEventReco",
    src  = cms.InputTag("genParticles"),
    init = cms.InputTag("SUSYInitSubset")
)


