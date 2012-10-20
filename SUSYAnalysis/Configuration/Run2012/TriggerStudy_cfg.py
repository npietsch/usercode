# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms

process = cms.Process("Trigger")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/752/3C0A66AC-789B-E111-94AB-003048CF99BA.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/774/88364725-889B-E111-B053-001D09F27003.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/806/ACB6E731-C89B-E111-811E-001D09F24664.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/812/145D80B4-D09B-E111-84E4-001D09F23A20.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/818/885D618A-E69B-E111-BBE8-001D09F25041.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/822/1CD1CEAC-EF9B-E111-A2EE-001D09F295A1.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/828/54B2DAB7-009C-E111-B06E-001D09F297EF.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/829/3AE91D27-049C-E111-A34A-BCAEC518FF8E.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/830/BA69838D-059C-E111-8DE1-003048D2BC30.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/833/FA7089D8-1C9C-E111-997A-BCAEC518FF68.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/834/6A191E05-5C9C-E111-8744-5404A63886A8.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/835/12C53245-4F9C-E111-B615-001D09F24FBA.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/836/54FABAD3-3E9C-E111-A345-003048D3C90E.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/840/E649764D-1E9C-E111-9253-E0CB4E55365C.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/842/C87C205C-1E9C-E111-9432-003048F117B4.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/844/FCB8716B-2F9C-E111-89D9-001D09F29533.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/849/7280AB7C-389C-E111-9C1E-001D09F292D1.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/852/3CFE30BF-379C-E111-8137-BCAEC518FF74.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/865/921A2468-429C-E111-8DA1-001D09F24682.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/870/8AF32BF0-459C-E111-B266-003048D2BC38.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/871/2850CFD1-489C-E111-AC3F-001D09F23174.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/875/64D47F8D-499C-E111-9770-BCAEC5329720.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/877/A43E0CCB-4D9C-E111-A0F9-003048D2BBF0.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/878/2E488939-B09C-E111-981E-003048D3C932.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/895/72117614-639C-E111-ACC0-001D09F27003.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/898/DAD6360A-F29C-E111-AF73-001D09F24D4E.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/913/7A865EF6-D49C-E111-8FBB-BCAEC518FF68.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/917/6AA85087-C29C-E111-ACE0-485B3962633D.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/919/18B22649-DC9C-E111-97E9-001D09F253D4.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/922/1C387506-D39C-E111-92B7-BCAEC5364CED.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/925/00F7F7AD-DD9C-E111-917E-001D09F2305C.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/928/1E78EB20-009D-E111-BAEE-001D09F253C0.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/928/6E97B96A-E79C-E111-B332-00215AEDFCCC.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/935/704D21FC-9A9C-E111-B38B-E0CB4E553651.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/938/CEE25F88-AF9C-E111-BB98-00237DDBE49C.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/942/3AAB807C-B59D-E111-82A1-003048D37666.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/944/68B323B8-B59C-E111-A0A4-0025B32034EA.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/948/58C3DFFE-B79C-E111-96D7-0025901D5C86.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/950/640933D7-D59C-E111-B8B1-BCAEC53296F4.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/955/26B43B74-D79C-E111-8645-5404A63886B2.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/958/C8AEDD3D-E39C-E111-A541-001D09F24682.root',
    '/store/data/Run2012B/MuHad/AOD/PromptReco-v1/000/193/959/54CF3DF9-E39C-E111-9E52-BCAEC5329720.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200),
    skipEvents = cms.untracked.uint32(1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Trigger.root')
                                   )

process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

## dummy output module
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Summer12.root')
)

#------------------------------------------------------------------------------
# Import modules for preselection (trigger, vertex selection, event cleaning)
#------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------------------
# Import modules and sequences for selection of objects and events
#------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#------------------------------------------------------------------------------
# Import and configure modules for trigger study 
#------------------------------------------------------------------------------

# import and configure trigger layer 1 modules
#------------------------------------------------------------------------------
process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")

# example given at http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/npietsch/SUSYAnalysis/Configuration/Run2011/Trigger_cfg.py?hideattic=0&revision=1.3&view=markup








# define a trigger matcher
#from PhysicsTools.PatAlgos.triggerLayer1.triggerMatcher_cfi import cleanMuonTriggerMatchHLTMu20
#process.myMatcher = cleanMuonTriggerMatchHLTMu20.clone()
# load the PAT trigger Python tools
from PhysicsTools.PatAlgos.tools.trigTools import *
# switch on the trigger matching
#switchOnTriggerMatching( process, myMatcher)

