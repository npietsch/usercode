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
    input = cms.untracked.int32(100),
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

#----------------------------------------------------------------------------
# pat configuration
#----------------------------------------------------------------------------

## std sequence for pat
process.load("PhysicsTools.PatAlgos.patSequences_cff")

## dummy output module
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Spring11.root')
)

## remove cleaning as it is not used
#from PhysicsTools.PatAlgos.tools.coreTools import *
#removeCleaning(process)

## switch off MC matching
from PhysicsTools.PatAlgos.tools.coreTools import *
#removeMCMatching(process, ['All'])

## remove tau and photon collection
#removeSpecificPATObjects(process, ['Taus', 'Photons'])

## use the correct jet energy corrections
process.patJetCorrFactors.flavorType = "T"

## calculate d0 wrt the beam spot
process.patMuons.usePV = False

## Add PfMET and TcMET to the event content
from PhysicsTools.PatAlgos.tools.metTools import *
addPfMET(process,'PF')
addTcMET(process,'JPT')
		
## add ak5JPTJets
from PhysicsTools.PatAlgos.tools.jetTools import *
addJetCollection(process,cms.InputTag('JetPlusTrackZSPCorJetAntiKt5'),'AK5', 'JPT',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5JPT', ['L1Offset', 'L2Relative','L3Absolute', 'L2L3Residual']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,                 
                 genJetCollection = None,
                 doJetID      = True
                )
		 
## Add particle flow jets
addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', ['L1Offset', 'L2Relative','L3Absolute', 'L2L3Residual']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True
                )

## add L1 offset corrections to Calo Jets
process.patJetCorrFactors.levels=['L1Offset', 'L2Relative','L3Absolute', 'L2L3Residual']

## remove L1 offset corrections
#process.patJetCorrFactors.levels.remove("L1Offset")
#process.patJetCorrFactorsAK5PF.levels.remove("L1Offset")
#process.patJetCorrFactorsAK5JPT.levels.remove("L1Offset")

## embedding of jet constituents into the jets
process.patJets.embedCaloTowers       = False
process.patJetsAK5JPT.embedCaloTowers = False
process.patJetsAK5PF.embedPFCandidates= False

## remove TagInfos from jets
process.patJets.addTagInfos       = False
process.patJetsAK5JPT.addTagInfos = False
process.patJetsAK5PF.addTagInfos  = False

## embed IsoDeposits
process.patMuons.isoDeposits = cms.PSet(
     tracker = cms.InputTag("muIsoDepositTk"),
     ecal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","ecal"),
     hcal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","hcal"),
     user    = cms.VInputTag(cms.InputTag("muIsoDepositCalByAssociatorTowers","ho"),
                             cms.InputTag("muIsoDepositJets")
                            ),
    )
    
## embedding of resolutions into the patObjects
process.load("TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_cff")
process.patJets.addResolutions = True
process.patJets.resolutions = cms.PSet(
default = cms.string("udscResolution"),
bjets = cms.string("bjetResolution"),
)
process.patJetsAK5PF.addResolutions = True
process.patJetsAK5PF.resolutions = cms.PSet(
default = cms.string("udscResolutionPF"),
bjets = cms.string("bjetResolutionPF"),
)
process.patElectrons.addResolutions = True
process.patElectrons.resolutions = cms.PSet( default = cms.string("elecResolution") )
process.patMuons.addResolutions = True
process.patMuons.resolutions = cms.PSet( default = cms.string("muonResolution") )
process.patMETs.addResolutions = True
process.patMETs.resolutions = cms.PSet( default = cms.string("metResolution") )
process.patMETsPF.addResolutions = True
process.patMETsPF.resolutions = cms.PSet( default = cms.string("metResolutionPF") )     

## add electron identification
## (needs cvs co -r V00-04-00 ElectroWeakAnalysis/WENu)
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
process.out.outputCommands += cms.untracked.vstring('keep *_addPileupInfo_*_*')
#from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
#process.out.outputCommands += SUSYEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent

process.outpath = cms.EndPath(process.out)
 
