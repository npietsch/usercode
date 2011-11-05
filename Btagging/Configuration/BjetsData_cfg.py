import FWCore.ParameterSet.Config as cms

process = cms.Process("AnalyzeBtags")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('AnalyzeBtags.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('GR_R_42_V14::All')

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")


from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *

process.highPtJets = selectedPatJets.clone(src = 'goodJets',
                                           cut =
                                           'pt > 240'
                                           )

process.lowPtJets = selectedPatJets.clone(src = 'goodJets',
                                          cut =
                                          'pt < 240'
                                          )

## select events with at least 2 high pt jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
process.twoHighPtJets = countPatJets.clone(src = 'highPtJets',
                                           minNumber = 2
                                           )

#----------------------------------------------------------------------------------------
# Load and configure modules for analysis of b-tagging
#----------------------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

# TCHEM
process.analyzeBtagsTCHEM3 = analyzeBtags.clone()
process.analyzeBtagsTCHEM3.bjets = "mediumTrackHighEffBjets"

process.analyzeBtagsTCHEM3highPt = process.analyzeBtagsTCHEM3.clone()
process.analyzeBtagsTCHEM3highPt.jets = "highPtJets"

process.analyzeBtagsTCHEM3lowPt = process.analyzeBtagsTCHEM3.clone()
process.analyzeBtagsTCHEM3lowPt.jets = "lowPtJets"

process.analyzeBtagsTCHEM3dilep = process.analyzeBtagsTCHEM3.clone()
process.analyzeBtagsTCHEM3highPtdilep = process.analyzeBtagsTCHEM3highPt.clone()
process.analyzeBtagsTCHEM3lowPtdilep  = process.analyzeBtagsTCHEM3lowPt.clone()

# SSVHEM
process.analyzeBtagsSSVHEM3 = analyzeBtags.clone()
process.analyzeBtagsSSVHEM3.bjets = "mediumSSVHighEffBjets"

process.analyzeBtagsSSVHEM3highPt = process.analyzeBtagsSSVHEM3.clone()
process.analyzeBtagsSSVHEM3highPt.jets = "highPtJets"

process.analyzeBtagsSSVHEM3lowPt = process.analyzeBtagsSSVHEM3.clone()
process.analyzeBtagsSSVHEM3lowPt.jets = "lowPtJets"

process.analyzeBtagsSSVHEM3dilep = process.analyzeBtagsSSVHEM3.clone()
process.analyzeBtagsSSVHEM3highPtdilep = process.analyzeBtagsSSVHEM3highPt.clone()
process.analyzeBtagsSSVHEM3lowPtdilep  = process.analyzeBtagsSSVHEM3lowPt.clone()

#--------------------------
# Test path
#--------------------------

process.analyzeBtags_test = cms.Path(# Standard RA4b preselection
                                     process.preselectionMuHTAllData *
                                     process.makeObjects *
                                     # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                     process.highPtJets *
                                     process.lowPtJets *
                                     process.twoHighPtJets *
                                     # match different triggers
                                     process.MuHadSelection *
                                     # muon selection
                                     process.muonSelection *
                                     # jet selection
                                     process.jetSelection *
                                     # analyze btags
                                     process.analyzeBtagsTCHEM3 *
                                     process.analyzeBtagsSSVHEM3 *
                                     process.analyzeBtagsTCHEM3lowPt *
                                     process.analyzeBtagsSSVHEM3lowPt *
                                     process.analyzeBtagsTCHEM3highPt *
                                     process.analyzeBtagsSSVHEM3highPt
                                     )

process.analyzeBtags_diLep = cms.Path(# Standard RA4b preselection
                                      process.preselectionMuHTAllData *
                                      process.makeObjects *
                                      # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                      process.highPtJets *
                                      process.lowPtJets *
                                      process.twoHighPtJets *
                                      # match different triggers
                                      process.MuHadSelection *
                                      # muon selection
                                      process.oneGoodMuon *
                                      # jet selection
                                      process.twoGoodJets*
                                      # analyze btags
                                      process.analyzeBtagsTCHEM3dilep *
                                      process.analyzeBtagsSSVHEM3dilep*
                                      process.analyzeBtagsTCHEM3lowPtdilep *
                                      process.analyzeBtagsSSVHEM3lowPtdilep *
                                      process.analyzeBtagsTCHEM3highPtdilep *
                                      process.analyzeBtagsSSVHEM3highPtdilep
                                      )
