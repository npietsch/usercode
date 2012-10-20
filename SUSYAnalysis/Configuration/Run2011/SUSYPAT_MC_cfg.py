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
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/00139A23-9417-E111-AB24-001EC9AA78B1.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/002FE566-7414-E111-A6F6-842B2B1811CE.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/00557A15-9214-E111-83A5-0025901AC3F0.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/005A4CEC-9314-E111-AD5F-A4BADB1C5D42.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/0078038C-BC17-E111-AE56-001EC9AAA2E7.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/00943269-7B17-E111-8E08-001EC9AA91F8.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/009C688D-B016-E111-A67C-0002C90A36B8.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/00B60D41-CF16-E111-BB5C-001EC9AAA3D7.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/00EF9363-1017-E111-A17D-001EC9AA9FE0.root',
    '/store/mc/Summer11/mSUGRA_m0-220to3000_m12-100to1000_tanb-40andA0-m500_7TeV-Pythia6Z/AODSIM/PU_START42_V11_FastSim-v2/0000/00F2F738-7A16-E111-BED8-D485644C0CF9.root'
    ##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/002FE237-B09C-E011-B7B1-0022199305B1.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/006518E6-A99C-E011-8535-E0CB4E29C51A.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0234044D-B89C-E011-93FD-E0CB4E5536BB.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/026B1823-A69C-E011-9D3F-E0CB4E1A118D.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0282098A-AF9C-E011-BDE4-90E6BA19A25A.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/02DE32D4-B79C-E011-B2E4-001A4BA9B97A.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/04388498-B99C-E011-B208-90E6BA442F1C.root',
##     '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/04412127-A89C-E011-8297-90E6BA19A22F.root'
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
options.maxEvents = 2

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
 
