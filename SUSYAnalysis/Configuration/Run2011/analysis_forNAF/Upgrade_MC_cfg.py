import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Upgrade.root')
                                   )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( "")
                            )

# load and configure modules for event weighting
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

## load and configure module for PU re-weighting
process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_TTJets.root"

# load modules for preselection
process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

# load modules to create objects and filter events on reco level
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

# load and configure module to smear jet energy
from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.doJetSmearing = True

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeight.jets      = "goodJets"

process.btagEventWeightMu         = process.btagEventWeight.clone( rootDir = "RA4bMuTCHEM3" )
process.btagEventWeightEl         = process.btagEventWeight.clone( rootDir = "RA4bElTCHEM3" )


#--------------------------
# selection paths
#--------------------------

process.createObjects = cms.Path(process.scaledJetEnergy *
                                 process.makeObjects *
                                 process.eventWeightPU *
                                 process.weightProducer
                                 )

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.met = "scaledJetEnergy:patMETsPF"
analyzeSUSY.useEventWeight = True

#--------------------------
# muon selection paths
#--------------------------

process.analyzeSUSY1b1m_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1b1m_1 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_2 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_3 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_4 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_5 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_mtSelection = analyzeSUSY.clone()

process.analyzeSUSY1b1m_6 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_6.useInclusiveBtagEventWeight = True
process.analyzeSUSY1b1m_6.inclusiveBtagBin = 1
process.analyzeSUSY1b1m_6.BtagEventWeights = "btagEventWeightMu:RA4bSFEventWeights"
process.analyzeSUSY1b1m_6.BtagJetWeights   = "btagEventWeightMu:RA4bSFJetWeights"

process.cutFlowMu = cms.Path(process.analyzeSUSY1b1m_noCuts *
                             process.preselectionMuHTMC2 *
                             process.analyzeSUSY1b1m_1 *
                             process.MuHadSelection *
                             process.muonSelection*
                             process.analyzeSUSY1b1m_2 *
                             process.jetSelection *
                             process.analyzeSUSY1b1m_3 *
                             process.HTSelection *
                             process.analyzeSUSY1b1m_4 *
                             process.metSelection *
                             process.analyzeSUSY1b1m_5 *
                             process.mTSelection *
                             process.analyzeSUSY1b1m_mtSelection
                             )

process.selection1m = cms.Sequence(process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection *
                                   process.jetSelection *
                                   process.btagEventWeightMu
                                   )

process.analysis1b1m = cms.Path(process.selection1m *
                                process.analyzeSUSY1b1m_6
                                )


#--------------------------
# electron selection paths
#--------------------------

process.analyzeSUSY1b1e_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1b1e_1 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_2 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_3 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_4 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_5 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_mtSelection = analyzeSUSY.clone()

process.analyzeSUSY1b1e_6 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_6.useInclusiveBtagEventWeight = True
process.analyzeSUSY1b1e_6.inclusiveBtagBin = 1
process.analyzeSUSY1b1e_6.BtagEventWeights = "btagEventWeightEl:RA4bSFEventWeights"
process.analyzeSUSY1b1e_6.BtagJetWeights   = "btagEventWeightEl:RA4bSFJetWeights"

process.cutFlowEle = cms.Path(process.analyzeSUSY1b1e_noCuts *
                              process.preselectionElHTMC2 *
                              process.analyzeSUSY1b1e_1 *
                              process.ElHadSelection *
                              process.electronSelection*
                              process.analyzeSUSY1b1e_2 *
                              process.jetSelection *
                              process.analyzeSUSY1b1e_3 *
                              process.HTSelection *
                              process.analyzeSUSY1b1e_4 *
                              process.metSelection *
                              process.analyzeSUSY1b1e_5 *
                              process.mTSelection *
                              process.analyzeSUSY1b1e_mtSelection
                              )

process.selection1e = cms.Sequence(process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.btagEventWeightEl
                                   )


process.analysis1b1e = cms.Path(process.selection1e *
                                process.analyzeSUSY1b1e_6
                                )
