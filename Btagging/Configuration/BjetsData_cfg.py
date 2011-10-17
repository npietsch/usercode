import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
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
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

from Btagging.BtagAnalyzer.BtagAnalyzer_cfi import *

analyzeBtags.jets = "goodJets"
analyzeBtags.muons = "goodMuons"
analyzeBtags.electrons = "goodElectrons"
#analyzeBtags.matchedLightJets = "goodJets"
#analyzeBtags.matchedBjets = "mediumTrackHighEffBjets"
analyzeBtags.useEventWeight = False

process.analyzeBtags1m_1 = analyzeBtags.clone()
process.analyzeBtags1m_2 = analyzeBtags.clone()

process.analyzeBtags1e_1 = analyzeBtags.clone()
process.analyzeBtags1e_2 = analyzeBtags.clone()

process.analyzeTightBtags1m_1 = analyzeBtags.clone()
process.analyzeTightBtags1m_2 = analyzeBtags.clone()

process.analyzeTightBtags1e_1 = analyzeBtags.clone()
process.analyzeTightBtags1e_2 = analyzeBtags.clone()

process.analyzeTightBtags1m_1.bjets = "tightTrackHighEffBjets"
process.analyzeTightBtags1m_2.bjets = "tightTrackHighEffBjets"

process.analyzeTightBtags1e_1.bjets = "tightTrackHighEffBjets"
process.analyzeTightBtags1e_2.bjets = "tightTrackHighEffBjets"

#--------------------------
# muon selection path
#--------------------------

process.analyzeBtags1m = cms.Path(#process.printGenParticles *
                                  process.preselectionMuHTAllData *
                                  process.makeObjects *
                                  process.MuHadSelection *
                                  process.muonSelection*
                                  process.jetSelection*
                                  process.analyzeBtags1m_1 *
                                  process.analyzeTightBtags1m_1 *
                                  process.metSelection *
                                  process.analyzeBtags1m_2 *
                                  process.analyzeTightBtags1m_2
                                  )

#--------------------------
# electron selection path
#--------------------------

process.analyzeBtags1e = cms.Path(#process.printGenParticles *
                                  process.preselectionElHTAllData *
                                  process.makeObjects *
                                  process.ElHadSelection *
                                  process.electronSelection*
                                  process.jetSelection*
                                  process.analyzeBtags1e_1 *
                                  process.analyzeTightBtags1e_1 *
                                  process.metSelection *
                                  process.analyzeBtags1e_2 *
                                  process.analyzeTightBtags1e_2
                                  )

