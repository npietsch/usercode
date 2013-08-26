import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeRA4Muons = cms.EDAnalyzer("RA4MuonAnalyzer",
                                 met = cms.InputTag("patPFMETsTypeIcorrected"),
                                 jets = cms.InputTag("selectedPatJetsAK5PF"),
                                 muons = cms.InputTag("cleanPatMuons"),
                                 pfMuons = cms.InputTag("selectedPatMuonsPF"),
                                 #pfMuons = cms.InputTag("patMuonsPF"),
                                 electrons = cms.InputTag("cleanPatElectrons"),
                                 PVSrc = cms.InputTag("offlinePrimaryVertices"),
                                 PUInfo = cms.InputTag("addPileupInfo"),
                                 
                                 PUWeight = cms.InputTag("eventWeightPU:eventWeightPU"),
                                 RA2Weight = cms.InputTag("weightProducer:weight"),
                                 BtagEventWeights = cms.InputTag("btagEventWeight:RA4bEventWeights"),
                                 BtagJetWeights   = cms.InputTag("btagEventWeight:RA4bJetWeights"),
                                 btagBin = cms.int32(0),
                                 inclusiveBtagBin = cms.int32(0),
                                 
                                 useEventWeight = cms.bool(False),
                                 useBtagEventWeight = cms.bool(False),
                                 useInclusiveBtagEventWeight = cms.bool(False),
                                 
                                 TriggerWeight = cms.InputTag("TriggerWeightProducer:triggerWeight"),
                                 useTriggerEventWeight = cms.bool(False),
                                 
                                 HT0 = cms.double(375),
                                 HT1 = cms.double(650),
                                 HT2 = cms.double(650),   
                                 Y0 = cms.double(3.25),
                                 Y1 = cms.double(5.5),
                                 Y2 = cms.double(5.5)
                                 )