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
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

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

#------------------------------------------------------------------
# Load and configure modules to estimate b-tag efficiency
#------------------------------------------------------------------

process.load("TopAnalysis.TopAnalyzer.BTagEfficiencyAnalyzer_cfi")

process.analyzeBTagEfficiency.jets = "goodJets"
process.analyzeBTagEfficiency.binsPtB      = 0.,20.,30.,40.,60.,80.,100.,160.,260.,400.,670.
process.analyzeBTagEfficiency.binsEtaB    =  0.,0.8,1.6,2.4,3.0
process.analyzeBTagEfficiency.binsPtL     =  0.,20.,30.,40.,60.,80.,100.,160.,260.,400.,670.
process.analyzeBTagEfficiency.binsEtaL    =  0.,0.8,1.6,2.4,3.0

#process.analyzeBTagEfficiency.binsPtB     =  0.,20.,30.,40.,50.,60.,70.,80.,100.,120.,160.,210.,260.,320.,400.,500.,670.
#process.analyzeBTagEfficiency.binsPtL     =  0.,20.,30.,40.,50.,60.,70.,80.,100.,120.,160.,210.,260.,320.,400.,500.,670.

process.bTagEffRA4bMuTCHEM = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bMuTCHEM.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffRA4bMuTCHEM.bTagDiscrCut = 3.3

process.bTagEffRA4bMuTCHEM_2 = process.bTagEffRA4bMuTCHEM.clone()
process.bTagEffRA4bMuTCHEM_3 = process.bTagEffRA4bMuTCHEM.clone()

process.bTagEffRA4bElTCHEM = process.analyzeBTagEfficiency.clone()
process.bTagEffRA4bElTCHEM.bTagAlgo = "trackCountingHighEffBJetTags"
process.bTagEffRA4bElTCHEM.bTagDiscrCut = 3.3

process.bTagEffRA4bElTCHEM_2 = process.bTagEffRA4bElTCHEM.clone()
process.bTagEffRA4bElTCHEM_3 = process.bTagEffRA4bElTCHEM.clone()

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
# muon selection paths
#--------------------------

## exactly 1 muon and at least 0 b-tags
process.Selection0b1m_1 = cms.Path(# execute producer modules
                                   process.scaledJetEnergy *
                                   process.preselectionMuHTMC2 *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer #*
                                   
##                                    # execute filter and analyzer modules
##                                    process.analyzeSUSYBjets1m_noCuts *
                                   
##                                    process.MuHadSelection *
##                                    process.analyzeSUSYBjets1m_preselection *
                                   
##                                    process.muonSelection*
##                                    process.analyzeSUSYBjets1m_leptonSelection *
                                   
##                                    process.jetSelection*
##                                    process.analyzeSUSYBjets1m_jetSelection
                                   )

## exactly one muon and at least 1 btag
process.Selection1b1m_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionMuHTMC2 *
                                   #process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.btagEventWeightMuJER *
                                   
                                   process.bTagEffRA4bMuTCHEM *
                                   process.monitorBtagWeightingMu *
                                   
                                   process.HTSelection *
                                   
                                   process.bTagEffRA4bMuTCHEM_2 *
                                   process.monitorBtagWeightingMu_2 *
                                   #process.analyzeSUSYBjets1b1m_1*

                                   process.metSelection *

                                   process.bTagEffRA4bMuTCHEM_3 *
                                   process.monitorBtagWeightingMu_3
                                   )

## ## exactly one muon and at least 2 btag
## process.Selection2b1m_1 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionMuHTMC2 *
##                                    process.MuHadSelection *
##                                    process.muonSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightMuJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets2b1m_1
##                                    )

## ## exactly 1 muon and at least 3 b-tags
## process.Selection3b1m_1 = cms.Path(# execute filter and b-tag analyzer and b-tag producer modules
##                                    process.preselectionMuHTMC2 *
##                                    process.MuHadSelection *
##                                    process.muonSelection*
##                                    process.jetSelection *
##                                    process.bTagEffRA4bMuTCHEM *
##                                    process.btagEventWeightMuJER *
                                   
