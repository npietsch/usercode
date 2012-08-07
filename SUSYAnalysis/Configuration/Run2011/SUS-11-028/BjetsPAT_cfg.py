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

# load and configure modules for event weighting
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

## load and configure module for PU re-weighting
process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")

process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_68000.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_64600.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_71400.root"

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

#---------------------------------------------------------------------------------
# Load module to estimate b-tag efficiency and mis-tag rate in simulated events
#---------------------------------------------------------------------------------

process.load("TopAnalysis.TopAnalyzer.BTagEfficiencyAnalyzer_cfi")

process.analyzeBTagEfficiency.jets = "goodJets"
#process.analyzeBTagEfficiency.binsPtB     =  0.,20.,30.,40.,50.,60.,70.,80.,100.,120.,160.,210.,260.,320.,400.,500.,670.
process.analyzeBTagEfficiency.binsPtB      = 0.,20.,30.,40.,60.,80.,100.,160.,260.,400.,670.
#process.analyzeBTagEfficiency.binsPtB     =  0.,20.,30.,40.,60.,80.,120.,210.,320.,500.
process.analyzeBTagEfficiency.binsEtaB    =  0.,0.8,1.6,2.4,3.0
#process.analyzeBTagEfficiency.binsPtL     =  0.,20.,30.,40.,50.,60.,70.,80.,100.,120.,160.,210.,260.,320.,400.,500.,670.
process.analyzeBTagEfficiency.binsPtL     =  0.,20.,30.,40.,60.,80.,100.,160.,260.,400.,670.
#process.analyzeBTagEfficiency.binsPtL     =  0.,20.,30.,40.,60.,80.,120.,210.,320.,500.
process.analyzeBTagEfficiency.binsEtaL    =  0.,0.8,1.6,2.4,3.0

process.bTagEffRA4bMuTCHEM = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuTCHEM.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffRA4bMuTCHEM.bTagDiscrCut = 3.3

process.bTagEffRA4bElTCHEM = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElTCHEM.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffRA4bElTCHEM.bTagDiscrCut = 3.3

#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

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
                                   process.bTagEffRA4bMuTCHEM *
                                   process.btagEventWeightMuJER *
                                   process.monitorBtagWeightingMu *
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
                                   process.bTagEffRA4bElTCHEM*
                                   process.btagEventWeightElJER *
                                   process.monitorBtagWeightingEl *
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
