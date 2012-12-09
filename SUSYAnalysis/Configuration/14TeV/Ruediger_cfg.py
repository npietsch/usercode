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
    #'file:../../../../../../Storage/QCD_HT700_JetPt40_14TeV_PAT.root'
    'file:SUSYPAT.root'
    )
 )
#process.source.duplictateCheckMode = cms.untracked.string('noDuplicateCheck')

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

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#-----------------------------------------------------------------
# load and configure modules to smear jet energy
#-----------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.GluinoAnalyzer_cfi")

process.analyzeLooseJets      = process.analyzeGluino.clone()
process.analyzeLooseJets.jets = "looseJets"

process.analyzeGoodJets       = process.analyzeGluino.clone()
process.analyzeGoodJets.jets  = "goodJets"

process.analyzeHiggs          = process.analyzeGluino.clone()
process.analyzeHiggs.jets     = "goodJets"

## analyzer modules for signal only
process.analyzeSignal1        = process.analyzeGluino.clone()
process.analyzeSignal1.jets   = "goodJets"

process.analyzeSignal2        = process.analyzeGluino.clone()
process.analyzeSignal2.jets   = "goodJets"

## analyzer modules for bino selection with 4 Jets
process.analyzeBino14         = process.analyzeGluino.clone()
process.analyzeBino14.jets     = "goodJets"

process.analyzeBino24          = process.analyzeGluino.clone()
process.analyzeBino24.jets     = "goodJets"

process.analyzeBino34          = process.analyzeGluino.clone()
process.analyzeBino34.jets     = "goodJets"

process.analyzeBino44          = process.analyzeGluino.clone()
process.analyzeBino44.jets     = "goodJets"

process.analyzeBino54          = process.analyzeGluino.clone()
process.analyzeBino54.jets     = "goodJets"

## analyzer modules for bino selection with 5 Jets
process.analyzeBino15         = process.analyzeGluino.clone()
process.analyzeBino15.jets     = "goodJets"

process.analyzeBino25          = process.analyzeGluino.clone()
process.analyzeBino25.jets     = "goodJets"

process.analyzeBino35          = process.analyzeGluino.clone()
process.analyzeBino35.jets     = "goodJets"

process.analyzeBino45          = process.analyzeGluino.clone()
process.analyzeBino45.jets     = "goodJets"

process.analyzeBino55          = process.analyzeGluino.clone()
process.analyzeBino55.jets     = "goodJets"

## analyzer modules for bino selection with 4-5 Jets
process.analyzeBino145          = process.analyzeGluino.clone()
process.analyzeBino145.jets     = "goodJets"

process.analyzeBino245          = process.analyzeGluino.clone()
process.analyzeBino245.jets     = "goodJets"

process.analyzeBino345          = process.analyzeGluino.clone()
process.analyzeBino345.jets     = "goodJets"

process.analyzeBino445          = process.analyzeGluino.clone()
process.analyzeBino445.jets     = "goodJets"

process.analyzeBino545          = process.analyzeGluino.clone()
process.analyzeBino545.jets     = "goodJets"

## analyzer modules for bino selection with 4-6 Jets
process.analyzeBino146          = process.analyzeGluino.clone()
process.analyzeBino146.jets     = "goodJets"

process.analyzeBino246          = process.analyzeGluino.clone()
process.analyzeBino246.jets     = "goodJets"

process.analyzeBino346          = process.analyzeGluino.clone()
process.analyzeBino346.jets     = "goodJets"

process.analyzeBino446          = process.analyzeGluino.clone()
process.analyzeBino446.jets     = "goodJets"

process.analyzeBino546          = process.analyzeGluino.clone()
process.analyzeBino546.jets     = "goodJets"

## analyzer modules for bino selection with 5-6 Jets
process.analyzeBino156          = process.analyzeGluino.clone()
process.analyzeBino156.jets     = "goodJets"

process.analyzeBino256          = process.analyzeGluino.clone()
process.analyzeBino256.jets     = "goodJets"

process.analyzeBino356          = process.analyzeGluino.clone()
process.analyzeBino356.jets     = "goodJets"

process.analyzeBino456          = process.analyzeGluino.clone()
process.analyzeBino456.jets     = "goodJets"

process.analyzeBino556          = process.analyzeGluino.clone()
process.analyzeBino556.jets     = "goodJets"

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

process.filterYmetBino = filterYmet.clone()
process.filterYmetBino.jets = "goodJets"
process.filterYmetBino.Cut =15

