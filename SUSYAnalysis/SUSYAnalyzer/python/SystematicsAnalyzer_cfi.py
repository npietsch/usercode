import FWCore.ParameterSet.Config as cms

#
# module to study systematics
#
analyzeSystematics = cms.EDAnalyzer("SystematicsAnalyzer",
                                    ## collections of RA4b objects
                                    jets = cms.InputTag("goodJets"),
                                    bjets = cms.InputTag("mediumTrackHighEffBjets"),  ## not needed anynore (?)
                                    muons = cms.InputTag("goodMuons"),
                                    electrons = cms.InputTag("goodElectrons"),
                                    met = cms.InputTag("patMETsPF"),
                                    ## for event weighting
                                    PVSrc = cms.InputTag("offlinePrimaryVertices"),
                                    PUInfo = cms.InputTag("addPileupInfo"),
                                    PUWeight = cms.InputTag("eventWeightPU:eventWeightPU"),
                                    RA2Weight = cms.InputTag("weightProducer:weight"),
                                    BtagEffWeights = cms.InputTag("BtagEventWeight:RA4bWeights"),
                                    BtagEffGrid = cms.InputTag("BtagEventWeight:effBTagEventGrid"),
                                    ## ...
                                    ## bool                             
                                    useEventWeight = cms.bool(False)
                                    )

