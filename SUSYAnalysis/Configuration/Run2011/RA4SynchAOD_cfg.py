import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4Synch")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/data/Run2011A/MuHad/AOD/PromptReco-v4/000/166/010/9AFCBFEC-1F8D-E011-A81B-001D09F24600.root'
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

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('GR_R_42_V14::All')

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

## dummy output module
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Summer11.root')
)

#-----------------------------------------------------------------
# From PhysicsTools/Configuration/test/SUSY_pattuple_cfg.py
#-----------------------------------------------------------------

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
#options.output = "SUSYPAT.root"
options.maxEvents = 100

#  for SusyPAT configuration
options.register('GlobalTag', "GR_R_42_V14::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
#options.jetCorrections.append('L2L3Residual')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
#options.register('hltSelection', '*', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.register('hltSelection', 'HLT_Mu8_HT200_v*', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.hltSelection.append('HLT_Mu15_HT200_v*')
options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")

process.maxEvents.input = options.maxEvents
# Due to problem in production of LM samples: same event number appears multiple times
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

#-- Calibration tag -----------------------------------------------------------
if options.GlobalTag:
    process.GlobalTag.globaltag = options.GlobalTag


############################# START SUSYPAT specifics ####################################
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands
#Apply SUSYPAT
addDefaultSUSYPAT(process,options.mcInfo,options.hltName,options.jetCorrections,options.mcVersion,options.jetTypes,options.doValidation,options.doExtensiveMatching,options.doSusyTopProjection)
SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )
############################## END SUSYPAT specifics ####################################


#-- TFileService --------------------------------------------------------------
process.load ( "PhysicsTools.UtilAlgos.TFileService_cfi")
process.TFileService = cms.Service("TFileService",
  fileName = cms.string('histo.root')
)

#-- HLT selection ------------------------------------------------------------
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
if options.hltSelection:
    process.hltFilter = hlt.hltHighLevel.clone(
        HLTPaths = cms.vstring(options.hltSelection),
        TriggerResultsTag = cms.InputTag("TriggerResults","",options.hltName),
        throw = False
    )
    process.susyPatDefaultSequence.replace(process.eventCountProducer, process.eventCountProducer * process.hltFilter)

process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3')

process.p = cms.Path( process.susyPatDefaultSequence )

#-----------------------------------------------------------------
# Load modules to monitor selection steps
#-----------------------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.RA4Analyzer_cfi import *
analyzeRA4.jets = "goodJets"
analyzeRA4.muons = "vertexMuons"
analyzeRA4.electrons ="goodElectrons"

process.RA4Preselection = analyzeRA4.clone()
process.RA4OneGoodJet = analyzeRA4.clone()
process.RA4TwoGoodJets = analyzeRA4.clone()
process.RA4ThreeGoodJets = analyzeRA4.clone()
process.RA4FourGoodJets = analyzeRA4.clone()

process.load("SUSYAnalysis.SUSYAnalyzer.Out_cfi")
process.Out.jets = "goodJets"
process.Out.muons = "goodMuons"
process.Out.electrons ="goodElectrons"

#------------------
# Selection paths
#------------------

process.ViennaMuonSelection = cms.Path(process.susyPatDefaultSequence *
                                       process.preselectionMuSynchData2 *
                                       process.goodObjects *
                                       process.RA4Preselection *
                                       process.oneGoodJet *
                                       process.RA4OneGoodJet *
                                       process.twoGoodJets *
                                       process.RA4TwoGoodJets *
                                       process.threeGoodJets *
                                       process.RA4ThreeGoodJets *
                                       process.fourGoodJets *
                                       process.RA4FourGoodJets *
                                       process.oneGoodMuon *
                                       process.exactlyOneGoodMuon *
                                       process.noGoodElectron *
                                       process.oneVetoMuon *
                                       process.noVetoElectron *
                                       process.ViennaHTSelection *
                                       process.oneTightMET *
                                       process.Out
                                       )

