import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000),
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
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

process.decaySubset.fillMode = "kME"

#-----------------------------------------------------------------
# load modules to filter on member functions of TtGenEvent
#-----------------------------------------------------------------

from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *

process.semilepTtGenEventFilter = ttGenEventFilter.clone(cut="semiLeptonicChannel()=1 || semiLeptonicChannel()=2")

#-----------------------------------------------------------------
# load modules to produce TtGenEventJet collection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.TtGenEventJetsProducer_cfi")

process.produceTtGenEventJets.inputRecoJets = "goodJets"

#-----------------------------------------------------------------
# load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
process.fourMatchedGoodJets = countPatJets.clone(src = 'produceTtGenEventJets:MatchedRecoJets',
                                                 minNumber = 4
                                                 )

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
# load and configure module for analysis based on ttGenEvent
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.TtGenEventAnalyzer_cfi")

process.analyzeTtGenEvent_noCuts_1l          = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_preselection_1l    = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_leptonSelection_1l = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_jetSelection_1l    = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_HTSelection_1l     = process.analyzeTtGenEvent.clone()
process.analyzeTtGenEvent_metSelection_1l    = process.analyzeTtGenEvent.clone()

#-----------------------------------------------------------------
# load and configure  modules for analysis on reco-level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

process.analyzeSUSY.jets = "goodJets"
process.analyzeSUSY.muons = "goodMuons"
process.analyzeSUSY.electrons = "goodElectrons"
process.analyzeSUSY.met = "scaledJetEnergy:patMETsPF"
process.analyzeSUSY.useEventWeight = True

process.analyzeSUSY_noCuts_1l          = process.analyzeSUSY.clone()
process.analyzeSUSY_preselection_1l    = process.analyzeSUSY.clone()
process.analyzeSUSY_leptonSelection_1l = process.analyzeSUSY.clone()
process.analyzeSUSY_jetSelection_1l    = process.analyzeSUSY.clone()
process.analyzeSUSY_HTSelection_1l     = process.analyzeSUSY.clone()
process.analyzeSUSY_metSelection_1l    = process.analyzeSUSY.clone()

process.analyzeSUSY_noCuts_1l_match           = process.analyzeSUSY.clone()
process.analyzeSUSY_noCuts_1l_match.jets      = "produceTtGenEventJets:MatchedRecoJets"

process.analyzeSUSY_preselection_1l_match     = process.analyzeSUSY_noCuts_1l_match.clone()
process.analyzeSUSY_leptonSelection_1l_match  = process.analyzeSUSY_noCuts_1l_match.clone()
process.analyzeSUSY_jetSelection_1l_match     = process.analyzeSUSY_noCuts_1l_match.clone()
process.analyzeSUSY_HTSelection_1l_match      = process.analyzeSUSY_noCuts_1l_match.clone()
process.analyzeSUSY_metSelection_1l_match     = process.analyzeSUSY_noCuts_1l_match.clone()

process.analyzeSUSY_noCuts_1l_match2          = process.analyzeSUSY.clone()
process.analyzeSUSY_noCuts_1l_match2.jets     = "produceTtGenEventJets:MatchedRecoJets"

process.analyzeSUSY_preselection_1l_match2    = process.analyzeSUSY_noCuts_1l_match2.clone()
process.analyzeSUSY_leptonSelection_1l_match2 = process.analyzeSUSY_noCuts_1l_match2.clone()
process.analyzeSUSY_jetSelection_1l_match2    = process.analyzeSUSY_noCuts_1l_match2.clone()
process.analyzeSUSY_HTSelection_1l_match2     = process.analyzeSUSY_noCuts_1l_match2.clone()
process.analyzeSUSY_metSelection_1l_match2    = process.analyzeSUSY_noCuts_1l_match2.clone()

#-----------------------------------------------------------------
# muon selection paths
#-----------------------------------------------------------------

process.Selection0b1l = cms.Path(## producer sequences
                                 process.scaledJetEnergy *
                                 process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.makeGenEvt *
                                 process.eventWeightPU *
                                 process.weightProducer *
                                 process.produceTtGenEventJets *
                                 ## filter and analyzer sequences
                                 process.semilepTtGenEventFilter *
                                 process.analyzeTtGenEvent_noCuts_1l *
                                 process.analyzeSUSY_noCuts_1l *
                                 process.analyzeSUSY_noCuts_1l_match *
                                 
                                 process.preselectionMuHTMC2 *
                                 #process.LepHadSelection *
                                 process.analyzeTtGenEvent_preselection_1l *
                                 process.analyzeSUSY_preselection_1l *
                                 process.analyzeSUSY_preselection_1l_match *

                                 process.leptonSelection*
                                 process.analyzeTtGenEvent_leptonSelection_1l *
                                 process.analyzeSUSY_leptonSelection_1l *
                                 process.analyzeSUSY_leptonSelection_1l_match *
                                 
                                 process.jetSelection*
                                 process.analyzeTtGenEvent_jetSelection_1l *
                                 process.analyzeSUSY_jetSelection_1l *
                                 process.analyzeSUSY_jetSelection_1l_match *
                                 
                                 process.HTSelection *
                                 process.analyzeTtGenEvent_HTSelection_1l *
                                 process.analyzeSUSY_HTSelection_1l *
                                 process.analyzeSUSY_HTSelection_1l_match *
                                 
                                 process.metSelection *
                                 process.analyzeTtGenEvent_metSelection_1l *
                                 process.analyzeSUSY_metSelection_1l *
                                 process.analyzeSUSY_metSelection_1l_match
                                 )


process.Selection0b1l_2 = cms.Path(## filter and analyzer sequences
                                   process.semilepTtGenEventFilter *
                                   process.fourMatchedGoodJets *
                                   process.analyzeSUSY_noCuts_1l_match2 *
                                   
                                   process.preselectionMuHTMC2 *
                                   #process.LepHadSelection *
                                   process.analyzeSUSY_preselection_1l_match2 *
                                   
                                   process.leptonSelection*
                                   process.analyzeSUSY_leptonSelection_1l_match2 *
                                   
                                   process.jetSelection *
                                   process.analyzeSUSY_jetSelection_1l_match2 *
                                   
                                   process.HTSelection *
                                   process.analyzeSUSY_HTSelection_1l_match2 *
                                   
                                   process.metSelection *
                                   process.analyzeSUSY_metSelection_1l_match2
                                   )
