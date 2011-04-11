import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
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
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')

#------------------------------------------------
# Event Selection
#------------------------------------------------

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RAPreselection_cff")

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

## process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")
## process.scaledJetEnergy.inputJets = "selectedPatJets"
## process.scaledJetEnergy.inputMETs = "patMETs"
## process.scaledJetEnergy.scaleType   = "jes:up"
## #process.scaledJetEnergy.scaleFactor = 0.985#flat offset when using scaleType = "top:*"
## process.scaledJetEnergy.payload = "AK5Calo"

#process.goodJets.src="scaledJetEnergy:selectedPatJets"

process.oneLepton.electronSource = "goodElectrons"
process.oneLepton.muonSource = "goodMuons"                           
process.oneLepton.minNumber = 1

process.twoLepton.electronSource = "goodElectrons"
process.twoLepton.muonSource = "goodMuons"                           
process.twoLepton.minNumber = 2

#------------------------------------------------
# Analysis
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYLooseBjetsAnalysis_Data_cff")

#-------------------------------------------------
# Temp
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")


#-------------------------------------------------
# Selection paths 
#-------------------------------------------------



## Medium Pur pathes
process.Selection1l = cms.Path(#process.printGenParticles *
                               #process.patDefaultSequence *
                               process.makeObjects *
                               #process.makeSUSYGenEvt *
                               #process.makeGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.ttGenEventFitler *
                               process.preselectionData2 *
                               process.muonSelection *
                               process.threeGoodJets *
                               #process.analyzeSUSYBjets1l_1 *
                               #process.fourGoodJets *
                               #process.analyzeSUSYBjets1l_2 *
                               process.analyzeSUSYBjets1l_3 *
                               process.oneLepton *
                               process.analyzeSUSYBjets1l_4 *
                               process.metSelection *
                               process.analyzeSUSYBjets1l_5
                               )

process.Selection2l = cms.Path(#process.patDefaultSequence *
                               process.makeObjects *
                               #process.makeSUSYGenEvt *
                               process.preselectionData2 *
                               process.muonSelection *
                               process.threeGoodJets *
                               #process.analyzeSUSYBjets2l_1 *
                               #process.fourGoodJets *
                               #process.analyzeSUSYBjets2l_2 *
                               process.analyzeSUSYBjets2l_3 *
                               process.twoLepton *
                               process.analyzeSUSYBjets2l_4 *
                               process.metSelection *
                               process.analyzeSUSYBjets2l_5
                               )

## process.Selection1b = cms.Path(#process.patDefaultSequence *
##                                process.makeObjects *
##                                #process.makeSUSYGenEvt *
##                                process.preselectionHT *
##                                process.threeGoodJets *
##                                #process.analyzeSUSYBjets1b_1 *
##                                #process.fourGoodJets *
##                                #process.analyzeSUSYBjets1b_2 *
##                                process.oneMediumTrackHighPurBjet *
##                                process.analyzeSUSYBjets1b_3 *
##                                process.analyzeSUSYBjets1b_4 *
##                                process.metSelection *
##                                process.analyzeSUSYBjets1b_5
##                                )
##
## process.Selection2b = cms.Path(#process.patDefaultSequence *
##                                process.makeObjects *
##                                #process.makeSUSYGenEvt *
##                                process.preselectionHT *
##                                process.threeGoodJets *
##                                #process.analyzeSUSYBjets2b_1 *
##                                #process.fourGoodJets *
##                                #process.analyzeSUSYBjets2b_2 *
##                                process.twoMediumTrackHighPurBjet *
##                                process.analyzeSUSYBjets2b_3 *
##                                process.analyzeSUSYBjets2b_4 *
##                                process.metSelection *
##                                process.analyzeSUSYBjets2b_5
##                                )
##
## process.Selection3b = cms.Path(#process.patDefaultSequence *
##                                process.makeObjects *
##                                #process.makeSUSYGenEvt *
##                                process.preselectionHT *
##                                process.threeGoodJets *
##                                #process.analyzeSUSYBjets3b_1 *
##                                #process.fourGoodJets *
##                                #process.analyzeSUSYBjets3b_2 *
##                                process.threeMediumTrackHighPurBjet *
##                                process.analyzeSUSYBjets3b_3 *
##                                process.analyzeSUSYBjets3b_4 *
##                                process.metSelection *
##                                process.analyzeSUSYBjets3b_5
##                                )
##
## process.Selection4b = cms.Path(#process.patDefaultSequence *
##                                process.makeObjects *
##                                #process.makeSUSYGenEvt *
##                                process.preselectionHT *
##                                process.threeGoodJets *
##                                #process.analyzeSUSYBjets4b_1 *
##                                #process.fourGoodJets *
##                                #process.analyzeSUSYBjets4b_2 *
##                                process.fourMediumTrackHighPurBjet *
##                                process.analyzeSUSYBjets4b_3 *
##                                process.analyzeSUSYBjets4b_4 *
##                                process.metSelection *
##                                process.analyzeSUSYBjets4b_5
##                                )

