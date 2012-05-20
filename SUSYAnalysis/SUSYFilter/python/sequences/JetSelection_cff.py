import FWCore.ParameterSet.Config as cms

#------------------------------
# collections of good leptons
#------------------------------

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
                                    'innerTrack().hitPattern().pixelLayersWithMeasurement() >= 1 &'
                                    '(globalTrack.ptError)/(pt*pt) < 0.001'
                                    )

goodMuons = vertexSelectedMuons.clone(src = "trackMuons"
                                      )

from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
from TopAnalysis.TopFilter.sequences.ElectronVertexDistanceSelector_cfi import *

isolatedElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                               cut =
                                               'pt >= 20. &'
                                               'abs(eta) <= 2.5 &'
                                               'electronID(\"simpleEleId80relIso\")=7 &'
                                               '(abs(superCluster.eta) < 1.4442 | abs(superCluster.eta) > 1.566) &'
                                               'abs(dB) < 0.02 '
                                               )

goodElectrons = vertexSelectedElectrons.clone(src = "isolatedElectrons"
                                              )

#------------------------------
# collections of loose leptons
#------------------------------

looseMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                    cut =
                                    'pt > 15. &'
                                    'abs(eta) < 2.5'
                                    )

looseElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                            cut =
                                            'pt > 15. &'
                                            'abs(eta) < 2.5 '
                                            )
#------------------------------
# veto-lepton collections
#------------------------------

trackVetoMuons = selectedPatMuons.clone(src = "selectedPatMuons",
                                        cut =
                                        'isGood("GlobalMuonPromptTight") &'
                                        'pt >= 15. &'
                                        'abs(eta) <= 2.5 &'
                                        '(trackIso+hcalIso+ecalIso)/pt <  0.15 &'
                                        'abs(dB) < 0.1'
                                        )

vetoMuons = vertexSelectedMuons.clone(src = "trackVetoMuons"
                                            )

looseVetoElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                                cut =
                                                'pt >= 15. &'
                                                'abs(eta) <= 2.5 &'
                                                'electronID(\"simpleEleId95relIso\")=7 &'
                                                '(abs(superCluster.eta) < 1.4442 | abs(superCluster.eta) > 1.566) &'
                                                'abs(dB) < 0.1'
                                                )

vetoElectrons = vertexSelectedElectrons.clone(src = "looseVetoElectrons"
                                              )
#------------------------------
# jet collections
#------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi import *
looseJets = cleanPatJets.clone(src = 'selectedPatJetsPF',
                               preselection =
                               'abs(eta) < 5 &'
                               'pt > 30. &'
                               'chargedHadronEnergyFraction > 0.0  &'
                               'neutralHadronEnergyFraction < 0.99 &'
                               'chargedEmEnergyFraction     < 0.99 &'
                               'neutralEmEnergyFraction     < 0.99 &'
                               'chargedMultiplicity > 0            &'
                               'nConstituents > 1'
                               )
                               
