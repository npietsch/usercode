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
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START42_V13::All')

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1000_1_TsG.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1001_1_7vH.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_100_1_PkZ.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1002_2_rDz.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1003_1_8PY.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1004_1_cjk.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1005_3_eV3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1006_1_85u.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1007_1_2vX.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1008_1_cf2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1009_1_ir8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1010_1_Ecn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1011_1_s4J.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_101_1_grq.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1012_1_jXR.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1013_1_lyy.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1014_1_qwA.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1015_1_iQ8.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1016_1_5V2.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1017_1_26Y.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1018_1_WGj.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1019_1_FKh.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_10_1_Yso.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1020_1_yhn.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1021_1_Ebx.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_102_1_Vg3.root',
'/store/user/npietsch/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11_TTJets/9e447c71221b3624d9d719e3ff15c500/Fall11_1022_1_581.root'
)
)

#-----------------------------------------------------------------
# load and configure modules for event weighting
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#-----------------------------------------------------------------
# load and configure module for PU re-weighting
#-----------------------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")

process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_68000.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_64600.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_71400.root"

#-----------------------------------------------------------------
# load modules to create SUSY- and ttGenEvent
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#-----------------------------------------------------------------
# load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#-----------------------------------------------------------------
# load and configure module to smear jet energy
#-----------------------------------------------------------------

from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.doJetSmearing = True

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

#-----------------------------------------------------------------
# load and configure modules for analysis on generator level,
# level of matched objects and reco-level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

process.analyzeSUSY1b1m_4.useInclusiveBtagEventWeight = True
process.analyzeSUSY1b1m_4.inclusiveBtagBin = 1
process.analyzeSUSY1b1m_4.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
process.analyzeSUSY1b1m_4.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

process.analyzeSUSY1b1m_6.useBtagEventWeight = True
process.analyzeSUSY1b1m_6.btagBin = 1
process.analyzeSUSY1b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
process.analyzeSUSY1b1m_6.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

process.monitorBtagWeightingMu                  = process.analyzeSUSY1b1m_6.clone()
process.monitorBtagWeightingMu.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
process.monitorBtagWeightingMu.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

process.analyzeSUSY2b1m_6.useBtagEventWeight = True
process.analyzeSUSY2b1m_6.btagBin = 2
process.analyzeSUSY2b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
process.analyzeSUSY2b1m_6.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

process.analyzeSUSY3b1m_6.useBtagEventWeight = True
process.analyzeSUSY3b1m_6.btagBin = 3
process.analyzeSUSY3b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
process.analyzeSUSY3b1m_6.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

process.analyzeSUSY1b1e_4.useInclusiveBtagEventWeight = True
process.analyzeSUSY1b1e_4.inclusiveBtagBin = 1
process.analyzeSUSY1b1e_4.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
process.analyzeSUSY1b1e_4.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

process.analyzeSUSY1b1e_6.useBtagEventWeight = True
process.analyzeSUSY1b1e_6.btagBin = 1
process.analyzeSUSY1b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
process.analyzeSUSY1b1e_6.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

process.monitorBtagWeightingEl                  = process.analyzeSUSY1b1m_6.clone()
process.monitorBtagWeightingEl.BtagEventWeights = "btagEventWeightElJER:RA4bEventWeights"
process.monitorBtagWeightingEl.BtagJetWeights   = "btagEventWeightElJER:RA4bJetWeights"

process.analyzeSUSY2b1e_6.useBtagEventWeight = True
process.analyzeSUSY2b1e_6.btagBin = 2
process.analyzeSUSY2b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
process.analyzeSUSY2b1e_6.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

process.analyzeSUSY3b1e_6.useBtagEventWeight = True
process.analyzeSUSY3b1e_6.btagBin = 3
process.analyzeSUSY3b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
process.analyzeSUSY3b1e_6.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

#-----------------------------------------------------------------
# load and configure module for analysis based on ttGenEvent
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.TtGenEventAnalyzer_cfi")

process.analyzeTtGenEvent_noCuts_1m          = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_preselection_1m    = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_leptonSelection_1m = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_jetSelection_1m    = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_HTSelection_1m     = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_metSelection_1m    = process.analyzeTtGenEvent.clone()

process.analyzeTtGenEvent_noCuts_1e          = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_preselection_1e    = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_leptonSelection_1e = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_jetSelection_1e    = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_HTSelection_1e     = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_metSelection_1e    = process.analyzeTtGenEvent.clone()

#-----------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#-----------------------------------------------------------------

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

#-----------------------------------------------------------------
# muon selection paths
#-----------------------------------------------------------------

process.Selection0b1m_1 = cms.Path(## producer sequences
                                   process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.makeGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   ## filter and analyzer sequences
                                   process.analyzeSUSY1m_noCuts *
                                   process.analyzeTtGenEvent_noCuts_1m *
                                   process.preselectionMuHTMC2 *
                                   process.analyzeSUSY1m_preselection *
                                   process.analyzeTtGenEvent_preselection_1m *
                                   process.muonSelection*
                                   process.analyzeSUSY1m_leptonSelection *
                                   process.analyzeTtGenEvent_leptonSelection_1m *
                                   process.jetSelection*
                                   process.analyzeSUSY1m_jetSelection *
                                   process.analyzeTtGenEvent_jetSelection_1m *
                                   process.HTSelection *
                                   process.analyzeSUSY1m_HTSelection *
                                   process.analyzeTtGenEvent_HTSelection_1m *
                                   process.metSelection *
                                   process.analyzeSUSY1m_metSelection *
                                   process.analyzeTtGenEvent_metSelection_1m
                                   )
