import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Correlation.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START42_V13::All')

#------------------------------------------------------------------
# Load and configure module to smear jet energy on reco level
#------------------------------------------------------------------

from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.doJetSmearing = True

#------------------------------------------------------------------
# Load and configure modules to create SUSYGenEvent and SUSYEvent
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("SUSYAnalysis.SUSYEventProducers.producers.SUSYEventProducer_cfi")

process.SUSYEvt.muons     = "goodMuons"
process.SUSYEvt.electrons = "goodElectrons"
process.SUSYEvt.jets      = "goodJets"
process.SUSYEvt.mets      = "scaledJetEnergy:patMETsPF"

#------------------------------------------------------------------
# Load and configure module for cross-section weighting
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#------------------------------------------------------------------
# Load and configure module for PU weighting
#------------------------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")

process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_73500_new.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_79380.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_67620.root"

#------------------------------------------------------------------
# Load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------------

process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight           = process.btagEventWeight.clone()
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/Btag_TTJetsFall11.root"

## create weights for muon selection
process.btagEventWeightMuJER                 = process.btagEventWeight.clone()
process.btagEventWeightMuJER.rootDir         = "RA4bMuTCHEM"
process.btagEventWeightMuJER.jets            = "goodJets"

## create weights for electron selection
process.btagEventWeightElJER                 = process.btagEventWeight.clone()
process.btagEventWeightElJER.rootDir         = "RA4bElTCHEM"
process.btagEventWeightElJER.jets            = "goodJets"

#------------------------------------------------------------------
# Load modules for preselection
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

#------------------------------------------------------------------
# Load analyzer modules
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.CorrelationMC_cff")

#--------------------------
# Temp
#--------------------------

process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

process.load("TopAnalysis.TopAnalyzer.BTags_cfi")

process.analyzeBTagsMu = process.analyzeBTags.clone()
process.analyzeBTagsEl = process.analyzeBTags.clone()

process.analyzeBTagsMu.src = "goodJets"
process.analyzeBTagsEl.src = "goodJets"

#--------------------------
# Selection paths
#--------------------------

## muon selection path
process.MuonSelection = cms.Path(# execute producer and preselection modules
                                 #process.printGenParticles *
                                 process.makeSUSYGenEvt *
                                 process.scaledJetEnergy *
                                 process.preselectionMuHTMC2 *
                                 process.makeObjects *
                                 process.SUSYEvt *
                                 process.eventWeightPU *
                                 process.weightProducer *
                                 
                                 # execute filter and analyzer modules
                                 process.analyzeTtGenEvent1m_noCuts *
                                 process.analyzeCorrelation1m_noCuts *
                                 
                                 process.MuHadSelection *
                                 process.analyzeTtGenEvent1m_preselection *
                                 process.analyzeCorrelation1m_preselection *
                                 
                                 process.muonSelection*
                                 process.analyzeTtGenEvent1m_leptonSelection *
                                 process.analyzeCorrelation1m_leptonSelection *
                                 
                                 # execute b-tag producer modules and analyzer modules
                                 process.btagEventWeightMuJER *

                                 process.analyzeCorrelation1m_MET60To100 *
                                 process.analyzeCorrelation1m_MET100To150 *
                                 process.analyzeCorrelation1m_MET150To200 *
                                 process.analyzeCorrelation1m_MET200To300 *
                                 process.analyzeCorrelation1m_MET300ToInf *
                                 
                                 process.analyzeCorrelation1m_nJets1To1 *
                                 process.analyzeCorrelation1m_nJets2To2 *
                                 process.analyzeCorrelation1m_nJets3To3 *
                                 process.analyzeCorrelation1m_nJets4To4 *
                                 process.analyzeCorrelation1m_nJets5To5 *
                                 process.analyzeCorrelation1m_nJets6To6 *
                                 process.analyzeCorrelation1m_nJets7To7 *

                                 process.jetSelection *
                                 process.analyzeTtGenEvent1m_jetSelection *
                                 process.analyzeCorrelation1m_jetSelection 
                                 )

## electron selection path
process.ElectronSelection = cms.Path(# execute producer and preselection modules
                                 process.makeSUSYGenEvt *
                                 process.scaledJetEnergy *
                                 process.preselectionElHTMC2 *
                                 process.makeObjects *
                                 process.SUSYEvt *
                                 process.eventWeightPU *
                                 process.weightProducer *
                                 
                                 # execute filter and analyzer modules
                                 process.analyzeTtGenEvent1e_noCuts *
                                 process.analyzeCorrelation1e_noCuts *

                                 process.ElHadSelection *
                                 process.analyzeTtGenEvent1e_preselection *
                                 process.analyzeCorrelation1e_preselection *
                                 
                                 process.electronSelection *
                                 process.analyzeTtGenEvent1e_leptonSelection *
                                 process.analyzeCorrelation1e_leptonSelection *
                                 
                                 # execute b-tag producer modules and analyzer modules
                                 process.btagEventWeightElJER *

                                 process.analyzeCorrelation1e_MET60To100 *
                                 process.analyzeCorrelation1e_MET100To150 *
                                 process.analyzeCorrelation1e_MET150To200 *
                                 process.analyzeCorrelation1e_MET200To300 *
                                 process.analyzeCorrelation1e_MET300ToInf *

                                 process.analyzeCorrelation1e_nJets1To1 *
                                 process.analyzeCorrelation1e_nJets2To2 *
                                 process.analyzeCorrelation1e_nJets3To3 *
                                 process.analyzeCorrelation1e_nJets4To4 *
                                 process.analyzeCorrelation1e_nJets5To5 *
                                 process.analyzeCorrelation1e_nJets6To6 *
                                 process.analyzeCorrelation1e_nJets7To7 *
                              
                                 process.jetSelection *
                                 process.analyzeTtGenEvent1e_leptonSelection *
                                 process.analyzeCorrelation1e_jetSelection 
                                 )
