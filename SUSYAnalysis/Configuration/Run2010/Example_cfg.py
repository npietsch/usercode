import FWCore.ParameterSet.Config as cms

process = cms.Process("Example")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/4E83A256-AAD6-DF11-93B3-00215E222382.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Example.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START311_V2A::All')

#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## std sequence for pat
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
## removeMCMatching(process, ['All'])

removeSpecificPATObjects(process,
                         ['Photons'],  # 'Tau' has currently been taken out due to problems with tau discriminators
                         outputInProcess=False)

removeCleaning(process,
               outputInProcess=False)

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
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

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

#-------------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
#       - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
#       - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-------------------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

## To produce the SUSYGenEvent (ttGenEvent) add "process.makeSUSYGenEvt" ("process.makeGenEvt") to the cmsPath.

#-----------------------------------------------------------------
# Importand configure modules to filter events on generator level 
#-----------------------------------------------------------------

#from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
#from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *

## These filters allow to filter events using member function of the SUSYGenEvent and ttGenEvt in the string cut parser.
## In order to the SUSYGenEventFilter (TtGenEventFilter), produce the corresponding gen event first, configure the filter and
## add "process.SUSYGenEventFilter" ("process.ttGenEventFilter") to the cmsPath.

## Example configurations
#process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay") ## <- selection of gluino-gluino events
#process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic") ## <- selection of semi-leptonic ttbar events

#-----------------------------------------------------------------
# Load modules for preselection.
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

## As the predefined preselections are cmsSequences you either have to modify them in ../Preselection_cff.py or
## configure the "sub-modules" and add them separately to the cmsPath.

## Examples how to configure the "sub modules"
#process.MUTrigger.HLTPaths = ["HLT_Mu15_v2"]
#process.primaryVertexFilter.maxAbsZ = 15 

#-------------------------------------------------------------------------------
# Load and configure modules to create objects and filter events on reco level
#-------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

## Example how to change the object definition
process.tightJets.cut = 'abs(eta) < 2.4 & pt > 100. &emEnergyFraction > 0.01 &jetID.fHPD < 0.98 &jetID.n90Hits > 1'
process.goodMETs.cut  = 'et > 150' 

## Example how to use the PAT count filter
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
process.twoTightJets = countPatJets.clone(src = 'tightJets',
                                          minNumber = 2
                                          )

## Example how to configure an evetn filter
process.filterHT.jets = "tightJets"
process.filterHT.Cut = 800

## Examples how to configure DiLepton filters
process.ZVetoMu.isVeto = False ## <- Events containing a muon pair with an inv. mass within the Z mass window will be selected, not vetoed
process.ZVetoMu.filterCharge = -1 ## <- Only events containing an os muon pair will be selected
process.ZVetoMu.isVeto.Cut = 70,120 ## <- define Z mass window

# Same example for electrons
#process.ZVetoEl.isVeto = False
#process.ZVetoEl.filterCharge = -1
#process.ZVetoMu.isVeto.Cut = 70,120

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

## As the predefined analysis modules are cmsSequences you either have to modify them in ../SUSYBjetsAnalysis_cff.py or
## configure the "sub-modules" and add them separately to the cmsPath.

## Example configurations
process.analyzeSUSY.jets = "tightJets"

#--------------------------------------------------------
# Load and configure other modules you want to use
#--------------------------------------------------------

## E.g: Load module to rescale jet energy by an abitrary factor 
#process.load("TopAnalysis.TopUtils.JetEnergyScale_cff")

## E.g: Load modules to reconstruct ttbar events with kinematic fit and anlyze hypotheses  
#process.load("TopQuarkAnalysis.TopEventProducers.producers.TtSemiLepEvtBuilder_cfi")
#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cfi")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-------------------------------------------------
# Selection paths
#-------------------------------------------------

process.p = cms.Path(process.patDefaultSequence *
                     process.makeSUSYGenEvt *
                     #process.SUSYGenEventFilter *
                     #process.makeGenEvt *
                     #process.ttGenEventFilter
                     #process.preselection *
                     process.ZVetoMu *
                     process.tightJets *
                     process.twoTightJets *
                     process.goodMETs *
                     process.oneGoodMET *
                     process.metSelection *
                     process.analyzeSUSYGenEvt *
                     process.analyzeSUSY *
                     process.analyzeBjets *
                     process.analyzeBTags
                     ) 

#-------------------------------------------------
# Optional: write patTuple
#-------------------------------------------------

## process.EventSelection = cms.PSet(
##     SelectEvents = cms.untracked.PSet(
##     SelectEvents = cms.vstring('p'
##                                )
##     )
##     )

## process.out = cms.OutputModule("PoolOutputModule",
##                                process.EventSelection,
                               #outputCommands = cms.untracked.vstring('drop *'),
                               #dropMetaData = cms.untracked.string('DROPPED'),
##                                fileName = cms.untracked.string('PATtuple.root')
##                                )

## # Specify what to keep in the event content
## from PhysicsTools.PatAlgos.patEventContent_cff import *
## process.out.outputCommands += patEventContentNoCleaning
## process.out.outputCommands += patExtraAodEventContent
## from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
## process.out.outputCommands += SUSYEventContent
## #from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
## #process.out.outputCommands += tqafEventContent

## process.outpath = cms.EndPath(process.out)
 
