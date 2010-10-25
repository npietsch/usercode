import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4Selection")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
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

#-------------------------------------------------
# create collections 
#-------------------------------------------------
      
## create genParticle collection
from SUSYAnalysis.SUSYAnalyzer.testSelector_cfi import *
process.selectedGenParticles = selectedGenParticles.clone(src= "genParticles",
                                                          cut =
                                                          'abs(pdgId)=1000021 &'
                                                          'numberOfDaughters > 0'
                                                          #'abs(daughter(0).pdgId) == 6'
                                                          )

## create jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
process.goodJets = selectedPatJets.clone(src = 'selectedPatJets',
                                     cut =
                                     'abs(eta) < 2.4 &'
                                     'pt > 30. &'
                                     'emEnergyFraction > 0.01 &'
                                     'jetID.fHPD < 0.98 &'
                                     'jetID.n90Hits > 1'
                                     )

## select events with gen Particles
from SUSYAnalysis.SUSYAnalyzer.testCountFilter_cfi import *
process.countGenParticles = countGenParticles.clone(src = 'selectedGenParticles',
                                               minNumber = 1
                                               )


#-------------------------------------------------
# module for generator studies 
#-------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYEventAnalyzer_cfi import analyzeSUSYEvent
process.analyzeSUSYEvent = analyzeSUSYEvent.clone(met = "patMETs",
                                                  source = "selectedGenParticles"
                                                  )

#-------------------------------------------------
# selection path
#-------------------------------------------------

process.Selection = cms.Path(process.patDefaultSequence *
                             process.goodJets *
                             process.selectedGenParticles *
                             process.countGenParticles *
                             process.analyzeSUSYEvent
                             )

#-------------------------------------------------
# optional: write patTuple
#-------------------------------------------------
#
#process.EventSelection = cms.PSet(
#    SelectEvents = cms.untracked.PSet(
#    SelectEvents = cms.vstring('RA4Selection')
#    )
#)
#
#process.out = cms.OutputModule("PoolOutputModule",
#    process.EventSelection,
#    outputCommands = cms.untracked.vstring('drop *'),
#    dropMetaData = cms.untracked.string('DROPPED'),
#    fileName = cms.untracked.string('PATtuple.root')
#)
#
#from PhysicsTools.PatAlgos.patEventContent_cff import *
#process.out.outputCommands += patEventContentNoCleaning
#process.out.outputCommands += patExtraAodEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent
#
#process.outpath = cms.EndPath(process.out)
