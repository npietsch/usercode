import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/044B18AA-7AD3-DF11-B099-0015170F9934.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/10103870-A0D3-DF11-9B7D-001A644EB15C.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/26D8F6C3-72D4-DF11-A377-E41F13181C30.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/5610C9C4-8DD3-DF11-85F7-001F29C99532.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/80C9D4F2-7AD3-DF11-9F24-001F29C9C5A8.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/AAC9F48B-74D3-DF11-BCF6-001F29C9C47A.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/D49478E0-88D3-DF11-A2C6-003048C56DE8.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/E002BB6E-7ED4-DF11-B0BB-E41F131816A8.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/E41850F8-73D3-DF11-85C3-001A644EB1E0.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/E4C250FC-79D3-DF11-A96A-003048C6B4E4.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/ECEF0249-68D4-DF11-A8D0-E41F13180DC8.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0001/FC16F0B4-C9D3-DF11-B1A2-00E0812C2860.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/0847325F-0DD6-DF11-B485-001A644E9812.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/5C74B460-61D7-DF11-A461-001F29C9C5A8.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/5C97AC2E-01D6-DF11-95EB-00304834FC5A.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/86C46674-09D6-DF11-B5C4-003048C6B4EA.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/B41F22A2-00D6-DF11-A419-0019BBEBB558.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/BC57A978-EED6-DF11-A8F4-003048C56D18.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/D8EFC64E-8DD6-DF11-9EBD-00215E22193E.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0004/DECFEC66-2DD6-DF11-B9A7-00E08145ED1F.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0007/448EC35B-D2D7-DF11-A282-00E08133C83B.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0020/461B7D9A-B6DF-DF11-9C3A-E41F13181A0C.root',
    '/store/mc/Fall10/LM1_SUSY_sftsht_7TeV-pythia6/AODSIM/START38_V12-v1/0023/0A1B2541-9BE3-DF11-95D4-00215E21D82E.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START311_V2A::All')


#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## Standard pat sequence
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
##removeMCMatching(process, ['All'])

#removeSpecificPATObjects(process,
#                         ['Photons'],  # 'Tau' has currently been taken out due to problems with tau discriminators
#                         outputInProcess=False)

#removeCleaning(process,
#               outputInProcess=False)

process.patJetCorrFactors.payload = 'AK5Calo'
# For data:
#process.patJetCorrFactors.levels = ['L2Relative', 'L3Absolute', 'L2L3Residual', 'L5Flavor', 'L7Parton']
# For MC:
process.patJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
#process.patJetCorrFactors.flavorType = "T"

# embed IsoDeposits
process.patMuons.isoDeposits = cms.PSet(
    tracker = cms.InputTag("muIsoDepositTk"),
    ecal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","ecal"),
    hcal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","hcal"),
    user    = cms.VInputTag(
                            cms.InputTag("muIsoDepositCalByAssociatorTowers","ho"),
                            cms.InputTag("muIsoDepositJets")
                            ),
    )
process.patMuons.usePV = False

## add PF MET
from PhysicsTools.PatAlgos.tools.metTools import addPfMET
addPfMET(process, 'PF')

## Add particle flow jets
from PhysicsTools.PatAlgos.tools.jetTools import *

addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', ['L2Relative', 'L3Absolute']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True,
                 )

## remove TagInfos from jets to run on AOD
process.patJets.addTagInfos = False

process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.electronMatch*process.patElectronIDs*process.patElectronIsolation*process.patElectrons)

process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
    simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
    simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
    simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
    simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
    simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
    simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
    simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
    simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),
)

#-------------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
#       - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
#       - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-------------------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#-----------------------------------------------------------------
# Load modules for preselection. Can be configured later
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYLooseBjetsAnalysis_cff")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#-----------------------------------------------------------------
# Selection paths. Configure your analysis here, if possible
#-----------------------------------------------------------------


## 1-lepton
process.Selection1l = cms.Path(process.patDefaultSequence *
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               #process.SUSYGenEventFilter *
                               #process.makeGenEvt *
                               #process.ttGenEventFitler *
                               process.preselection *
                               process.oneGoodMuon *
                               process.oneVetoMuon *
                               process.noVetoElectron *
                               process.oneGoodJet*
                               process.twoGoodJets *
                               process.threeGoodJets *
                               process.fourGoodJets *
                               process.metSelection
                               )
## process.Selection2l = cms.Path(process.patDefaultSequence *
##                                process.makeObjects *
##                                process.makeSUSYGenEvt *
##                                #process.SUSYGenEventFilter *
##                                #process.makeGenEvt *
##                                #process.ttGenEventFitler *
##                                process.preselection *
##                                process.oneGoodElectron *
##                                process.oneVetoElectron *
##                                process.noVetoMuon *
##                                process.oneGoodJet*
##                                process.twoGoodJets *
##                                process.threeGoodJets *
##                                process.fourGoodJets*
##                                process.metSelection 
##                                )
