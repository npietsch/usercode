import FWCore.ParameterSet.Config as cms

multiEventFilter = cms.EDFilter(
  "MultiEventFilter",
  EventList = cms.vstring(
    "0:0:0"  # run:lumi:event
  )
)
