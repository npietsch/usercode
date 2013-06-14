import FWCore.ParameterSet.Config as cms

#
# module to filter events based on member functions of the HerwigGenEvent
#
HerwigGenEventFilter = cms.EDFilter("HerwigGenEventFilter",
                                    src = cms.InputTag("HerwigGenEvent"),
                                    cut = cms.string("")
                                    )
