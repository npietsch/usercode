import FWCore.ParameterSet.Config as cms

#
# module to make simple ttbar analysis on generator level 
#
analyzeTtGenEvent = cms.EDAnalyzer("TtGenEventAnalyzer",
                                   genEvent = cms.InputTag("genEvt"),
                                   genEvtInfoHandle = cms.InputTag("generator"),
                                   genParticles = cms.InputTag("genParticles"),
                                   )