process.Selection1b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets1b1l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets1b1l_2 *
                                 process.oneMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets1b1l_3 *
                                 process.oneLepton *
                                 process.analyzeSUSYBjets1b1l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets1b1l_5
                                 )

process.Selection2b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets2b1l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets2b1l_2 *
                                 process.twoMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets2b1l_3 *
                                 process.oneLepton *
                                 process.analyzeSUSYBjets2b1l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets2b1l_5
                                 )

process.Selection3b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets3b1l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets3b1l_2 *
                                 process.threeMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets3b1l_3 *
                                 process.oneLepton *
                                 process.analyzeSUSYBjets3b1l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets3b1l_5
                                 )

process.Selection4b1l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets4b1l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets4b1l_2 *
                                 process.fourMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets4b1l_3 *
                                 process.oneLepton *
                                 process.analyzeSUSYBjets4b1l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets4b1l_5
                                 )

process.Selection1b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets1b2l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets1b2l_2 *
                                 process.oneMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets1b2l_3 *
                                 process.twoLepton *
                                 process.analyzeSUSYBjets1b2l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets1b2l_5
                                 )

process.Selection2b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets2b2l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets2b2l_2 *
                                 process.twoMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets2b2l_3 *
                                 process.twoLepton *
                                 process.analyzeSUSYBjets2b2l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets2b2l_5
                                 )

process.Selection3b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets3b2l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets3b2l_2 *
                                 process.threeMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets3b2l_3 *
                                 process.twoLepton *
                                 process.analyzeSUSYBjets3b2l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets3b2l_5
                                 )

process.Selection4b2l = cms.Path(#process.patDefaultSequence *
                                 process.makeObjects *
                                 #process.makeSUSYGenEvt *
                                 process.preselectionData2 *
                                 process.muonSelection *
                                 process.threeGoodJets *
                                 #process.analyzeSUSYBjets4b2l_1 *
                                 #process.fourGoodJets *
                                 #process.analyzeSUSYBjets4b2l_2 *
                                 process.fourMediumTrackHighPurBjet *
                                 process.analyzeSUSYBjets4b2l_3 *
                                 process.twoLepton *
                                 process.analyzeSUSYBjets4b2l_4 *
                                 process.metSelection *
                                 process.analyzeSUSYBjets4b2l_5
                                 )

## Medium Eff pathes
process.Selection1l_eff = cms.Path(#process.patDefaultSequence *
                                   process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselectionData2 *
                                   process.muonSelection *
                                   process.threeGoodJets *
                                   #process.analyzeSUSYLooseBjets1l_1 *
                                   #process.fourGoodJets *
                                   #process.analyzeSUSYLooseBjets1l_2 *
                                   process.analyzeSUSYLooseBjets1l_3 *
                                   process.oneLepton *
                                   process.analyzeSUSYLooseBjets1l_4 *
                                   process.metSelection *
                                   process.analyzeSUSYLooseBjets1l_5
                                   )

process.Selection2l_eff = cms.Path(#process.patDefaultSequence *
                                   process.makeObjects *
                                   #process.makeSUSYGenEvt *
                                   process.preselectionData2 *
                                   process.muonSelection *
                                   process.threeGoodJets *
                                   #process.analyzeSUSYLooseBjets2l_1 *
                                   #process.fourGoodJets *
                                   #process.analyzeSUSYLooseBjets2l_2 *
                                   process.analyzeSUSYLooseBjets2l_3 *
                                   process.twoLepton *
                                   process.analyzeSUSYLooseBjets2l_4 *
                                   process.metSelection *
                                   process.analyzeSUSYLooseBjets2l_5
                                   )

## process.Selection1b_eff = cms.Path(#process.patDefaultSequence *
##                                    process.makeObjects *
##                                    #process.makeSUSYGenEvt *
##                                    process.preselectionHT *
##                                    process.threeGoodJets *
##                                    #process.analyzeSUSYLooseBjets1b_1 *
##                                    #process.fourGoodJets *
##                                    #process.analyzeSUSYLooseBjets1b_2 *
##                                    process.oneMediumTrackHighEffBjet *
##                                    process.analyzeSUSYLooseBjets1b_3 *
##                                    process.analyzeSUSYLooseBjets1b_4 *
##                                    process.metSelection *
##                                    process.analyzeSUSYBjets1b_5
##                                    )

