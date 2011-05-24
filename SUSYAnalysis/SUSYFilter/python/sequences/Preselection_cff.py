import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.hltHighLevel_cfi import *

##----------------------------------------
## Define high level trigger filter
##----------------------------------------

## HT trigger
HTTrigger = hltHighLevel.clone(HLTPaths = ['HLT_HT100U'],throw = False)
HTTriggerQCD = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI38X',
                                  HLTPaths = ['HLT_HT100U',
                                              'HLT_HT120U',
                                              'HLT_HT140U'],
                                  throw = False)

## Single Muon Trigger
MuTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu9'],throw = False)
ElTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Ele10_LW_L1R'],throw = False)

MuTriggerSynch = hltHighLevel.clone(TriggerResultsTag='TriggerResults::REDIGI311X',HLTPaths = ['HLT_Mu9'], throw = False)

ElTriggerSynch = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                    HLTPaths = ['HLT_Ele10_LW_L1R',
                                                'HLT_Ele15_SW_L1R',
                                                'HLT_Ele15_SW_CaloEleId_L1R',
                                                'HLT_Ele17_SW_CaloEleId_L1R',
                                                'HLT_Ele17_SW_TighterEleIdIsol_L1R_v1',
                                                'HLT_Ele17_SW_TighterEleIdIsol_L1R_v2',
                                                'HLT_Ele17_SW_TighterEleIdIsol_L1R_v3'],
                                    throw = False)

MuTriggerQCD = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI38X', HLTPaths = ['HLT_Mu9'],throw = False)
MuTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu9'],throw = False)
MuTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_v*'],throw = False)

## MuHad trigger
MuHTTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                   HLTPaths = ['HLT_Mu5_HT*'],throw = False)
ElHTTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                   HLTPaths = ['HLT_Ele10*_HT100*'],throw = False)
MuHTTriggerOSET = hltHighLevel.clone(HLTPaths = ['HLT_Mu9'],throw = False)

MuHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_*_HT200_v*'],throw = False)
ElHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Ele10*_HT200*'],throw = False)

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

preselection = cms.Sequence(MuTrigger *
                            primaryVertexFilter *
                            #HBHENoiseFilter *
                            scrapingVeto
                            )

preselection2 = cms.Sequence(ElTrigger *
                             primaryVertexFilter *
                             #HBHENoiseFilter *
                             scrapingVeto
                             )

preselectionHT = cms.Sequence(HTTrigger *
                              primaryVertexFilter *
                              ##HBHENoiseFilter *
                              scrapingVeto
                              )

preselectionQCD = cms.Sequence(MuTriggerQCD *
                               primaryVertexFilter *
                               ##HBHENoiseFilter *
                               scrapingVeto
                               )

preselectionQCDHT = cms.Sequence(HTTriggerQCD *
                                 primaryVertexFilter *
                                 ##HBHENoiseFilter *
                                 scrapingVeto
                                 )

preselectionData = cms.Sequence(MuTriggerData##  *
##                                 primaryVertexFilter *
##                                 HBHENoiseFilter *
##                                 scrapingVeto
                                )

preselectionData2 = cms.Sequence(MuTriggerData2##  *
##                                 primaryVertexFilter *
##                                 HBHENoiseFilter *
##                                 scrapingVeto
                                 )

preselectionMuHTMC = cms.Sequence(MuHTTriggerMC *
                                  primaryVertexFilter *
                                  ##HBHENoiseFilter *
                                  scrapingVeto
                                  )

preselectionElHTMC = cms.Sequence(ElHTTriggerMC *
                                  primaryVertexFilter *
                                  ##HBHENoiseFilter *
                                  scrapingVeto
                                  )

preselectionOSET = cms.Sequence(MuHTTriggerOSET *
                                primaryVertexFilter *
                                ##HBHENoiseFilter *
                                scrapingVeto
                                )

preselectionMuHTData = cms.Sequence(MuHTTriggerData ## *
##                                  primaryVertexFilter *
##                                  HBHENoiseFilter *
##                                  scrapingVeto
                                    )

preselectionElHTData = cms.Sequence(ElHTTriggerData ## *
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
                                  #primaryVertexFilter *
                                  HBHENoiseFilter #*
                                  #scrapingVeto
                                  )

preselectionMuSynch = cms.Sequence(MuTriggerSynch *
                                   primaryVertexFilter *
                                   #HBHENoiseFilter *
                                   scrapingVeto
                                   )

preselectionElSynch = cms.Sequence(ElTriggerSynch *
                                   primaryVertexFilter *
                                   #HBHENoiseFilter *
                                   scrapingVeto
                                   )

##----------------------------------------------
## Filter on member functions of TtGenEvent
##----------------------------------------------

from TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff import *
from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
ttGenEventFilterSemiMuon = ttGenEventFilter.clone(cut="semiLeptonicChannel==2")
ttGenEventFilterOther = ttGenEventFilter.clone(cut="semiLeptonicChannel!=2")

preselectionSemiMuonTTBar = cms.Sequence(makeGenEvt *
                                         ttGenEventFilterSemiMuon *
                                         MuTrigger *
                                         primaryVertexFilter *
                                         HBHENoiseFilter *
                                         scrapingVeto
                                         )

preselectionOtherTTBar = cms.Sequence(makeGenEvt *
                                      ttGenEventFilterOther *
                                      MuTrigger *
                                      primaryVertexFilter *
                                      HBHENoiseFilter *
                                      scrapingVeto
                                      )

preselectionSemiMuonTTBar2 = cms.Sequence(makeGenEvt *
                                          ttGenEventFilterSemiMuon *
                                          MuHTTriggerMC *
                                          primaryVertexFilter *
                                          #HBHENoiseFilter *
                                          scrapingVeto
                                          )

preselectionOtherTTBar2 = cms.Sequence(makeGenEvt *
                                       ttGenEventFilterOther *
                                       MuHTTriggerMC *
                                       primaryVertexFilter *
                                       #HBHENoiseFilter *
                                       scrapingVeto
                                       )