looseJets.checkOverlaps = cms.PSet(
    muons = cms.PSet(
    src       = cms.InputTag("goodMuons"),
    algorithm = cms.string("byDeltaR"),
    preselection        = cms.string(""),
    deltaR              = cms.double(0.3),
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

goodJets = cleanPatJets.clone(src = 'selectedPatJetsPF',
                               preselection =
                               'abs(eta) < 2.5 &'
                               'pt > 50. &'
                               'chargedHadronEnergyFraction > 0.0  &'
                               'neutralHadronEnergyFraction < 0.99 &'
                               'chargedEmEnergyFraction     < 0.99 &'
                               'neutralEmEnergyFraction     < 0.99 &'
                               'chargedMultiplicity > 0            &'
                               'nConstituents > 1' 
                               )
                               
goodJets.checkOverlaps = cms.PSet(
    muons = cms.PSet(
    src       = cms.InputTag("goodMuons"),
    algorithm = cms.string("byDeltaR"),
    preselection        = cms.string(""),
    deltaR              = cms.double(0.3),
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

from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
tightJets = selectedPatJets.clone(src = 'goodJets',
                                  cut =
                                  'pt > 120.'
                                  )

from SUSYAnalysis.SUSYEventProducers.JetCollectionProducer_cfi import *
produceJetCollection.inputJets = "goodJets"

## create collection of good Jets with scaled up jet energy corrections
goodJetsJECUp = goodJets.clone()
goodJetsJECUp.src = "scaledJetEnergyJECUp:selectedPatJetsAK5PF"

## create collection of good Jets with scaled down jet energy corrections
goodJetsJECDown = goodJets.clone()
goodJetsJECDown.src = "scaledJetEnergyJECDown:selectedPatJetsAK5PF"

## create collection of good Jets with scaled up jet energy resolution
goodJetsJERUp = goodJets.clone()
goodJetsJERUp.src = "scaledJetEnergyJERUp:selectedPatJetsAK5PF"

## create collection of good Jets with scaled down jet energy resolution
goodJetsJERDown = goodJets.clone()
goodJetsJERDown.src = "scaledJetEnergyJERDown:selectedPatJetsAK5PF"
 

#------------------------------
# MET collection
#------------------------------

## create MET collection
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
looseMETs = selectedPatMET.clone(src = 'patMETsPF',
                                 cut =
                                 'et > 200.'
                                 )
## create MET collection
goodMETs = selectedPatMET.clone(src = 'patMETsPF',
                                cut =
                                'et > 300.'
                                )
## create MET collection
mediumMETs = selectedPatMET.clone(src = 'patMETsPF',
                                  cut =
                                  'et > 300.'
                                  )
## create MET collection
tightMETs = selectedPatMET.clone(src = 'patMETsPF',
                                 cut =
                                 'et > 450.'
                                 )

#------------------------------
# muon countFilter
#------------------------------

## select events with at least one loose muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneLooseMuon = countPatMuons.clone(src = 'looseMuons',
                                   minNumber = 1
                                   )

## select events with at least one vertex muon
oneVertexMuon = countPatMuons.clone(src = 'vertexMuons',
                                    minNumber = 1
                                    )

## select events with at least good muon
oneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                  minNumber = 1
                                  )

## select events with exactly one good muon
exactlyOneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )
## select events with no good muon
noGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                 maxNumber = 0
                                 )

## select events with at least two good muons
twoGoodMuons = countPatMuons.clone(src = 'goodMuons',
                                   minNumber = 2
                                   )
#------------------------------
# electron countFilter
#------------------------------

## select events with at least one loose electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneLooseElectron = countPatElectrons.clone(src = 'looseElectrons',
                                           minNumber = 1
                                           )

## select events with at least one iosolated electron
oneIsolatedElectron = countPatElectrons.clone(src = 'isolatedElectrons',
                                              minNumber = 1
                                              )

## select events with at least one good electron
oneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                          minNumber = 1
                                          )

## select events with exactly one good electron
exactlyOneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1
                                                 )

## select events with no good electron
noGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                         maxNumber = 0
                                         )

## select events with at least two good electrons
twoGoodElectrons = countPatElectrons.clone(src = 'goodElectrons',
                                           minNumber = 2
                                           )
#------------------------------
# veto-lepton countFilter
#------------------------------

## select events with exactly one veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
exactlyOneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )
## select events with no veto muon
noVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  maxNumber = 0
                                  )
## select events with exactly one veto electron
exactlyOneVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1
                                                 )
## select events with no veto electron
noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                         maxNumber = 0
                                         )
#------------------------------
# jet countFilter
#------------------------------

## select events with 2 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneGoodJet = countPatJets.clone(src = 'goodJets',
                                minNumber = 1
                                )
## select events with 2 good jets
twoGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 2
                                  )
## select events with 3 good jets
threeGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 3
                                  )
## select events with 4 good jets
fourGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 4
                                  )
## select events with 4 good jets
maxFourGoodJets = countPatJets.clone(src = 'goodJets',
                                     maxNumber = 4
                                     )

## select events with 4 good jets
sixGoodJets = countPatJets.clone(src = 'goodJets',
                                 minNumber = 6
                                 )

#------------------------------
# MET countFilter
#------------------------------

## select events with one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneLooseMET = countPatMET.clone(src = 'looseMETs',
                                minNumber = 1
                                )
## select events with one good MET
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )
## select events with one good MET
oneMediumMET = countPatMET.clone(src = 'mediumMETs',
                                 minNumber = 1
                                 )
