import FWCore.ParameterSet.Config as cms

process = cms.Process("test")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/GEN-SIM-RECO/START38_V12-v1/0004/287CF124-2ED6-DF11-AA7D-002618943C22.root'
    #'/store/mc/Fall10/TTJets_TuneD6T_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0021/0EC47D66-39E3-DF11-AEDE-0026B958EFD4.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('GR_R_38X_V8::All')

#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.patMuons.isoDeposits = cms.PSet(
    tracker = cms.InputTag("muIsoDepositTk"),
    ecal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","ecal"),
    hcal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","hcal"),
    user    = cms.VInputTag(
                            cms.InputTag("muIsoDepositCalByAssociatorTowers","ho"),
                            cms.InputTag("muIsoDepositJets")
                            ),
    )

#process.patMuons.embedTrack = True
#process.patMuons.addResolutions = True
#process.patMuons.resolutions = cms.PSet(
#        default = cms.string("muonResolution")
#)

process.patJets.addTagInfos = False

#-------------------------------------------------
# Create muon collection
#-------------------------------------------------

from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.goodMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                           cut =
                                           'isGlobalMuon &'
                                           'combinedMuon.normalizedChi2 < 10 &'
                                           'combinedMuon.hitPattern.numberOfValidTrackerHits > 10 &'
                                           'combinedMuon.hitPattern.numberOfValidMuonHits > 0 &'
                                           'abs(eta) < 2.4 &'
                                           'pt > 5. &'
                                           'isTrackerMuon &'
                                           'abs(dB) < 0.02 &'
                                           'ecalIsoDeposit.candEnergy < 4 &'
                                           'hcalIsoDeposit.candEnergy < 6 &'
                                           '(trackIso+caloIso)/pt < 0.15'
                                           )

#-------------------------------------------------
# Selection path
#-------------------------------------------------

process.Test = cms.Path(process.patDefaultSequence *
                        process.goodMuons
                        )
 
