import FWCore.ParameterSet.Config as cms

process = cms.Process("Ruediger") 

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
                                   fileName = cms.string(
    'Ruediger.root'
    )
)                                   
  
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START44_V10::All')

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:SUSYPAT.root'
    )
 )
#process.source.duplictateCheckMode = cms.untracked.string('noDuplicateCheck')

#------------------------------------------------------------------
# Load and configure module for cross-section weighting
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#------------------------------------------------------------------
# Load modules to create SUSYGenEvent
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#-----------------------------------------------------------------
# Import modules to filter events on generator level 
#-----------------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *

#------------------------------------------------------------------
# Load modules for preselection
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#------------------------------------------------------------------
# Load and configure module to smear jet energy on reco level
#------------------------------------------------------------------

from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
         
process.scaledJetEnergyJECUp                     = scaledJetEnergy.clone()
process.scaledJetEnergyJECUp.scaleType           = "jes:up"

process.scaledJetEnergyJECDown                   = scaledJetEnergy.clone()
process.scaledJetEnergyJECDown.scaleType         = "jes:down"

process.scaledJetEnergyJERUp                     = scaledJetEnergy.clone()
process.scaledJetEnergyJERUp.resolutionFactors   = cms.vdouble(1.2, 1.25, 1.3)

process.scaledJetEnergyJERDown                   = scaledJetEnergy.clone()
process.scaledJetEnergyJERDown.resolutionFactors = cms.vdouble(1., 0.95, 0.9)

process.L2L3ResidualMC = cms.ESSource(
    'LXXXCorrectionService',
    era = cms.string('Jec11V12'),
    section   = cms.string(''),
    level     = cms.string('L2L3Residual'),
    # the above 3 elements are needed only when the service is initialized from local txt files
    algorithm = cms.string('AK5PF'),
    # the 'algorithm' tag is also the name of the DB payload
    useCondDB = cms.untracked.bool(True)
    )

#------------------------------------------------------------------
# Load and configure analyzer modules
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.GluinoAnalyzer_cfi")

## analyzer modules for bino selection
process.analyzeBino_noCuts            = process.analyzeGluino.clone()
process.analyzeBino_noCuts.jets       = "goodJets"

process.analyzeBino_Preselection      = process.analyzeGluino.clone()
process.analyzeBino_Preselection.jets = "goodJets"

process.analyzeBino_45Jets_1          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_1.jets     = "goodJets"

process.analyzeBino_45Jets_1          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_1.jets     = "goodJets"

process.analyzeBino_45Jets_2          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_2.jets     = "goodJets"

process.analyzeBino_45Jets_3          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_3.jets     = "goodJets"

process.analyzeBino_45Jets_4          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_4.jets     = "goodJets"

process.analyzeBino_45Jets_5          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_5.jets     = "goodJets"

process.analyzeBino_45Jets_6          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_6.jets     = "goodJets"

process.analyzeBino_45Jets_7          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_7.jets     = "goodJets"

process.analyzeBino_45Jets_8          = process.analyzeGluino.clone()
process.analyzeBino_45Jets_8.jets     = "goodJets"

## analyzer modules for wino selection
process.analyzeWino_noCuts            = process.analyzeGluino.clone()
process.analyzeWino_noCuts.jets       = "goodJets"

process.analyzeWino_Preselection      = process.analyzeGluino.clone()
process.analyzeWino_Preselection.jets = "goodJets"

process.analyzeWino_1                 = process.analyzeGluino.clone()
process.analyzeWino_1.jets            = "goodJets"

process.analyzeWino_1                 = process.analyzeGluino.clone()
process.analyzeWino_1.jets            = "goodJets"

process.analyzeWino_2                 = process.analyzeGluino.clone()
process.analyzeWino_2.jets            = "goodJets"

process.analyzeWino_3                 = process.analyzeGluino.clone()
process.analyzeWino_3.jets            = "goodJets"

process.analyzeWino_4                 = process.analyzeGluino.clone()
process.analyzeWino_4.jets            = "goodJets"

process.analyzeWino_5                 = process.analyzeGluino.clone()
process.analyzeWino_5.jets            = "goodJets"

process.analyzeWino_6                 = process.analyzeGluino.clone()
process.analyzeWino_6.jets            = "goodJets"

