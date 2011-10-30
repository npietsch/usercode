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

#----------------------------------------------------------------------------------------
# Load and configure modules for analysis of b-tagging
#----------------------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

process.analyzeBtags = analyzeBtags.clone()

# TCHEM
process.analyzeBtagsTCHEM1 = process.analyzeBtags.clone()
process.analyzeBtagsTCHEM1.bjets = "mediumTrackHighEffBjets"

process.analyzeBtagsTCHEM2 = process.analyzeBtagsTCHEM1.clone()

process.analyzeBtagsTCHEM3 = process.analyzeBtagsTCHEM1.clone()

process.analyzeBtagsTCHEM4 = process.analyzeBtagsTCHEM1.clone()

# TCHEM with scale factors
process.analyzeBtagsTCHEM3sf = process.analyzeBtagsTCHEM1.clone()

# SSVHEM
process.analyzeBtagsSSVHEM1 = process.analyzeBtags.clone()
process.analyzeBtagsSSVHEM1.bjets = "mediumSSVHighEffBjets"

process.analyzeBtagsSSVHEM2 = process.analyzeBtagsSSVHEM1.clone()

process.analyzeBtagsSSVHEM3 = process.analyzeBtagsSSVHEM1.clone()

process.analyzeBtagsSSVHEM4 = process.analyzeBtagsSSVHEM1.clone()

# TCHEM  with scale factors
process.analyzeBtagsSSVHEM3sf = process.analyzeBtagsSSVHEM1.clone()

#--------------------------
# Test path
#--------------------------

process.analyzeBtags_test = cms.Path(process.preselectionMuHTAllData *
                                     process.makeObjects *
                                     # MuHad selection
                                     process.MuHadSelection *
                                     # muon selection
                                     process.muonSelection*
                                     # jet selection
                                     process.jetSelection*
                                     process.analyzeBtagsTCHEM3 *
                                     process.analyzeBtagsSSVHEM3*
                                     process.analyzeBtagsTCHEM3sf *
                                     process.analyzeBtagsSSVHEM3sf #*
                                     # tight selection
                                     #process.filterMediumHT *
                                     #process.oneMediumMET *
                                     #process.analyzeBtagsTCHEM4 *
                                     #process.analyzeBtagsSSVHEM4
                                     )
