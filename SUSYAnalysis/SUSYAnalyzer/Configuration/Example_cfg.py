import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
##     '/store/mc/Summer10/TTbar/GEN-SIM-RECO/START36_V9_S09-v1/0055/36AC87AA-8C78-DF11-8C7B-0017A4770838.root'
    '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('RA.root')
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

#from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput
#run36xOn35xInput(process)

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
removeMCMatching(process, ['All'])
removeSpecificPATObjects(process,
                         ['Photons','Taus'],
                         outputInProcess=False)
removeCleaning(process,
               outputInProcess=False)

## add PF jets and MET
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5', 'PF'),
                 doType1MET   = False,
                 doL1Cleaning = True,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True,
                 ) 
from PhysicsTools.PatAlgos.tools.metTools import addPfMET
addPfMET(process, 'PF')

## remove TagInfos from jets
process.patJets.addTagInfos = False
process.patJetsAK5PF.addTagInfos = False

## use the correct jet energy corrections
process.patJetCorrFactors.corrSample = "Spring10"
process.patJetCorrFactors.sampleType = "ttbar"
process.patJetCorrFactorsAK5PF.corrSample = "Spring10"
process.patJetCorrFactorsAK5PF.sampleType = "ttbar"

#calculate impact parameter w.r.t beam spot (instead of primary vertex)
process.patMuons.usePV = False

process.load("TopAnalysis.TopAnalyzer.simpleEleIdSequence_cff")

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectronIsolation*process.patElectrons)

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

#------------------------------------------------
# Create Gen Events 
#------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------
# Gen Event Selection 
#------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="numberOfLeptons()=2")

##from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
## process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#------------------------------------------------
# RA4 Event Selection
#------------------------------------------------

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RA4Preselection_cff")

# Example how to change selection criteria:
# process.scrapingVeto.thresh = 15

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.RA4Selection_cff")                                                

# Example how to change selection criteria:
# process.oneGoodMuon.cut = 'minNumber = 2 &'
#                           'pt > 30 &'
#                           ... 

#------------------------------------------------
# Sequence for analysis of single objects
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.singleObjectsAnalysis_cff")

# Example how to change input tags:
# process.analyzeMuonKinematics.src = "selectedPAtMuons"

#------------------------------------------------
# Modules for analysis on generator level
#------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import analyzeSUSY

# change input tags to analyze selected Jets and MET
process.analyzeSUSY = analyzeSUSY.clone(met = "goodMETs",
                                        jets = "goodJets"
                                        )

# SUSYAnalyzer will be replaced/extended by SUSYGenEventAnalyzer soon
# from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import analyzeSUSYGenEvent

#-------------------------------------------------
# Load any other modules you want to use
#-------------------------------------------------

# E.g: Load module to rescale jet energy by an abitrary factor 
process.load("TopAnalysis.TopUtils.JetEnergyScale_cff")

# E.g: Load modules to reconstruct ttbar events with
#      kinematic fit and anlyze hypotheses  
process.load("TopQuarkAnalyis.TopEventProducers.TtSemiLepEvtBuilder")
process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cff")

# ...

#-------------------------------------------------
# Selection paths
#-------------------------------------------------

process.RA4MuonSelection = cms.Path(process.patDefaultSequence *
                                    process.makeSUSYGenEvt *
                                    process.SUSYGenEventFilter *
                                    process.preselection *
                                    process.muonSelection *
                                    process.jetSelection *
                                    process.metSelection *
                                    process.singleObjectsAnalysis *
                                    process.muonVeto
                                    ) 

process.RA4ElecSelection = cms.Path(process.patDefaultSequence *
                                    process.makeSUSYGenEvt *
                                    process.SUSYGenEventFilter *
                                    process.preselection *
                                    process.electronSelection *
                                    process.jetSelection *
                                    process.metSelection *
                                    process.singleObjectsAnalysis *
                                    process.electronVeto
                                    )

#-------------------------------------------------
# Optional: write patTuple
#-------------------------------------------------

process.EventSelection = cms.PSet(
   SelectEvents = cms.untracked.PSet(
   SelectEvents = cms.vstring('RA4MuonSelection',
                              'RA4ElecSelection'
                              )
   )
)

process.out = cms.OutputModule("PoolOutputModule",
   process.EventSelection,
   outputCommands = cms.untracked.vstring('drop *'),
   dropMetaData = cms.untracked.string('DROPPED'),
   fileName = cms.untracked.string('PATtuple.root')
)

# Specify what to keep in the event content
from PhysicsTools.PatAlgos.patEventContent_cff import *
process.out.outputCommands += patEventContentNoCleaning
process.out.outputCommands += patExtraAodEventContent
from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
process.out.outputCommands += SUSYEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent

process.outpath = cms.EndPath(process.out)
