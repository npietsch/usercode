import FWCore.ParameterSet.Config as cms

process = cms.Process("test")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:/afs/cern.ch/user/n/npietsch/public/testfile.root'
    #'/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
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
# create selectedGenParticle collection
#-------------------------------------------------
      
## create genParticle collection
from SUSYAnalysis.SUSYAnalyzer.testSelector_cfi import *
process.selectedGenParticles = selectedGenParticles.clone(src= "genParticles",
                                                          cut =
                                                          'abs(pdgId)=1000021 &'
                                                          'numberOfDaughters > 0'
                                                          #'abs(daughter(0).pdgId) == 6'
                                                          )

#-------------------------------------------------
# CountFilter
#-------------------------------------------------

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

process.Selection = cms.Path(process.selectedGenParticles *
                             process.countGenParticles *
                             process.analyzeSUSYEvent
                             )

#-------------------------------------------------
# optional: write patTuple
#-------------------------------------------------

## process.EventSelection = cms.PSet(
##    SelectEvents = cms.untracked.PSet(
##    SelectEvents = cms.vstring('Selection')
##    )
## )

## process.out = cms.OutputModule("PoolOutputModule",
##    process.EventSelection,
##    outputCommands = cms.untracked.vstring('drop *'),
##    dropMetaData = cms.untracked.string('DROPPED'),
##    fileName = cms.untracked.string('testfile.root')
## )

## from PhysicsTools.PatAlgos.patEventContent_cff import *
## process.out.outputCommands += patEventContentNoCleaning
## process.out.outputCommands += patExtraAodEventContent
## from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
## process.out.outputCommands += tqafEventContent

## process.outpath = cms.EndPath(process.out)
