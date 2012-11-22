import FWCore.ParameterSet.Config as cms

process = cms.Process("nJets") 

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
                                   fileName = cms.string('nJets.root')
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
# Load and configure modules to create SUSYGenEvent and SUSYEvent
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("SUSYAnalysis.SUSYEventProducers.producers.SUSYEventProducer_cfi")

process.SUSYEvt.muons     = "goodMuons"
process.SUSYEvt.electrons = "goodElectrons"
process.SUSYEvt.jets      = "goodJets"

#---------------------------------------------------------------------------
# load and configure module to create TtGenEvent
#---------------------------------------------------------------------------

process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")
process.decaySubset.fillMode = "kME"

#---------------------------------------------------------------------------
# load and configure modules to filter on member functions of TtGenEvent
#---------------------------------------------------------------------------

process.load("TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi")

process.SemiLepTtGenEventFilter = process.ttGenEventFilter.clone(cut="semiLeptonicChannel()=1 || semiLeptonicChannel()=2")
process.DiLepTtGenEventFilter   = process.ttGenEventFilter.clone(cut="isFullLeptonic() && fullLeptonicChannel.first!=3 && fullLeptonicChannel.second!=3 ")
process.FullHadTtGenEventFilter = process.ttGenEventFilter.clone(cut="isFullHadronic()")
process.TauTtGenEventFilter     = process.ttGenEventFilter.clone(cut="semiLeptonicChannel()=3 || fullLeptonicChannel.first=3 || fullLeptonicChannel.second=3")

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

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.Correlation_cff")

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

## lepton selection path for all SemiLep TTJets
process.LeptonSelection_SemiLep = cms.Path(# execute producer and preselection modules
                                          process.makeGenEvt *
                                          process.makeSUSYGenEvt *
                                          process.SemiLepTtGenEventFilter *
                                          process.scaledJetEnergy *
                                          process.preselectionLepHTMC2 *
                                          process.makeObjects *
                                          process.SUSYEvt *
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          
                                          # execute filter and analyzer modules
                                          process.leptonSelection *
                                          process.threeGoodJets *
                                          process.analyzeCorrelation1l_HT200To300
                                          )
