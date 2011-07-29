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

MuTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                 HLTPaths = ['HLT_Mu9'],throw = False)
ElTriggerMC = hltHighLevel.clone(TriggerResultsTag = 'TriggerResults::REDIGI311X',
                                 HLTPaths = ['HLT_Ele10_SW_L1R_v2'],throw = False)

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

MuTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_HT200_v*', 'HLT_Mu8_HT200_v*'],throw = False)
ElTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v5'],throw = False)

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

## primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
##                                    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
##                                    minimumNDOF = cms.uint32(4) ,
##                                    maxAbsZ = cms.double(24),
##                                    maxd0 = cms.double(2) )

goodVertices = cms.EDFilter(
 "VertexSelector",
 filter = cms.bool(False),
 src = cms.InputTag("offlinePrimaryVertices"),
 cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)

oneGoodVertex = cms.EDFilter(
  "VertexCountFilter",
  src = cms.InputTag("goodVertices"),
  minNumber = cms.uint32(1),
  maxNumber = cms.uint32(999)
)

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

from SUSYAnalysis.SUSYFilter.filters.TrackingFailureFilter_cfi import *

from RecoMET.METAnalyzers.CSCHaloFilter_cfi import *

from JetMETAnalysis.ecalDeadCellTools.RA2TPfilter_cff import *

## Load EcalDeadCellBEFilter modules; see UserCode/crohringer/DeadCellFilterLists/python for update
from SUSYAnalysis.SUSYFilter.SingleMu_Run2011A_May10ReReco_v1_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.MuHad_Run2011A_May10ReReco_v1_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.Mu_Run2010A_Apr21ReReco_v1_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.MuHad_Run2011A_PromptReco_v4_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.SingleMu_Run2011A_PromptReco_v4_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.Mu_Run2010B_Apr21ReReco_v1_missed1Job__filteredEventsBE_cfi import *

Mu_BEfilterSequence=cms.Sequence(
    veto_SingleMu_Run2011A_May10ReReco_v1_filteredEventsBE*
    veto_MuHad_Run2011A_May10ReReco_v1_filteredEventsBE*
    veto_Mu_Run2010A_Apr21ReReco_v1_filteredEventsBE*
    veto_MuHad_Run2011A_PromptReco_v4_filteredEventsBE*
    veto_SingleMu_Run2011A_PromptReco_v4_filteredEventsBE*
    veto_Mu_Run2010B_Apr21ReReco_v1_missed1Job__filteredEventsBE
    )

from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011A_PromptReco_v4_filteredEventsBE_cfi  import *
from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011A_May10ReReco_v1_filteredEventsBE_cfi  import *
from SUSYAnalysis.SUSYFilter.Electron_Run2010B_Apr21ReReco_v1_filteredEventsBE_cfi  import *
from SUSYAnalysis.SUSYFilter.EG_Run2010A_Apr21ReReco_v1_missed4Jobs_filteredEventsBE_cfi  import *

Electron_BEfilterSequence=cms.Sequence(
    veto_ElectronHad_Run2011A_PromptReco_v4_filteredEventsBE*
    veto_ElectronHad_Run2011A_May10ReReco_v1_filteredEventsBE*
    veto_Electron_Run2010B_Apr21ReReco_v1_filteredEventsBE*
    veto_EG_Run2010A_Apr21ReReco_v1_missed4Jobs_filteredEventsBE
    )

##-------------------------------
## Define preselection sequences
##-------------------------------

## MC Spring11
preselectionMuHTMC = cms.Sequence(MuHTTriggerMC *
                                  goodVertices *
                                  oneGoodVertex *
                                  scrapingVeto *
                                  trackingFailureFilter *
                                  #CSCTightHaloFilter *
                                  ecalDeadCellTPfilter
                                  )

preselectionElHTMC = cms.Sequence(ElHTTriggerMC *
                                  goodVertices *
                                  oneGoodVertex *
                                  scrapingVeto *
                                  trackingFailureFilter *
                                  #CSCTightHaloFilter *
                                  ecalDeadCellTPfilter
                                  )

preselectionLepHTMC = cms.Sequence(LepHTTriggerMC *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto *
                                   trackingFailureFilter *
                                   #CSCTightHaloFilter *
                                   ecalDeadCellTPfilter
                                   )

## MC Summer11
preselectionMuHTMC2 = cms.Sequence(MuHTTriggerMC2 *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto *
                                   goodVertices *
                                   trackingFailureFilter *
                                   #CSCTightHaloFilter *
                                   ecalDeadCellTPfilter
                                   )

preselectionElHTMC2 = cms.Sequence(ElHTTriggerMC2 *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto *
                                   goodVertices *
                                   trackingFailureFilter *
                                   #CSCTightHaloFilter *
                                   ecalDeadCellTPfilter
                                   )

preselectionLepHTMC2 = cms.Sequence(LepHTTriggerMC2 *
                                    goodVertices *
                                    oneGoodVertex *
                                    scrapingVeto *
                                    trackingFailureFilter *
                                    #CSCTightHaloFilter *
                                    ecalDeadCellTPfilter
                                    )

## Data
preselectionMuHTData = cms.Sequence(Mu_BEfilterSequence *
                                    MuHTTriggerData *
                                    goodVertices *
                                    trackingFailureFilter *
                                    #CSCTightHaloFilter *
                                    ecalDeadCellTPfilter
                                    )

