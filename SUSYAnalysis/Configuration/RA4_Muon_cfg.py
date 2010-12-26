import FWCore.ParameterSet.Config as cms

process = cms.Process("Preselection")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'/store/mc/Summer10/TTbar/GEN-SIM-RECO/START36_V9_S09-v1/0063/308A872D-F578-DF11-96F3-0017A4770020.root'

    '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root'

    
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0026/B27B78AC-1548-DF11-8117-E41F13181AF8.root',
    
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0073/B4D5AD28-2D4B-DF11-B5DD-00215E21D540.root',
    
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/0EA67C6B-2648-DF11-A71C-00215E21DA50.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/123A11CA-2248-DF11-AA3D-00215E2227D8.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/1841D0EC-2448-DF11-A6D3-00215E2218F6.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/1AA5DB69-2748-DF11-84B3-E41F1318170C.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/1AEC6181-1A48-DF11-ABA6-00215E21DC72.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/1E473D2E-1F48-DF11-9C92-00215E222712.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/200BD6CF-2348-DF11-BB38-00215E2223D6.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/280AEE81-1B48-DF11-9720-00215E21F214.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/2AC981DB-1C48-DF11-9351-00215E21D4D4.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/2C0D4F08-1E48-DF11-9B05-00215E2211D6.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/3222AB09-1E48-DF11-B2C5-00215E22190E.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/32697E42-2548-DF11-80E7-E41F13181AF8.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/385AB567-2748-DF11-AC05-00215E93EFCC.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/3E63583F-2548-DF11-AE49-E41F131815FC.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/40D04607-1E48-DF11-88BE-00215E222382.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/46475E7A-2048-DF11-89B0-00215E22223E.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/4CC9F5D6-1C48-DF11-8C48-00215E21D47A.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/504FEC84-1B48-DF11-AB19-00215E21D8CA.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/585BBC29-1F48-DF11-97CD-E41F13181668.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/5A034B55-1F48-DF11-BE48-00215E21DC72.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/5C52E685-1B48-DF11-AA6F-00215E21D702.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/5C9085A7-2148-DF11-80CB-00215E222712.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/6246A356-2048-DF11-8F17-00215E222742.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/68A90139-1C48-DF11-8EA7-00215E222316.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/68D646EE-1C48-DF11-A42E-00215E2205AC.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/68E492D5-1C48-DF11-A7A5-00215E21D8CA.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/6A52EAED-2348-DF11-8697-00215E2212D2.root',
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/6AE070DB-1C48-DF11-9153-00215E2227D8.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/6E81BF2B-1F48-DF11-9DB7-00215E221812.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/76F6E44B-2548-DF11-9531-00215E222394.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/7C75C753-1F48-DF11-B50A-00215E221170.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/7CB0E7C4-1B48-DF11-A316-00215E21DAB0.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/7E4B6F6D-2648-DF11-9B06-00215E222244.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/8C9EEE0D-1E48-DF11-BE13-00215E21F214.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/90965058-2048-DF11-B617-00215E2212D2.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/90A5F6CD-2248-DF11-8B8A-E41F13181594.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/92E90302-1E48-DF11-9B06-00215E2227D8.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/9683C6D9-1C48-DF11-B070-00215E22190E.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/98A470C9-2348-DF11-8823-00215E2218F6.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/9A9573CA-2248-DF11-8F49-E41F13181D48.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/A2722709-1E48-DF11-ABC0-00215E21D972.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/A2BF38C9-2248-DF11-9C89-00215E21DCA2.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/A848EFA7-2148-DF11-851C-00215E222712.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/AC217E56-2048-DF11-A246-00215E222316.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/AE4FD327-1F48-DF11-9018-00215E2227D8.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/B68D9353-1A48-DF11-A87D-E41F13181598.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/BA080E24-1948-DF11-87E1-E41F13181568.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/BCC074B0-1B48-DF11-9BC6-00215E2205AC.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C2EAD854-1F48-DF11-BE94-00215E2223B2.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C4965A08-1E48-DF11-A1E0-00215E93EF9C.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C6765904-1E48-DF11-8D43-00215E21DC1E.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C6B63758-1F48-DF11-BA03-00215E21DC1E.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/C81088D6-1C48-DF11-A9A8-00215E222316.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/CE6A4C0B-1E48-DF11-A153-00215E221158.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D2E1A306-1E48-DF11-AA62-00215E222286.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D4DAE8A4-2148-DF11-855B-00215E21DD32.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D867DC8A-1B48-DF11-AE5E-00215E222286.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/D8C41ADA-1C48-DF11-B199-00215E221B48.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/DAC3277D-2048-DF11-861A-00215E222382.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/DE8C3F84-1B48-DF11-B7C8-00215E2212D2.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/E0748A3F-2648-DF11-B4CA-00215E21DB76.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/E274B6DE-1C48-DF11-BF41-00215E21F214.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/E616FA77-2148-DF11-91D9-00215E222316.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/EE6A2E5D-1F48-DF11-8D26-00215E222382.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/F2D79107-1E48-DF11-A41E-00215E21DD0E.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/F2DE9158-2048-DF11-B19D-00215E222382.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/FC2646A6-2148-DF11-90E1-00215E21DD32.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/FC386523-1948-DF11-A821-00215E22053A.root'
##     '/store/mc/Spring10/LM1/GEN-SIM-RECO/START3X_V26_S09-v1/0027/FC44C654-2048-DF11-A3AA-00215E2211F4.root'

    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('RA.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('START38_V7::All')
process.GlobalTag.globaltag = cms.string('GR_R_38X_V8::All')

#-------------------------------------------------------------
# Basic sequenzes
#-------------------------------------------------------------

#HLT
#import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
#process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
#from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed

#process.hltbits = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('0 AND NOT (36 OR 37 OR 38 OR 39)'))

#from HLTrigger.HLTfilters.hltHighLevelDev_cfi import hltHighLevelDev
#process.physDecl = hltHighLevelDev.clone(HLTPaths = ['HLT_PhysicsDeclared'], HLTPathsPrescales = [1])
#process.trigger = hltHighLevelDev.clone(HLTPaths = ['HLT_Mu9'], HLTPathsPrescales = [1])

process.load("TopAnalysis/TopFilter/sequences/triggerFilter_cff")

#Filter
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.25)
                                    )
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
             vertexCollection = cms.InputTag('offlinePrimaryVertices'),
             minimumNDOF = cms.uint32(4) ,
             maxAbsZ = cms.double(24),
             maxd0 = cms.double(2) )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## std sequence for pat
