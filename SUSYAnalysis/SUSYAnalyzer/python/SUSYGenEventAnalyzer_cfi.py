import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeSUSYGenEvt = cms.EDAnalyzer("SUSYGenEventAnalyzer",
                                   susyGenEvent = cms.InputTag("SUSYGenEvt"),
                                   initSubset = cms.InputTag("SUSYInitSubset"),
                                   jets = cms.InputTag("selectedPatJets"),
                                   bjets = cms.InputTag("selectedPatJets"),
                                   matchedbjets = cms.InputTag("selectedPatJets"),
                                   matchedqjets = cms.InputTag("selectedPatJets"),
                                   matchedmuons = cms.InputTag("selectedPatMuons"),
                                   matchedelectrons = cms.InputTag("selectedPatElectrons"),
                                   met = cms.InputTag("patMETs")
                                   )

