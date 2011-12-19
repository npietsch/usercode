import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSY = cms.EDAnalyzer("SUSYAnalyzer",
                             met = cms.InputTag("patMETsPF"),
                             jets = cms.InputTag("selectedPatJetsAK5PF"),
                             lightJets = cms.InputTag("lightJets"),
                             bjets = cms.InputTag("mediumTrackHighEffBjets"),
                             muons = cms.InputTag("selectedPatMuons"),
                             electrons = cms.InputTag("selectedPatElectrons"),
                             pvSrc = cms.InputTag("offlinePrimaryVertices"),
                             weight = cms.InputTag("eventWeightPU:eventWeightPU"),
                             PUInfo = cms.InputTag("addPileupInfo"),
                             RA2weight = cms.InputTag("weightProducer:weight"),
                             TriggerWeight = cms.InputTag("TriggerWeightProducer:triggerWeight"),
                             useEventWeight = cms.bool(False),
                             useTriggerEventWeight = cms.bool(False),
                             HT0 = cms.double(375),
                             HT1 = cms.double(650),
                             HT2 = cms.double(650),   
                             Y0 = cms.double(3.25),
                             Y1 = cms.double(5.5),
                             Y2 = cms.double(5.5),
                             )
                
