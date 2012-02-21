import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSY = cms.EDAnalyzer("SUSYAnalyzer",
                             met = cms.InputTag("scaledJetEnergy:patMETsPF"),
                             jets = cms.InputTag("selectedPatJetsAK5PF"),
                             lightJets = cms.InputTag("lightJets"),
                             bjets = cms.InputTag("mediumTrackHighEffBjets"),
                             muons = cms.InputTag("selectedPatMuons"),
                             electrons = cms.InputTag("selectedPatElectrons"),
                             PVSrc = cms.InputTag("offlinePrimaryVertices"),
                             PUInfo = cms.InputTag("addPileupInfo"),

                             PUWeight = cms.InputTag("eventWeightPU:eventWeightPU"),
                             RA2Weight = cms.InputTag("weightProducer:weight"),
                             BtagEventWeights = cms.InputTag("btagEventWeight:RA4bEventWeights"),
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
                
