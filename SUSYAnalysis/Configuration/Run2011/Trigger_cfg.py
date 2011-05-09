import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(    
    '/store/user/cakir/MuHad/PAT_Data2011_PrompReco160404-163757_DESYv2/fde7716b94bbd42567b10bc1a2b9c4ae/Data2011_PrompReco160404-163757_100_1_zTl.root',
    '/store/user/cakir/MuHad/PAT_Data2011_PrompReco160404-163757_DESYv2/fde7716b94bbd42567b10bc1a2b9c4ae/Data2011_PrompReco160404-163757_101_1_68f.root',
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

from HLTrigger.HLTfilters.hltHighLevel_cfi import *


process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.25)
                                    )

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag("offlinePrimaryVertices"),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2) )

from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *
process.HBHENoiseFilter = HBHENoiseFilter.clone()

process.preselection = cms.Sequence(process.primaryVertexFilter *
                                    process.HBHENoiseFilter *
                                    process.scrapingVeto
                                    )

process.MuTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu8*'],throw = False)
process.MuHadTrigger = hltHighLevel.clone(HLTPaths = ['HLT_Mu8_HT200_v*'],throw = False)


#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
#process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")

#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------


process.SingleMu = cms.Path(#process.preselection *
                            process.MuTrigger * 
                            process.makeObjects *
                            process.oneGoodTriggerMuon *
                            process.oneGoodJet *
                            process.analyzeSUSYBjets1l_1
                            )

process.MuHad = cms.Path(#process.preselection *
                         process.MuHadTrigger * 
                         process.makeObjects *
                         process.oneGoodTriggerMuon *
                         process.oneGoodJet *
                         process.analyzeSUSYBjets1l_2
                         )
