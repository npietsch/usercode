# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms

process = cms.Process("Synch")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:ECDEFDB7-AAE1-E111-B576-003048C68A88.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    skipEvents = cms.untracked.uint32(1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Synch.root')
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


# import and configure analyzer
#------------------------------------------------------------------------------
from SUSYAnalysis.SUSYAnalyzer.RA4MuonAnalyzer_cfi import *

process.analyzeRA4VetoTrackerMuons       = analyzeRA4Muons.clone()
process.analyzeRA4VetoTrackerMuons.muons = "vetoTrackerMuons"

process.analyzeRA4VetoGlobalMuons       = analyzeRA4Muons.clone()
process.analyzeRA4VetoGlobalMuons.muons = "vetoGlobalMuons"

process.analyzeRA4VetoGlobalTrackerMuons       = analyzeRA4Muons.clone()
process.analyzeRA4VetoGlobalTrackerMuons.muons = "vetoGlobalTrackerMuons"

process.analyzeRA4VetoMuons       = analyzeRA4Muons.clone()
process.analyzeRA4VetoMuons.muons = "vetoMuons"

process.analyzeRA4GoodMuons       = analyzeRA4Muons.clone()
process.analyzeRA4GoodMuons.muons = "goodMuons"

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
    cms.InputTag('pfJetMETcorr', 'type1') ,
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

#------------------------------------------------------------------------------
# Execution path
#------------------------------------------------------------------------------

process.PATTuple = cms.Path(# execute producer modules
                            process.susyPatDefaultSequence *
                            process.pfMEtSysShiftCorrSequence *
                            process.producePFMETCorrections *
                            process.patPFMETsTypeIcorrected *
                            process.kt6PFJetsForIsolation2011 *
                            process.preselection
                            )



## process.p1 = cms.Path(# execute producer modules
##                       process.susyPatDefaultSequence *
##                       process.pfMEtSysShiftCorrSequence *
##                       process.producePFMETCorrections *
##                       process.patPFMETsTypeIcorrected *
##                       process.kt6PFJetsForIsolation2011 *
                      
##                       process.preselection *
                      
##                       process.createObjects *
##                       # execute analyzer and filter modules
##                       process.oneGoodJet *
##                       process.twoGoodJets *
##                       process.threeGoodJets *
##                       process.jetSelection *
##                       process.muonSelection *
##                       process.HTSelection *
##                       process.metSelection
##                       )

## process.p2 = cms.Path(#execute producer modules
##                       process.susyPatDefaultSequence *

##                       process.pfMEtSysShiftCorrSequence *
##                       process.producePFMETCorrections *
##                       process.patPFMETsTypeIcorrected *
##                       process.kt6PFJetsForIsolation2011 *
                      
##                       process.preselection *
                      
##                       process.createObjects *
##                       # execute analyzer and filter modules
##                       process.exactlyOneGoodMuon *
##                       process.noGoodElectron *
##                       process.analyzeRA4VetoGlobalMuons *
##                       process.analyzeRA4VetoTrackerMuons *
##                       process.analyzeRA4VetoMuons *
##                       process.analyzeRA4GoodMuons *
##                       process.analyzeRA4VetoGlobalTrackerMuons *
##                       process.exactlyOneVetoMuon *
##                       process.exactlyOneVetoLepton
##                       #process.muonSelection 
##                       )

## process.p3 = cms.Path(# execute producer modules
##                       process.susyPatDefaultSequence *
                      
##                       process.pfMEtSysShiftCorrSequence *
##                       process.producePFMETCorrections *
##                       process.patPFMETsTypeIcorrected *
##                       process.kt6PFJetsForIsolation2011 *
                      
##                       process.preselection *
                      
##                       process.createObjects *
##                       # execute analyzer and filter modules
##                       process.electronSelection 
##                       )


#------------------------------------------------------------------------------
# Output module configuration
#------------------------------------------------------------------------------

process.PATTuple = cms.Path(process.susyPatDefaultSequence)

process.EventSelection = cms.PSet(
    SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('PATTuple'
                               )
    )
    )

process.out = cms.OutputModule("PoolOutputModule",
                               process.EventSelection,
                               outputCommands = cms.untracked.vstring('drop *'),
                               dropMetaData = cms.untracked.string('DROPPED'),
                               fileName = cms.untracked.string('SUSYPAT.root')
                               )

# Specify what to keep in the event content

from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patEventContentNoCleaning
process.out.outputCommands += patExtraAodEventContent

from SUSYAnalysis.SUSYEventProducers.RA4bEventContent_cff import *
process.out.outputCommands += RA4bEventContent

process.outpath = cms.EndPath(process.out)
