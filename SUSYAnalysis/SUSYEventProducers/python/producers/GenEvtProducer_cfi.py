import FWCore.ParameterSet.Config as cms

#
# module to combine the persistent genParticles
# from the top decay and top mothers
#
GenEvt = cms.EDProducer("GenEventReco",            
    genParticles     = cms.InputTag("genParticles"),
    initialParticles = cms.InputTag("SUSYInitSubset:genParticles")
)