## process.Selection2b_eff = cms.Path(#process.patDefaultSequence *
##                                    process.makeObjects *
##                                    #process.makeSUSYGenEvt *
##                                    process.preselectionHT *
##                                    process.threeGoodJets *
##                                    #process.analyzeSUSYLooseBjets2b_1 *
##                                    #process.fourGoodJets *
##                                    #process.analyzeSUSYLooseBjets2b_2 *
##                                    process.twoMediumTrackHighEffBjet *
##                                    process.analyzeSUSYLooseBjets2b_3 *
##                                    process.analyzeSUSYLooseBjets2b_4 *
##                                    process.metSelection *
##                                    process.analyzeSUSYLooseBjets2b_5
##                                    )


## process.Selection3b_eff = cms.Path(#process.patDefaultSequence *
##                                    process.makeObjects *
##                                    #process.makeSUSYGenEvt *
##                                    process.preselectionHT *
##                                    process.threeGoodJets *
##                                    #process.analyzeSUSYLooseBjets3b_1 *
##                                    #process.fourGoodJets *
##                                    #process.analyzeSUSYLooseBjets3b_2 *
##                                    process.threeMediumTrackHighEffBjet *
##                                    process.analyzeSUSYLooseBjets3b_3 *
##                                    process.analyzeSUSYLooseBjets3b_4 *
##                                    process.metSelection *
##                                    process.analyzeSUSYLooseBjets3b_5
##                                    )
##
## process.Selection4b_eff = cms.Path(#process.patDefaultSequence *
##                                    process.makeObjects *
##                                    #process.makeSUSYGenEvt *
##                                    process.preselectionHT *
##                                    process.threeGoodJets *
##                                    #process.analyzeSUSYLooseBjets4b_1 *
##                                    #process.fourGoodJets *
##                                    #process.analyzeSUSYLooseBjets4b_2 *
##                                    process.fourMediumTrackHighEffBjet *
##                                    process.analyzeSUSYLooseBjets4b_3 *
##                                    process.analyzeSUSYLooseBjets4b_4 *
##                                    process.metSelection *
##                                    process.analyzeSUSYLooseBjets4b_5
##                                    )

process.Selection1b1l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets1b1l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets1b1l_2 *
                                     process.oneMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets1b1l_3 *
                                     process.oneLepton *
                                     process.analyzeSUSYLooseBjets1b1l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets1b1l_5
                                     )

process.Selection2b1l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets2b1l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets2b1l_2 *
                                     process.twoMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets2b1l_3 *
                                     process.oneLepton *
                                     process.analyzeSUSYLooseBjets2b1l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets2b1l_5
                                     )

process.Selection3b1l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets3b1l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets3b1l_2 *
                                     process.threeMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets3b1l_3 *
                                     process.oneLepton *
                                     process.analyzeSUSYLooseBjets3b1l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets3b1l_5
                                     )

process.Selection4b1_effl = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets4b1l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets4b1l_2 *
                                     process.fourMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets4b1l_3 *
                                     process.oneLepton *
                                     process.analyzeSUSYLooseBjets4b1l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets4b1l_5
                                     )

process.Selection1b2l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets1b2l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets1b2l_2 *
                                     process.oneMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets1b2l_3 *
                                     process.twoLepton *
                                     process.analyzeSUSYLooseBjets1b2l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets1b2l_5
                                     )

process.Selection2b2l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets2b2l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets2b2l_2 *
                                     process.twoMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets2b2l_3 *
                                     process.twoLepton *
                                     process.analyzeSUSYLooseBjets2b2l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets2b2l_5
                                     )

process.Selection3b2l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets3b2l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets3b2l_2 *
                                     process.threeMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets3b2l_3 *
                                     process.twoLepton *
                                     process.analyzeSUSYLooseBjets3b2l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets3b2l_5
                                     )

process.Selection4b2l_eff = cms.Path(#process.patDefaultSequence *
                                     process.makeObjects *
                                     #process.makeSUSYGenEvt *
                                     process.preselectionData2 *
                                     process.muonSelection *
                                     process.threeGoodJets *
                                     #process.analyzeSUSYLooseBjets4b2l_1 *
                                     #process.fourGoodJets *
                                     #process.analyzeSUSYLooseBjets4b2l_2 *
                                     process.fourMediumTrackHighEffBjet *
                                     process.analyzeSUSYLooseBjets4b2l_3 *
                                     process.twoLepton *
                                     process.analyzeSUSYLooseBjets4b2l_4 *
                                     process.metSelection *
                                     process.analyzeSUSYLooseBjets4b2l_5
                                     )




