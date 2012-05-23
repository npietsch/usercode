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
    'file:../../../../../../Storage/QCD_HT700_JetPt40_14TeV_PAT.root'
    )
 )
process.source.duplictateCheckMode = cms.untracked.string('noDuplicateCheck')

# load and configure modules for event weighting
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

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
#process.looseJets.src  = "scaledJetEnergy:selectedPatJetsAK5PF"
#process.goodJets.src   = "scaledJetEnergy:selectedPatJetsAK5PF"

#process.looseMETs.src  = "scaledJetEnergy:patMETsPF"
#process.mediumMETs.src = "scaledJetEnergy:patMETsPF"
#process.tightMETs.src  = "scaledJetEnergy:patMETsPF"
#process.looseMETs.src  = "scaledJetEnergy:patMETsPF"

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

#-----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.GluinoAnalyzer_cfi")

process.analyzeLooseJets      = process.analyzeGluino.clone()
process.analyzeLooseJets.jets = "looseJets"

process.analyzeGoodJets      = process.analyzeGluino.clone()
process.analyzeGoodJets.jets = "goodJets"

## analyzer modules for bino selection
process.analyzeBino1          = process.analyzeGluino.clone()
process.analyzeBino1.jets     = "goodJets"

process.analyzeBino2          = process.analyzeGluino.clone()
process.analyzeBino2.jets     = "goodJets"

process.analyzeBino3          = process.analyzeGluino.clone()
process.analyzeBino3.jets     = "goodJets"

process.analyzeBino4          = process.analyzeGluino.clone()
process.analyzeBino4.jets     = "goodJets"

process.analyzeBino5          = process.analyzeGluino.clone()
process.analyzeBino5.jets     = "goodJets"

## analyzer modules for bino selection type A
process.analyzeBino1A         = process.analyzeGluino.clone()
process.analyzeBino1A.jets    = "goodJets"

process.analyzeBino2A         = process.analyzeGluino.clone()
process.analyzeBino2A.jets    = "goodJets"

process.analyzeBino3A         = process.analyzeGluino.clone()
process.analyzeBino3A.jets    = "goodJets"

process.analyzeBino4A         = process.analyzeGluino.clone()
process.analyzeBino4A.jets    = "goodJets"

process.analyzeBino5A         = process.analyzeGluino.clone()
process.analyzeBino5A.jets    = "goodJets"

## analyzer modules for wino selection
process.analyzeWino1          = process.analyzeGluino.clone()
process.analyzeWino1.jets     = "goodJets"

process.analyzeWino2          = process.analyzeGluino.clone()
process.analyzeWino2.jets     = "goodJets"

process.analyzeWino3          = process.analyzeGluino.clone()
process.analyzeWino3.jets     = "goodJets"

process.analyzeWino4          = process.analyzeGluino.clone()
process.analyzeWino4.jets     = "goodJets"   

process.analyzeWino5          = process.analyzeGluino.clone()
process.analyzeWino5.jets     = "goodJets"

# Configure modules for JER/JEC studies
process.analyzeBino1JECUp         = process.analyzeGluino.clone()
process.analyzeBino1JECUp.jets    = "goodJetsJECUp"

process.analyzeBino1JECDown       = process.analyzeGluino.clone()
process.analyzeBino1JECDown.jets  = "goodJetsJECDown"

process.analyzeBino1JERUp         = process.analyzeGluino.clone()
process.analyzeBino1JERUp.jets    = "goodJetsJERUp"

process.analyzeBino1JERDown       = process.analyzeGluino.clone()
process.analyzeBino1JERDown.jets  = "goodJetsJERDown"

process.analyzeWino1JECUp         = process.analyzeGluino.clone()
process.analyzeWino1JECUp.jets    = "goodJetsJECUp"

process.analyzeWino1JECDown       = process.analyzeGluino.clone()
process.analyzeWino1JECDown.jets  = "goodJetsJECDown"

process.analyzeWino1JERUp         = process.analyzeGluino.clone()
process.analyzeWino1JERUp.jets    = "goodJetsJERUp"

process.analyzeWino1JERDown       = process.analyzeGluino.clone()
process.analyzeWino1JERDown.jets  = "goodJetsJERDown"

#-------------------------------------------------
# Load additional filter modules 
#-------------------------------------------------

from SUSYAnalysis.SUSYFilter.filters.DeltaPhiFilter_cfi import *

process.filterDeltaPhi1=filterDeltaPhi.clone()
process.filterDeltaPhi1.Jet = 0
process.filterDeltaPhi1.jets = "goodJets"

process.filterDeltaPhi2=filterDeltaPhi.clone()
process.filterDeltaPhi2.Jet = 1
process.filterDeltaPhi2.jets = "goodJets"

from SUSYAnalysis.SUSYFilter.filters.YmetFilter_cfi import *

process.filterYmet = filterYmet.clone()
process.filterYmet.jets = "goodJets"
process.filterYmet.Cut =15

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#--------------------------
# selection paths
#--------------------------

process.Bino = cms.Path(# producer sequneces
                        process.weightProducer *
                        #process.scaledJetEnergy *
                        process.scaledJetEnergyJECUp *
                        process.scaledJetEnergyJECDown *
                        process.scaledJetEnergyJERUp *
                        process.scaledJetEnergyJERDown *
                        process.makeObjects *
                        process.makeSUSYGenEvt *
                        # filter and analyzer sequences
                        process.filterMediumHT *
                        process.oneLooseMET *
                        process.analyzeLooseJets *
                        process.analyzeGoodJets *
                        
                        process.threeGoodJets *
                        process.maxFiveGoodJets *
                        process.analyzeBino1 *
                        
                        process.noVetoMuon *
                        process.noVetoElectron *
                        process.analyzeBino2 *
                        
                        process.filterDeltaPhi1 *
                        process.analyzeBino3 *
                        
                        process.filterDeltaPhi2 *
                        process.analyzeBino4 *

                        process.filterYmet *
                        process.analyzeBino5 *
                        # study JES dependence
                        process.analyzeBino1JECUp *
                        process.analyzeBino1JECDown *
                        process.analyzeBino1JERUp *
                        process.analyzeBino1JERDown
                        )


process.BinoA = cms.Path(# filter and analyzer sequences
                         process.filterMediumHT *
                         process.oneLooseMET *
                                                
                         process.threeGoodJets *
                         process.maxFourGoodJets *
                         process.analyzeBino1A *
                        
                         process.noVetoMuon *
                         process.noVetoElectron *
                         process.analyzeBino2A *
                         
                         process.filterDeltaPhi1 *
                         process.analyzeBino3A *
                         
                         process.filterDeltaPhi2 *
                         process.analyzeBino4A*

                         process.filterYmet *
                         process.analyzeBino5A
                         )

process.Wino = cms.Path(# filter and analyzer sequences
                        process.filterMediumHT *
                        process.oneLooseMET *

                        process.sixGoodJets *
                        process.analyzeWino1 *
                        
                        process.oneGoodLepton *
                        process.analyzeWino2 *

                        process.filterTightHT *
                        process.analyzeWino3 *
                                                
                        process.oneMediumMET *
                        process.analyzeWino4 *

                        process.filterYmet *
                        process.analyzeWino5 *
                        # study JES dependence
                        process.analyzeWino1JECUp *
                        process.analyzeWino1JECDown *
                        process.analyzeWino1JERUp *
                        process.analyzeWino1JERDown 
                        )
