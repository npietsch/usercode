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
    #'/store/mc/Fall10/LM3_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/0224B8CD-D5D3-DF11-BC57-0019BBEB54B2.root',
    '/store/mc/Spring11/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/AODSIM/PU_S1_START311_V1G1-v1/0009/84209FB0-4B51-E011-8538-001D0967C035.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    skipEvents = cms.untracked.uint32(1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

## process.TFileService = cms.Service("TFileService",
##                                    fileName = cms.string('Bjets.root')
##                                    )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('START38_V7::All')
process.GlobalTag.globaltag = cms.string('START311_V2A::All')




#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## std sequence for pat
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput

## dummy output module
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Spring11.root')
)

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
#removeMCMatching(process, ['All'])

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

process.patElectrons.electronIDSources = cms.PSet(
    eidTight = cms.InputTag("eidTight"),
    eidLoose = cms.InputTag("eidLoose"),
    eidRobustTight = cms.InputTag("eidRobustTight"),
    eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
    eidRobustLoose = cms.InputTag("eidRobustLoose"),
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
    simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"))
process.patDefaultSequence.replace(process.patElectrons,process.simpleEleIdSequence+process.patElectronIsolation+process.patElectrons)

## # Trigger + Noise cleaning sequence
## process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

## high level trigger filter (non existing Triggers are ignored)
process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
process.filterHlt = process.hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X' ,HLTPaths = [
    #2010 trigger ('v*' to be immune to version changes)
    'HLT_Mu15_v*',
    #2011 1E33 trigger ('v*' to be immune to version changes)
    'HLT_Mu17_TriCentralJet30_v*', 'HLT_Mu17_CentralJet30_v*', 'HLT_Mu17_DiCentralJet30_v*',
    #2011 1E33-2E33 trigger ('v*' to be immune to version changes)
    'HLT_IsoMu17_DiCentralJet30_v*', 'HLT_IsoMu17_CentralJet30_v*',
    'HLT_Mu17_CentralJet40_BTagIP_v*', 'HLT_IsoMu17_CentralJet40_BTagIP_v*',
    #2011 HT trigger requested by Niklas ('v*' to be immune to version changes)
    'HLT_Mu8_HT200_v*'],throw = False)

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-------------------------------------------------
# cmsPath
#----------------------------------------------

process.PATTuple = cms.Path(process.patDefaultSequence *
                            process.preselectionMC2PAT
                            )

#-------------------------------------------------
# Optional: write patTuple
goodJets.checkOverlaps.muons.src = "goodMuons"
goodJets.checkOverlaps.muons.deltaR = 0.3
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
                               fileName = cms.untracked.string('Spring11.root')
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
 
