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
process.GlobalTag.globaltag = cms.string('START311_V2A::All')

#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## Standard pat sequence
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
##removeMCMatching(process, ['All'])

#removeSpecificPATObjects(process,
#                         ['Photons'],  # 'Tau' has currently been taken out due to problems with tau discriminators
#                         outputInProcess=False)

#removeCleaning(process,
#               outputInProcess=False)

process.patJetCorrFactors.payload = 'AK5Calo'
# For data:
#process.patJetCorrFactors.levels = ['L2Relative', 'L3Absolute', 'L2L3Residual', 'L5Flavor', 'L7Parton']
# For MC:
process.patJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
#process.patJetCorrFactors.flavorType = "T"

# embed IsoDeposits
process.patMuons.isoDeposits = cms.PSet(
    tracker = cms.InputTag("muIsoDepositTk"),
    ecal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","ecal"),
    hcal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","hcal"),
    user    = cms.VInputTag(
                            cms.InputTag("muIsoDepositCalByAssociatorTowers","ho"),
                            cms.InputTag("muIsoDepositJets")
                            ),
    )
process.patMuons.usePV = False

## add PF MET
from PhysicsTools.PatAlgos.tools.metTools import addPfMET
addPfMET(process, 'PF')

## Add particle flow jets
from PhysicsTools.PatAlgos.tools.jetTools import *

addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', ['L2Relative', 'L3Absolute']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True,
                 )

## remove TagInfos from jets to run on AOD
process.patJets.addTagInfos = False

process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.electronMatch*process.patElectronIDs*process.patElectronIsolation*process.patElectrons)

process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
    simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
    simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
    simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
    simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
    simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
    simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
    simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
    simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),
)

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
process.Selection1l = cms.Path(process.patDefaultSequence *
                               process.makeObjects *
                               process.RA4MuonCollections *
                               process.makeSUSYGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.makeGenEvt *
                               #process.ttGenEventFilter *
                               process.analyzeSUSYBjets1l_noCuts *
                               process.preselection *
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
                               process.tightHTSelection *
                               process.analyzeSUSYBjets1l_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1l_metSelection *
                               process.analyzeSUSYBjets1l_1
                               )

process.Selection2 = cms.Path(process.patDefaultSequence *
                              process.makeObjects *
                              process.RA4MuonCollections *
                              process.makeSUSYGenEvt *
                              #process.SUSYGenEventFilter *
                              #process.makeGenEvt *
                              #process.ttGenEventFilter *
                              process.preselection *
                              process.muonSelection*
                              process.fourGoodJets *
                              process.oneTightJet *
                              process.twoMediumJets *
                              process.tightHTSelection *
                              process.analyzeSUSYBjets1l_2 *
                              process.looseMetSelection *
                              process.analyzeSUSYBjets1l_3
                              )

process.Selection3 = cms.Path(process.patDefaultSequence *
                              process.makeObjects *
                              process.RA4MuonCollections *
                              process.makeSUSYGenEvt *
                              #process.SUSYGenEventFilter *
                              #process.makeGenEvt *
                              #process.ttGenEventFilter *
                              process.preselection *
                              process.muonSelection*
                              process.fourGoodJets *
                              process.oneTightJet *
                              process.twoMediumJets *
                              process.HTSelection *
                              process.analyzeSUSYBjets1l_4 *
                              process.metSelection *
                              process.analyzeSUSYBjets1l_5
                              )

## 1-lepton n-1 plots
process.Selection1l_nminus1_oneGoodMuon = cms.Path(process.patDefaultSequence *
                                                   process.makeObjects *
                                                   process.makeSUSYGenEvt *
                                                   #process.SUSYGenEventFilter *
                                                   #process.makeGenEvt *
                                                   #process.ttGenEventFilter *
                                                   process.preselection *
                                                   process.fourGoodJets *
                                                   process.oneTightJet *
                                                   process.twoMediumJets *
                                                   process.metSelection *
                                                   process.tightHTSelection *
                                                   process.analyzeSUSYBjets1l_nminus1_oneGoodMuon
                                                   )
process.Selection1l_nminus1_fourGoodJets = cms.Path(process.patDefaultSequence *
                                                    process.makeObjects *
                                                    process.makeSUSYGenEvt *
                                                    #process.SUSYGenEventFilter *
                                                    #process.makeGenEvt *
                                                    #process.ttGenEventFilter *
                                                    process.preselection *
                                                    process.muonSelection *
                                                    process.metSelection *
                                                    process.tightHTSelection *
                                                    process.analyzeSUSYBjets1l_nminus1_fourGoodJets
                                                    )
