import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY for HCal Upgrade
#
analyzeHCal = cms.EDAnalyzer("HCalAnalyzer",
                             met = cms.InputTag("patMETsPF"),
                             caloMet = cms.InputTag("patMETsAK5Calo"),
                             genMet = cms.InputTag("genMetTrue"),
                             muons = cms.InputTag("selectedPatMuons"),
                             electrons = cms.InputTag("selectedPatElectrons"),
                             jets = cms.InputTag("selectedPatJetsAK5PF"),
                             genJets = cms.InputTag("selectedPatJetsAK5PF:genJets"),
                             bjets = cms.InputTag("mediumCSVBjets"),
                             caloJets = cms.InputTag("cleanPatJetsAK5Calo"),
                             PVSrc = cms.InputTag("offlinePrimaryVertices"),
                             PUInfo = cms.InputTag("addPileupInfo"),

                             usePileUp = cms.bool(False),
                             useJetID = cms.bool(True)
                             
                             )
                
