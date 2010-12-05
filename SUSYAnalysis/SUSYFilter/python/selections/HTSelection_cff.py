import FWCore.ParameterSet.Config as cms

from RA2.Selection.RA2Selection_cfi import *

RA2Selection.selectors.HT.clone(jetTag = "goodJets")
RA2Selection.selectionSequence = cms.vstring('HT')

HTCut = cms.EDFilter("Selection",
                     selections = RA2Selection,
                     filterSelection = cms.vstring('HT'),
                     weightName = cms.InputTag('weightProducer:weight'),
                     showStatistics = cms.bool(True),
                     writeVariables = cms.bool(True),
                     onlySimulation = cms.bool(False)
                     )
