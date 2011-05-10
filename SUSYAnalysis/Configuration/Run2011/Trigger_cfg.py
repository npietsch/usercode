import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(    
    '/store/user/cakir/MuHad/PAT_Data2011_PrompReco160404-163757_DESYv2/fde7716b94bbd42567b10bc1a2b9c4ae/Data2011_PrompReco160404-163757_100_1_zTl.root',
    '/store/user/cakir/MuHad/PAT_Data2011_PrompReco160404-163757_DESYv2/fde7716b94bbd42567b10bc1a2b9c4ae/Data2011_PrompReco160404-163757_101_1_68f.root',
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500),
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
process.GlobalTag.globaltag = cms.string('GR_R_311_V3::All')

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

from HLTrigger.HLTfilters.hltHighLevel_cfi import *


process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.25)
                                    )

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag("offlinePrimaryVertices"),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2) )

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *
process.HBHENoiseFilter = HBHENoiseFilter.clone()

process.preselection = cms.Sequence(process.primaryVertexFilter *
                                    process.HBHENoiseFilter *
                                    process.scrapingVeto
                                    )

process.MuTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_v*'],throw = False)
process.MuHadTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*'],throw = False)


#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
#process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")

#-----------------------------------------------------------------------------
# ----- C o n f i g u r e   P A T   T r i g g e r ----- #
#-----------------------------------------------------------------------------

## trigger sequences
process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )
#print triggerPathSelector
## define HLT_Mu9 (or other trigger path) matches
process.muonTriggerMatchHLTMuons = cms.EDProducer( "PATTriggerMatcherDRLessByR",
    src     = cms.InputTag( "goodMuons" ),
    matched = cms.InputTag( "patTrigger" ),
    andOr          = cms.bool( False ),
    filterIdsEnum  = cms.vstring( 'TriggerMuon' ),
    filterIds      = cms.vint32 ( 0 ),
    filterLabels   = cms.vstring( '*' ),
    #pathNames      = cms.vstring( triggerPathSelector ),
    matchedCuts = cms.string( 'path( "HLT_Mu8_v*"  )' ),#"HLT_Mu9""HLT_Mu5_HT200_v3"
    #collectionTags = cms.vstring( '*' ),
    maxDPtRel = cms.double( 0.2 ),  #originally: 0.5
    maxDeltaR = cms.double( 0.2 ),  #originally: 0.5
    resolveAmbiguities    = cms.bool( True ),
    resolveByMatchQuality = cms.bool( True )
)

## take obsolete matches out of the patTriggerMatcher sequence
## and add the match that is relevant for this analysis
###process.triggerMatchingDefaultSequence+= process.muonTriggerMatchHLTMuons
#process.patTriggerMatcher += process.muonTriggerMatchHLTMuons
#process.patTriggerMatcher.remove( process.patTriggerMatcherElectron )

#process.patTriggerMatcher.remove( process.patTriggerMatcherMuon )
#process.patTriggerMatcher.remove( process.patTriggerMatcherTau )

## configure patTrigger & patTriggerEvent
#process.patTrigger.onlyStandAlone = False
process.patTriggerEvent.patTriggerMatches = [ "muonTriggerMatchHLTMuons" ]

##-----NP: Just for embedding the trigger match info 

## Trigger match embedding in selectedPatMuons. In the following selectedPatMuonsTriggerMatch
## must be used to make use of the embedded match
## works with CMSSW_3_8_4, might need change for 3_8_7
process.goodMuonsTriggerMatch = cms.EDProducer( "PATTriggerMatchMuonEmbedder",
   src     = cms.InputTag( "goodMuons" ),
   matches = cms.VInputTag( "muonTriggerMatchHLTMuons" )
)
###process.patTriggerMatchEmbedderDefaultSequence *= process.selectedPatMuonsTriggerMatch
#process.patTriggerDefaultSequence *= process.muonTriggerMatchHLTMuons
#process.patTriggerDefaultSequence *= process.selectedPatMuonsTriggerMatch

process.patTriggerDefaultSequence2 = cms.Sequence(
  process.patTrigger *
  process.muonTriggerMatchHLTMuons *
  process.patTriggerEvent *
  process.goodMuonsTriggerMatch
)

## create triggerMatchedMuons
process.triggerMatchedPatMuons = selectedPatMuons.clone(
  src = "goodMuonsTriggerMatch",
  cut = "triggerObjectMatches.size > 0"
)

from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.oneTriggerMatch = countPatMuons.clone(src = 'triggerMatchedPatMuons',
                                              minNumber = 1
                                              )


#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------


process.SingleMu = cms.Path(#process.preselection *
                            process.goodObjects *
                            process.patTriggerDefaultSequence2*
                            process.triggerMatchedPatMuons *
                            #process.oneTriggerMatch *
                            process.oneGoodJet *
                            process.MuTrigger * 
                            process.analyzeSUSYBjets1l_1
                            )

process.SingleMuMuHad = cms.Path(#process.preselection *
                                 process.goodObjects *
                                 process.patTriggerDefaultSequence2*
                                 process.triggerMatchedPatMuons *
                                 #process.oneTriggerMatch *
                                 process.oneGoodJet *
                                 process.MuTrigger *
                                 process.MuHadTrigger *
                                 process.analyzeSUSYBjets1l_2
                                 )
