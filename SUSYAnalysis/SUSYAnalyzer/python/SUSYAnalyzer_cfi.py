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
                             useEventWeight = cms.bool(False),
                             RA2weight = cms.InputTag("weightProducer:weight")
                             )
                
