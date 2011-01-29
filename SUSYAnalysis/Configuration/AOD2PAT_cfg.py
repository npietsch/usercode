import FWCore.ParameterSet.Config as cms

process = cms.Process("MakePATTuple")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0002/141EEE1B-90D4-DF11-8D67-003048C6B50E.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/00AD38DB-BAD4-DF11-BD52-001A644EB21C.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/1483817B-A6D4-DF11-8C18-003048C6B548.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/245D9D92-38D5-DF11-BA5B-00215E21DAF2.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/2ADA1E6A-9ED4-DF11-817C-003048C559D2.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/3A2C5144-A8D4-DF11-BB36-003048CEABE0.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/5A13A826-3AD5-DF11-B46E-00215E22200A.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/7EDA374B-AAD4-DF11-9425-00304894566E.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/805DA928-A4D4-DF11-AF15-001F29C95558.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/8AD90145-9FD4-DF11-8EA1-001A644E9962.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/8E3354A5-ACD4-DF11-A838-001F29C9650A.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/8EB5D8E8-80D4-DF11-A8ED-003048C56D1A.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/9E700298-AFD4-DF11-B7DF-003048C57484.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/B6AB1253-D7D4-DF11-B123-002618943C0A.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/C60AED24-9ED4-DF11-9217-001A644E983C.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/0A52B527-38D5-DF11-A055-00215E21D702.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/4E83A256-AAD6-DF11-93B3-00215E222382.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/72DB7D50-09D6-DF11-A593-003048C56E68.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/CEE3BC1F-00D6-DF11-A416-000AE482D11E.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/EECF6F19-FCD5-DF11-A402-001A4B0A3420.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/F4A32D4D-61D7-DF11-916D-001F29C9A554.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/F6F42B47-26D6-DF11-B107-002618943C2B.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/F85D031A-D4D6-DF11-A13E-003048C56E86.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/FE3AF903-0DD6-DF11-837D-001A644EACEE.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0007/74AB9400-D8D7-DF11-AAC9-00215E2217E2.root',\
    
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
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
#process.GlobalTag.globaltag = cms.string('START38_V7::All')
process.GlobalTag.globaltag = cms.string('GR_R_38X_V8::All')

#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## std sequence for pat
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
## removeMCMatching(process, ['All'])

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

## produce cut based electron IDs
process.load("SUSYAnalysis.SUSYAnalyzer.simpleEleIdSequence_cff")

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

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RAPreselection_cff")

# Example how to change prselection criteria:
process.scrapingVeto.thresh = 0.15 ## <-- for MC

#-------------------------------------------------
# cmsPath
#----------------------------------------------

process.PATTuple = cms.Path(process.patDefaultSequence*
                            process.preselection)

#-------------------------------------------------
# Optional: write patTuple
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
                               fileName = cms.untracked.string('PAT.root')
                               )

# Specify what to keep in the event content
from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patEventContentNoCleaning
process.out.outputCommands += patExtraAodEventContent
#from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
#process.out.outputCommands += SUSYEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent

process.outpath = cms.EndPath(process.out)
 
