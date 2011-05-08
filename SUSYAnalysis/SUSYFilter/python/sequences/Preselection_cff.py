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
MUTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_v*'],throw = False)

## MuHad trigger
MUHTTrigger = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X', HLTPaths = ['HLT_Mu5_HT100*', 'HLT_Mu5_HT200*', 'HLT_Mu8_HT200_v*'],throw = False)

## AOD2PAT trigger
AOD2PATTrigger = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X' ,HLTPaths = [
    #2010 trigger ('v*' to be immune to version changes)
    'HLT_Mu15_v*',
    #2011 1E33 trigger ('v*' to be immune to version changes)
    'HLT_Mu17_TriCentralJet30_v*', 'HLT_Mu17_CentralJet30_v*', 'HLT_Mu17_DiCentralJet30_v*',
    #2011 1E33-2E33 trigger ('v*' to be immune to version changes)
    'HLT_IsoMu17_DiCentralJet30_v*', 'HLT_IsoMu17_CentralJet30_v*',
    'HLT_Mu17_CentralJet40_BTagIP_v*', 'HLT_IsoMu17_CentralJet40_BTagIP_v*',
    #2011 HT trigger requested by Niklas ('v*' to be immune to version changes)
    'HLT_Mu5_HT*','HLT_Mu8_HT200_v*'],throw = False)

##----------------------------
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
                            #HBHENoiseFilter *
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

preselectionMC2PAT = cms.Sequence(#AOD2PATTrigger *
                                  primaryVertexFilter *
                                  HBHENoiseFilter *
                                  scrapingVeto
                                  )

## Filter on member functions of TtGenEvent

from TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff import *
from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
ttGenEventFilterSemiMuon = ttGenEventFilter.clone(cut="semiLeptonicChannel==2")
ttGenEventFilterOther = ttGenEventFilter.clone(cut="semiLeptonicChannel!=2")

preselectionSemiMuonTTBar = cms.Sequence(makeGenEvt *
                                         ttGenEventFilterSemiMuon *
                                         MUTrigger *
                                         primaryVertexFilter *
                                         HBHENoiseFilter *
                                         scrapingVeto
                                         )

preselectionOtherTTBar = cms.Sequence(makeGenEvt *
                                      ttGenEventFilterOther *
                                      MUTrigger *
                                      primaryVertexFilter *
                                      HBHENoiseFilter *
                                      scrapingVeto
                                      )
