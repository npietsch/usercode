
import FWCore.ParameterSet.Config as cms

process = cms.Process("TDR12") 

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
                            fileNames = cms.untracked.vstring("")
                            )

# load and configure modules for event weighting
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

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

#--------------------------
# selection paths
#--------------------------

process.createObjects = cms.Path(process.scaledJetEnergy *
                                 process.makeObjects
                                 )

#--------------------------
# muon paths
#--------------------------

from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

analyzeHCal.jets = "goodJets"
analyzeHCal.muons = "goodMuons"
analyzeHCal.electrons = "goodElectrons"

process.analyzeHCal1m_noCuts = analyzeHCal.clone()
process.analyzeHCal1m_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1m_lepton = analyzeHCal.clone()
process.analyzeHCal1m_jet    = analyzeHCal.clone()
process.analyzeHCal1m_HT     = analyzeHCal.clone()
process.analyzeHCal1m_met    = analyzeHCal.clone()
process.analyzeHCal1m_1b     = analyzeHCal.clone()
process.analyzeHCal1m_2b     = analyzeHCal.clone()
process.analyzeHCal1m_3b     = analyzeHCal.clone()
process.analyzeHCal1m_mt     = analyzeHCal.clone()

process.cutFlow1bMuPF = cms.Path(process.analyzeHCal1m_noCuts *
                                 
                                 process.preselectionMuHTMC2 *
                                 
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.analyzeHCal1m_lepton *
                                 
                                 process.jetSelection *
                                 process.analyzeHCal1m_jet *
                               
                                 process.HTSelection *
                                 process.analyzeHCal1m_HT *
                                 
                                 process.metSelection *
                                 process.analyzeHCal1m_met *

                                 process.oneMediumCSVBjet *
                                 process.analyzeHCal1m_1b *
                                 
                                 process.twoMediumCSVBjet *
                                 process.analyzeHCal1m_2b *
                                 
                                 process.threeMediumCSVBjet *
                                 process.analyzeHCal1m_3b *
                                                                
                                 process.mTSelection *
                                 process.analyzeHCal1m_mt
                                 )

#----------------------------
# electron paths
#----------------------------

from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

analyzeHCal.jets = "goodJets"
analyzeHCal.muons = "goodMuons"
analyzeHCal.electrons = "goodElectrons"

process.analyzeHCal1e_noCuts = analyzeHCal.clone()
process.analyzeHCal1e_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1e_lepton = analyzeHCal.clone()
process.analyzeHCal1e_jet    = analyzeHCal.clone()
process.analyzeHCal1e_HT     = analyzeHCal.clone()
process.analyzeHCal1e_met    = analyzeHCal.clone()
process.analyzeHCal1e_1b     = analyzeHCal.clone()
process.analyzeHCal1e_2b     = analyzeHCal.clone()
process.analyzeHCal1e_3b     = analyzeHCal.clone()
process.analyzeHCal1e_mt     = analyzeHCal.clone()

process.cutFlow1bElPF = cms.Path(process.analyzeHCal1e_noCuts *
                                 
                                 process.preselectionElHTMC2 *
                                 
                                 process.ElHadSelection *
                                 process.electronSelection*
                                 process.analyzeHCal1e_lepton *
                                 
                                 process.jetSelection *
                                 process.analyzeHCal1e_jet *
                               
                                 process.HTSelection *
                                 process.analyzeHCal1e_HT *

                                 process.metSelection *
                                 process.analyzeHCal1e_met *

                                 process.oneMediumCSVBjet *
                                 process.analyzeHCal1e_1b *
                                 
                                 process.twoMediumCSVBjet *
                                 process.analyzeHCal1e_2b *
                                 
                                 process.threeMediumCSVBjet *
                                 process.analyzeHCal1e_3b *
                                 
                                 process.mTSelection *
                                 process.analyzeHCal1e_mt
                                 )