#process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )
### change triggerProcessName, e.g. to HLT or REDIGIXXXX
#process.patTrigger.processName      = triggerProcessName
#process.patTriggerEvent.processName = triggerProcessName
### inpu tag for selectedPatMuons/Electrons
#if(leptonTypeId == 11):
    #selectedPatLeptons = "selectedPatElectrons"
#elif(leptonTypeId == 13):
    #selectedPatLeptons = "selectedPatMuons" 

#switchOnTrigger( process )
process.patTriggerSequence = cms.Sequence(process.patTrigger)
#switchOnTrigger( process, HLT, patTrigger, patTriggerEvent, patDefaultSequence, out )

## ---
## PAT trigger matching
## --
process.muonTriggerMatchHLTMuons = cms.EDProducer(
  "PATTriggerMatcherDRLessByR"
  #"PATTriggerMatcherDRDPtLessByR"
#, src     = cms.InputTag( 'patMuons' )
, src     = cms.InputTag( 'cleanPatMuons' )
, matched = cms.InputTag( 'patTrigger' )
  # selections of trigger objects
#, matchedCuts = cms.string( 'type( "TriggerMuon" ) && path( "HLT_IsoMu24_eta2p1_v*" )' )
#, matchedCuts = cms.string( 'type( "TriggerMuon" ) && path( "HLT_Mu*" )' )
, matchedCuts = cms.string('path("*")')
, maxDeltaR   = cms.double( 0.5 )
#, maxDPtRel   = cms.double( 0.5 )
, resolveAmbiguities    = cms.bool( True )
, resolveByMatchQuality = cms.bool( True )
)

process.electronTriggerMatchHLTElectrons = process.muonTriggerMatchHLTMuons.clone()
#process.electronTriggerMatchHLTElectrons.src = 'patElectrons'
process.electronTriggerMatchHLTElectrons.src = 'cleanPatElectrons'
#process.electronTriggerMatchHLTElectrons.matchedCuts = 'type( "TriggerElectron" ) && path( "HLT_Ele*" )'

process.muonTriggerMatchHLTMuonsEmbedder = cms.EDProducer(
  "PATTriggerMatchMuonEmbedder",
  src = cms.InputTag("cleanPatMuons"),
  matches = cms.VInputTag("muonTriggerMatchHLTMuons")
)

process.electronTriggerMatchHLTElectronsEmbedder = cms.EDProducer(
  "PATTriggerMatchElectronEmbedder",
  src = cms.InputTag("cleanPatElectrons"),
  matches = cms.VInputTag("electronTriggerMatchHLTElectrons")
)


# import and configure test analyzer
#------------------------------------------------------------------------------
from SUSYAnalysis.SUSYAnalyzer.TreeWriter_cfi import *

# clone analyzer module named testAnalysis
process.muTriggerStudy = writeTrees.clone()

process.muTriggerStudy.jets      = "goodJets"
#process.muTriggerStudy.muons     = "goodMuons"
#process.muTriggerStudy.muons     = "patMuons"
process.muTriggerStudy.muons     = "cleanPatMuons"
process.muTriggerStudy.electrons = "goodElectrons"

process.elTriggerStudy  = process.muTriggerStudy.clone()
process.hadTriggerStudy = process.muTriggerStudy.clone()






#process.selectedPatMuonsTriggerMatch = cms.EDProducer(
#"PATTriggerMatchElectronEmbedder",
      #src     = cms.InputTag( "selectedPatElectrons" ),
      #matches = cms.VInputTag( "muonTriggerMatchHLTMuons" )
      #)

#process.triggerFireElectrons = selectedPatElectrons.clone(
            #src = 'selectedPatMuonsTriggerMatch',
            #cut = 'triggerObjectMatches.size > 0'       
            #)
       


#------------------------------------------------------------------------------
# From PhysicsTools/Configuration/test/SUSY_pattuple_cfg.py
#------------------------------------------------------------------------------

## NP: Disregard this for the moment

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')

