import FWCore.ParameterSet.Config as cms

###################################################
from RA2.Selection.RA2Selection_cfi import *

RA2FinalSelection = cms.EDFilter("Selection",
	selections = RA2Selection,
	filterSelection = cms.vstring(
		#'HLTHT',
		'PrimaryVertex', 
		'JetID',
		'JetSelection',
		'HT',
		'MHT',
		'MHTdPhiMin',
		'LeptonVeto',
		'Other'
		),
    weightName = cms.InputTag('weightProducer:weight'),
    showStatistics = cms.bool(True),
    writeVariables = cms.bool(True),
    onlySimulation = cms.bool(False)
)
RA2FinalSelection.selections.selectionSequence = RA2FinalSelection.filterSelection

###################################################
RA2ReducedSelection = RA2FinalSelection.clone()

RA2ReducedSelection.selections.selectors.MHTdPhiMin.dPhiJet1MHTMin = -1
RA2ReducedSelection.selections.selectors.MHTdPhiMin.dPhiJet2MHTMin = -1
RA2ReducedSelection.selections.selectors.MHT.minMHT = 60.

###################################################
RA2PreSelection = RA2ReducedSelection.clone()

RA2PreSelection.selections.selectors.HT.minHT = -1
RA2PreSelection.selections.selectors.MHTdPhiMin.rDistJetsMin = -1
RA2PreSelection.selections.selectors.MHTdPhiMin.mhtDPhiMin = -1
RA2PreSelection.selections.selectors.MHTdPhiMin.dPhiJet1MHTMin = -1
RA2PreSelection.selections.selectors.MHTdPhiMin.dPhiJet2MHTMin = -1
RA2PreSelection.selections.selectors.MHT.minMHT = 0.

###################################################
RA2SeedSelection = RA2PreSelection.clone()

RA2SeedSelection.selections.selectors.MHT.minMHT = -1
RA2SeedSelection.selections.selectors.MHT.maxMHT = -1
RA2SeedSelection.selections.selectors.MHT.maxMHTsig = 3

###################################################
RA2abcdSelection = RA2ReducedSelection.clone()

RA2abcdSelection.selections.selectors.MHTdPhiMin.mhtDPhiMin = 0
RA2abcdSelection.writeVariables = True

###################################################
RA2abcdFinalSelection = RA2abcdSelection.clone()

RA2abcdFinalSelection.selections.selectors.MHT.minMHT = 150.
RA2abcdFinalSelection.writeVariables = False

###################################################
