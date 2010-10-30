import FWCore.ParameterSet.Config as cms

#
# module to filter events based on member functions of the SUSYGenEvent
#
SUSYGenEventFilter = cms.EDFilter("SUSYGenEvtFilter",
    src = cms.InputTag("SUSYGenEvt"),
    cut = cms.string("")
)
