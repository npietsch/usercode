import FWCore.ParameterSet.Config as cms

scrapingVeto = cms.EDFilter("FilterOutScraping",
                            applyfilter = cms.untracked.bool(True),
                            debugOn = cms.untracked.bool(False),
                            numtrack = cms.untracked.uint32(10),
                            thresh = cms.untracked.double(0.25)
                            )

## primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
##                                    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
##                                    minimumNDOF = cms.uint32(4) ,
##                                    maxAbsZ = cms.double(24),
##                                    maxd0 = cms.double(2))

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

from RecoMET.METFilters.hcalLaserEventFilter_cfi import *
hcalLaserEventFilter.vetoByRunEventNumber=cms.untracked.bool(False)
hcalLaserEventFilter.vetoByHBHEOccupancy=cms.untracked.bool(True)

from RecoMET.METFilters.eeBadScFilter_cfi import *
from RecoMET.METAnalyzers.CSCHaloFilter_cfi import *
from RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi import *
#from RecoMET.METFilters.trackingFailureFilter_cfi import *

from SUSYAnalysis.SUSYFilter.filters.TrackingFailure_cfi import *

trackingFailure.JetSource = "selectedPatJetsAK5PF"
trackingFailure.VertexSource  = "selectedVertices" 


selectedVertices = cms.EDFilter(
    "VertexSelector",
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2")
    )

oneGoodVertex = cms.EDFilter(
  "VertexCountFilter",
  src = cms.InputTag("selectedVertices"),
  minNumber = cms.uint32(1),
  maxNumber = cms.uint32(999)
)

preselection = cms.Sequence(
    #hltFilter *
    scrapingVeto *
    #primaryVertexFilter*
    selectedVertices *
    oneGoodVertex *
    HBHENoiseFilter *
    trackingFailure *
    hcalLaserEventFilter *
    CSCTightHaloFilter *
    eeBadScFilter *
    EcalDeadCellTriggerPrimitiveFilter
    )
