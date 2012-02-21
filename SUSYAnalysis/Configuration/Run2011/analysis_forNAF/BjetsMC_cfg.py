import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000),
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

## # load and configure modules for event weighting
## process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
## process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Run2011_bin70.root"
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

## load and configure module for PU re-weighting
process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
#process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/Data_PUDist_2011Full_bin70.root"
process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_TTJets.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/Data_PUDist_sysUp_2011Full_bin70.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/Data_PUDist_sysDown_2011Full_bin70.root"

# load modules to create SUSYGenEvent
process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

# load modules for preselection
process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

# load modules to create objects and filter events on reco level
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

# load and configure module to smear jet energy
from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.doJetSmearing = True

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

# load modules for analysis on generator level, level of matched objects and reco-level
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")


process.analyzeSUSY1b1m_4.useInclusiveBtagEventWeight = True
process.analyzeSUSY1b1m_4.inclusiveBtagBin = 1
process.analyzeSUSY1b1m_4.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

process.analyzeSUSY1b1m_6.useBtagEventWeight = True
process.analyzeSUSY1b1m_6.btagBin = 1
process.analyzeSUSY1b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

process.analyzeSUSY2b1m_6.useBtagEventWeight = True
process.analyzeSUSY2b1m_6.btagBin = 2
process.analyzeSUSY2b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

process.analyzeSUSY3b1m_6.useBtagEventWeight = True
process.analyzeSUSY3b1m_6.btagBin = 3
process.analyzeSUSY3b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

process.analyzeSUSY1b1e_4.useInclusiveBtagEventWeight = True
process.analyzeSUSY1b1e_4.inclusiveBtagBin = 1
process.analyzeSUSY1b1e_4.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

process.analyzeSUSY1b1e_6.useBtagEventWeight = True
process.analyzeSUSY1b1e_6.btagBin = 1
process.analyzeSUSY1b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

process.analyzeSUSY2b1e_6.useBtagEventWeight = True
process.analyzeSUSY2b1e_6.btagBin = 2
process.analyzeSUSY2b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

process.analyzeSUSY3b1e_6.useBtagEventWeight = True
process.analyzeSUSY3b1e_6.btagBin = 3
process.analyzeSUSY3b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight           = process.btagEventWeight.clone()
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"

## create weights for muon selection
process.btagEventWeightMuJER                 = process.btagEventWeight.clone()
process.btagEventWeightMuJER.rootDir         = "RA4bMuTCHEM3"
process.btagEventWeightMuJER.jets            = "goodJets"

## create weights for electron selection
process.btagEventWeightElJER                 = process.btagEventWeight.clone()
process.btagEventWeightElJER.rootDir         = "RA4bElTCHEM3"
process.btagEventWeightElJER.jets            = "goodJets"

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
                               process.analyzeSUSYBjets1m_metSelection #*
                               #process.mTSelection *
                               #process.analyzeSUSYBjets1m_mTSelection
                               )


## at least 1 btag
process.Selection1b1m_1 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.btagEventWeightMuJER *
                                   #process.oneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1m_4
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
                                   process.btagEventWeightMuJER *
                                   #process.exactlyOneMediumTrackHighEffBjet *
                                   #process.analyzeSUSYBjets1b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1m_6 #*
                                   #process.mTSelection *
                                   #process.analyzeSUSYBjets1b1m_1
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
                                   process.btagEventWeightMuJER *
                                   #process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_6 #*
                                   #process.mTSelection *
                                   #process.analyzeSUSYBjets2b1m_1
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
                                   process.btagEventWeightMuJER *
                                   #process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1m_6 #*
                                   #process.mTSelection *
                                   #process.analyzeSUSYBjets3b1m_1
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
                               process.analyzeSUSYBjets1e_metSelection #*
                               #process.mTSelection *
                               #process.analyzeSUSYBjets1e_mTSelection
                               )

## at least 1 btag
process.Selection1b1e_1 = cms.Path(process.scaledJetEnergy *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer *
                                   process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.btagEventWeightElJER *
                                   #process.oneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1e_4
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
                                   process.btagEventWeightElJER *
                                   #process.exactlyOneMediumTrackHighEffBjet *
                                   #process.analyzeSUSYBjets1b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1e_6 #*
                                   #process.mTSelection *
                                   #process.analyzeSUSYBjets1b1e_1
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
                                   process.btagEventWeightElJER *
                                   #process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1e_6 #*
                                   #process.mTSelection *
                                   #process.analyzeSUSYBjets2b1e_1
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
                                   process.btagEventWeightElJER *
                                   #process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1e_6 #*
                                   #process.mTSelection *
                                   #process.analyzeSUSYBjets3b1e_1
                                   )