process.filterYmetWino = filterYmet.clone()
process.filterYmetWino.jets = "goodJets"
process.filterYmetWino.Cut = 8

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#--------------------------
# selection paths
#--------------------------

##------------------------------
## Bino selection paths
##------------------------------

process.Bino45 = cms.Path(# producer sequneces
                          process.weightProducer *
                          #process.scaledJetEnergy *
                          process.scaledJetEnergyJECUp *
                          process.scaledJetEnergyJECDown *
                          process.scaledJetEnergyJERUp *
                          process.scaledJetEnergyJERDown *
                          process.preselection14TeV *
                          process.makeObjects *
                          process.makeSUSYGenEvt *
                          # filter and analyzer sequences
                          process.analyzeSignal1 *
                          
                          process.filterMediumHT *
                          process.oneLooseMET *
                          process.analyzeLooseJets *
                          process.analyzeGoodJets *
                          
                          process.fourGoodJets *
                          process.maxFiveGoodJets *
                          process.analyzeBino145 *
                          
                          process.noVetoMuon *
                          process.noVetoElectron *
                          process.analyzeBino245 *
                          
                          process.filterDeltaPhi1 *
                          process.analyzeBino345 *
                          
                          process.filterDeltaPhi2 *
                          process.analyzeBino445 *
                          
                          process.filterYmetBino *
                          process.analyzeBino545 *
                          # study JES dependence
                          process.analyzeBinoJECUp *
                          process.analyzeBinoJECDown *
                          process.analyzeBinoJERUp *
                          process.analyzeBinoJERDown
                          )

process.test = cms.Path(process.preselection14TeV *
                        process.analyzeHiggs)

process.Bino4 = cms.Path(# filter and analyzer sequences
                         process.preselection14TeV *
                         process.filterMediumHT *
                         process.oneLooseMET *
                                                
                         process.fourGoodJets *
                         process.maxFourGoodJets *
                         process.analyzeBino14 *
                        
                         process.noVetoMuon *
                         process.noVetoElectron *
                         process.analyzeBino24 *
                         
                         process.filterDeltaPhi1 *
                         process.analyzeBino34 *
                         
                         process.filterDeltaPhi2 *
                         process.analyzeBino44*

                         process.filterYmetBino *
                         process.analyzeBino54
                         )

process.Bino5 = cms.Path(# filter and analyzer sequences
                         process.preselection14TeV *
                         process.filterMediumHT *
                         process.oneLooseMET *
                                                
                         process.fiveGoodJets *
                         process.maxFiveGoodJets *
                         process.analyzeBino15 *
                        
                         process.noVetoMuon *
                         process.noVetoElectron *
                         process.analyzeBino25 *
                         
                         process.filterDeltaPhi1 *
                         process.analyzeBino35 *
                         
                         process.filterDeltaPhi2 *
                         process.analyzeBino45*

                         process.filterYmetBino *
                         process.analyzeBino55
                         )

process.Bino46 = cms.Path(# filter and analyzer sequences
                          process.preselection14TeV *
                          process.filterMediumHT *
                          process.oneLooseMET *
                          
                          process.fourGoodJets *
                          process.maxSixGoodJets *
                          process.analyzeBino146 *
                          
                          process.noVetoMuon *
                          process.noVetoElectron *
                          process.analyzeBino246 *
                          
                          process.filterDeltaPhi1 *
                          process.analyzeBino346 *
                          
                          process.filterDeltaPhi2 *
                          process.analyzeBino446*
                          
                          process.filterYmetBino *
                          process.analyzeBino546
                         )

process.Bino56 = cms.Path(# filter and analyzer sequences
                          process.preselection14TeV *
                          process.filterMediumHT *
                          process.oneLooseMET *
                          
                          process.fiveGoodJets *
                          process.maxSixGoodJets *
                          process.analyzeBino156 *
                          
                          process.noVetoMuon *
                          process.noVetoElectron *
                          process.analyzeBino256 *
                          
                          process.filterDeltaPhi1 *
                          process.analyzeBino356 *
                          
                          process.filterDeltaPhi2 *
                          process.analyzeBino456*
                          
                          process.filterYmetBino *
                          process.analyzeBino556
                         )

##------------------------------
## Wino selection path
##------------------------------

process.Wino = cms.Path(# filter and analyzer sequences
                        process.preselection14TeV *
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

                        process.filterYmetWino *
                        process.analyzeWino5 *
                        # study JES dependence
                        process.analyzeWinoJECUp *
                        process.analyzeWinoJECDown *
                        process.analyzeWinoJERUp *
                        process.analyzeWinoJERDown 
                        )
