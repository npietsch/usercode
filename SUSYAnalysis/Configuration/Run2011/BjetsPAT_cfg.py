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
#process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')
process.GlobalTag.globaltag = cms.string('START42_V13::All')

#------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
# - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
# - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-----------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

#from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
#process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

## from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
## process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")
#process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis2_cff")

#process.load("SUSYAnalysis.SUSYAnalyzer.sequences.EventTopology_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#--------------------------
# muon selection paths
#--------------------------

## no btag
process.Selection1m = cms.Path(#process.printGenParticles *
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
process.Selection1b1m_2 = cms.Path(process.makeObjects *
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
process.Selection2b1m_2 = cms.Path(process.makeObjects *
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
process.Selection3b1m_1 = cms.Path(process.makeObjects *
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
process.Selection1e = cms.Path(process.makeObjects *
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
process.Selection1b1e_2 = cms.Path(process.makeObjects *
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
process.Selection2b1e_2 = cms.Path(process.makeObjects *
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
process.Selection3b1e_1 = cms.Path(process.makeObjects *
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

## #--------------------------
## # two lepton selection
## #--------------------------

## ## no btag
## process.Selection2l = cms.Path(process.makeObjects *
##                                process.makeSUSYGenEvt *
##                                process.eventWeightPU *
##                                process.analyzeSUSYBjets2l_noCuts *
##                                process.preselectionLepHTMC *
##                                process.LepHadSelection *
##                                process.analyzeSUSYBjets2l_preselection *
##                                process.twoGoodLeptons *
##                                process.analyzeSUSYBjets2l_leptonSelection *
##                                process.jetSelection*
##                                process.analyzeSUSYBjets2l_jetSelection *
##                                process.HTSelection *
##                                process.analyzeSUSYBjets2l_HTSelection *
##                                process.metSelection *
##                                process.analyzeSUSYBjets2l_metSelection *
##                                process.analyzeEventTopology2l_3
##                                )

## #--------------------------
## # combined selection paths
## #--------------------------

## ## no btag
## process.Selection1l = cms.Path(process.makeObjects *
##                                process.makeSUSYGenEvt *
##                                process.eventWeightPU *
##                                process.analyzeSUSYBjets1l_noCuts *
##                                process.preselectionLepHTMC *
##                                process.LepHadSelection *
##                                process.analyzeSUSYBjets1l_preselection *
##                                process.leptonSelection*
##                                process.analyzeSUSYBjets1l_leptonSelection *
##                                process.jetSelection*
##                                process.analyzeSUSYBjets1l_jetSelection *
##                                process.HTSelection *
##                                process.analyzeSUSYBjets1l_HTSelection *
##                                process.metSelection *
##                                process.analyzeSUSYBjets1l_metSelection *
##                                process.analyzeEventTopology1l_3
##                                )
## ## exactly 1 btag
## process.Selection1b1l_2 = cms.Path(process.makeObjects *
##                                    process.makeSUSYGenEvt *
##                                    process.eventWeightPU *
##                                    process.preselectionLepHTMC *
##                                    process.LepHadSelection *
##                                    process.leptonSelection*
##                                    process.jetSelection *
##                                    process.exactlyOneMediumTrackHighEffBjet *
##                                    process.analyzeSUSYBjets1b1l_4 *
##                                    process.HTSelection *
##                                    process.analyzeSUSYBjets1b1l_5 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets1b1l_6 *
##                                    process.analyzeEventTopology1b1l_6
##                                    )
## ## exactly 2 btags
## process.Selection2b1l_2 = cms.Path(process.makeObjects *
##                                    process.makeSUSYGenEvt *
##                                    process.eventWeightPU *
##                                    process.preselectionLepHTMC *
##                                    process.LepHadSelection *
##                                    process.leptonSelection*
##                                    process.jetSelection *
##                                    process.exactlyTwoMediumTrackHighEffBjets *
##                                    process.analyzeSUSYBjets2b1l_4 *
##                                    process.HTSelection *
##                                    process.analyzeSUSYBjets2b1l_5 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets2b1l_6 *
##                                    process.analyzeEventTopology2b1l_6
##                                    )
## ## at least 3 btags
## process.Selection3b1l_1 = cms.Path(process.makeObjects *
##                                    process.makeSUSYGenEvt *
##                                    process.eventWeightPU *
##                                    process.preselectionLepHTMC *
##                                    process.LepHadSelection *
##                                    process.leptonSelection *
##                                    process.jetSelection *
##                                    process.threeMediumTrackHighEffBjets *
##                                    process.analyzeSUSYBjets3b1l_1 *
##                                    process.HTSelection *
##                                    process.analyzeSUSYBjets3b1l_2 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets3b1l_3 *
##                                    process.analyzeEventTopology3b1l_3
##                                    )

