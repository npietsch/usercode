import FWCore.ParameterSet.Config as cms

process = cms.Process("Debug") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Debug.root')
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
# Load modules to create objects and filter events on reco level
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

#------------------------------------------------------------------
# Load modules to create SUSYGenEvent
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#------------------------------------------------------------------
# Load and configure modules for event weighting
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")

process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_68000.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_64600.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_71400.root"

#------------------------------------------------------------------
# Load modules for preselection
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------
# Load analyzer modules
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

# clone and configure modules to monitor b-tag efficiency weighting
process.monitorBtagWeightingMu                    = process.analyzeSUSY.clone()
process.monitorBtagWeightingMu.useBtagEventWeight = True
process.monitorBtagWeightingMu.BtagEventWeights   = "btagEventWeightMuJER:RA4bEventWeights"
process.monitorBtagWeightingMu.BtagJetWeights     = "btagEventWeightMuJER:RA4bJetWeights"

process.monitorBtagWeightingMu_2 = process.monitorBtagWeightingMu.clone()
process.monitorBtagWeightingMu_3 = process.monitorBtagWeightingMu.clone()

process.monitorBtagWeightingEl                    = process.analyzeSUSY.clone()
process.monitorBtagWeightingEl.useBtagEventWeight = True
process.monitorBtagWeightingEl.BtagEventWeights   = "btagEventWeightElJER:RA4bEventWeights"
process.monitorBtagWeightingEl.BtagJetWeights     = "btagEventWeightElJER:RA4bJetWeights"

process.monitorBtagWeightingEl_2 = process.monitorBtagWeightingEl.clone()
process.monitorBtagWeightingEl_3 = process.monitorBtagWeightingEl.clone()

process.load("SUSYAnalysis.SUSYAnalyzer.RA4MuonAnalyzer_cfi")

process.analyzeRA4Muons.jets           = "goodJets"
process.analyzeRA4Muons.muons          = "looseMuons"
process.analyzeRA4Muons.electrons      = "goodElectrons"
process.analyzeRA4Muons.met            = "scaledJetEnergy:patMETsPF"
process.analyzeRA4Muons.PVSrc          = "goodVertices"
process.analyzeRA4Muons.useEventWeight = True

process.load("SUSYAnalysis.SUSYAnalyzer.RA4ElectronAnalyzer_cfi")

process.analyzeRA4Electrons.jets           = "goodJets"
process.analyzeRA4Electrons.muons          = "goodMuons"
process.analyzeRA4Electrons.electrons      = "looseElectrons"
process.analyzeRA4Electrons.met            = "scaledJetEnergy:patMETsPF"
process.analyzeRA4Electrons.PVSrc          = "goodVertices"
process.analyzeRA4Electrons.useEventWeight = True

#------------------------------------------------------------------
# Load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------------

process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight           = process.btagEventWeight.clone()
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/TTJetsSummer11.root"

## create weights for muon selection
process.btagEventWeightMuJER                 = process.btagEventWeight.clone()
process.btagEventWeightMuJER.rootDir         = "RA4bMuTCHEM"
process.btagEventWeightMuJER.jets            = "goodJets"

## create weights for electron selection
process.btagEventWeightElJER                 = process.btagEventWeight.clone()
process.btagEventWeightElJER.rootDir         = "RA4bElTCHEM"
process.btagEventWeightElJER.jets            = "goodJets"

#--------------------------
# Selection paths
#--------------------------

process.MuonSelection1 = cms.Path(# execute producer and preselection modules
                                  process.scaledJetEnergy *
                                  process.preselectionMuHTMC2 *
                                  process.makeObjects *
                                  process.makeSUSYGenEvt *
                                  process.eventWeightPU *
                                  process.weightProducer *
                                  
                                  # execute filter and analyzer modules
                                  process.trackMuons *
                                  process.vertexSelectedGoodMuons *
                                  process.exactlyOneVertexSelectedGoodMuon *
                                  process.goodMuons *
                                  process.exactlyOneGoodMuon *
                                  process.exactlyOneVetoMuon *
                                  process.noVetoElectron *
                                  process.noGoodElectron
                                  )

process.MuonSelection2 = cms.Path(# execute producer and preselection modules
                                  process.scaledJetEnergy *
                                  process.preselectionMuHTMC2 *
                                  process.makeObjects *
                                  process.makeSUSYGenEvt *
                                  process.eventWeightPU *
                                  process.weightProducer *
                                  
                                  # execute filter and analyzer modules
                                  process.trackMuons *
                                  process.vertexSelectedGoodMuons *
                                  process.exactlyOneVertexSelectedGoodMuon *
                                  process.pfMuonConsistency *
                                  process.exactlyOneVetoMuon *
                                  process.noVetoElectron *
                                  process.noGoodElectron
                                  )


process.MuonSelection3 = cms.Path(# execute producer and preselection modules
                                  process.scaledJetEnergy *
                                  process.preselectionMuHTMC2 *
                                  process.makeObjects *
                                  process.makeSUSYGenEvt *
                                  process.eventWeightPU *
                                  process.weightProducer *
                                  
                                  # execute filter and analyzer modules
                                  process.oneGoodMuon *
                                  process.exactlyOneVetoMuon *
                                  process.exactlyOneGoodMuon *
                                  process.noVetoElectron *
                                  process.noGoodElectron
                                  )

## electron selection paths
process.ElectronSelection1 = cms.Path(# execute producer and preselection modules
                                      process.scaledJetEnergy *
                                      process.preselectionElHTMC2 *
                                      process.makeObjects *
                                      process.makeSUSYGenEvt *
                                      process.eventWeightPU *
                                      process.weightProducer *
                                      
                                      # execute filter and analyzer modules
                                      process.oneGoodElectron *
                                      process.exactlyOneVetoElectron *
                                      process.exactlyOneGoodElectron *
                                      process.noVetoMuon *
                                      process.noGoodMuon                           
                                      )
