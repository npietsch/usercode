import FWCore.ParameterSet.Config as cms

#
# module to study systematics
#
analyzeSystematics = cms.EDAnalyzer("SystematicsAnalyzer",
                                    ## collections of RA4b objects
                                    jets = cms.InputTag("goodJets"),
                                    bjets = cms.InputTag("mediumTrackHighEffBjets"),
                                    lightJets = cms.InputTag("lightJets"),
                                    muons = cms.InputTag("goodMuons"),
                                    electrons = cms.InputTag("goodElectrons"),
                                    met = cms.InputTag("patMETsPF"),
                                    ## for event weighting
                                    PVSrc = cms.InputTag("offlinePrimaryVertices"),
                                    PUInfo = cms.InputTag("addPileupInfo"),
                                    PUWeight = cms.InputTag("eventWeightPU:eventWeightPU"),
                                    RA2Weight = cms.InputTag("weightProducer:weight"),
                                    BtagEventWeights = cms.InputTag("btagEventWeight:RA4bEventWeights"),
                                    ## ...
                                    ## bool                             
                                    useEventWeight = cms.bool(False),
                                    useBtagEventWeight = cms.bool(False),
                                    ## 0: 0 btags, 1: 1 btag; 2: 2 btags, 3: 3 or more btags 
                                    btagBin = cms.int32(0)
                                    )

