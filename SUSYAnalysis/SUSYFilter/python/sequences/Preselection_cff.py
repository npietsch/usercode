import FWCore.ParameterSet.Config as cms

##----------------------------------------
## Define high level trigger filter
##----------------------------------------

from HLTrigger.HLTfilters.hltHighLevel_cfi import *

## MC trigger Summer11
MuHTTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*'],throw = False)
ElHTTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele10*_HT200_v*'],throw = False)
LepHTTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*','HLT_Ele10*_HT200_v*'], throw = False)

MuTriggerMC2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_v1'],throw = False)

DiLeptonTriggerMC = hltHighLevel.clone(HLTPaths = ['HLT_Mu*_Ele*'],throw = False)

## Data trigger
MuHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*'],throw = False)
ElHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v*'],throw = False)

## Data trigger 2
MuHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_HT200_v*','HLT_HT250_Mu15_PFMHT20_v*'],throw = False)
ElHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*','HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*'],throw = False)

## Data trigger 3
MuHTTriggerData3 = hltHighLevel.clone(HLTPaths = ['HLT_HT250_Mu15_PFMHT20_v*'],throw = False)
ElHTTriggerData3 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*'],throw = False)

## Data trigger all
MuHTTriggerAllData = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*',
                                                    'HLT_Mu15_HT200_v*',
                                                    'HLT_HT250_Mu15_PFMHT20_v*',
                                                    'HLT_HT250_Mu15_PFMHT40_v*',
                                                    'HLT_HT300_Mu15_PFMHT40_v*'
                                                    ],
                                        throw = False)

ElHTTriggerAllData = hltHighLevel.clone(HLTPaths = ['HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v*',
                                                    'HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*',
                                                    'HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*',
                                                    'HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_v*',
                                                    'HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_v*'
                                                    ],
                                        throw = False)

## AOD2PAT trigger
AOD2PATTrigger = hltHighLevel.clone(HLTPaths = [
    'HLT_Mu*','HLT_Ele*',
    'HLT_HT*_Mu*_PFMHT*', 'HLT_HT*_EL*_PFMHT*',
    'HLT_HT*_Mu*_PFMET*','HLT_HT*_EL*_PFMET*',
    'HLT_Mu*_HT*','HLT_Ele*_HT*',
    'HLT_Mu17_TriCentralJet30_v*', 'HLT_Mu17_CentralJet30_v*', 'HLT_Mu17_DiCentralJet30_v*',
    'HLT_IsoMu17_DiCentralJet30_v*', 'HLT_IsoMu17_CentralJet30_v*',
    'HLT_Mu17_CentralJet40_BTagIP_v*', 'HLT_IsoMu17_CentralJet40_BTagIP_v*'
    ],throw = False)

# For synchronization
MuTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_HT200_v*', 'HLT_Mu8_HT200_v*'],throw = False)
ElTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v5'],throw = False)

##----------------------------
## Event cleaning modules
##-----------------------------

scrapingVeto = cms.EDFilter("FilterOutScraping",
                            applyfilter = cms.untracked.bool(True),
                            debugOn = cms.untracked.bool(False),
                            numtrack = cms.untracked.uint32(10),
                            thresh = cms.untracked.double(0.25)
                            )

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

from GeneratorInterface.GenFilters.TotalKinematicsFilter_cfi import *

totalKinematicsFilter = cms.EDFilter('TotalKinematicsFilter',
  src             = cms.InputTag("genParticles"),
  tolerance       = cms.double(0.5),
  verbose         = cms.untracked.bool(False)                                   
)

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

from SUSYAnalysis.SUSYFilter.filters.TrackingFailureFilter_cfi import *

from RecoMET.METAnalyzers.CSCHaloFilter_cfi import *

from JetMETAnalysis.ecalDeadCellTools.RA2TPfilter_cff import *

## Load EcalDeadCellBEFilter modules; see UserCode/crohringer/DeadCellFilterLists/python for update
from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011A_Aug5ReReco_v3_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011A_May10ReReco_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011A_Prompt_v4_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011A_Prompt_v6_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.ElectronHad_Run2011B_Prompt_v1_filteredEventsBE_cfi import *