process.load("PhysicsTools.PatAlgos.patSequences_cff")

#from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput
#run36xOn35xInput(process)

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
removeMCMatching(process, ['All'])
removeSpecificPATObjects(process,
                         ['Photons','Taus'],
                         outputInProcess=False)
removeCleaning(process,
               outputInProcess=False)

## add PF jets and MET
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5', 'PF'),
                 doType1MET   = False,
                 doL1Cleaning = True,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True,
                 ) 
from PhysicsTools.PatAlgos.tools.metTools import addPfMET
addPfMET(process, 'PF')

## remove TagInfos from jets
process.patJets.addTagInfos = False
process.patJetsAK5PF.addTagInfos = False

## use the correct jet energy corrections
process.patJetCorrFactors.corrSample = "Spring10"
process.patJetCorrFactors.sampleType = "ttbar"
process.patJetCorrFactorsAK5PF.corrSample = "Spring10"
process.patJetCorrFactorsAK5PF.sampleType = "ttbar"

#calculate impact parameter w.r.t beam spot (instead of primary vertex)
process.patMuons.usePV = False

process.load("TopAnalysis.TopAnalyzer.simpleEleIdSequence_cff")

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectronIsolation*process.patElectrons)

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

#-------------------------------------------------
# lepton collections 
#-------------------------------------------------

## create good muon collection
from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *

process.goodMuons = cleanPatMuons.clone(preselection =
                                        # Global Muon Prompt Tight !!
                                        'isGlobalMuon &'
                                        'globalTrack.normalizedChi2 < 10.0 &'
                                        'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                        # other requirements 
                                        'isTrackerMuon &'
                                        'pt > 20. &'
                                        'abs(eta) < 2.1 &'
                                        '(trackIso+caloIso)/pt < 0.05 &'
                                        'abs(dB) < 0.02 &' # !! 'abs(track.d0) < 0.02 &' # abs(dB) = abs(dxy(Beam Spot))??
                                        'innerTrack.hitPattern.numberOfValidHits > 10' # to be changed to ValidTrackerHits!
                                        )

## Check good Muons for overlap with jets 
process.goodMuons.checkOverlaps = cms.PSet(
    jets = cms.PSet(src       = cms.InputTag("goodJets"),
                    algorithm = cms.string("byDeltaR"),
                    preselection        = cms.string(""),
                    deltaR              = cms.double(0.3),
                    checkRecoComponents = cms.bool(False),
                    pairCut             = cms.string(""),
                    requireNoOverlaps   = cms.bool(True),
                    )
    )

## create good electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.goodElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                                   cut =
                                                   'pt > 20. &'
                                                   'abs(eta) < 2.4 &'
                                                   'electronID(\"simpleEleId80relIso\")=7 '
                                                   #'(abs(eta) < 1.47 | abs(eta) > 1.507) $'
                                                   )

#------------------------------------------------
# lepton-veto collections
#------------------------------------------------