##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets3b1m_1
##                                    )

## ## exactly one muon and exactly 0 btags
## process.Selection0b1m_2 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionMuHTMC2 *
##                                    process.MuHadSelection *
##                                    process.muonSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightMuJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets0b1m_2
##                                    )

## ## exactly one muon and exactly 1 btag
## process.Selection1b1m_2 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionMuHTMC2 *
##                                    process.MuHadSelection *
##                                    process.muonSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightMuJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets1b1m_2
##                                    )

## ## exactly one muon and exactly 2 btags
## process.Selection2b1m_2 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionMuHTMC2 *
##                                    process.MuHadSelection *
##                                    process.muonSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightMuJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets2b1m_2
##                                    )


#--------------------------
# electron selection paths
#--------------------------

## ## exactly 1 electron and at least 0 b-tags
process.Selection0b1e_1 = cms.Path(# execute producer modules
                                   process.scaledJetEnergy *
                                   process.preselectionElHTMC2 *
                                   process.makeObjects *
                                   process.makeSUSYGenEvt *
                                   process.eventWeightPU *
                                   process.weightProducer #*
                                   
##                                    # execute filter and analyzer modules
##                                    process.analyzeSUSYBjets1e_noCuts *
                                   
##                                    process.ElHadSelection *
##                                    process.analyzeSUSYBjets1e_preselection *
                                   
##                                    process.electronSelection*
##                                    process.analyzeSUSYBjets1e_leptonSelection *
                                   
##                                    process.jetSelection*
##                                    process.analyzeSUSYBjets1e_jetSelection
                                   )

## exactly one electron and at least 1 btag
process.Selection1b1e_1 = cms.Path(# execute filter and b-tag producer modules
                                   process.preselectionElHTMC2 *
                                   #process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.btagEventWeightElJER *
                                   
                                   process.bTagEffRA4bElTCHEM *
                                   process.monitorBtagWeightingEl *
                                   
                                   process.HTSelection *
                                   
                                   process.bTagEffRA4bElTCHEM_2 *
                                   process.monitorBtagWeightingEl_2 *
                                   #process.analyzeSUSYBjets1b1m_1*

                                   process.metSelection *

                                   process.bTagEffRA4bElTCHEM_3 *
                                   process.monitorBtagWeightingEl_3
                                   )

## ## exactly one electron and at least 2 btag


## process.Selection2b1e_1 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionElHTMC2 *
##                                    process.ElHadSelection *
##                                    process.electronSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightElJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets2b1e_1
##                                    )

## ## exactly 1 electron and at least 3 b-tags
## process.Selection3b1e_1 = cms.Path(# execute filter and b-tag analyzer and b-tag producer modules
##                                    process.preselectionElHTMC2 *
##                                    process.ElHadSelection *
##                                    process.electronSelection*
##                                    process.jetSelection *
##                                    process.bTagEffRA4bElTCHEM *
##                                    process.btagEventWeightElJER *
                                   
##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets3b1e_1
##                                    )

## ## exactly one electron and exactly 0 btags
## process.Selection0b1e_2 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionElHTMC2 *
##                                    process.ElHadSelection *
##                                    process.electronSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightElJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets0b1e_2
##                                    )

## ## exactly one electron and exactly 1 btag
## process.Selection1b1e_2 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionElHTMC2 *
##                                    process.ElHadSelection *
##                                    process.electronSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightElJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets1b1e_2
##                                    )

## ## exactly one electron and exactly 2 btags
## process.Selection2b1e_2 = cms.Path(# execute filter and b-tag producer modules
##                                    process.preselectionElHTMC2 *
##                                    process.ElHadSelection *
##                                    process.electronSelection*
##                                    process.jetSelection *
##                                    process.btagEventWeightElJER *

##                                    # execute analyzer modules
##                                    process.analyzeSUSYBjets2b1e_2
##                                    )