Electron_BEfilterSequence=cms.Sequence(
    veto_ElectronHad_Run2011A_Aug5ReReco_v3_filteredEventsBE*
    veto_ElectronHad_Run2011A_May10ReReco_filteredEventsBE*
    veto_ElectronHad_Run2011A_Prompt_v4_filteredEventsBE*
    veto_ElectronHad_Run2011A_Prompt_v6_filteredEventsBE*
    veto_ElectronHad_Run2011B_Prompt_v1_filteredEventsBE
    )

from SUSYAnalysis.SUSYFilter.MuHad_Run2011A_May10ReReco_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.MuHad_Run2011A_Aug5ReReco_v3_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.MuHad_Run2011A_Prompt_v4_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.MuHad_Run2011A_Prompt_v6_filteredEventsBE_cfi import *
from SUSYAnalysis.SUSYFilter.MuHad_Run2011B_Prompt_v1_filteredEventsBE_cfi import *

Mu_BEfilterSequence=cms.Sequence(
    veto_MuHad_Run2011A_May10ReReco_filteredEventsBE*
    veto_MuHad_Run2011A_Aug5ReReco_v3_filteredEventsBE*
    veto_MuHad_Run2011A_Prompt_v4_filteredEventsBE*
    veto_MuHad_Run2011A_Prompt_v6_filteredEventsBE*
    veto_MuHad_Run2011B_Prompt_v1_filteredEventsBE
    )

##-------------------------------
## Define preselection sequences
##-------------------------------

## MC Summer11
preselectionMuHTMC2 = cms.Sequence(MuHTTriggerMC2 *
                                   totalKinematicsFilter *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto
                                   )

preselectionElHTMC2 = cms.Sequence(ElHTTriggerMC2 *
                                   totalKinematicsFilter *
                                   goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto
                                   )


preselectionDiLeptonMC = cms.Sequence(DiLeptonTriggerMC *
                                      totalKinematicsFilter *
                                      goodVertices *
                                      oneGoodVertex *
                                      scrapingVeto
                                      )

## Data
preselectionMuHTData = cms.Sequence(Mu_BEfilterSequence *
                                    MuHTTriggerData
                                    )

preselectionElHTData = cms.Sequence(Electron_BEfilterSequence *
                                    ElHTTriggerData
                                    )

## Data2
preselectionMuHTData2 = cms.Sequence(Mu_BEfilterSequence *
                                     MuHTTriggerData2
                                     )

preselectionElHTData2 = cms.Sequence(Electron_BEfilterSequence *
                                     ElHTTriggerData2
                                     )

## Data3
preselectionMuHTData3 = cms.Sequence(Mu_BEfilterSequence *
                                     MuHTTriggerData3
                                     )

preselectionElHTData3 = cms.Sequence(Electron_BEfilterSequence *
                                     ElHTTriggerData3
                                     )

## All Data
preselectionMuHTAllData = cms.Sequence(Mu_BEfilterSequence *
                                       Electron_BEfilterSequence *
                                       MuHTTriggerAllData
                                       )

preselectionElHTAllData = cms.Sequence(Electron_BEfilterSequence *
                                       Mu_BEfilterSequence *
                                       ElHTTriggerAllData
                                       )

# AOD2PAT data
preselectionData2PAT = cms.Sequence(AOD2PATTrigger *
                                    goodVertices *
                                    oneGoodVertex *
                                    HBHENoiseFilter *
                                    scrapingVeto *
                                    trackingFailureFilter *
                                    CSCTightHaloFilter *
                                    ecalDeadCellTPfilter
                                    )

# AOD2PAT MC
preselectionMC2PAT = cms.Sequence(LepHTTriggerMC2 *
                                  goodVertices *
                                  HBHENoiseFilter *
                                  trackingFailureFilter *
                                  CSCTightHaloFilter *
                                  ecalDeadCellTPfilter
                                  )

## For synchronization
preselectionMuSynchMC = cms.Sequence(#MuHTTriggerMC *
                                     totalKinematicsFilter *
                                     goodVertices *
                                     scrapingVeto *
                                     oneGoodVertex *
                                     HBHENoiseFilter *
                                     CSCTightHaloFilter *
                                     trackingFailureFilter *
                                     ecalDeadCellTPfilter
                                     )

preselectionElSynchMC = cms.Sequence(#ElHTTriggerMC *
                                     totalKinematicsFilter *
                                     goodVertices *
                                     scrapingVeto *
                                     oneGoodVertex *
                                     HBHENoiseFilter *
                                     CSCTightHaloFilter *
                                     trackingFailureFilter *
                                     ecalDeadCellTPfilter
                                     )

