import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
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

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

## process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")
## process.scaledJetEnergy.inputJets = "selectedPatJets"
## process.scaledJetEnergy.inputMETs = "patMETs"
## process.scaledJetEnergy.scaleType   = "jes:up"
## #process.scaledJetEnergy.scaleFactor = 0.985#flat offset when using scaleType = "top:*"
## process.scaledJetEnergy.payload = "AK5Calo"

#process.goodJets.src="scaledJetEnergy:selectedPatJets"

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------

#-------------------------
# muon selections
#-------------------------

## no btag
process.Selection1m = cms.Path(process.makeObjects *
                               #process.makeSUSYGenEvt *
                               process.analyzeSUSYBjets1m_noCuts *
                               process.preselection *
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
                               process.analyzeSUSYBjets1m_metSelection
                               )

## al least 1 btag
process.Selection1b1m_1 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.oneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1m_1 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1m_2 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1m_3
                                   )

## exactly 1 btag
process.Selection1b1m_2 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1m_6
                                   )

## al least 2 btags
process.Selection2b1m_1 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.twoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_1 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_2 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_3
                                   )

## exactly 2 btags
process.Selection2b1m_2 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_6
                                   )

## at least 3 btags
process.Selection3b1m_1 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1m_1 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1m_2 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1m_3
                                   )

## ## n-1 plots
## process.Selection1m_nminus1_leptonSelection = cms.Path(process.makeObjects *
##                                                        #process.makeSUSYGenEvt *
##                                                        process.preselection *
##                                                        process.MuHadSelection *
##                                                        process.jetSelection *
##                                                        process.HTSelection *
##                                                        process.metSelection *
##                                                        process.analyzeSUSYBjets1m_nminus1_leptonSelection
##                                                        )

## process.Selection1m_nminus1_jetSelection = cms.Path(process.makeObjects *
##                                                     #process.makeSUSYGenEvt *
##                                                     process.preselection *
##                                                     process.MuHadSelection *
##                                                     process.muonSelection *
##                                                     process.HTSelection *
##                                                     process.metSelection *
##                                                     process.analyzeSUSYBjets1m_nminus1_jetSelection
##                                                     )

## process.Selection1m_nminus1_metSelection = cms.Path(process.makeObjects *
##                                                     #process.makeSUSYGenEvt *
##                                                     process.preselection *
##                                                     process.MuHadSelection *
##                                                     process.muonSelection *
##                                                     process.jetSelection *
##                                                     process.HTSelection *
##                                                     process.analyzeSUSYBjets1m_nminus1_metSelection
##                                                     )

## process.Selection1m_nminus1_HTSelection = cms.Path(process.makeObjects *
##                                                    #process.makeSUSYGenEvt *
##                                                    process.preselection *
##                                                    process.MuHadSelection *
##                                                    process.muonSelection *
##                                                    process.jetSelection *
##                                                    process.metSelection *
##                                                    process.analyzeSUSYBjets1m_nminus1_HTSelection
##                                                    )
#-------------------------
# electron selections
#-------------------------

## no btag
process.Selection1e = cms.Path(process.makeObjects *
                               #process.makeSUSYGenEvt *
                               process.analyzeSUSYBjets1e_noCuts *
                               process.preselection2 *
                               process.ElHadSelection *
                               process.analyzeSUSYBjets1e_preselection *
                               #process.RA4ElectronCollections *
                               #process.RA4ElectronSelection *
                               process.electronSelection*
                               process.analyzeSUSYBjets1e_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1e_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1e_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1e_metSelection
                               )

## al least 1 btag
process.Selection1b1e_1 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.oneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1e_1 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1e_2 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1e_3
                                   )

## exactly 1 btag
process.Selection1b1e_2 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1e_6
                                   )

## al least 2 btags
process.Selection2b1e_1 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.twoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1e_1 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1e_2 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1e_3
                                   )

## exactly 2 btags
process.Selection2b1e_2 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1e_6
                                   )

## at least 3 btags
process.Selection3b1e_1 = cms.Path(process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselection2 *
                                   process.ElHadSelection *
                                   process.electronSelection *
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1e_1 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1e_2 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1e_3
                                   )

## ## n-1 plots
## process.Selection1e_nminus1_leptonSelection = cms.Path(process.makeObjects *
##                                                        #process.makeSUSYGenEvt *
##                                                        process.preselection2 *
##                                                        process.ElHadSelection *
##                                                        process.jetSelection *
##                                                        process.HTSelection *
##                                                        process.metSelection *
##                                                        process.analyzeSUSYBjets1e_nminus1_leptonSelection
##                                                        )

## process.Selection1e_nminus1_jetSelection = cms.Path(process.makeObjects *
##                                                     #process.makeSUSYGenEvt *
##                                                     process.preselection2 *
##                                                     process.ElHadSelection *
##                                                     process.electronSelection *
##                                                     process.HTSelection *
##                                                     process.metSelection *
##                                                     process.analyzeSUSYBjets1e_nminus1_jetSelection
##                                                     )

## process.Selection1e_nminus1_metSelection = cms.Path(process.makeObjects *
##                                                     #process.makeSUSYGenEvt *
##                                                     process.preselection2 *
##                                                     process.ElHadSelection *
##                                                     process.electronSelection *
##                                                     process.jetSelection *
##                                                     process.HTSelection *
##                                                     process.analyzeSUSYBjets1e_nminus1_metSelection
##                                                     )

## process.Selection1e_nminus1_HTSelection = cms.Path(process.makeObjects *
##                                                    #process.makeSUSYGenEvt *
##                                                    process.preselection2 *
##                                                    process.ElHadSelection *
##                                                    process.electronSelection *
##                                                    process.jetSelection *
##                                                    process.metSelection *
##                                                    process.analyzeSUSYBjets1e_nminus1_HTSelection
##                                                    )