# Configure modules for JER/JEC studies
process.analyzeBinoJECUp         = process.analyzeGluino.clone()
process.analyzeBinoJECUp.jets    = "goodJetsJECUp"

process.analyzeBinoJECDown       = process.analyzeGluino.clone()
process.analyzeBinoJECDown.jets  = "goodJetsJECDown"

process.analyzeBinoJERUp         = process.analyzeGluino.clone()
process.analyzeBinoJERUp.jets    = "goodJetsJERUp"

process.analyzeBinoJERDown       = process.analyzeGluino.clone()
process.analyzeBinoJERDown.jets  = "goodJetsJERDown"

process.analyzeWinoJECUp         = process.analyzeGluino.clone()
process.analyzeWinoJECUp.jets    = "goodJetsJECUp"

process.analyzeWinoJECDown       = process.analyzeGluino.clone()
process.analyzeWinoJECDown.jets  = "goodJetsJECDown"

process.analyzeWinoJERUp         = process.analyzeGluino.clone()
process.analyzeWinoJERUp.jets    = "goodJetsJERUp"

process.analyzeWinoJERDown       = process.analyzeGluino.clone()
process.analyzeWinoJERDown.jets  = "goodJetsJERDown"

#-----------------------------------------------------------------
# Load additional filter modules 
#-----------------------------------------------------------------

from SUSYAnalysis.SUSYFilter.filters.DeltaPhiFilter_cfi import *

process.filterDeltaPhi1 = filterDeltaPhi.clone()
process.filterDeltaPhi1.Jet = 0
process.filterDeltaPhi1.jets = "goodJets"

process.filterDeltaPhi2 = filterDeltaPhi.clone()
process.filterDeltaPhi2.Jet = 1
process.filterDeltaPhi2.jets = "goodJets"

process.filterDeltaPhi3 = filterDeltaPhi.clone()
process.filterDeltaPhi3.Jet = 2
process.filterDeltaPhi3.jets = "goodJets"
process.filterDeltaPhi3.Cut = 0.3 
from SUSYAnalysis.SUSYFilter.filters.YmetFilter_cfi import *

process.filterYmet_1 = filterYmet.clone()
process.filterYmet_1.jets = "goodJets"
process.filterYmet_1.Cut = 10

process.filterYmet_2 = filterYmet.clone()
process.filterYmet_2.jets = "goodJets"
process.filterYmet_2.Cut = 15

#-----------------------------------------------------------------
# Temp
#-----------------------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

##------------------------------
## Bino selection paths
##------------------------------

process.Bino_45Jets = cms.Path(# execute producer and preselection modules
                               process.weightProducer *
                               process.preselection14TeV *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               
                               # execute filter and analyzer modules
                               process.analyzeBino_noCuts *
                               
                               process.HTSelection *
                               process.metSelection *
                               
                               process.analyzeBino_Preselection *
                               
                               process.filterTightHT *
                               process.analyzeBino_45Jets_1 *
                               
                               process.fourToFiveGoodJets *
                               process.analyzeBino_45Jets_2 *

                               process.noVetoLepton *
                               process.analyzeBino_45Jets_3 *
                               
                               process.filterDeltaPhi1 *
                               process.analyzeBino_45Jets_4 *
                               
                               process.filterDeltaPhi2 *
                               process.analyzeBino_45Jets_5 *
                               
                               process.filterDeltaPhi3 *
                               process.analyzeBino_45Jets_6 *

                               process.filterYmet_1 *
                               process.analyzeBino_45Jets_7 *
                               
                               process.filterYmet_2 *
                               process.analyzeBino_45Jets_8
                               )

process.Wino = cms.Path(# execute producer and preselection modules
                        process.weightProducer *
                        process.preselection14TeV *
                        process.makeObjects *
                        process.makeSUSYGenEvt *
                        
                        # execute filter and analyzer modules
                        process.analyzeWino_noCuts *
                        
                        process.HTSelection *
                        process.metSelection *
                        
                        process.analyzeWino_Preselection *

                        process.filterTightHT *
                        process.analyzeWino_1 *
                        
                        process.sixGoodJets *
                        process.analyzeWino_2 *
                        
                        process.leptonSelection *
                        process.analyzeWino_3 *
                        
                        process.filterMT *
                        process.analyzeWino_4 *
                        
                        process.filterYmet_2 *
                        process.analyzeWino_5
                        )