preselectionMuSynchData = cms.Sequence(#MuHTTriggerData2 *
                                       goodVertices *
                                       scrapingVeto *
                                       oneGoodVertex *
                                       HBHENoiseFilter *
                                       CSCTightHaloFilter *
                                       trackingFailureFilter *
                                       ecalDeadCellTPfilter
                                       )

preselectionElSynchData = cms.Sequence(#ElHTTriggerData2 *
                                       goodVertices *
                                       scrapingVeto *
                                       oneGoodVertex *
                                       HBHENoiseFilter *
                                       CSCTightHaloFilter *
                                       trackingFailureFilter *
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

## MC Summer11 TTJets MuHT preselection
preselectionMuHTMCSemiLepTTBar = cms.Sequence(makeGenEvt *
                                              ttGenEventFilterSemiLep *
                                              MuHTTriggerMC2 *
                                              totalKinematicsFilter *
                                              goodVertices *
                                              oneGoodVertex *
                                              scrapingVeto
                                              )

preselectionMuHTMCSemiLepTTBarOther = cms.Sequence(makeGenEvt *
                                                   ttGenEventFilterSemiLepOther *
                                                   MuHTTriggerMC2 *
                                                   totalKinematicsFilter *
                                                   goodVertices *
                                                   oneGoodVertex *
                                                   scrapingVeto
                                                   )

preselectionMuHTMCFullLepTTBar = cms.Sequence(makeGenEvt *
                                              ttGenEventFilterFullLep *
                                              MuHTTriggerMC2 *
                                              totalKinematicsFilter *
                                              goodVertices *
                                              oneGoodVertex *
                                              scrapingVeto
                                              )

preselectionMuHTMCFullHadTTBar = cms.Sequence(makeGenEvt *
                                              ttGenEventFilterFullHad *
                                              MuHTTriggerMC2 *
                                              totalKinematicsFilter *
                                              goodVertices *
                                              oneGoodVertex *
                                              scrapingVeto
                                              )

preselectionMuHTMCTauTTBar = cms.Sequence(makeGenEvt *
                                          ttGenEventFilterTau *
                                          MuHTTriggerMC2 *
                                          totalKinematicsFilter *
                                          goodVertices *
                                          oneGoodVertex *
                                          scrapingVeto
                                          )

## MC Summer11 TTJets ElHT preselection
preselectionElHTMCSemiLepTTBar = cms.Sequence(makeGenEvt *
                                              ttGenEventFilterSemiLep *
                                              ElHTTriggerMC2 *
                                              totalKinematicsFilter *
                                              goodVertices *
                                              oneGoodVertex *
                                              scrapingVeto
                                              )


preselectionElHTMCSemiLepTTBarOther = cms.Sequence(makeGenEvt *
                                                   ttGenEventFilterSemiLepOther *
                                                   ElHTTriggerMC2 *
                                                   totalKinematicsFilter *
                                                   goodVertices *
                                                   oneGoodVertex *
                                                   scrapingVeto
                                                   )

preselectionElHTMCFullLepTTBar = cms.Sequence(makeGenEvt *
                                              ttGenEventFilterFullLep *
                                              ElHTTriggerMC2 *
                                              totalKinematicsFilter *
                                              goodVertices *
                                              oneGoodVertex *
                                              scrapingVeto
                                              )

preselectionElHTMCFullHadTTBar = cms.Sequence(makeGenEvt *
                                              ttGenEventFilterFullHad *
                                              ElHTTriggerMC2 *
                                              totalKinematicsFilter *
                                              goodVertices *
                                              oneGoodVertex *
                                              scrapingVeto
                                              )

preselectionElHTMCTauTTBar = cms.Sequence(makeGenEvt *
                                          ttGenEventFilterTau *
                                          ElHTTriggerMC2 *
                                          totalKinematicsFilter *
                                          goodVertices *
                                          oneGoodVertex *
                                          scrapingVeto
                                          )


## MC Summer11 TTJets  preselection
preselectionSemiLepTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterSemiLep
                                        )

preselectionFullLepTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterFullLep
                                        )

preselectionFullHadTTBar = cms.Sequence(makeGenEvt *
                                        ttGenEventFilterFullHad
                                        )

preselectionTauTTBar = cms.Sequence(makeGenEvt *
                                    ttGenEventFilterTau
                                    )
