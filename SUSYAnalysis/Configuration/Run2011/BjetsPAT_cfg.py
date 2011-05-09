import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20000),
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


#-------------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
#       - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
#       - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-------------------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

## from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
## process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------


## 1-lepton
process.Selection1l = cms.Path(#process.patDefaultSequence *
                               process.makeObjects *
                               process.RA4MuonCollections *
                               process.makeSUSYGenEvt *
                               process.analyzeSUSYBjets1l_noCuts *
                               process.preselection *
                               process.MuHadSelection *
                               process.analyzeSUSYBjets1l_preselection *
                               process.RA4MuonSelection *
                               process.muonSelection*
                               process.analyzeSUSYBjets1l_oneGoodMuon *
                               process.fourGoodJets *
                               process.analyzeSUSYBjets1l_fourGoodJets *
                               process.oneTightJet *
                               process.analyzeSUSYBjets1l_oneTightJet *
                               process.twoMediumJets *
                               process.analyzeSUSYBjets1l_twoMediumJets *
                               process.HTSelection *
                               process.analyzeSUSYBjets1l_1 *
                               process.metSelection *
                               process.analyzeSUSYBjets1l_2
                               )

# 1-lepton selections
process.Selection1b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.oneMediumTrackHighEffBjet *
                                 process.analyzeSUSYBjets1b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets1b1l_2
                                 )

process.Selection2b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.twoMediumTrackHighEffBjets *
                                 process.analyzeSUSYBjets2b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets2b1l_2
                                 )

process.Selection3b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.threeMediumTrackHighEffBjets *
                                 process.analyzeSUSYBjets3b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets3b1l_2
                                 )

process.Selection4b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.fourMediumTrackHighEffBjets *
                                 process.analyzeSUSYBjets4b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets4b1l_2
                                 )

## 2 lepton
process.Selection2l = cms.Path(#process.patDefaultSequence *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.analyzeSUSYBjets2l_noCuts *
                               process.preselection *
                               process.MuHadSelection *
                               process.analyzeSUSYBjets2l_preselection *
                               process.oneGoodMuon*
                               process.twoGoodLeptons*
                               process.analyzeSUSYBjets2l_twoGoodLeptons *
                               process.threeGoodJets *
                               process.analyzeSUSYBjets2l_threeGoodJets *
                               process.oneTightJet *
                               process.analyzeSUSYBjets2l_oneTightJet *
                               process.twoMediumJets *
                               process.analyzeSUSYBjets2l_twoMediumJets *
                               process.HTSelection *
                               process.analyzeSUSYBjets2l_1 *
                               process.metSelection *
                               process.analyzeSUSYBjets2l_2
                               )
## 2-lepton selections
process.Selection1b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.oneMediumTrackHighEffBjet *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets1b2l_1
                                 )

process.Selection2b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.twoMediumTrackHighEffBjets *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets2b2l_1
                                 )

process.Selection3b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.threeMediumTrackHighEffBjets *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets3b2l_1
                                 )

process.Selection4b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.preselection *
                                 process.MuHadSelection *
                                 process.oneGoodMuon*
                                 process.twoGoodLeptons *
                                 process.threeGoodJets *
                                 process.twoMediumJets *
                                 process.fourMediumTrackHighEffBjets *
                                 process.oneTightJet *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets4b2l_1
                                 )
