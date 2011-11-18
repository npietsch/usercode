import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4Synch")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/002FE237-B09C-E011-B7B1-0022199305B1.root',
    '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/006518E6-A99C-E011-8535-E0CB4E29C51A.root',
    '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0234044D-B89C-E011-93FD-E0CB4E5536BB.root',
    '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/026B1823-A69C-E011-9D3F-E0CB4E1A118D.root',
    '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0282098A-AF9C-E011-BDE4-90E6BA19A25A.root',
    '/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/02DE32D4-B79C-E011-B2E4-001A4BA9B97A.root',
'/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/04388498-B99C-E011-B208-90E6BA442F1C.root',
'/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/04412127-A89C-E011-8297-90E6BA19A22F.root'
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_9_1_etL.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_99_1_xJ5.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_98_1_t7j.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_97_1_ziv.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_96_1_qKp.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_95_1_x3I.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_94_1_UxC.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_93_1_L0X.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_92_1_91X.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_91_1_2Ee.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_90_1_bWe.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_8_1_fv3.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_89_1_J6z.root',
##     '/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/SUSYPAT/1bd78d5132693ded1fbe0b8a82b5b12c/Summer11_88_1_fq3.root'
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
#process.GlobalTag.globaltag = cms.string('START42_V13::All')

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
options.maxEvents = -1

#  for SusyPAT configuration
options.register('GlobalTag', "START42_V13::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
#options.jetCorrections.append('L2L3Residual')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
#options.register('hltSelection', '*', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.register('hltSelection', 'HLT_Mu8_v1', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
#options.hltSelection.append('HLT_Mu8_HT200_v*')
#options.hltSelection.append('HLT_Mu15_HT200_v*')
#options.hltSelection.append('HLT_HT250_Mu15_PFMHT20_v*')
#options.hltSelection.append('HLT_HT250_Mu15_PFMHT40_v*')
#options.hltSelection.append('HLT_HT300_Mu15_PFMHT40_v*')
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
analyzeRA4.muons = "goodMuons"
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
                                       process.preselectionMuSynchMC *
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
                                       process.muonSelection *
                                       process.HTSelection *
                                       process.oneMediumMET *
                                       process.Out
                                       )

