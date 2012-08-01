import FWCore.ParameterSet.Config as cms

RA4bEventContent = [
    'keep *_generator_*_*',
    'keep *_TriggerResults_*_*',
    'keep *_offlineBeamSpot_*_*',
    'keep *_addPileupInfo_*_*',
    'keep *_genParticles_*_*',
    'keep *_offlinePrimaryVertices_*_*',
    'keep *_hltTriggerSummaryAOD_*_*',
    'keep *_TriggerResults_*_*',
    'keep *_selectedPatElectrons_*_*',
    'keep *_selectedPatElectronsPF_*_*',
    'keep *_selectedPatJetsPF_*_*',
    'keep *_selectedPatJetsAK5PF_*_*',
    'keep *_cleanPatJetsAK5Calo_*_*',
    'keep *_patMETsPF_*_*',
    'keep *_patMETsTypeIPF_*_*',
    'keep *_patMETsTypeIIPF_*_*',
    'keep *_genMetCalo_*_*',
    'keep *_genMetTrue_*_*',
    'keep *_patMETsAK5Calo_*_*',
    'keep *_patMETsAK5CaloTypeII_*_*',   
    'keep *_selectedPatMuons_*_*',
    'keep *_selectedPatMuonsPF_*_*',
    'keep *_generalTracks_*_*',
    "keep *_puJetId*_*_*", # input variables
    "keep *_puJetMva*_*_*", # final MVAs and working point flags   
    'keep LHEEventProduct_source_*_*'
]
