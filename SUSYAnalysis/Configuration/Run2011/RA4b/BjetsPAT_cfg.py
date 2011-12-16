import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
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

# load and configure modules for event weighting
process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_data2011_upTo178078_bin70.root"
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

# load modules to create SUSYGenEvent
process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

# load modules for preselection
process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

# load modules to create objects and filter events on reco level
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

# load modules for analysis on generator level, level of matched objects and reco-level
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

# Load and configure module to scale jet energy
process.load("SUSYAnalysis.Uncertainties.JetEnergy_cfi")

process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"

process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, 1.5, 1.5, 2.0, 2.0, -1)
process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.1, 1.1, 1.1)

process.scaledJetEnergy.jetPTThresholdForMET = 10. ## proposed on Nov 15 in RA4 meeting
process.scaledJetEnergy.maxJetEtaForMET = 4.7      ## proposed on Nov 15 in RA4 meeting

process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

#--------------------------
# muon selection paths
#--------------------------

## no btag
process.Selection1m = cms.Path(process.scaledJetEnergy *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.eventWeightPU *
                               process.weightProducer *
                               process.analyzeSUSYBjets1m_noCuts *
                               process.preselectionMuHTMC2 *
                               process.MuHadSelection *
                               process.analyzeSUSYBjets1m_preselection *
                               process.RA4MuonCollections *
                               process.RA4MuonSelection *
                               process.muonSelection*
                               process.analyzeSUSYBjets1m_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1m_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1m_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1m_metSelection *
                               process.mTSelection *
                               process.analyzeSUSYBjets1m_mTSelection
                               )
## exactly 1 btag
process.Selection1b1m_2 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1m_1
                                   
                                   )
## exactly 2 btags
process.Selection2b1m_2 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets2b1m_1
                                   )
## at least 3 btags
process.Selection3b1m_1 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1m_1
                                   )

#--------------------------
# electron selection paths
#--------------------------

## no btag
process.Selection1e = cms.Path(process.scaledJetEnergy *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.eventWeightPU *
                               process.weightProducer *
                               process.analyzeSUSYBjets1e_noCuts *
                               process.preselectionElHTMC2 *
                               process.ElHadSelection *
                               process.analyzeSUSYBjets1e_preselection *
                               process.electronSelection*
                               process.analyzeSUSYBjets1e_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1e_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1e_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1e_metSelection *
                               process.mTSelection *
                               process.analyzeSUSYBjets1e_mTSelection
                               )

## exactly 1 btag
process.Selection1b1e_2 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1e_1
                                   )

## exactly 2 btags
process.Selection2b1e_2 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets2b1e_1
                                   )

## at least 3 btags
process.Selection3b1e_1 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection *
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1e_1
                                   )
