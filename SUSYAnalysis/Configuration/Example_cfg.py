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
##     '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/GEN-SIM-RECO/START38_V12-v1/0004/287CF124-2ED6-DF11-AA7D-002618943C22.root'
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/4E83A256-AAD6-DF11-93B3-00215E222382.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0002/141EEE1B-90D4-DF11-8D67-003048C6B50E.root',
    '/store/mc/Fall10/LM8_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0003/00AD38DB-BAD4-DF11-BD52-001A644EB21C.root'
##     '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/B41F22A2-00D6-DF11-A419-0019BBEBB558.root'
##    '/store/mc/Fall10/TTJets_TuneD6T_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0021/0EC47D66-39E3-DF11-AEDE-0026B958EFD4.root'
##    'file:/afs/naf.desy.de/user/n/npietsch/CMSSW_3_8_6/src/test.root'

##     '/store/mc/Summer10/TTbar/GEN-SIM-RECO/START36_V9_S09-v1/0055/36AC87AA-8C78-DF11-8C7B-0017A4770838.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
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
                                   fileName = cms.string('Example.root')
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

## use the correct jet energy corrections
process.patJetCorrFactors.corrSample = "Spring10"
process.patJetCorrFactors.sampleType = "ttbar"
#process.patJetCorrFactorsAK5PF.corrSample = "Spring10"
#process.patJetCorrFactorsAK5PF.sampleType = "ttbar"

#calculate impact parameter w.r.t beam spot (instead of primary vertex)
process.patMuons.usePV = False

## add PF MET
from PhysicsTools.PatAlgos.tools.metTools import addPfMET
addPfMET(process, 'PF')

## remove MC matching, photons, taus and cleaning from PAT default sequence
## from PhysicsTools.PatAlgos.tools.coreTools import *
## removeMCMatching(process, ['All'])
## removeSpecificPATObjects(process,
##                          ['Photons','Taus'],
##                          outputInProcess=False)
## removeCleaning(process,
##                outputInProcess=False)

## add PF jets
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                  doJTA        = True,
                  doBTagging   = True,
                  jetCorrLabel = ('AK5', 'PF'),
                  doType1MET   = False,
                  doL1Cleaning = False,
                  doL1Counters = False,
                  genJetCollection=cms.InputTag("ak5GenJets"),
                  doJetID      = True,
                  ) 

## remove TagInfos from jets
process.patJets.addTagInfos = False
process.patJetsAK5PF.addTagInfos = False

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

#------------------------------------------------
# Create Gen Events 
#------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------
# Gen Event Selection 
#------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="decayChainA()==1000021")

from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

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
#process.goodElectrons.cut = 'pt > 20. & abs(eta) < 2.4'


#------------------------------------------------
# Sequence for analysis of single objects
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.singleObjectsAnalysis_cff")

# Example how to change input tags:
# process.analyzeMuonKinematics.src = "selectedPAtMuons"

#------------------------------------------------
# Modules for analysis on generator level
#------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import analyzeSUSYGenEvt

# change input tags to analyze selected Jets and MET
process.analyzeSUSYGenEvt1 = analyzeSUSYGenEvt.clone()
process.analyzeSUSYGenEvt2 = analyzeSUSYGenEvt.clone()
process.analyzeSUSYGenEvt2.jets = "goodJets"

#-------------------------------------------------
# Load any other modules you want to use
#-------------------------------------------------

# E.g: Load module to rescale jet energy by an abitrary factor 
process.load("TopAnalysis.TopUtils.JetEnergyScale_cff")

# E.g: Load modules to reconstruct ttbar events with
#      kinematic fit and anlyze hypotheses  
process.load("TopQuarkAnalysis.TopEventProducers.producers.TtSemiLepEvtBuilder_cfi")
process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cfi")

# ...


#-------------------------------------------------
# Temp
#-------------------------------------------------

process.load("TopAnalysis.TopAnalyzer.ElectronQuality_cfi")

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")


#-------------------------------------------------
# Selection paths
#-------------------------------------------------

process.RA4MuonSelection = cms.Path(#process.printGenParticles *
                                    process.patDefaultSequence *
                                    process.SUSYInitSubset *
                                    process.makeSUSYGenEvt *
                                    #process.analyzeSUSYGenEvt1 *
                                    process.SUSYGenEventFilter *
                                    process.preselection *
                                    process.jetSelection *
                                    process.muonSelection *
                                    process.metSelection *
                                    process.singleObjectsAnalysis *
                                    process.muonVeto *
                                    process.analyzeSUSYGenEvt2
                                    ) 

process.RA4ElecSelection = cms.Path(process.patDefaultSequence *
                                    process.SUSYInitSubset *
                                    process.makeSUSYGenEvt *
                                    #process.analyzeSUSYGenEvt1 *
                                    process.SUSYGenEventFilter *
                                    process.preselection *
                                    process.jetSelection *
                                    process.electronSelection *
                                    process.metSelection *
                                    process.singleObjectsAnalysis *
                                    process.electronVeto *
                                    process.analyzeSUSYGenEvt2
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
                               #outputCommands = cms.untracked.vstring('drop *'),
                               #dropMetaData = cms.untracked.string('DROPPED'),
                               fileName = cms.untracked.string('PATtuple.root')
                               )

## # Specify what to keep in the event content
## from PhysicsTools.PatAlgos.patEventContent_cff import *
## process.out.outputCommands += patEventContentNoCleaning
## process.out.outputCommands += patExtraAodEventContent
## from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
## process.out.outputCommands += SUSYEventContent
## #from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
## #process.out.outputCommands += tqafEventContent

process.outpath = cms.EndPath(process.out)
 