## select events with one good MET
oneTightMET = countPatMET.clone(src = 'tightMETs',
                                minNumber = 1
                                )
#-----------------------------
# Event Filter
#-----------------------------

## HT filter
from SUSYAnalysis.SUSYFilter.filters.HTFilter_cfi import *

filterLooseHT = filterHT.clone()
filterLooseHT.jets = "goodJets"
filterLooseHT.Cut = 400

filterMediumHT = filterHT.clone()
filterMediumHT.jets = "goodJets"
filterMediumHT.Cut = 800

filterTightHT = filterHT.clone()
filterTightHT.jets = "goodJets"
filterTightHT.Cut = 1000

## MHT filter
from SUSYAnalysis.SUSYFilter.filters.MHTFilter_cfi import *

filterMediumMHT = filterMHT.clone()
filterMediumMHT.jets = "goodJets"
filterMediumMHT.Cut = 400

## DiLepton filter
from TopAnalysis.TopFilter.filters.DiMuonFilter_cfi import *
SSignMuMuFilter = filterMuonPair.clone()
ZVetoMu = filterMuonPair.clone()
ZVetoMu.isVeto = True

from TopAnalysis.TopFilter.filters.DiElectronFilter_cfi import *          

SSignElElFilter = filterElecPair.clone()
ZVetoEl = filterElecPair.clone()
ZVetoEl.isVeto = True

## Lepton filter
from PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi import *

oneLooseLepton = countPatLeptons.clone()
oneLooseLepton.electronSource = "looseElectrons"
oneLooseLepton.muonSource = "looseMuons"  
oneLooseLepton.minNumber = 1

oneGoodLepton = countPatLeptons.clone()
oneGoodLepton.electronSource = "goodElectrons"
oneGoodLepton.muonSource = "goodMuons"                           
oneGoodLepton.minNumber = 1

exactlyOneGoodLepton = countPatLeptons.clone()
exactlyOneGoodLepton.electronSource = "goodElectrons"
exactlyOneGoodLepton.muonSource = "goodMuons"                           
exactlyOneGoodLepton.minNumber = 1
exactlyOneGoodLepton.maxNumber = 1

twoGoodLeptons = countPatLeptons.clone()
twoGoodLeptons.electronSource = "goodElectrons"
twoGoodLeptons.muonSource = "goodMuons"                           
twoGoodLeptons.minNumber = 2

leptonVeto = countPatLeptons.clone()

## Transverse mass filter
from SUSYAnalysis.SUSYFilter.filters.TransverseMassFilter_cfi import *
filterMT = filterTransverseMass.clone()
filterMT.muons = "goodMuons"
filterMT.electrons = "goodElectrons"

#------------------------------
# Define sequences
#------------------------------


makeObjects = cms.Sequence(## loose leptons
                           looseMuons *
                           looseElectrons *
                           ## muons
                           trackMuons *
                           goodMuons *
                           trackVetoMuons *
                           vetoMuons *
                           ## electrons
                           isolatedElectrons *
                           goodElectrons*
                           looseVetoElectrons *
                           vetoElectrons *
                           ## jets
                           looseJets *
                           goodJets *
                           tightJets *
                           produceJetCollection *
                           goodJetsJECUp *
                           goodJetsJECDown *
                           goodJetsJERUp *
                           goodJetsJERDown *
                           ## METs
                           looseMETs *
                           goodMETs *
                           mediumMETs *
                           tightMETs
                           )

from SUSYAnalysis.SUSYFilter.filters.PFMuonConsistency_cfi import *

muonSelection = cms.Sequence(oneGoodMuon *
                             exactlyOneGoodMuon *
                             pfMuonConsistency *
                             noGoodElectron *
                             exactlyOneVetoMuon *
                             noVetoElectron
                             )

electronSelection = cms.Sequence(oneGoodElectron *
                                 exactlyOneGoodElectron *
                                 noGoodMuon *
                                 exactlyOneVetoElectron *
                                 noVetoMuon
                                 )

muonVeto = cms.Sequence(exactlyOneVetoMuon *
                        noVetoElectron
                        )

electronVeto = cms.Sequence(exactlyOneVetoElectron *
                            noVetoMuon
                            )
