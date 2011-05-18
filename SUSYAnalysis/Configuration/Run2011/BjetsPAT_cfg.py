import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
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
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')


#-------------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
#       - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
#       - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-------------------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

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

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------


#-------------------------
# muon
#-------------------------

## no btag
process.Selection1l = cms.Path(process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.analyzeSUSYBjets1l_noCuts *
                               process.preselection *
                               process.MuHadSelection *
                               process.analyzeSUSYBjets1l_preselection *
                               process.RA4MuonCollections *
                               process.RA4MuonSelection *
                               process.muonSelection*
                               process.analyzeSUSYBjets1l_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1l_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1l_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1l_metSelection
                               )

## 1 btag
process.Selection1b1l = cms.Path(process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.jetSelection *
                                 process.oneMediumTrackHighEffBjet *
                                 process.analyzeSUSYBjets1b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets1b1l_2
                                 )

## 2 btags
process.Selection2b1l = cms.Path(process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.jetSelection *
                                 process.oneMediumTrackHighEffBjet *
                                 process.analyzeSUSYBjets2b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets2b1l_2
                                 )

## 3 btags
process.Selection3b1l = cms.Path(process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.jetSelection *
                                 process.oneMediumTrackHighEffBjet *
                                 process.analyzeSUSYBjets3b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets3b1l_2
                                 )

## 4 btags
process.Selection4b1l = cms.Path(process.makeObjects *
                                 process.makeSUSYGenEvt *
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.jetSelection *
                                 process.oneMediumTrackHighEffBjet *
                                 process.analyzeSUSYBjets4b1l_1 *
                                 process.HTSelection *
                                 process.metSelection *
                                 process.analyzeSUSYBjets4b1l_2
                                 )

## n-1 plots
process.Selection1l_nminus1_leptonSelection = cms.Path(process.makeObjects *
                                                       process.makeSUSYGenEvt *
                                                       process.preselection *
                                                       process.MuHadSelection *
                                                       process.preselection *
                                                       process.jetSelection *
                                                       process.HTSelection *
                                                       process.metSelection *
                                                       process.analyzeSUSYBjets1l_nminus1_leptonSelection
                                                       )

process.Selection1l_nminus1_jetSelection = cms.Path(process.makeObjects *
                                                    process.makeSUSYGenEvt *
                                                    process.preselection *
                                                    process.MuHadSelection *
                                                    process.preselection *
                                                    process.muonSelection *
                                                    process.HTSelection *
                                                    process.metSelection *
                                                    process.analyzeSUSYBjets1l_nminus1_jetSelection
                                                    )

process.Selection1l_nminus1_metSelection = cms.Path(process.makeObjects *
                                                    process.makeSUSYGenEvt *
                                                    process.preselection *
                                                    process.MuHadSelection *
                                                    process.preselection *
                                                    process.muonSelection *
                                                    process.jetSelection *
                                                    process.HTSelection *
                                                    process.analyzeSUSYBjets1l_nminus1_metSelection
                                                    )

process.Selection1l_nminus1_HTSelection = cms.Path(process.makeObjects *
                                                   process.makeSUSYGenEvt *
                                                   process.preselection *
                                                   process.MuHadSelection *
                                                   process.preselection *
                                                   process.muonSelection *
                                                   process.jetSelection *
                                                   process.metSelection *
                                                   process.analyzeSUSYBjets1l_nminus1_HTSelection
                                                   )
#-------------------------
# electron
#-------------------------

## no btag
process.ElectronSelection1l = cms.Path(process.makeObjects *
                                       process.makeSUSYGenEvt *
                                       process.analyzeSUSYBjets1l_noCuts_2 *
                                       process.preselection *
                                       process.analyzeSUSYBjets1l_preselection_2 *
                                       process.electronSelection*
                                       process.analyzeSUSYBjets1l_leptonSelection_2 *
                                       process.jetSelection*
                                       process.analyzeSUSYBjets1l_jetSelection_2 *
                                       process.HTSelection *
                                       process.analyzeSUSYBjets1l_HTSelection_2 *
                                       process.metSelection *
                                       process.analyzeSUSYBjets1l_metSelection_2
                                       )

process.ElectronSelection1b1l = cms.Path(process.makeObjects *
                                         process.makeSUSYGenEvt *
                                         process.electronSelection*
                                         process.jetSelection *
                                         process.oneMediumTrackHighEffBjet *
                                         process.analyzeSUSYBjets1b1l_3 *
                                         process.HTSelection *
                                         process.metSelection *
                                         process.analyzeSUSYBjets1b1l_4
                                         )

process.ElectronSelection2b1l = cms.Path(process.makeObjects *
                                         process.makeSUSYGenEvt *
                                         process.electronSelection*
                                         process.jetSelection *
                                         process.oneMediumTrackHighEffBjet *
                                         process.analyzeSUSYBjets2b1l_3 *
                                         process.HTSelection *
                                         process.metSelection *
                                         process.analyzeSUSYBjets2b1l_4
                                         )

process.ElectronSelection3b1l = cms.Path(process.makeObjects *
                                         process.makeSUSYGenEvt *
                                         process.electronSelection*
                                         process.jetSelection *
                                         process.oneMediumTrackHighEffBjet *
                                         process.analyzeSUSYBjets3b1l_3 *
                                         process.HTSelection *
                                         process.metSelection *
                                         process.analyzeSUSYBjets3b1l_4
                                         )

process.ElectronSelection4b1l = cms.Path(process.makeObjects *
                                         process.makeSUSYGenEvt *
                                         process.electronSelection*
                                         process.jetSelection *
                                         process.oneMediumTrackHighEffBjet *
                                         process.analyzeSUSYBjets4b1l_3 *
                                         process.HTSelection *
                                         process.metSelection *
                                         process.analyzeSUSYBjets4b1l_4
                                         )
