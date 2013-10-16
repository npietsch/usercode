import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSY = cms.EDAnalyzer("SUSYAnalyzer",
                             SUSYEvent = cms.InputTag("SUSYEvt"),
                             nJetsCut  = cms.vint32(0,99),
                             HTCut = cms.vdouble(0.,9999.),
                             METCut = cms.vdouble(0.,9999.),
                             YMETCut = cms.vdouble(0.,999.),
                             
                             met = cms.InputTag("patMETsPF"),
                             jets = cms.InputTag("selectedPatJetsAK5PF"),
                             lightJets = cms.InputTag("lightJets"),
                             bjets = cms.InputTag("mediumTrackHighEffBjets"),
                             muons = cms.InputTag("selectedPatMuons"),
                             electrons = cms.InputTag("selectedPatElectrons"),
                             PVSrc     = cms.InputTag("offlinePrimaryVertices"),
                             GoodPVSrc = cms.InputTag("goodVertices"),
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
                             Y2 = cms.double(5.5),

                             TTJets = cms.bool(False),
                             TtGenEvent = cms.InputTag("genEvt")
                             )
