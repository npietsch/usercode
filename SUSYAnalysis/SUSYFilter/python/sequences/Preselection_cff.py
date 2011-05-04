import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.hltHighLevel_cfi import *

##----------------------------------------
## Define high level trigger filter
##----------------------------------------

## HT trigger
HTTrigger = hltHighLevel.clone(HLTPaths = ['HLT_HT100U'],throw = False)
HTTriggerQCD = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI38X', HLTPaths = ['HLT_HT100U','HLT_HT120U','HLT_HT140U'],throw = False)

## Single Muon Trigger
MUTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu9'],throw = False)
MUTriggerQCD = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI38X', HLTPaths = ['HLT_Mu9'],throw = False)
MUTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu9'],throw = False)
MUTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_v1'],throw = False)

## MuHad trigger
MUHTTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v1','HLT_Mu8_HT200_v2','HLT_Mu8_HT200_v3','HLT_Mu8_HT200_v4','HLT_Mu8_HT200_v5'],throw = False)

## AOD2PAT trigger
AOD2PATTrigger = hltHighLevel.clone(HLTPaths = [
    #2010 trigger (different versions with "or" to be somewhat immune to changes)
    'HLT_Mu15_v2', 'HLT_Mu15_v3', 'HLT_Mu15_v4', 'HLT_Mu15_v5',
    #2011 1E33 trigger (different versions with 'or' to be somewhat immune to changes)
    'HLT_Mu17_TriCentralJet30_v1', 'HLT_Mu17_CentralJet30_v1', 'HLT_Mu17_DiCentralJet30_v1',
    'HLT_Mu17_TriCentralJet30_v2', 'HLT_Mu17_CentralJet30_v2', 'HLT_Mu17_DiCentralJet30_v2',
    'HLT_Mu17_TriCentralJet30_v3', 'HLT_Mu17_CentralJet30_v3', 'HLT_Mu17_DiCentralJet30_v3',
    'HLT_Mu17_TriCentralJet30_v4', 'HLT_Mu17_CentralJet30_v4', 'HLT_Mu17_DiCentralJet30_v4',
    'HLT_Mu17_TriCentralJet30_v5', 'HLT_Mu17_CentralJet30_v5', 'HLT_Mu17_DiCentralJet30_v5',
    #2011 1E33-2E33 trigger (different versions with 'or' to be somewhat immune to changes)
    'HLT_IsoMu17_DiCentralJet30_v1', 'HLT_IsoMu17_CentralJet30_v1', 'HLT_Mu17_CentralJet40_BTagIP_v1', 'HLT_IsoMu17_CentralJet40_BTagIP_v1',
    'HLT_IsoMu17_DiCentralJet30_v2', 'HLT_IsoMu17_CentralJet30_v2', 'HLT_Mu17_CentralJet40_BTagIP_v2', 'HLT_IsoMu17_CentralJet40_BTagIP_v2',
    'HLT_IsoMu17_DiCentralJet30_v3', 'HLT_IsoMu17_CentralJet30_v3', 'HLT_Mu17_CentralJet40_BTagIP_v3', 'HLT_IsoMu17_CentralJet40_BTagIP_v3',
    'HLT_IsoMu17_DiCentralJet30_v4', 'HLT_IsoMu17_CentralJet30_v4', 'HLT_Mu17_CentralJet40_BTagIP_v4', 'HLT_IsoMu17_CentralJet40_BTagIP_v4',
    'HLT_IsoMu17_DiCentralJet30_v5', 'HLT_IsoMu17_CentralJet30_v5', 'HLT_Mu17_CentralJet40_BTagIP_v5', 'HLT_IsoMu17_CentralJet40_BTagIP_v5',
    #2011 HT trigger requested by Niklas (different versions with "or" to be somewhat immune to changes)
    'HLT_Mu8_HT200_v1', 'HLT_Mu8_HT200_v2', 'HLT_Mu8_HT200_v3', 'HLT_Mu8_HT200_v4', 'HLT_Mu8_HT200_v5'],throw = False)

##-----------------------------
## event cleaning modules
##-----------------------------

scrapingVeto = cms.EDFilter("FilterOutScraping",
                            applyfilter = cms.untracked.bool(True),
                            debugOn = cms.untracked.bool(False),
                            numtrack = cms.untracked.uint32(10),
                            thresh = cms.untracked.double(0.25)
                            )

primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                   vertexCollection = cms.InputTag("offlinePrimaryVertices"),
                                   minimumNDOF = cms.uint32(4) ,
                                   maxAbsZ = cms.double(24),
                                   maxd0 = cms.double(2) )

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

##-------------------------------
## Define preselectio sequences
##-------------------------------

preselection = cms.Sequence(MUTrigger *
                            primaryVertexFilter *
                            HBHENoiseFilter *
                            scrapingVeto
                            )

preselectionHT = cms.Sequence(HTTrigger *
                              primaryVertexFilter *
                              ##HBHENoiseFilter *
                              scrapingVeto
                              )

preselectionQCD = cms.Sequence(MUTriggerQCD *
                               primaryVertexFilter *
                               ##HBHENoiseFilter *
                               scrapingVeto
                               )

preselectionQCDHT = cms.Sequence(HTTriggerQCD *
                                 primaryVertexFilter *
                                 ##HBHENoiseFilter *
                                 scrapingVeto
                                 )

preselectionData = cms.Sequence(MUTriggerData##  *
##                                 primaryVertexFilter *
##                                 HBHENoiseFilter *
##                                 scrapingVeto
                                )

preselectionData2 = cms.Sequence(MUTriggerData2##  *
##                                 primaryVertexFilter *
##                                 HBHENoiseFilter *
##                                 scrapingVeto
                                 )

preselectionMuHT = cms.Sequence(MUHTTrigger ## *
##                                  primaryVertexFilter *
##                                  HBHENoiseFilter *
##                                  scrapingVeto
                                 )

preselectionData2PAT = cms.Sequence(AOD2PATTrigger *
                                    primaryVertexFilter *
                                    HBHENoiseFilter *
                                    scrapingVeto
                                    )

preselectionMC2PAT = cms.Sequence(AOD2PATTrigger *
                                  primaryVertexFilter *
                                  HBHENoiseFilter *
                                  scrapingVeto
                                  )
