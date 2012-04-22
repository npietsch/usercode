import FWCore.ParameterSet.Config as cms

process = cms.Process("Ruediger") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(
    #'/store/mc/Fall11/QCD_Pt-15to3000_Tune23_Flat_7TeV_herwigpp/AODSIM/PU_S6_START44_V9B-v1/0000/4276495A-A840-E111-B631-003048F0E5A4.root'
    'file:Ruediger.root'
    )
)                                   
  

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START44_V10::All')

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:A1PAT.root'
    #'file:Test.root'
    )
 )

#------------------------------------------------------
# Import module to produce SUSYGenEvent
#------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.JetSelection_cff")

#-----------------------------------------------------------------
# load and configure modules to smear jet energy
#-----------------------------------------------------------------

from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()

# Define sources for jets and met producer modules
process.looseJets.src  = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodJets.src   = "scaledJetEnergy:selectedPatJetsAK5PF"

process.looseMETs.src  = "scaledJetEnergy:patMETsPF"
process.mediumMETs.src = "scaledJetEnergy:patMETsPF"
process.tightMETs.src  = "scaledJetEnergy:patMETsPF"
process.looseMETs.src  = "scaledJetEnergy:patMETsPF"

process.scaledJetEnergyJECUp                     = scaledJetEnergy.clone()
process.scaledJetEnergyJECUp.scaleType           = "jes:up"

process.scaledJetEnergyJECDown                   = scaledJetEnergy.clone()
process.scaledJetEnergyJECDown.scaleType         = "jes:down"

process.scaledJetEnergyJERUp                     = scaledJetEnergy.clone()
process.scaledJetEnergyJERUp.resolutionFactors   = cms.vdouble(1.2, 1.25, 1.3)

process.scaledJetEnergyJERDown                   = scaledJetEnergy.clone()
process.scaledJetEnergyJERDown.resolutionFactors = cms.vdouble(1., 0.95, 0.9)

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.GluinoAnalyzer_cfi")

process.analyzeLooseJets      = process.analyzeGluino.clone()
process.analyzeLooseJets.jets = "looseJets"

process.analyzeGoodJets      = process.analyzeGluino.clone()
process.analyzeGoodJets.jets = "goodJets"

process.analyzeBino1          = process.analyzeGluino.clone()
process.analyzeBino1.jets     = "goodJets"

process.analyzeBino2          = process.analyzeGluino.clone()
process.analyzeBino2.jets     = "goodJets"

process.analyzeBino3          = process.analyzeGluino.clone()
process.analyzeBino3.jets     = "goodJets"

process.analyzeWino1          = process.analyzeGluino.clone()
process.analyzeWino1.jets     = "goodJets"

process.analyzeWino2          = process.analyzeGluino.clone()
process.analyzeWino2.jets     = "goodJets"

process.analyzeWino3          = process.analyzeGluino.clone()
process.analyzeWino3.jets     = "goodJets"

# Configure modules for JER/JEC studies
process.analyzeBino1JECUp         = process.analyzeGluino.clone()
process.analyzeBino1JECUp.jets    = "goodJetsJECUp"

process.analyzeBino1JECDown       = process.analyzeGluino.clone()
process.analyzeBino1JECDown.jets  = "goodJetsJECDown"

process.analyzeBino1JERUp         = process.analyzeGluino.clone()
process.analyzeBino1JERUp.jets    = "goodJetsJERUp"

process.analyzeBino1JERDown       = process.analyzeGluino.clone()
process.analyzeBino1JERDown.jets  = "goodJetsJERDown"

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#--------------------------
# selection paths
#--------------------------

process.Bino = cms.Path(process.scaledJetEnergy *
                        process.scaledJetEnergyJECUp *
                        process.scaledJetEnergyJECDown *
                        process.scaledJetEnergyJERUp *
                        process.scaledJetEnergyJERDown *
                        process.makeObjects *
                        process.makeSUSYGenEvt *
                        process.analyzeLooseJets *
                        process.analyzeGoodJets *
                        process.maxFourGoodJets *
                        process.analyzeBino1 *
                        process.analyzeBino1JECUp *
                        process.analyzeBino1JECDown *
                        process.analyzeBino1JERUp *
                        process.analyzeBino1JERDown
                        )

process.Wino = cms.Path(process.scaledJetEnergy *
                        process.scaledJetEnergyJECUp *
                        process.scaledJetEnergyJECDown *
                        process.scaledJetEnergyJERUp *
                        process.scaledJetEnergyJERDown *
                        process.makeObjects *
                        process.makeSUSYGenEvt *
                        process.sevenGoodJets *
                        process.analyzeWino1 *
                        process.oneGoodLepton *
                        process.analyzeWino2 
                        )
