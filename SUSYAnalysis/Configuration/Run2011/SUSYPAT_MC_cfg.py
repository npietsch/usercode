#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 42X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV10
#

# Starting with a skeleton process which gets imported with the following line
from PhysicsTools.PatAlgos.patTemplate_cfg import *

#-- Meta data to be logged in DBS ---------------------------------------------
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.8 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/UserCode/npietsch/SUSYAnalysis/Configuration/Run2011/SUSYPAT_MC_cfg.py,v $'),
    annotation = cms.untracked.string('SUSY pattuple definition')
)

#-- Message Logger ------------------------------------------------------------
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(
    limit = cms.untracked.int32(1000
                                ),
    reportEvery = cms.untracked.int32(1)
    )
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/02719D6B-1398-E011-AA71-001A92971B94.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/02C07708-9898-E011-BC86-001A92971B0C.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/02C63308-8198-E011-8B1A-002618943896.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0412B109-8298-E011-A01C-00304867C0FC.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/06167CD9-7798-E011-809D-0018F3D0967A.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/06790363-7C98-E011-B101-0018F3D0968C.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0699073A-7C98-E011-848B-001A92971B94.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/069E0A93-F897-E011-9B35-0026189438AD.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/06EC73E8-0E98-E011-9FA6-001A928116FA.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/06EE00FF-9F98-E011-9A0E-0018F3D0967E.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/085D13DC-F997-E011-99F1-001A92971B9C.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/089A3147-ED97-E011-968C-0026189438B3.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0C67147F-FC97-E011-8542-001A928116E0.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0E3B5039-FE97-E011-BBF5-001A92810A9E.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0E590A33-7798-E011-894D-002354EF3BE1.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/10C8D92D-7898-E011-ABC7-0018F3D096AA.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/10F9FA3E-E397-E011-8DC1-003048678D6C.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/12015E8E-9998-E011-9793-00261894393A.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1204EE92-F397-E011-99E8-003048679012.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/123FFA56-9298-E011-9BBE-002618943856.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/12C7067C-F297-E011-91BA-0026189438AF.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/149F27A2-EF97-E011-AEFF-00261894387E.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/14CECE0B-EC97-E011-B70B-003048D15D04.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/14D9985C-7A98-E011-9E67-00261894396F.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/16B57224-0598-E011-A5E9-001A928116FA.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/18202867-1D98-E011-A384-0018F3D09600.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/185BEA84-9D98-E011-A238-001A92810AA8.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/18F1D3EA-E597-E011-8452-00304867BFBC.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1A854B2C-FB97-E011-B016-001A92971ACC.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1CEFFC2B-A198-E011-A820-0018F3D096AE.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1E31B084-E897-E011-97CF-003048D15E24.root',
    '/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/1EE75BD6-7A98-E011-8584-001A92810AD2.root'
    )
)

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
options.maxEvents = 1000

#  for SusyPAT configuration
options.register('GlobalTag', 'START42_V13::All', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
options.register('hltSelection', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
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

#-- HLT selection ------------------------------------------------------------
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
if options.hltSelection:
    process.hltFilter = hlt.hltHighLevel.clone(
        HLTPaths = cms.vstring(options.hltSelection),
        TriggerResultsTag = cms.InputTag("TriggerResults","",options.hltName),
        throw = False
    )
    process.susyPatDefaultSequence.replace(process.eventCountProducer, process.eventCountProducer * process.hltFilter)

## Note: L1FastJet propagation is working only with reco jets and can therefore not be applied here 
process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3')

process.p = cms.Path( process.susyPatDefaultSequence )

#------------------
# Selection paths
#------------------

process.PATTuple = cms.Path(process.susyPatDefaultSequence *
                            process.preselectionMC2PAT
                            )

#-------------------------------------------------
# Create patTuple
#-------------------------------------------------

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
                               fileName = cms.untracked.string('Summer11.root')
                               )

# Specify what to keep in the event content

#from PhysicsTools.PatAlgos.patEventContent_cff import *
#process.out.outputCommands += patEventContentNoCleaning
#process.out.outputCommands += patExtraAodEventConten

from SUSYAnalysis.SUSYEventProducers.RA4bEventContent_cff import *
process.out.outputCommands += RA4bEventContent

process.outpath = cms.EndPath(process.out)
 
