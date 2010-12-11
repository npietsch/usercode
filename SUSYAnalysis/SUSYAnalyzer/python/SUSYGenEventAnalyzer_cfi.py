import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSYGenEvt = cms.EDAnalyzer("SUSYGenEventAnalyzer",
                                   susyGenEvent = cms.InputTag("SUSYGenEvent")
                                   )


