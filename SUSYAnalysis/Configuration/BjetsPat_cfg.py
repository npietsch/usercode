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
# Create Gen Events 
#------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
# trace back susy decay cascades to 1st, 2nd, 3rd, 4th or 5th sparticle
process.SUSYGenEvt.Generation = 3
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------
# Gen Event Selection 
#------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#------------------------------------------------
# Event Selection
#------------------------------------------------

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RAPreselection_cff")

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

process.oneLepton.electronSource = "goodElectrons"
process.oneLepton.muonSource = "goodMuons"                           
process.oneLepton.minNumber = 1

process.twoLepton.electronSource = "goodElectrons"
process.twoLepton.muonSource = "goodMuons"                           
process.twoLepton.minNumber = 2

#------------------------------------------------
# Analysis
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYLooseBjetsAnalysis_cff")

#-------------------------------------------------
# Temp
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-------------------------------------------------
# Selection paths 
#-------------------------------------------------

process.Selection1l = cms.Path(#process.patDefaultSequence *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               #process.makeGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.ttGenEventFitler *
                               process.preselection *
                               process.twoLepton *
                               process.threeGoodJets *
                               process.twoMediumJets *
                               process.oneTightJet *
                               process.metSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1l_1 *
                               process.ZVetoMu *
                               process.analyzeSUSYBjets1l_2
                               )

process.Selection1b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.makeGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.twoLepton *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.oneMediumTrackHighEffBjet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets1b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets1b1l_2
                                 )

process.Selection2b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.makeGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.twoLepton *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.twoMediumTrackHighEffBjet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets2b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets2b1l_2
                                 )

process.Selection3b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.makeGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.twoLepton *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.threeMediumTrackHighEffBjet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets3b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets3b1l_2
                                 )

process.Selection4b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.makeGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.twoLepton *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.fourMediumTrackHighEffBjet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets4b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets4b1l_2
                                 )
