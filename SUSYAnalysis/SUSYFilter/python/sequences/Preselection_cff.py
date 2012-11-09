import FWCore.ParameterSet.Config as cms

##----------------------------------------
## Define high level trigger filter
##----------------------------------------

from HLTrigger.HLTfilters.hltHighLevel_cfi import *

## Data trigger
MuHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*'],
                                     throw = False)
ElHTTriggerData = hltHighLevel.clone(HLTPaths = ['HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v*'],
                                     throw = False)

## Data trigger 2
MuHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Mu15_HT200_v*','HLT_HT250_Mu15_PFMHT20_v*'],
                                      throw = False)
ElHTTriggerData2 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*',
                                                  'HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*'],
                                      throw = False)

## Data trigger 3
MuHTTriggerData3 = hltHighLevel.clone(HLTPaths = ['HLT_HT250_Mu15_PFMHT20_v*'],
                                      throw = False)
ElHTTriggerData3 = hltHighLevel.clone(HLTPaths = ['HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*'],
                                      throw = False)

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
AOD2PATTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu*','HLT_Ele*',
                                                'HLT_HT*_Mu*_PFMHT*',
                                                'HLT_HT*_EL*_PFMHT*',
                                                'HLT_HT*_Mu*_PFMET*',
                                                'HLT_HT*_EL*_PFMET*',
                                                'HLT_Mu*_HT*','HLT_Ele*_HT*',
                                                'HLT_Mu17_TriCentralJet30_v*',
                                                'HLT_Mu17_CentralJet30_v*',
                                                'HLT_Mu17_DiCentralJet30_v*',
                                                'HLT_IsoMu17_DiCentralJet30_v*',
                                                'HLT_IsoMu17_CentralJet30_v*',
                                                'HLT_Mu17_CentralJet40_BTagIP_v*',
                                                'HLT_IsoMu17_CentralJet40_BTagIP_v*'],
                                    throw = False)

##----------------------------------------
## Vertex selection
##----------------------------------------

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

##----------------------------------------
## Configure event cleaning modules
##----------------------------------------

## totalKinematicsFilter
from GeneratorInterface.GenFilters.TotalKinematicsFilter_cfi import *

totalKinematicsFilter = cms.EDFilter('TotalKinematicsFilter',
  src             = cms.InputTag("genParticles"),
  tolerance       = cms.double(0.5),
  verbose         = cms.untracked.bool(False)                                   
)

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

scrapingVeto = cms.EDFilter("FilterOutScraping",
                            applyfilter = cms.untracked.bool(True),
                            debugOn = cms.untracked.bool(False),
                            numtrack = cms.untracked.uint32(10),
                            thresh = cms.untracked.double(0.25)
                            )


from SUSYAnalysis.SUSYFilter.filters.TrackingFailureFilter_cfi import *
trackingFailureFilter.VertexSource = "goodVertices"

from RecoMET.METAnalyzers.CSCHaloFilter_cfi import *

from JetMETAnalysis.ecalDeadCellTools.RA2TPfilter_cff import *

## Load EcalDeadCellBEFilter modules
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

##-------------------------------------
## Define MC preselection sequences
##-------------------------------------

# AOD2PAT MC
preselectionMC2PAT = cms.Sequence(goodVertices *
                                  HBHENoiseFilter *
                                  trackingFailureFilter *
                                  CSCTightHaloFilter *
                                  ecalDeadCellTPfilter
                                  )

## MC Summer11
preselectionMuHTMC2 = cms.Sequence(goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto
                                   )

preselectionElHTMC2 = cms.Sequence(goodVertices *
                                   oneGoodVertex *
                                   scrapingVeto
                                   )

preselectionLepHTMC2 = cms.Sequence(goodVertices *
                                    oneGoodVertex *
                                    scrapingVeto
                                    )

preselectionMuHTMC2ZJets = cms.Sequence(goodVertices *
                                        oneGoodVertex *
                                        totalKinematicsFilter *
                                        scrapingVeto
                                        )

preselectionElHTMC2ZJets = cms.Sequence(goodVertices *
                                        oneGoodVertex *
                                        totalKinematicsFilter *
                                        scrapingVeto
                                        )

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *

StopPairFilter     = SUSYGenEventFilter.clone(cut='StopStopDecay')
SbottomPairFilter  = SUSYGenEventFilter.clone(cut='SbottomSbottomDecay')
GluinoSquarkFilter = SUSYGenEventFilter.clone(cut='GluinoSquarkDecay')
GluinoPairFilter   = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay')
SquarkPairFilter   = SUSYGenEventFilter.clone(cut='SquarkSquarkDecay')

preselectionStopPair = cms.Sequence(goodVertices *
                                    oneGoodVertex *
                                    scrapingVeto *
                                    StopPairFilter
                                    )

preselectionSbottomPair = cms.Sequence(goodVertices *
                                       oneGoodVertex *
                                       scrapingVeto *
                                       SbottomPairFilter
                                       )

preselectionGluinoSquark = cms.Sequence(goodVertices *
                                        oneGoodVertex *
                                        scrapingVeto *
                                        GluinoSquarkFilter
                                        )

preselectionGluinoPair = cms.Sequence(goodVertices *
                                      oneGoodVertex *
                                      scrapingVeto *
                                      GluinoPairFilter
                                      )

preselectionSquarkPair = cms.Sequence(goodVertices *
                                      oneGoodVertex *
                                      scrapingVeto *
                                      SquarkPairFilter
                                      )

##-------------------------------------
## Define data preselection sequences
##-------------------------------------

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

## Data
preselectionMuHTData = cms.Sequence(goodVertices *
                                    Mu_BEfilterSequence *
                                    MuHTTriggerData
                                    )

preselectionElHTData = cms.Sequence(goodVertices *
                                    Electron_BEfilterSequence *
                                    ElHTTriggerData
                                    )

## Data2
preselectionMuHTData2 = cms.Sequence(goodVertices *
                                     Mu_BEfilterSequence *
                                     MuHTTriggerData2
                                     )

preselectionElHTData2 = cms.Sequence(goodVertices *
                                     Electron_BEfilterSequence *
                                     ElHTTriggerData2
                                     )

## Data3
preselectionMuHTData3 = cms.Sequence(goodVertices *
                                     Mu_BEfilterSequence *
                                     MuHTTriggerData3
                                     )

preselectionElHTData3 = cms.Sequence(goodVertices *
                                     Electron_BEfilterSequence *
                                     ElHTTriggerData3
                                     )

## All Data
preselectionMuHTAllData = cms.Sequence(goodVertices *
                                       Mu_BEfilterSequence *
                                       MuHTTriggerAllData
                                       )

preselectionElHTAllData = cms.Sequence(goodVertices *
                                       Electron_BEfilterSequence *
                                       ElHTTriggerAllData
                                       )