preselectionElHTData = cms.Sequence(Electron_BEfilterSequence *
                                    ElHTTriggerData *
                                    goodVertices *
                                    trackingFailureFilter *
                                    #CSCTightHaloFilter *
                                    ecalDeadCellTPfilter
                                    )

preselectionLepHTData = cms.Sequence(LepHTTriggerData
                                     )

## Data2
preselectionMuHTData2 = cms.Sequence(Mu_BEfilterSequence *
                                     MuHTTriggerData2 *
                                     goodVertices *
                                     trackingFailureFilter *
                                     #CSCTightHaloFilter *
                                     ecalDeadCellTPfilter
                                     )

preselectionElHTData2 = cms.Sequence(Electron_BEfilterSequence *
                                     ElHTTriggerData2 *
                                     goodVertices *
                                     trackingFailureFilter *
                                     #CSCTightHaloFilter *
                                     ecalDeadCellTPfilter
                                     )

preselectionLepHTData2 = cms.Sequence(LepHTTriggerData2
                                      )

## For synchronization
preselectionMuSynch = cms.Sequence(MuTriggerMC *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto *
                                   trackingFailureFilter *
                                   #CSCTightHaloFilter *
                                   ecalDeadCellTPfilter
                                   )

preselectionElSynch = cms.Sequence(ElTriggerMC *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto *
                                   trackingFailureFilter *
                                   #CSCTightHaloFilter *
                                   ecalDeadCellTPfilter
                                   )

preselectionMuSynchData2 = cms.Sequence(MuTriggerData2 *
                                        goodVertices *
                                        oneGoodVertex *
                                        HBHENoiseFilter *
                                        scrapingVeto *
                                        trackingFailureFilter *
                                        CSCTightHaloFilter *
                                        ecalDeadCellTPfilter
                                        )

preselectionElSynchData2 = cms.Sequence(ElTriggerData2 *
                                        goodVertices *
                                        oneGoodVertex *
                                        HBHENoiseFilter *
                                        scrapingVeto *
                                        trackingFailureFilter *
                                        CSCTightHaloFilter *
                                        ecalDeadCellTPfilter
                                        )

# AOD2PAT data
preselectionData2PAT = cms.Sequence(AOD2PATTrigger *
                                    goodVertices *
                                    oneGoodVertex *
                                    HBHENoiseFilter *
                                    scrapingVeto #*
                                    #trackingFailureFilter *
                                    #CSCTightHaloFilter *
                                    #ecalDeadCellTPfilter
                                    )

preselectionSingleMu2PAT = cms.Sequence(MuTriggerData *
                                        goodVertices *
                                        oneGoodVertex *
                                        HBHENoiseFilter *
                                        scrapingVeto *
                                        trackingFailureFilter *
                                        #CSCTightHaloFilter *
                                        ecalDeadCellTPfilter
                                        )

preselectionSingleElectron2PAT = cms.Sequence(ElTriggerData *
                                              goodVertices *
                                              oneGoodVertex *
                                              HBHENoiseFilter *
                                              scrapingVeto *
                                              trackingFailureFilter *
                                              #CSCTightHaloFilter *
                                              ecalDeadCellTPfilter
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
                                        goodVertices *
                                        oneGoodVertex *
                                        scrapingVeto *
                                        trackingFailureFilter *
                                        #CSCTightHaloFilter *
                                        ecalDeadCellTPfilter
                                        )

preselectionSemiLepTTBarOther = cms.Sequence(makeGenEvt *
                                             ttGenEventFilterSemiLepOther *
                                             LepHTTriggerMC *
                                             goodVertices *
                                             oneGoodVertex *
                                             scrapingVeto *
                                             trackingFailureFilter *
                                             #CSCTightHaloFilter *
                                             ecalDeadCellTPfilter
                                             )

preselectionFullLepTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterFullLep *
                                        LepHTTriggerMC *
                                        goodVertices *
                                        oneGoodVertex *
                                        scrapingVeto *
                                        trackingFailureFilter *
                                        #CSCTightHaloFilter *
                                        ecalDeadCellTPfilter
                                        )

preselectionFullLepTTBarOther = cms.Sequence(makeGenEvt *
                                             ttGenEventFilterFullLepOther *
                                             LepHTTriggerMC *
                                             goodVertices *
                                             oneGoodVertex *
                                             scrapingVeto *
                                             trackingFailureFilter *
                                             #CSCTightHaloFilter *
                                             ecalDeadCellTPfilter
                                             )

preselectionFullHadTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterFullHad *
                                        LepHTTriggerMC *
                                        goodVertices *
                                        oneGoodVertex *
                                        scrapingVeto *
                                        trackingFailureFilter *
                                        #CSCTightHaloFilter *
                                        ecalDeadCellTPfilter
                                        )

preselectionTauTTBar = cms.Sequence(makeGenEvt *
                                    ttGenEventFilterTau *
                                    LepHTTriggerMC *
                                    goodVertices *
                                    oneGoodVertex *
                                    scrapingVeto *
                                    trackingFailureFilter *
                                    #CSCTightHaloFilter *
                                    ecalDeadCellTPfilter
                                    )
