import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.hltHighLevel_cfi import *

##----------------------------------------
## Define high level trigger filter
##----------------------------------------

## MC trigger Spring11
MuHTTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                   HLTPaths = ['HLT_Mu5_HT100*'],throw = False)
ElHTTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                   HLTPaths = ['HLT_Ele10*_HT100*'],throw = False)
LepHTTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                    HLTPaths = ['HLT_Mu5_HT100*','HLT_Ele10*_HT100*'], throw = False)

## MC trigger Summer11
MuHTTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200*'],throw = False)
ElHTTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele10*_HT200*'],throw = False)
LepHTTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200*','HLT_Ele10*_HT200*'], throw = False)

## Data trigger v1, v2
MuHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200*'],throw = False)
ElHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Ele10*_HT200*'],throw = False)
LepHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200*','HLT_Ele10*_HT200*'],throw = False)

## Data trigger v4
MuHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_HT200*'],throw = False)
ElHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15*_HT200*'],throw = False)
LepHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_HT200*','HLT_Ele15*_HT200*'],throw = False)


## AOD2PAT trigger
AOD2PATTrigger = hltHighLevel.clone(HLTPaths = [
    'HLT_Mu*_HT*','HLT_Ele*_HT*',
    'HLT_Mu17_TriCentralJet30_v*', 'HLT_Mu17_CentralJet30_v*', 'HLT_Mu17_DiCentralJet30_v*',
    'HLT_IsoMu17_DiCentralJet30_v*', 'HLT_IsoMu17_CentralJet30_v*',
    'HLT_Mu17_CentralJet40_BTagIP_v*', 'HLT_IsoMu17_CentralJet40_BTagIP_v*'
    ],throw = False)

MuTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu*'],throw = False)

ElTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Ele*'],throw = False)

##----------------------------
## Event cleaning modules
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
## Define preselection sequences
##-------------------------------

## MC Spring11
preselectionMuHTMC = cms.Sequence(MuHTTriggerMC *
                                  primaryVertexFilter *
                                  scrapingVeto
                                  )

preselectionElHTMC = cms.Sequence(ElHTTriggerMC *
                                  primaryVertexFilter *
                                  scrapingVeto
                                  )

preselectionLepHTMC = cms.Sequence(LepHTTriggerMC *
                                   primaryVertexFilter *
                                   scrapingVeto
                                   )

## MC Summer11
preselectionMuHTMC2 = cms.Sequence(MuHTTriggerMC2 *
                                   primaryVertexFilter *
                                   scrapingVeto
                                   )

preselectionElHTMC2 = cms.Sequence(ElHTTriggerMC2 *
                                   primaryVertexFilter *
                                   scrapingVeto
                                   )

preselectionLepHTMC2 = cms.Sequence(LepHTTriggerMC2 *
                                    primaryVertexFilter *
                                    scrapingVeto
                                    )

## Data
preselectionMuHTData = cms.Sequence(MuHTTriggerData
                                    )

preselectionElHTData = cms.Sequence(ElHTTriggerData
                                    )

preselectionLepHTData = cms.Sequence(LepHTTriggerData
                                     )

## Data2
preselectionMuHTData2 = cms.Sequence(MuHTTriggerData2
                                     )

preselectionElHTData2 = cms.Sequence(ElHTTriggerData2
                                     )

preselectionLepHTData2 = cms.Sequence(LepHTTriggerData2
                                      )

# AOD2PAT data
preselectionData2PAT = cms.Sequence(AOD2PATTrigger *
                                    primaryVertexFilter *
                                    HBHENoiseFilter *
                                    scrapingVeto
                                    )

preselectionSingleMu2PAT = cms.Sequence(MuTriggerData *
                                        primaryVertexFilter *
                                        HBHENoiseFilter *
                                        scrapingVeto
                                        )

preselectionSingleElectron2PAT = cms.Sequence(ElTriggerData *
                                              primaryVertexFilter *
                                              HBHENoiseFilter *
                                              scrapingVeto
                                              )

##----------------------------------------------
## Filter on member functions of TtGenEvent
##----------------------------------------------

from TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff import *
from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *

ttGenEventFilterSemiLep = ttGenEventFilter.clone(cut="semiLeptonicChannel()=1 || semiLeptonicChannel()=2")
ttGenEventFilterSemiLepOther = ttGenEventFilter.clone(cut="!semiLeptonicChannel()=1 && !semiLeptonicChannel()=2")

ttGenEventFilterFullLep = ttGenEventFilter.clone(cut="isFullLeptonic() && fullLeptonicChannel.first!=3 && fullLeptonicChannel.second!=3 ")
ttGenEventFilterFullLepOther = ttGenEventFilter.clone(cut="isSemiLeptonic() || isFullHadronic() || fullLeptonicChannel.first=3 || fullLeptonicChannel.second=3 ")

ttGenEventFilterFullHad = ttGenEventFilter.clone(cut="isFullHadronic()")

ttGenEventFilterTau = ttGenEventFilter.clone(cut="semiLeptonicChannel()=3 || fullLeptonicChannel.first=3 || fullLeptonicChannel.second=3")

preselectionSemiLepTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterSemiLep *
                                        LepHTTriggerMC *
                                        primaryVertexFilter *
                                        scrapingVeto
                                        )

preselectionSemiLepTTBarOther = cms.Sequence(makeGenEvt *
                                             ttGenEventFilterSemiLepOther *
                                             LepHTTriggerMC *
                                             primaryVertexFilter *
                                             scrapingVeto
                                             )

preselectionFullLepTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterFullLep *
                                        LepHTTriggerMC *
                                        primaryVertexFilter *
                                        scrapingVeto
                                        )

preselectionFullLepTTBarOther = cms.Sequence(makeGenEvt *
                                             ttGenEventFilterFullLepOther *
                                             LepHTTriggerMC *
                                             primaryVertexFilter *
                                             scrapingVeto
                                             )

preselectionFullHadTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterFullHad *
                                        LepHTTriggerMC *
                                        primaryVertexFilter *
                                        scrapingVeto
                                        )

preselectionTauTTBar = cms.Sequence(makeGenEvt *
                                    ttGenEventFilterTau *
                                    LepHTTriggerMC *
                                    primaryVertexFilter *
                                    scrapingVeto
                                    )
