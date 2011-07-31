import FWCore.ParameterSet.Config as cms

#
# module to make simple analyses of SUSY
#
analyzeRA4 = cms.EDAnalyzer("RA4Analyzer",
                            met = cms.InputTag("patMETsTypeIPF"),
                            jets = cms.InputTag("selectedPatJetsAK5PF"),
                            muons = cms.InputTag("selectedPatMuons"),
                            electrons = cms.InputTag("selectedPatElectrons")
                            )
                
