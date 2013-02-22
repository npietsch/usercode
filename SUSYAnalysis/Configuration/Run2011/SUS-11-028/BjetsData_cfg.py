import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20000),
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
process.GlobalTag.globaltag = cms.string('GR_R_42_V19::All')

#------------------------------------------------------------------
# Load modules for preselection
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#------------------------------------------------------------------
# Load analyzer modules
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")

process.load("SUSYAnalysis.SUSYAnalyzer.RA4MuonAnalyzer_cfi")

process.analyzeRA4Muons.jets           = "goodJets"
process.analyzeRA4Muons.muons          = "looseMuons"
process.analyzeRA4Muons.electrons      = "goodElectrons"
process.analyzeRA4Muons.met            = "scaledJetEnergy:patMETsPF"
process.analyzeRA4Muons.PVSrc          = "goodVertices"
process.analyzeRA4Muons.useTriggerEventWeight = True

process.load("SUSYAnalysis.SUSYAnalyzer.RA4ElectronAnalyzer_cfi")

process.analyzeRA4Electrons.jets           = "goodJets"
process.analyzeRA4Electrons.muons          = "goodMuons"
process.analyzeRA4Electrons.electrons      = "looseElectrons"
process.analyzeRA4Electrons.met            = "scaledJetEnergy:patMETsPF"
process.analyzeRA4Electrons.PVSrc          = "goodVertices"
process.analyzeRA4Electrons.useTriggerEventWeight = True

#------------------------------------------------------------------
# Load modules for trigger weighting
#------------------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.TriggerWeightProducer_cfi import *
process.TriggerWeightProducer = TriggerWeightProducer.clone()


#--------------------------
# muon selection paths
#--------------------------

## exactly 1 muon and at least 0 b-tags
process.Selection0b1m_1 = cms.Path(# execute preselection and producer modules
                                   process.preselectionMuHTAllData *
                                   process.makeObjects *
                                   process.TriggerWeightProducer *
                                   
                                   # execute filter and analyzer modules
                                   process.analyzeSUSYBjets1m_noCuts *
                                   
                                   process.MuHadSelection *
                                   process.analyzeSUSYBjets1m_preselection *
                                   process.analyzeRA4Muons *
                                   
                                   process.muonSelection*
                                   process.analyzeSUSYBjets1m_leptonSelection *
                                   
                                   process.jetSelection*
                                   process.analyzeSUSYBjets1m_jetSelection
                                   )

## exactly one muon and at least 1 btag
process.Selection1b1m_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.oneMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets1b1m_1
                                   )

## exactly one muon and at least 2 btag
process.Selection2b1m_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.twoMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets2b1m_1
                                   )

## exactly 1 muon and at least 3 b-tags
process.Selection3b1m_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets3b1m_1
                                   )

## exactly one muon and exactly 0 btags
process.Selection0b1m_2 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyZeroMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets0b1m_2
                                   )

## exactly one muon and exactly 1 btag
process.Selection1b1m_2 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets1b1m_2
                                   )

## exactly one muon and exactly 2 btags
process.Selection2b1m_2 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets2b1m_2
                                   )

#--------------------------
# electron selection paths
#--------------------------

## exactly 1 electron and at least 0 b-tags
process.Selection0b1e_1 = cms.Path(# execute preselection and producer modules
                                   process.preselectionElHTAllData *
                                   process.makeObjects *
                                   process.TriggerWeightProducer *
                                   
                                   # execute filter and analyzer modules
                                   process.analyzeSUSYBjets1e_noCuts *
                                   
                                   process.MuHadSelection *
                                   process.analyzeSUSYBjets1e_preselection *
                                   process.analyzeRA4Electrons *
                                   
                                   process.electronSelection*
                                   process.analyzeSUSYBjets1e_leptonSelection *
                                   
                                   process.jetSelection*
                                   process.analyzeSUSYBjets1e_jetSelection
                                   )

## exactly one electron and at least 1 btag
process.Selection1b1e_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTAllData *
                                   process.MuHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.oneMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets1b1e_1
                                   )

## exactly one electron and at least 2 btag
process.Selection2b1e_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTAllData *
                                   process.MuHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.twoMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets2b1e_1
                                   )

## exactly 1 electron and at least 3 b-tags
process.Selection3b1e_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTAllData *
                                   process.MuHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets3b1e_1
                                   )

## exactly one electron and exactly 0 btags
process.Selection0b1e_2 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTAllData *
                                   process.MuHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyZeroMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets0b1e_2
                                   )

## exactly one electron and exactly 1 btag
process.Selection1b1e_2 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTAllData *
                                   process.MuHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets1b1e_2
                                   )

## exactly one electron and exactly 2 btags
process.Selection2b1e_2 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTAllData *
                                   process.MuHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   
                                   # execute analyzer modules
                                   process.analyzeSUSYBjets2b1e_2
                                   )
