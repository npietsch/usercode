import FWCore.ParameterSet.Config as cms

##from TopAnalysis.TopFilter.sequences.triggerFilter_cff import *

## high level trigger filter
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
trigger = hltHighLevel.clone(HLTPaths = ["HLT_HT100U"]) ## add trigger: HLTPaths = ["HLT_Mu9", "HLT_Ele10_SW_L1R", ...]

scrapingVeto = cms.EDFilter("FilterOutScraping",
                            applyfilter = cms.untracked.bool(True),
                            debugOn = cms.untracked.bool(False),
                            numtrack = cms.untracked.uint32(10),
                            thresh = cms.untracked.double(0.25)
                            )

primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                   vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                   minimumNDOF = cms.uint32(4) ,
                                   maxAbsZ = cms.double(24),
                                   maxd0 = cms.double(2) )

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

preselection = cms.Sequence(trigger *
                            primaryVertexFilter *
                            ##HBHENoiseFilter *
                            scrapingVeto
                            )
