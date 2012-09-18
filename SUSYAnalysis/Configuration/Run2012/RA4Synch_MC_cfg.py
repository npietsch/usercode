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
    '/store/mc/Summer12_DR53X/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/0000/ECDEFDB7-AAE1-E111-B576-003048C68A88.root'  
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
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


# import and configure test analyzer
#------------------------------------------------------------------------------
from SUSYAnalysis.SUSYAnalyzer.TestAnalyzer_cfi import *

# clone analyzer module named testAnalysis
process.test = testAnalysis.clone()

# configure module test, e.g.
process.test.jets = "goodJets"

#------------------------------------------------------------------------------
# From PhysicsTools/Configuration/test/SUSY_pattuple_cfg.py
#------------------------------------------------------------------------------

## NP: Disregard this for the moment

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')

#  for SusyPAT configuration
options.register('GlobalTag', "START53_V7A::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
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
process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3"
process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_mc
## else:
## process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3Residual"
## process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_data

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


#------------------------------------------------------------------------------
# Execution path
#------------------------------------------------------------------------------

process.p = cms.Path(# execute producer modules
                     process.susyPatDefaultSequence *

                     process.pfMEtSysShiftCorrSequence *
                     process.producePFMETCorrections *
                     process.patPFMETsTypeIcorrected *
                     
                     process.createObjects *
                     # execute analyzer and filter modules
                     process.preselection *
                     process.test *
                     process.muonSelection *
                     process.jetSelection *
                     process.HTSelection *
                     process.metSelection
                     )