process.Selection1l_nminus1_oneTightJet = cms.Path(process.patDefaultSequence *
                                                   process.makeObjects *
                                                   process.makeSUSYGenEvt *
                                                   #process.SUSYGenEventFilter *
                                                   #process.makeGenEvt *
                                                   #process.ttGenEventFilter *
                                                   process.preselection *
                                                   process.muonSelection *
                                                   process.fourGoodJets *
                                                   process.metSelection *
                                                   process.tightHTSelection *
                                                   process.analyzeSUSYBjets1l_nminus1_oneTightJet
                                                   )
process.Selection1l_nminus1_twoMediumJets = cms.Path(process.patDefaultSequence *
                                                     process.makeObjects *
                                                     process.makeSUSYGenEvt *
                                                     #process.SUSYGenEventFilter *
                                                     #process.makeGenEvt *
                                                     #process.ttGenEventFilter *
                                                     process.preselection *
                                                     process.muonSelection *
                                                     process.fourGoodJets *
                                                     process.oneTightJet *
                                                     process.metSelection *
                                                     process.tightHTSelection *
                                                     process.analyzeSUSYBjets1l_nminus1_twoMediumJets
                                                     )
process.Selection1l_nminus1_metSelection = cms.Path(process.patDefaultSequence *
                                                    process.makeObjects *
                                                    process.makeSUSYGenEvt *
                                                    #process.SUSYGenEventFilter *
                                                    #process.makeGenEvt *
                                                    #process.ttGenEventFilter *
                                                    process.preselection *
                                                    process.muonSelection *
                                                    process.fourGoodJets *
                                                    process.oneTightJet *
                                                    process.twoMediumJets *
                                                    process.tightHTSelection *
                                                    process.analyzeSUSYBjets1l_nminus1_metSelection
                                                    )
process.Selection1l_nminus1_HTSelection = cms.Path(process.patDefaultSequence *
                                                   process.makeObjects *
                                                   process.makeSUSYGenEvt *
                                                   #process.SUSYGenEventFilter *
                                                   #process.makeGenEvt *
                                                   #process.ttGenEventFilter *
                                                   process.preselection *
                                                   process.muonSelection *
                                                   process.fourGoodJets *
                                                   process.oneTightJet *
                                                   process.twoMediumJets *
                                                   process.metSelection *
                                                   process.analyzeSUSYBjets1l_nminus1_HTSelection
                                                   )
# 1-lepton selections
process.Selection1b1l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
                                 process.preselection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.oneMediumTrackHighEffBjet *
                                 process.metSelection *
                                 process.tightHTSelection *
                                 process.analyzeSUSYBjets1b1l_1
                                 )

process.Selection2b1l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
                                 process.preselection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.twoMediumTrackHighEffBjets *
                                 process.metSelection *
                                 process.tightHTSelection *
                                 process.analyzeSUSYBjets2b1l_1
                                 )

process.Selection3b1l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
                                 process.preselection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.oneTightJet *
                                 process.threeMediumTrackHighEffBjets *
                                 process.metSelection *
                                 process.tightHTSelection *
                                 process.analyzeSUSYBjets3b1l_1
                                 )

process.Selection4b1l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
                                 process.preselection *
                                 process.muonSelection*
                                 process.fourGoodJets *
                                 process.twoMediumJets *
                                 process.fourMediumTrackHighEffBjets *
                                 process.oneTightJet *
                                 process.metSelection *
                                 process.tightHTSelection *
                                 process.analyzeSUSYBjets4b1l_1
                                 )
## 2 lepton
process.Selection2l = cms.Path(process.patDefaultSequence *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.makeGenEvt *
                               #process.ttGenEventFilter *
                               process.analyzeSUSYBjets2l_noCuts *
                               process.preselection *
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
                               process.analyzeSUSYBjets2l_metSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets2l_HTSelection *
                               process.analyzeSUSYBjets2l_1 *
                               process.ZVetoMu *
                               process.analyzeSUSYBjets2l_2
                               )
## 2-lepton selections
process.Selection1b2l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
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

process.Selection2b2l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
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

process.Selection3b2l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
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

process.Selection4b2l = cms.Path(process.patDefaultSequence *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 #process.SUSYGenEventFilter *
                                 #process.makeGenEvt *
                                 #process.ttGenEventFilter *
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
