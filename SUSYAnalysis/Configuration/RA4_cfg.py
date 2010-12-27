import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
##     '/store/mc/Summer10/TTbar/GEN-SIM-RECO/START36_V9_S09-v1/0055/36AC87AA-8C78-DF11-8C7B-0017A4770838.root'
    '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('RA.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('START38_V7::All')
process.GlobalTag.globaltag = cms.string('GR_R_38X_V8::All')

#------------------------------------------------
# Create Gen Events 
#------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------
# Gen Event Selection 
#------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="numberOfLeptons()=2")

##from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
## process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#------------------------------------------------
# RA4 Event Selection
#------------------------------------------------

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RA4Preselection_cff")

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.RA4Selection_cff")    

#------------------------------------------------
# Sequence for analysis of single objects
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.singleObjectsAnalysis_cff")

#------------------------------------------------
# Modules for analysis on generator level
#------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import analyzeSUSY

# change input tags to analyze selected Jets and MET
process.analyzeSUSY = analyzeSUSY.clone(met = "goodMETs",
                                        jets = "goodJets"
                                        )

#-------------------------------------------------
# Load any other modules you want to use
#-------------------------------------------------

# E.g: Load module to rescale jet energy by an abitrary factor 
process.load("TopAnalysis.TopUtils.JetEnergyScale_cff")

# E.g: Load modules to reconstruct ttbar events with
#      kinematic fit and anlyze hypotheses  
process.load("TopQuarkAnalyis.TopEventProducers.TtSemiLepEvtBuilder")
process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cff")

# ...

#-------------------------------------------------
# Selection paths
#-------------------------------------------------

process.RA4MuonSelection = cms.Path(process.patDefaultSequence *
                                    process.makeSUSYGenEvt *
                                    process.SUSYGenEventFilter *
                                    process.preselection *
                                    process.muonSelection *
                                    process.jetSelection *
                                    process.metSelection *
                                    process.singleObjectsAnalysis *
                                    process.muonVeto
                                    ) 

process.RA4ElecSelection = cms.Path(process.patDefaultSequence *
                                    process.makeSUSYGenEvt *
                                    process.SUSYGenEventFilter *
                                    process.preselection *
                                    process.electronSelection *
                                    process.jetSelection *
                                    process.metSelection *
                                    process.singleObjectsAnalysis *
                                    process.electronVeto
                                    )