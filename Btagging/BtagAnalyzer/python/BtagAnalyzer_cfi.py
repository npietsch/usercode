import FWCore.ParameterSet.Config as cms

#
# module for b-tag study
#


analyzeBtags = cms.EDAnalyzer("BtagAnalyzer",
                              ## collections of RA4b objects
                              jets = cms.InputTag("goodJets"),
                              bjets = cms.InputTag("mediumTrackHighEffBjets"),
                              muons = cms.InputTag("goodMuons"),
                              electrons = cms.InputTag("goodElectrons"),
                              met = cms.InputTag("patMETsPF"),
                              ## collections of matched objects
                              matchedLightJets = cms.InputTag("matchedLightJets"),
                              matchedBjets = cms.InputTag("matchedBjets"),
                              ## for event and jet weighting
                              PVSrc = cms.InputTag("offlinePrimaryVertices"),
                              PUInfo = cms.InputTag("addPileupInfo"),
                              PUWeight = cms.InputTag("eventWeightPU:eventWeightPU"),
                              RA2Weight = cms.InputTag("weightProducer:weight"),
                              BtagEventWeights = cms.InputTag("btagEventWeight:RA4bEventWeights"),
                              BtagJetWeights = cms.InputTag("btagEventWeight:RA4bJetWeights"),
                              BtagJetWeightsGrid = cms.InputTag("BtagEventWeight:RA4bJetWeightsGrid"),
                              BtagEventWeightsGrid = cms.InputTag("btagEventWeight:RA4bJetWeightsGrid"),
                              BtagEffGrid = cms.InputTag("btagEventWeight:effBTagEventGrid"),
                              ## ...
                              ## bool                             
                              useEventWeight = cms.bool(False),
                              useBtagEventWeight = cms.bool(False),
                              ## 0: 0 btags, 1: 1 btag; 2: 2 btags, 3: 3 or more btags 
                              btagBin = cms.int32(0)
                              )