#  for SusyPAT configuration
options.register('GlobalTag', "START53_V7F::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
#options.jetCorrections.append('L2L3Residual')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
options.register('hltSelection', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")


#-- Calibration tag -----------------------------------------------------------
if options.GlobalTag:
    process.GlobalTag.globaltag = options.GlobalTag

#-- import SUSY PAT sequence --------------------------------------------------
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands

addDefaultSUSYPAT(process,options.mcInfo,options.hltName,options.jetCorrections,options.mcVersion,options.jetTypes,options.doValidation,options.doExtensiveMatching,options.doSusyTopProjection)


#------------------------------------------------------------------------------
# Type-1 MET corrections
#------------------------------------------------------------------------------

process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
## if isMC:
##   process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3"
##   process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_mc
## else:
process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3Residual"
process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_data

process.patPFMETs = process.patMETs.clone(
             metSource = cms.InputTag('pfMet'),
             addMuonCorrections = cms.bool(False),
             #genMETSource = cms.InputTag('genMetTrue'),
             #addGenMET = cms.bool(True)
             )
process.pfType1CorrectedMet.applyType0Corrections = cms.bool(False)
process.pfType1CorrectedMet.srcType1Corrections = cms.VInputTag(
    cms.InputTag('pfJetMETcorr', 'type1'),
    cms.InputTag('pfMEtSysShiftCorr')
)
process.patPFMETsTypeIcorrected = process.patPFMETs.clone(
             metSource = cms.InputTag('pfType1CorrectedMet'),
             )

## process.p += process.pfMEtSysShiftCorrSequence
## process.p += process.producePFMETCorrections
## process.p += process.patPFMETsTypeIcorrected

from RecoJets.JetProducers.kt4PFJets_cfi import *
process.kt6PFJetsForIsolation2011 = kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True )
process.kt6PFJetsForIsolation2011.Rho_EtaMax = cms.double(2.5)


switchOnTrigger( process )
switchOnTriggerMatching( process, triggerMatchers = [ 'muonTriggerMatchHLTMuons' , 'electronTriggerMatchHLTElectrons' ] )
process.patTriggerEvent.patTriggerMatches = [ "muonTriggerMatchHLTMuons" , "electronTriggerMatchHLTElectrons" ]


#------------------------------------------------------------------------------
# Execution path
#------------------------------------------------------------------------------
# write ntuple (tree) for muon trigger study
process.p = cms.Path(# execute producer modules
                     process.susyPatDefaultSequence *
                     process.pfMEtSysShiftCorrSequence *
                     process.producePFMETCorrections *
                     process.patPFMETsTypeIcorrected *
                     process.kt6PFJetsForIsolation2011 *
                     
                     process.createObjects *
                     # execute analyzer and filter modules
                     process.preselection *
                     process.twoGoodMuons *
                     process.muTriggerStudy
                     )

# write ntuple (tree) for electron trigger study
process.p2 = cms.Path(# execute producer modules
                     process.susyPatDefaultSequence *
                     process.pfMEtSysShiftCorrSequence *
                     process.producePFMETCorrections *
                     process.patPFMETsTypeIcorrected *
                     process.kt6PFJetsForIsolation2011 *
                     
                     process.createObjects *
                     #execute analyzer and filter modules
                     process.preselection *
                     process.twoGoodElectrons *
                     process.elTriggerStudy
                     )

# write ntuple (tree) for hadron trigger study
process.p3 = cms.Path(# execute producer modules
                     process.susyPatDefaultSequence *
                     process.pfMEtSysShiftCorrSequence *
                     process.producePFMETCorrections *
                     process.patPFMETsTypeIcorrected *
                     process.kt6PFJetsForIsolation2011 *
                     
                     process.createObjects *
                     # execute analyzer and filter modules
                     process.preselection *
                     process.patTriggerSequence *
                     process.muonTriggerMatchHLTMuons *
                     process.muonTriggerMatchHLTMuonsEmbedder *
                     process.electronTriggerMatchHLTElectrons *
                     process.electronTriggerMatchHLTElectronsEmbedder *
                     #process.threeGoodJets *
                     process.hadTriggerStudy##  *
                     #process.muonTriggerMatchHLTMuons
##                      process.selectedTriggers
)


                              
                              
#from PhysicsTools.PatAlgos.tools.trigTools import *
#switchOnTrigger( process )
#switchOnTrigger( process )
#switchOnTriggerMatching( process, triggerMatchers = [ 'muonTriggerMatchHLTMuons' , 'electronTriggerMatchHLTElectrons' ] )
#process.patTriggerEvent.patTriggerMatches = [ "muonTriggerMatchHLTMuons" ]
#removeCleaningFromTriggerMatching( process )







