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

#----------------------------------------------------------------------------
# Load and configure modules for muon channel b-tag event weighting
#----------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

# TCHEM
process.analyzeBtagsMuTCHEM3 = analyzeBtags.clone()
process.analyzeBtagsMuTCHEM3.bjets = "mediumTrackHighEffBjets"

process.analyzeBtagsMuTCHEM3highPt = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsMuTCHEM3highPt.jets = "highPtJets"

process.analyzeBtagsMuTCHEM3lowPt = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsMuTCHEM3lowPt.jets = "lowPtJets"

process.analyzeBtagsMuTCHEM4       = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsMuTCHEM4highPt = process.analyzeBtagsMuTCHEM3highPt.clone()
process.analyzeBtagsMuTCHEM4lowPt  = process.analyzeBtagsMuTCHEM3lowPt.clone()

## clones
process.analyzeBtagsMuTCHEM3dilep = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsMuTCHEM3highPtdilep = process.analyzeBtagsMuTCHEM3highPt.clone()
process.analyzeBtagsMuTCHEM3lowPtdilep  = process.analyzeBtagsMuTCHEM3lowPt.clone()

process.analyzeBtagsMuTCHEM4dilep = process.analyzeBtagsMuTCHEM4.clone()
process.analyzeBtagsMuTCHEM4highPtdilep = process.analyzeBtagsMuTCHEM4highPt.clone()
process.analyzeBtagsMuTCHEM4lowPtdilep  = process.analyzeBtagsMuTCHEM4lowPt.clone()

## for cross-check
process.analyzeBtagsRA4bMuTCHEM3 = process.analyzeBtagsMuTCHEM3.clone()
process.analyzeBtagsRA4bMuTCHEM4 = process.analyzeBtagsMuTCHEM4.clone()

# SSVHEM
process.analyzeBtagsMuSSVHEM3 = analyzeBtags.clone()
process.analyzeBtagsMuSSVHEM3.bjets = "mediumSSVHighEffBjets"

process.analyzeBtagsMuSSVHEM3highPt = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsMuSSVHEM3highPt.jets = "highPtJets"

process.analyzeBtagsMuSSVHEM3lowPt = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsMuSSVHEM3lowPt.jets = "lowPtJets"

process.analyzeBtagsMuSSVHEM4       = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsMuSSVHEM4highPt = process.analyzeBtagsMuSSVHEM3highPt.clone()
process.analyzeBtagsMuSSVHEM4lowPt  = process.analyzeBtagsMuSSVHEM3lowPt.clone()

## clones
process.analyzeBtagsMuSSVHEM3dilep = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsMuSSVHEM3highPtdilep = process.analyzeBtagsMuSSVHEM3highPt.clone()
process.analyzeBtagsMuSSVHEM3lowPtdilep  = process.analyzeBtagsMuSSVHEM3lowPt.clone()

process.analyzeBtagsMuSSVHEM4dilep = process.analyzeBtagsMuSSVHEM4.clone()
process.analyzeBtagsMuSSVHEM4highPtdilep = process.analyzeBtagsMuSSVHEM4highPt.clone()
process.analyzeBtagsMuSSVHEM4lowPtdilep  = process.analyzeBtagsMuSSVHEM4lowPt.clone()

## for cross-check
process.analyzeBtagsRA4bMuSSVHEM3 = process.analyzeBtagsMuSSVHEM3.clone()
process.analyzeBtagsRA4bMuSSVHEM4 = process.analyzeBtagsMuSSVHEM4.clone()

#--------------------------
# Muon selection paths
#--------------------------

## Standard RA4b selection
##-------------------------
process.analyzeBtags_RA4bMu = cms.Path(# Standard RA4b preselection
                                       process.preselectionMuHTAllData *
                                       process.makeObjects *
                                       # match different triggers
                                       process.MuHadSelection *
                                       # muon selection
                                       process.muonSelection*
                                       # jet selection
                                       process.jetSelection*
                                       # analyze btags
                                       process.analyzeBtagsRA4bMuTCHEM3 *
                                       process.analyzeBtagsRA4bMuSSVHEM3 *
                                       # additinal cut
                                       process.oneNoSignalMET *
                                       # analyze btags
                                       process.analyzeBtagsRA4bMuTCHEM4 *
                                       process.analyzeBtagsRA4bMuSSVHEM4
                                       )


## RA4b selection with cut on two high pt jets in and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_RA4b = cms.Path(# Standard RA4b preselection
                                     process.preselectionMuHTAllData *
                                     process.makeObjects *
                                     # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                     process.highPtJets *
                                     process.lowPtJets *
                                     # additinal cut
                                     process.twoHighPtJets *
                                     # match different triggers
                                     process.MuHadSelection *
                                     # muon selection
                                     process.muonSelection*
                                     # jet selection
                                     process.jetSelection*
                                     # analyze btags
                                     process.analyzeBtagsMuTCHEM3 *
                                     process.analyzeBtagsMuSSVHEM3*
                                     process.analyzeBtagsMuTCHEM3lowPt *
                                     process.analyzeBtagsMuSSVHEM3lowPt *
                                     process.analyzeBtagsMuTCHEM3highPt *
                                     process.analyzeBtagsMuSSVHEM3highPt *
                                     # additinal cut
                                     process.oneNoSignalMET *
                                     # analyze btags
                                     process.analyzeBtagsMuTCHEM4 *
                                     process.analyzeBtagsMuSSVHEM4*
                                     process.analyzeBtagsMuTCHEM4lowPt *
                                     process.analyzeBtagsMuSSVHEM4lowPt *
                                     process.analyzeBtagsMuTCHEM4highPt *
                                     process.analyzeBtagsMuSSVHEM4highPt
                                     )

