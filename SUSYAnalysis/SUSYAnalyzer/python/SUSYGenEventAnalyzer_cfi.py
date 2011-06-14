import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSYGenEvt = cms.EDAnalyzer("SUSYGenEventAnalyzer",
                                   susyGenEvent = cms.InputTag("SUSYGenEvt"),
                                   initSubset = cms.InputTag("SUSYInitSubset"),
                                   jets = cms.InputTag("selectedPatJetsAK5PF"),
                                   bjets = cms.InputTag("selectedPatJetsAK5PF"),
                                   matchedbjets = cms.InputTag("selectedPatJetsAK5PF"),
                                   matchedqjets = cms.InputTag("selectedPatJetsAK5PF"),
                                   matchedmuons = cms.InputTag("selectedPatMuons"),
                                   matchedelectrons = cms.InputTag("selectedPatElectrons"),
                                   met = cms.InputTag("patMETsPF")
                                   )

