import FWCore.ParameterSet.Config as cms

#from HLTrigger.HLTfilters.hltHighLevelDev_cfi import hltHighLevelDev
#process.trigger = hltHighLevelDev.clone(HLTPaths = ['HLT_Mu9'], HLTPathsPrescales = [1], andOr = True)

##from TopAnalysis.TopFilter.sequences.triggerFilter_cff import *

## high level trigger filter
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
hltMu9 = hltHighLevel.clone(HLTPaths = ["HLT_Mu9"])

trigger=hltMu9.clone()

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
                            scrapingVeto *
                            primaryVertexFilter #*
                            #HBHENoiseFilter
                            )
