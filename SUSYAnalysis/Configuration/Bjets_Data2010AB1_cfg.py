import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
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
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')

#------------------------------------------------
# Event Selection
#------------------------------------------------

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RAPreselection_cff")

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

## process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")
## process.scaledJetEnergy.inputJets = "selectedPatJets"
## process.scaledJetEnergy.inputMETs = "patMETs"
## process.scaledJetEnergy.scaleType   = "jes:up"
## #process.scaledJetEnergy.scaleFactor = 0.985#flat offset when using scaleType = "top:*"
## process.scaledJetEnergy.payload = "AK5Calo"

#process.goodJets.src="scaledJetEnergy:selectedPatJets"

process.oneLepton.electronSource = "goodElectrons"
process.oneLepton.muonSource = "goodMuons"                           
process.oneLepton.minNumber = 1

process.twoLepton.electronSource = "goodElectrons"
process.twoLepton.muonSource = "goodMuons"                           
process.twoLepton.minNumber = 2

#------------------------------------------------
# Analysis
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYLooseBjetsAnalysis_Data_cff")

#-------------------------------------------------
# Temp
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

from TopAnalysis.TopAnalyzer.MuonQuality_cfi import *
from TopAnalysis.TopAnalyzer.ElectronQuality_cfi import *

process.analyzeMuonQuality1 = analyzeMuonQuality.clone()
process.analyzeMuonQuality1.src= 'looseMuons'
process.analyzeMuonQuality1.analyze.index = 1

process.analyzeMuonQuality2 = analyzeMuonQuality.clone()
process.analyzeMuonQuality2.src= 'looseMuons'
process.analyzeMuonQuality2.analyze.index = 2

process.analyzeElectronQuality1 = analyzeElectronQuality.clone()
process.analyzeElectronQuality1.src= 'looseElectrons'
process.analyzeElectronQuality1.analyze.index = 1

process.analyzeElectronQuality2 = analyzeElectronQuality.clone()
process.analyzeElectronQuality2.src= 'looseElectrons'
process.analyzeElectronQuality2.analyze.index = 2

#-------------------------------------------------
# Selection paths 
#-------------------------------------------------

process.Selection2b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 process.preselectionData *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 process.twoMediumTrackHighEffBjet *
                                 process.analyzeSUSYLooseBjets2b1l_1 *
                                 process.analyzeMuonQuality1 *
                                 process.analyzeMuonQuality2 *
                                 process.analyzeElectronQuality1 *
                                 process.analyzeElectronQuality2
                                 )