## create veto-muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.vetoMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                           cut =
                                           'isGlobalMuon &'
                                           'pt > 10. &'
                                           'abs(eta) < 2.5 &'
                                           '(trackIso+caloIso)/pt <  0.2'
                                           )

## create veto-electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.vetoElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                                   cut =
                                                   'pt > 15. &'
                                                   'abs(eta) < 2.5 &'
                                                   #'(abs(eta) < 1.47 | abs(eta) > 1.507) $'
                                                   '(dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/et<0.2 '
                                                   )

#------------------------------------------------
# jet collection
#------------------------------------------------

## create jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
process.goodJets = selectedPatJets.clone(src = 'selectedPatJets',
                                     cut =
                                     'abs(eta) < 2.4 &'
                                     'pt > 30. &'
                                     'emEnergyFraction > 0.01 &'
                                     'jetID.fHPD < 0.98 &'
                                     'jetID.n90Hits > 1'
                                     )

#------------------------------------------------
# MET collection
#------------------------------------------------

## create MET collection
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
process.goodMET = selectedPatMET.clone(src = 'patMETs',
                                       cut =
                                       'et > 20.'
                                       )

#------------------------------------------------
# filter
#------------------------------------------------

## select events with at least good hard muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.oneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                          minNumber = 1,
                                          maxNumber = 1
                                          )

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.oneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                                  minNumber = 1
                                                  )

## select events with no veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.oneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                          maxNumber = 1
                                          )

## select events with one veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                                 maxNumber = 0
                                                 )

## select events with 4 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
process.fourGoodJets = countPatJets.clone(src = 'goodJets',
                                            minNumber = 2
                                            )
## select events with MET > 100
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
process.cutMET = countPatMET.clone(src = 'goodMET',
                                   minNumber = 1
                                   )

#------------------------------------------------
# analysis modules
#------------------------------------------------

## analyze electrons
process.load("TopAnalysis.TopAnalyzer.ElectronKinematics_cfi")
process.analyzeElectronKinematics.src = "goodElectrons"

## analyze muons
process.load("TopAnalysis.TopAnalyzer.MuonKinematics_cfi")
process.analyzeMuonKinematics.src = "goodMuons"

## analyze jets
process.load("TopAnalysis.TopAnalyzer.JetKinematics_cfi")
process.analyzeJetKinematics.src = "goodJets"

## analyze MET
process.load("TopAnalysis.TopAnalyzer.METKinematics_cfi")
process.analyzeMETKinematics.srcA = "goodMET"

#------------------------------------------------
# Modules for generator studies
#------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYEventAnalyzer_cfi import analyzeSUSYEvent
process.analyzeSUSYEvent = analyzeSUSYEvent.clone()

#------------------------------------------------
# Event weight
#------------------------------------------------

## specify event weight
from TopAnalysis.TopUtils.EventWeightPlain_cfi import *
process.eventWeight = eventWeight
process.eventWeight.nevts = 207273
process.eventWeight.xsec = 0.73
process.eventWeight.eff = 1
process.eventWeight.lumi = 10

#-------------------------------------------------
# selection paths
#-------------------------------------------------

process.RA4Selection = cms.Path(#process.makeGenEvt *
                                #process.analyzeTopGenEventBSM *
                                process.patDefaultSequence *
                                #process.eventWeight *
                                
                                process.hltMu9 *
                                #process.hltbits * 
                                process.primaryVertexFilter * 
                                process.HBHENoiseFilter *
                                process.scrapingVeto *

                                process.goodJets *
                                process.goodMuons *
                                #process.goodElectronS *
                                                                
                                process.oneGoodMuon *
                                #process.goodElectron *
                                process.vetoMuons *
                                process.oneVetoMuon *
                                process.vetoElectrons *
                                process.noVetoElectron *
                                
                                process.analyzeMuonKinematics *
                                #process.analyzeElectronKinematics *
                                
                                process.fourGoodJets *
                                process.analyzeJetKinematics  *
                                
                                process.goodMET *
                                process.cutMET *
                                process.analyzeMETKinematics
                                )

#-------------------------------------------------
# optional: write patTuple
#-------------------------------------------------
#
#process.EventSelection = cms.PSet(
#    SelectEvents = cms.untracked.PSet(
#    SelectEvents = cms.vstring('RA4Selection')
#    )
#)
#
#process.out = cms.OutputModule("PoolOutputModule",
#    process.EventSelection,
#    outputCommands = cms.untracked.vstring('drop *'),
#    dropMetaData = cms.untracked.string('DROPPED'),
#    fileName = cms.untracked.string('PATtuple.root')
#)
#
#from PhysicsTools.PatAlgos.patEventContent_cff import *
#process.out.outputCommands += patEventContentNoCleaning
#process.out.outputCommands += patExtraAodEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent
#
#process.outpath = cms.EndPath(process.out)
