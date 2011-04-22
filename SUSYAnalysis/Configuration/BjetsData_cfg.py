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

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

## process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")
## process.scaledJetEnergy.inputJets = "selectedPatJets"
## process.scaledJetEnergy.inputMETs = "patMETs"
## process.scaledJetEnergy.scaleType   = "jes:up"
## #process.scaledJetEnergy.scaleFactor = 0.985#flat offset when using scaleType = "top:*"
## process.scaledJetEnergy.payload = "AK5Calo"

#process.goodJets.src="scaledJetEnergy:selectedPatJets"

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#------------------------------------------------
# Load modules for analysis reco-level
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYLooseBjetsAnalysis_Data_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------

## 1-lepton selections
process.Selection1l = cms.Path(#process.patDefaultSequence *
                               process.makeObjects *
                               #process.makeSUSYGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.makeGenEvt *
                               #process.ttGenEventFitler *
                               process.preselection *
                               process.oneGoodMuon*
                               process.fourGoodJets *
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
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.fourGoodJets *
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
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.twoMediumTrackHighEffBjets *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets2b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets2b1l_2
                                 )

process.Selection3b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.threeMediumTrackHighEffBjets *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets3b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets3b1l_2
                                 )

process.Selection4b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.fourMediumTrackHighEffBjets *
                                 process.oneTightJet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets4b1l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets4b1l_2
                                 )
## 2-lepton selections
process.Selection2l = cms.Path(#process.patDefaultSequence *
                               process.makeObjects *
                               #process.makeSUSYGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.makeGenEvt *
                               #process.ttGenEventFitler *
                               process.preselection *
                               process.oneGoodMuon*
                               process.twoGoodLeptons *
                               process.threeGoodJets *
                               process.twoMediumJets *
                               process.oneTightJet *
                               process.metSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets2l_1 *
                               process.ZVetoMu *
                               process.analyzeSUSYBjets2l_2
                               )

process.Selection1b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.oneMediumTrackHighEffBjet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets1b2l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets1b2l_2
                                 )

process.Selection2b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.twoMediumTrackHighEffBjets *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets2b2l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets2b2l_2
                                 )

process.Selection3b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.threeMediumTrackHighEffBjets *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets3b2l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets3b2l_2
                                 )

process.Selection4b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFitler *
                                 process.preselection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.fourMediumTrackHighEffBjets *
                                 process.oneTightJet *
                                 process.metSelection *
                                 process.HTSelection *
                                 process.analyzeSUSYBjets4b2l_1 *
                                 process.ZVetoMu *
                                 process.analyzeSUSYBjets4b2l_2
                                 )

