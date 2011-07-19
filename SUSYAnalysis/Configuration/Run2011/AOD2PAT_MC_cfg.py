import FWCore.ParameterSet.Config as cms

process = cms.Process("MakePATTuple")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'/store/mc/Summer11/QCD_Pt-20_MuEnrichedPt-10_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/769EC1F5-1B81-E011-988E-002481E14F38.root'
    #'/store/mc/Spring11/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/AODSIM/PU_S1_START311_V1G1-v1/0008/9C7D9D09-4351-E011-9F8F-0015178C49A4.root'
    '/store/mc/Summer11/QCD_Pt-15to3000_TuneZ2_Flat_7TeV_pythia6/AODSIM/PU_S3_START42_V11-v2/0004/8C149DD9-8C7E-E011-B3C0-001A92811706.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000),
    skipEvents = cms.untracked.uint32(1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START42_V11::All')

#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## load standard pat sequence
process.load("PhysicsTools.PatAlgos.patSequences_cff")

## dummy output module
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Summer11.root')
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
                 jetCorrLabel = ('AK5JPT', ['L1FastJet', 'L2Relative','L3Absolute']),
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
                 jetCorrLabel = ('AK5PF', ['L1FastJet', 'L2Relative','L3Absolute']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True
                )

## add L1 offset corrections to Calo Jets
process.patJetCorrFactors.levels=['L1FastJet', 'L2Relative','L3Absolute'']

## fix bug in patDefaultSequence
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.kt6PFJets.doRhoFastjet = True

## only for CMSSW_4_1_4
process.kt6PFJets.Rho_EtaMax = cms.double(3.0)

process.patDefaultSequence.replace(process.patJetCorrFactors,
                                   process.kt6PFJets + process.patJetCorrFactors)

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

# Turn off photon-electron cleaning (i.e., flag only)
process.cleanPatPhotons.checkOverlaps.electrons.requireNoOverlaps = False

# Embed tracks, since we drop them
process.patElectrons.embedTrack = True
process.patMuons.embedTrack   = True

## add electron identification
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
process.patDefaultSequence.replace(process.patElectrons,process.simpleEleIdSequence+process.patElectrons)

## runOnMC = True
## from PhysicsTools.PatAlgos.tools.pfTools import *
## postfix = "PFlow"
## jetAlgo="AK5"
## usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=runOnMC, postfix=postfix) 

#----------------------------------------------
# cmsPath
#----------------------------------------------

process.PATTuple = cms.Path(#process.preselectionMC2PAT *
                            process.patDefaultSequence
                            #getattr(process,"patPF2PATSequence"+postfix)
                            )

#------------------------------------------------
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
from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patEventContentNoCleaning
process.out.outputCommands += patExtraAodEventContent
process.out.outputCommands += cms.untracked.vstring('keep *_addPileupInfo_*_*')
#from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
#process.out.outputCommands += SUSYEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent

process.outpath = cms.EndPath(process.out)

