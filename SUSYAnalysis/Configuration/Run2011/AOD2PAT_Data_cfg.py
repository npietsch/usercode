import FWCore.ParameterSet.Config as cms

process = cms.Process("MakePATTuple")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'/store/data/Run2011A/MuHad/AOD/PromptReco-v4/000/166/530/CCA90DCA-4C92-E011-A5D3-0030487CD17C.root'
    #'/store/data/Run2011A/SingleElectron/AOD/PromptReco-v4/000/166/502/8A879F0A-1C91-E011-A640-003048F11DE2.root'
    '/store/data/Run2011A/MuHad/AOD/PromptReco-v4/000/166/010/9AFCBFEC-1F8D-E011-A81B-001D09F24600.root'
    #'/store/data/Run2011A/SingleElectron/AOD/PromptReco-v4/000/165/098/88EB5F4F-DA7F-E011-A8DC-003048F24A04.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    skipEvents = cms.untracked.uint32(1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('GR_R_43_V0::All')

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
removeMCMatching(process, ['All'])

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
                 jetCorrLabel = ('AK5JPT', ['L1FastJet', 'L2Relative','L3Absolute', 'L2L3Residual']),
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
                 jetCorrLabel = ('AK5PF', ['L1FastJet', 'L2Relative','L3Absolute', 'L2L3Residual']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True
                )

## add L1 offset corrections to Calo Jets
process.patJetCorrFactors.levels=['L1FastJet', 'L2Relative','L3Absolute', 'L2L3Residual']

## fix bug in patDefaultSequence
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.kt6PFJets.doRhoFastjet = True
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

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-------------------------------------------------
# cmsPath
#----------------------------------------------

process.PATTuple = cms.Path(process.preselectionData2PAT *
                            process.patDefaultSequence
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
from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patEventContentNoCleaning
process.out.outputCommands += patExtraAodEventContent
process.out.outputCommands += cms.untracked.vstring('keep *_addPileupInfo_*_*')
#from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
#process.out.outputCommands += SUSYEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent

process.outpath = cms.EndPath(process.out)
 
