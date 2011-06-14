import FWCore.ParameterSet.Config as cms

#------------------------------
# lepton collections 
#------------------------------

## create good muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
from TopAnalysis.TopFilter.sequences.MuonVertexDistanceSelector_cfi import *

trackMuons = selectedPatMuons.clone(src = "selectedPatMuons",
                                    cut =
                                    'isGood("GlobalMuonPromptTight") &'
                                    'isGood("AllTrackerMuons") &'
                                    'pt >= 20. &'
                                    'abs(eta) <= 2.1 &'
                                    '(trackIso+hcalIso+ecalIso)/pt < 0.1 &'
                                    'abs(dB) < 0.02 &'
                                    'globalTrack.hitPattern.numberOfValidTrackerHits > 10 &'
                                    'numberOfMatches() > 1 &'
                                    'innerTrack().hitPattern().pixelLayersWithMeasurement() >= 1'
                                    )

vertexMuons = vertexSelectedMuons.clone(src = "trackMuons"
                                        )

from TopAnalysis.TopFilter.filters.MuonJetOverlapSelector_cfi import *
goodMuons = checkJetOverlapMuons.clone()
goodMuons.muons = 'vertexMuons'
goodMuons.jets = 'looseJets'
goodMuons.deltaR = 0.3
goodMuons.overlap=False

## create good electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
from TopAnalysis.TopFilter.sequences.ElectronVertexDistanceSelector_cfi import *

isolatedElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                               cut =
                                               'pt >= 20. &'
                                               'abs(eta) <= 2.5 &'
                                               'electronID(\"simpleEleId80relIso\")=7 &'
                                               '(abs(eta) < 1.4442 | abs(eta) > 1.566) &'
                                               'abs(dB) < 0.02 '
                                               )

goodElectrons = vertexSelectedElectrons.clone(src = "isolatedElectrons"
                                              )

#------------------------------
# veto-lepton collections
#------------------------------

## create veto-muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
vetoMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                   cut =
                                   'isGlobalMuon &'
                                   'pt >= 10. &'
                                   'abs(eta) <= 2.5 &'
                                   '(trackIso+hcalIso+ecalIso)/pt <  0.2'
                                   )

## create veto-electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
vetoElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt >= 15. &'
                                           'abs(eta) <= 2.5 &'
                                           'electronID(\"simpleEleId95relIso\")=7 '
                                           )

#------------------------------
# jet collections
#------------------------------

## create good jet collection
from PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi import *
looseJets = cleanPatJets.clone(src = 'selectedPatJetsAK5PF',
                               preselection =
                               'abs(eta) < 2.4 &'
                               'pt > 30. &'
                               ## PURE09 LOOSE
                               #'emEnergyFraction > 0.01 &'
                               #'jetID.fHPD < 0.98 &'
                               #'jetID.n90Hits > 1'
                               ## Loose PF Jet ID
                               'chargedHadronEnergyFraction > 0.0  &'
                               'neutralHadronEnergyFraction < 0.99 &'
                               'chargedEmEnergyFraction     < 0.99 &'
                               'neutralEmEnergyFraction     < 0.99 &'
                               'chargedMultiplicity > 0            &'
                               'nConstituents > 1'
                               
                               )

looseJets.checkOverlaps = cms.PSet(
    muons = cms.PSet(
    src       = cms.InputTag("vertexMuons"),
    algorithm = cms.string("byDeltaR"),
    preselection        = cms.string(""),
    deltaR              = cms.double(0.1),
    checkRecoComponents = cms.bool(False),
    pairCut             = cms.string(""),
    requireNoOverlaps   = cms.bool(True),
    ),
    electrons = cms.PSet(
    src       = cms.InputTag("goodElectrons"),
    algorithm = cms.string("byDeltaR"),
    preselection        = cms.string(""),
    deltaR              = cms.double(0.3),
    checkRecoComponents = cms.bool(False),
    pairCut             = cms.string(""),
    requireNoOverlaps   = cms.bool(True),
    )
)
    
#------------------------------
# MET collection
#------------------------------

## create MET collection
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
goodMETs = selectedPatMET.clone(src = 'patMETsPF',
                                cut =
                                'et > 100.'
                                )
## create MET collection
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
tightMETs = selectedPatMET.clone(src = 'patMETsPF',
                                 cut =
                                 'et > 700.'
                                 )

#------------------------------
# muon countFilter
#------------------------------

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneVertexMuon = countPatMuons.clone(src = 'vertexMuons',
                                    minNumber = 1
                                    )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                  minNumber = 1
                                  )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
exactlyOneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )
## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
noGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                 maxNumber = 0
                                 )

#------------------------------
# electron countFilter
#------------------------------


## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneIsolatedElectron = countPatElectrons.clone(src = 'isolatedElectrons',
                                              minNumber = 1
                                              )

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                          minNumber = 1
                                          )

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
exactlyOneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1,
                                                 )

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
noGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                         maxNumber = 0
                                         )
#------------------------------
# veto-lepton countFilter
#------------------------------

## select events with one veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  maxNumber = 1
                                  )

## select events with no veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                         maxNumber = 0
                                         )
#------------------------------
# jet countFilter
#------------------------------

## select events with 1 loose jet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneLooseJet = countPatJets.clone(src = 'looseJets',
                                 minNumber = 1
                                 )
## select events with 2 loose jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoLooseJets = countPatJets.clone(src = 'looseJets',
                                  minNumber = 2
                                  )
## select events with 3 loose jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeLooseJets = countPatJets.clone(src = 'looseJets',
                                  minNumber = 3
                                    )
## select events with 4 loose jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourLooseJets = countPatJets.clone(src = 'looseJets',
                                   minNumber = 4
                                           )
#------------------------------
# MET countFilter
#------------------------------

## select events with one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )

## select events with one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneTightMET = countPatMET.clone(src = 'tightMETs',
                                minNumber = 1
                                )

#------------------------------
# Define sequences
#------------------------------

goodObjects = cms.Sequence(trackMuons *
                           vertexMuons *
                           vetoMuons *
                           isolatedElectrons *
                           goodElectrons *
                           vetoElectrons *
                           looseJets *
                           goodMuons *
                           goodMETs *
                           tightMETs
                           )
