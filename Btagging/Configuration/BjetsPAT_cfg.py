import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50000),
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
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')

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
analyzeBtags.useEventWeight = True

process.analyzeBtags1m_1 = analyzeBtags.clone()
process.analyzeBtags1m_2 = analyzeBtags.clone()

process.analyzeBtags1e_1 = analyzeBtags.clone()
process.analyzeBtags1e_2 = analyzeBtags.clone()

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#--------------------------
# muon selection path
#--------------------------

process.analyzeBtags1m = cms.Path(#process.printGenParticles *
                                  process.preselectionMuHTMC2 *
                                  process.makeObjects *
                                  process.eventWeightPU *
                                  process.weightProducer *
                                  process.MuHadSelection *
                                  process.muonSelection*
                                  process.jetSelection*
                                  process.analyzeBtags1m_1 *
                                  process.metSelection *
                                  process.analyzeBtags1m_2
                                  )

#--------------------------
# electron selection path
#--------------------------

process.analyzeBtags1e = cms.Path(#process.printGenParticles *
                                  process.preselectionElHTMC2 *
                                  process.makeObjects *
                                  process.eventWeightPU *
                                  process.weightProducer *
                                  process.ElHadSelection *
                                  process.electronSelection*
                                  process.jetSelection*
                                  process.analyzeBtags1e_1 *
                                  process.metSelection *
                                  process.analyzeBtags1e_2
                                  )