## Incl. RA4b selection with cut on two high pt jets and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_diLep = cms.Path(# Standard RA4b preselection
                                      process.preselectionMuHTAllData *
                                      process.makeObjects *
                                      # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                      process.highPtJets *
                                      process.lowPtJets *
                                      ## additional cut
                                      process.twoHighPtJets *
                                      # match different triggers
                                      process.MuHadSelection *
                                      # muon selection
                                      process.oneGoodMuon *
                                      # jet selection
                                      process.twoGoodJets*
                                      # analyze btags
                                      process.analyzeBtagsMuTCHEM3dilep *
                                      process.analyzeBtagsMuSSVHEM3dilep*
                                      process.analyzeBtagsMuTCHEM3lowPtdilep *
                                      process.analyzeBtagsMuSSVHEM3lowPtdilep *
                                      process.analyzeBtagsMuTCHEM3highPtdilep *
                                      process.analyzeBtagsMuSSVHEM3highPtdilep *
                                      # additinal cut
                                      process.oneNoSignalMET*
                                      # analyze btags
                                      process.analyzeBtagsMuTCHEM4dilep *
                                      process.analyzeBtagsMuSSVHEM4dilep*
                                      process.analyzeBtagsMuTCHEM4lowPtdilep *
                                      process.analyzeBtagsMuSSVHEM4lowPtdilep *
                                      process.analyzeBtagsMuTCHEM4highPtdilep *
                                      process.analyzeBtagsMuSSVHEM4highPtdilep
                                      )


#----------------------------------------------------------------------------
# Load and configure modules for electron channel b-tag event weighting
#----------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

# TCHEM
process.analyzeBtagsElTCHEM3 = analyzeBtags.clone()
process.analyzeBtagsElTCHEM3.bjets = "mediumTrackHighEffBjets"

process.analyzeBtagsElTCHEM3highPt = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElTCHEM3highPt.jets = "highPtJets"

process.analyzeBtagsElTCHEM3lowPt = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElTCHEM3lowPt.jets = "lowPtJets"

process.analyzeBtagsElTCHEM4       = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElTCHEM4highPt = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsElTCHEM4lowPt  = process.analyzeBtagsElTCHEM3lowPt.clone()

## clones
process.analyzeBtagsElTCHEM3dilep = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElTCHEM3highPtdilep = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsElTCHEM3lowPtdilep  = process.analyzeBtagsElTCHEM3lowPt.clone()

process.analyzeBtagsElTCHEM4dilep = process.analyzeBtagsElTCHEM4.clone()
process.analyzeBtagsElTCHEM4highPtdilep = process.analyzeBtagsElTCHEM4highPt.clone()
process.analyzeBtagsElTCHEM4lowPtdilep  = process.analyzeBtagsElTCHEM4lowPt.clone()

process.analyzeBtagsElElTCHEM3dilep = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsElElTCHEM3highPtdilep = process.analyzeBtagsElTCHEM3highPt.clone()
process.analyzeBtagsElElTCHEM3lowPtdilep  = process.analyzeBtagsElTCHEM3lowPt.clone()

process.analyzeBtagsElElTCHEM4dilep = process.analyzeBtagsElTCHEM4.clone()
process.analyzeBtagsElElTCHEM4highPtdilep = process.analyzeBtagsElTCHEM4highPt.clone()
process.analyzeBtagsElElTCHEM4lowPtdilep  = process.analyzeBtagsElTCHEM4lowPt.clone()

## for cross-check
process.analyzeBtagsRA4bElTCHEM3 = process.analyzeBtagsElTCHEM3.clone()
process.analyzeBtagsRA4bElTCHEM4 = process.analyzeBtagsElTCHEM4.clone()

# SSVHEM
process.analyzeBtagsElSSVHEM3 = analyzeBtags.clone()
process.analyzeBtagsElSSVHEM3.bjets = "mediumSSVHighEffBjets"

process.analyzeBtagsElSSVHEM3highPt = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElSSVHEM3highPt.jets = "highPtJets"

process.analyzeBtagsElSSVHEM3lowPt = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElSSVHEM3lowPt.jets = "lowPtJets"

process.analyzeBtagsElSSVHEM4       = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElSSVHEM4highPt = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsElSSVHEM4lowPt  = process.analyzeBtagsElSSVHEM3lowPt.clone()

## clones
process.analyzeBtagsElSSVHEM3dilep = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElSSVHEM3highPtdilep = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsElSSVHEM3lowPtdilep  = process.analyzeBtagsElSSVHEM3lowPt.clone()

process.analyzeBtagsElSSVHEM4dilep = process.analyzeBtagsElSSVHEM4.clone()
process.analyzeBtagsElSSVHEM4highPtdilep = process.analyzeBtagsElSSVHEM4highPt.clone()
process.analyzeBtagsElSSVHEM4lowPtdilep  = process.analyzeBtagsElSSVHEM4lowPt.clone()

process.analyzeBtagsElElSSVHEM3dilep = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsElElSSVHEM3highPtdilep = process.analyzeBtagsElSSVHEM3highPt.clone()
process.analyzeBtagsElElSSVHEM3lowPtdilep  = process.analyzeBtagsElSSVHEM3lowPt.clone()

process.analyzeBtagsElElSSVHEM4dilep = process.analyzeBtagsElSSVHEM4.clone()
process.analyzeBtagsElElSSVHEM4highPtdilep = process.analyzeBtagsElSSVHEM4highPt.clone()
process.analyzeBtagsElElSSVHEM4lowPtdilep  = process.analyzeBtagsElSSVHEM4lowPt.clone()

## for cross-check
process.analyzeBtagsRA4bElSSVHEM3 = process.analyzeBtagsElSSVHEM3.clone()
process.analyzeBtagsRA4bElSSVHEM4 = process.analyzeBtagsElSSVHEM4.clone()

#--------------------------
# Electron selection paths
#--------------------------

## Standard RA4b selection
##-------------------------
process.analyzeBtags_RA4bEl = cms.Path(# Standard RA4b preselection
                                       process.preselectionElHTAllData *
                                       process.makeObjects *
                                       # match different triggers
                                       process.ElHadSelection *
                                       # electron selection
                                       process.electronSelection*
                                       # jet selection
                                       process.jetSelection*
                                       # analyze btags
                                       process.analyzeBtagsRA4bElTCHEM3 *
                                       process.analyzeBtagsRA4bElSSVHEM3 *
                                       # additinal cut
                                       process.oneNoSignalMET *
                                       # analyze btags
                                       process.analyzeBtagsRA4bElTCHEM4 *
                                       process.analyzeBtagsRA4bElSSVHEM4
                                       )


## RA4b selection with cut on two high pt jets in and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_RA4b = cms.Path(# Standard RA4b preselection
                                     process.preselectionElHTAllData *
                                     process.makeObjects *
                                     # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                     process.highPtJets *
                                     process.lowPtJets *
                                     # additinal cut
                                     process.twoHighPtJets *
                                     # match different triggers
                                     process.ElHadSelection *
                                     # electron selection
                                     process.electronSelection*
                                     # jet selection
                                     process.jetSelection*
                                     # analyze btags
                                     process.analyzeBtagsElTCHEM3 *
                                     process.analyzeBtagsElSSVHEM3*
                                     process.analyzeBtagsElTCHEM3lowPt *
                                     process.analyzeBtagsElSSVHEM3lowPt *
                                     process.analyzeBtagsElTCHEM3highPt *
                                     process.analyzeBtagsElSSVHEM3highPt *
                                     # additinal cut
                                     process.oneNoSignalMET *
                                     # analyze btags
                                     process.analyzeBtagsElTCHEM4 *
                                     process.analyzeBtagsElSSVHEM4*
                                     process.analyzeBtagsElTCHEM4lowPt *
                                     process.analyzeBtagsElSSVHEM4lowPt *
                                     process.analyzeBtagsElTCHEM4highPt *
                                     process.analyzeBtagsElSSVHEM4highPt
                                     )

## Incl. RA4b selection with cut on two high pt jets and MET < 300 in addition
##---------------------------------------------------------------------------------
process.analyzeBtags_diLep = cms.Path(# Standard RA4b preselection
                                      process.preselectionElHTAllData *
                                      process.makeObjects *
                                      # produce collections of low pt (< 240) and hight pt (>240) jets in addition
                                      process.highPtJets *
                                      process.lowPtJets *
                                      ## additional cut
                                      process.twoHighPtJets *
                                      # match different triggers
                                      process.ElHadSelection *
                                      # electron selection
                                      process.oneGoodElectron *
                                      # jet selection
                                      process.twoGoodJets*
                                      # analyze btags
                                      process.analyzeBtagsElTCHEM3dilep *
                                      process.analyzeBtagsElSSVHEM3dilep*
                                      process.analyzeBtagsElTCHEM3lowPtdilep *
                                      process.analyzeBtagsElSSVHEM3lowPtdilep *
                                      process.analyzeBtagsElTCHEM3highPtdilep *
                                      process.analyzeBtagsElSSVHEM3highPtdilep *
                                      # additinal cut
                                      process.oneNoSignalMET*
                                      # analyze btags
                                      process.analyzeBtagsElTCHEM4dilep *
                                      process.analyzeBtagsElSSVHEM4dilep*
                                      process.analyzeBtagsElTCHEM4lowPtdilep *
                                      process.analyzeBtagsElSSVHEM4lowPtdilep *
                                      process.analyzeBtagsElTCHEM4highPtdilep *
                                      process.analyzeBtagsElSSVHEM4highPtdilep
                                      )







