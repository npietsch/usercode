import FWCore.ParameterSet.Config as cms

#------------------------------------------------------------------------------
# Configure modules to produce collections of leptons
#------------------------------------------------------------------------------

## create collection of good muons
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
                                    '((globalTrack.ptError)/(pt*pt)) < 0.001'
                                    )

goodMuons = vertexSelectedMuons.clone(src = "trackMuons",
                                      primaryVertex = "goodVertices"
                                      )

## create collection of good electrons
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
from TopAnalysis.TopFilter.sequences.ElectronVertexDistanceSelector_cfi import *

isolatedElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                               cut =
                                               'pt >= 20. &'
                                               'electronID(\"simpleEleId80cIso\")=7 &'
                                               'abs(superCluster.eta) <= 2.5 &'
                                               '(abs(superCluster.eta) < 1.4442 || abs(superCluster.eta) > 1.566) &'
                                               'abs(dB) < 0.02 '
                                               )

goodElectrons = vertexSelectedElectrons.clone(src = "isolatedElectrons",
                                              primaryVertex = "goodVertices"
                                              )

## create collection of loose muons
looseMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                    cut =
                                    'pt > 10. &'
                                    'abs(eta) < 2.5'
                                    )

## create collection of loose electrons
looseElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                            cut =
                                            'pt > 10. &'
                                            'abs(eta) < 2.5 '
                                            )

## create collection of veto muons
trackVetoMuons = selectedPatMuons.clone(src = "selectedPatMuons",
                                        cut =
                                        'isGood("GlobalMuonPromptTight") &'
                                        'pt >= 15. &'
                                        'abs(eta) <= 2.5 &'
                                        '((trackIso+hcalIso+ecalIso)/pt) <  0.15 &'
                                        'abs(dB) < 0.1'
                                        )

vetoMuons = vertexSelectedMuons.clone(src = "trackVetoMuons",
                                      primaryVertex = "goodVertices"
                                      )

## create collection of veto electrons
looseVetoElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                                cut =
                                                'pt >= 15. &'
                                                'electronID(\"simpleEleId95cIso\")=7 &'
                                                'abs(superCluster.eta) <= 2.5 &'
                                                '(abs(superCluster.eta) < 1.4442 || abs(superCluster.eta) > 1.566) &'
                                                'abs(dB) < 0.1'
                                                )

vetoElectrons = vertexSelectedElectrons.clone(src = "looseVetoElectrons",
                                              primaryVertex = "goodVertices"
                                              )

#------------------------------------------------------------------------------
# Configure modules to produce collections of jets
#------------------------------------------------------------------------------

## create collection of loose jets
from PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi import *
looseJets = cleanPatJets.clone(src = 'selectedPatJetsAK5PF',
                               preselection =
                               'abs(eta) < 2.4 &'
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
    requireNoOverlaps   = cms.bool(False),
    ),
    electrons = cms.PSet(
    src       = cms.InputTag("goodElectrons"),
    algorithm = cms.string("byDeltaR"),
    preselection        = cms.string(""),
    deltaR              = cms.double(0.3),
    checkRecoComponents = cms.bool(False),
    pairCut             = cms.string(""),
    requireNoOverlaps   = cms.bool(False),
    )
)

## create collections of good jets
goodJets = cleanPatJets.clone(src = 'selectedPatJetsAK5PF',
                               preselection =
                               'abs(eta) < 2.4 &'
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

## create collection of medium jets
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
mediumJets = selectedPatJets.clone(src = 'goodJets',
                                   cut =
                                   'pt > 50.'
                                   )
## create collection of tight jets
tightJets = selectedPatJets.clone(src = 'goodJets',
                                  cut =
                                  'pt > 100.'
                                  )

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


#------------------------------------------------------------------------------
# Configure modules to produce collections of b-jets
#------------------------------------------------------------------------------

## create collections of b-jets
looseTrackHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighPurBJetTags\") > 1.19'
                                               )

mediumTrackHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                                cut = 'bDiscriminator(\"trackCountingHighPurBJetTags\") > 1.93'
                                                )

tightTrackHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighPurBJetTags\") > 3.41'
                                               )
looseTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 1.7'
                                               )

mediumTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                                cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                )

tightTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 10.2'
                                               )

lightJets = selectedPatJets.clone(src = 'goodJets',
                                  cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") < 3.3'
                                  )

mediumSSVHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                              cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                              )

tightSSVHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                             cut = 'bDiscriminator(\"simpleSecondaryVertexHighPurBJetTags\") > 2.0'
                                             )

## create collections of matched good jets
matchedBjets = selectedPatJets.clone(src = 'goodJets',
                                     cut = 'abs(partonFlavour())=5'
                                     )

matchedLightJets = selectedPatJets.clone(src = 'goodJets',
                                         cut = 'abs(partonFlavour())<5'
                                         )

#------------------------------------------------------------------------------
# Configure modules to produce collections of MET
#------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
looseMETs = selectedPatMET.clone(src = 'patMETsPF',
                                 cut =
                                 'et > 50.'
                                 )

goodMETs = selectedPatMET.clone(src = 'patMETsPF',
                                cut =
                                'et > 60.'
                                )

mediumMETs = selectedPatMET.clone(src = 'patMETsPF',
                                  cut =
                                  'et > 100.'
                                  )

tightMETs = selectedPatMET.clone(src = 'patMETsPF',
                                 cut =
                                 'et > 150.'
                                 )

noSignalMETs = selectedPatMET.clone(src = 'patMETsPF',
                                    cut =
                                    'et > 50. &'
                                    'et < 300.'
                                    )

#------------------------------------------------------------------------------
# Configure filter modules for selection of events based on number of leptons
#------------------------------------------------------------------------------

## select events with at least one loose muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneLooseMuon = countPatMuons.clone(src = 'looseMuons',
                                   minNumber = 1
                                   )

## select events with at least one vertex muon
oneVertexMuon = countPatMuons.clone(src = 'vertexMuons',
                                    minNumber = 1
                                    )

## select events with at least one good muon
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

## select events with exactly one veto muon
exactlyOneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )

## select events with no veto muon
noVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                 maxNumber = 0
                                 )

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

## select events with exactly one veto electron
exactlyOneVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1
                                                 )

## select events with no veto electron
noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                         maxNumber = 0
                                         )

#------------------------------------------------------------------------------
# Configure filter modules for selection of events based on number of jets
#------------------------------------------------------------------------------

## select events with at least 1 loose jet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneLooseJet = countPatJets.clone(src = 'looseJets',
                                 minNumber = 1
                                 )
## select events with at least 2 loose jets
twoLooseJets = countPatJets.clone(src = 'looseJets',
                                  minNumber = 2
                                  )
## select events with at least 3 loose jets
threeLooseJets = countPatJets.clone(src = 'looseJets',
                                    minNumber = 3
                                    )
## select events with at least 4 loose jets
fourLooseJets = countPatJets.clone(src = 'looseJets',
                                   minNumber = 4
                                   )

## select events with 1 good jet
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
## select events with max 4 good jets
maxFourGoodJets = countPatJets.clone(src = 'goodJets',
                                     maxNumber = 4
                                     )
## select events with 4 good jets
fourGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 4
                                  )
## select events with max 5 good jets
maxFiveGoodJets = countPatJets.clone(src = 'goodJets',
                                     maxNumber = 5
                                     )
## select events with 5 good jets
fiveGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 5
                                  )
## select events with max 6 good jets
maxSixGoodJets = countPatJets.clone(src = 'goodJets',
                                     maxNumber = 6
                                     )
## select events with  6 good jets
sixGoodJets = countPatJets.clone(src = 'goodJets',
                                 minNumber = 6
                                 )

## select events with 2 medium jets
twoMediumJets = countPatJets.clone(src = 'mediumJets',
                                   minNumber = 2
                                   )

## select events with 3 one tight jet
oneTightJet = countPatJets.clone(src = 'tightJets',
                                 minNumber = 1
                                 )

#------------------------------------------------------------------------------
# Configure filter modules for selection of events based on number of b-jets
#------------------------------------------------------------------------------

## select events with 1 loose TCHE bjet
oneLooseTrackHighEffBjet = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                              minNumber = 1
                                              )
## select events with 2 loose TCHE bjets
twoLooseTrackHighEffBjets = countPatJets.clone(src = 'looseTrackHighEffTCHE Bjets',
                                               minNumber = 2 
                                               )
## select events with 3 loose TCHE bjets
threeLooseTrackHighEffBjets = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                                 minNumber = 3
                                                 ) 
## select events with 4 loose TCHE bjets
fourLooseTrackHighEffBjets = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                                minNumber = 4
                                                )
## select events with 1 medium TCHE bjet
oneMediumTrackHighEffBjet = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                               minNumber = 1
                                               )
## select events with 2 medium TCHE bjets
twoMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                minNumber = 2
                                                )
## select events with 3 medium TCHE bjets
threeMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                  minNumber = 3
                                                  )
## select events with 4 medium TCHE bjets
fourMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                 minNumber = 4
                                                 )
## select events with exactly 1 medium TCHE bjet
exactlyOneMediumTrackHighEffBjet = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                      minNumber = 1,
                                                      maxNumber = 1
                                                      )
## select events with exactly 2 medium TCHE bjets
exactlyTwoMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                       minNumber = 2,
                                                       maxNumber = 2
                                                       )
## select events with exactly 3 medium TCHE bjets
exactlyThreeMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                         minNumber = 3,
                                                         maxNumber = 3
                                                         )
## select events with exactly 4 medium TCHE bjets
exactlyFourMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                        minNumber = 4,
                                                        maxNumber = 4
                                                        )

## select events with 1 medium TCHP bjet
oneLooseTrackHighPurBjet = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                              minNumber = 1
                                              )
## select events with 2 loose TCHP bjets
twoLooseTrackHighPurBjets = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                               minNumber = 2
                                               )
## select events with 3 loose TCHP bjets
threeLooseTrackHighPurBjets = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                                 minNumber = 3
                                                 )
## select events with 4 loose TCHP bjets
fourLooseTrackHighPurBjets = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                                minNumber = 4
                                                )
## select events with 1 medium TCHP bjet
oneMediumTrackHighPurBjet = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                               minNumber = 1
                                               )
## select events with 2 medium TCHP bjets
twoMediumTrackHighPurBjetss = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                                 minNumber = 2
                                                 )
## select events with 3 medium TCHP bjets
threeMediumTrackHighPurBjets = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                                  minNumber = 3
                                                  )
## select events with 4 medium TCHP bjets
fourMediumTrackHighPurBjets = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                                 minNumber = 4
                                                 )

#------------------------------------------------------------------------------
# Configure filter modules for selection of events based on number of MET
#------------------------------------------------------------------------------

## select events with one loose MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneLooseMET = countPatMET.clone(src = 'looseMETs',
                                minNumber = 1
                                )

## select events with one good MET
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )

## select events with one medium MET
oneMediumMET = countPatMET.clone(src = 'mediumMETs',
                                 minNumber = 1
                                 )

## select events with one tight MET
oneTightMET = countPatMET.clone(src = 'tightMETs',
                                minNumber = 1
                                )

## select events with one no signal MET
oneNoSignalMET = countPatMET.clone(src = 'noSignalMETs',
                                   minNumber = 1
                                   )

#------------------------------------------------------------------------------
# Configure other filter modules
#------------------------------------------------------------------------------

## HT filter
from SUSYAnalysis.SUSYFilter.filters.HTFilter_cfi import *

filterLooseHT = filterHT.clone()
filterLooseHT.jets = "looseJets"
filterLooseHT.Cut = 400

filterMediumHT = filterHT.clone()
filterMediumHT.jets = "goodJets"
filterMediumHT.Cut = 700

filterTightHT = filterHT.clone()
filterTightHT.jets = "goodJets"
filterTightHT.Cut = 800

## MHT filter
from SUSYAnalysis.SUSYFilter.filters.MHTFilter_cfi import *

filterMediumMHT = filterMHT.clone()
filterMediumMHT.jets = "goodJets"
filterMediumMHT.Cut = 60

## Di-lepton filter
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

exactlyOneVetoLepton = countPatLeptons.clone()
exactlyOneVetoLepton.electronSource = "vetoElectrons"
exactlyOneVetoLepton.muonSource = "vetoMuons"                           
exactlyOneVetoLepton.minNumber = 1
exactlyOneVetoLepton.maxNumber = 1

## Transverse mass filter
from SUSYAnalysis.SUSYFilter.filters.TransverseMassFilter_cfi import *
filterMT = filterTransverseMass.clone()
filterMT.muons = "goodMuons"
filterMT.electrons = "goodElectrons"

#------------------------------------------------------------------------------
# Define producer and filter sequences
#------------------------------------------------------------------------------

matchedGoodObjects = cms.Sequence(matchedBjets *
                                  matchedLightJets
                                  )

goodObjects = cms.Sequence(## loose leptons
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
                           mediumJets *
                           tightJets *
                           lightJets *
                           goodJetsJECUp *
                           goodJetsJECDown *
                           goodJetsJERUp *
                           goodJetsJERDown *
                           ## METs
                           looseMETs *
                           goodMETs *
                           mediumMETs *
                           tightMETs *
                           noSignalMETs *
                           ## bjets
                           looseTrackHighPurBjets *
                           mediumTrackHighPurBjets *
                           tightTrackHighPurBjets *
                           looseTrackHighEffBjets *
                           mediumTrackHighEffBjets *
                           tightTrackHighEffBjets *
                           mediumSSVHighEffBjets *
                           tightSSVHighPurBjets
                           )

makeObjects = cms.Sequence(goodObjects *
                           matchedGoodObjects
                           )

from SUSYAnalysis.SUSYFilter.filters.PFMuonConsistency_cfi import *
pfMuonConsistency.muons = "goodMuons"

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

leptonSelection = cms.Sequence(exactlyOneGoodLepton *
                               exactlyOneVetoLepton
                               )

jetSelection = cms.Sequence(fourGoodJets)

mTSelection = cms.Sequence(filterMT)

metSelection = cms.Sequence(oneGoodMET
                            )

HTSelection = cms.Sequence(filterMediumHT)

tightHTSelection = cms.Sequence(filterTightHT)

MuHadSelection = cms.Sequence(filterMediumHT *
                              oneGoodMET *
                              oneLooseMuon
                              )

ElHadSelection = cms.Sequence(filterMediumHT *
                              oneGoodMET *
                              oneLooseElectron
                              )

LepHadSelection = cms.Sequence(filterMediumHT *
                               oneGoodMET *
                               oneLooseLepton
                               )

muonVeto = cms.Sequence(exactlyOneVetoMuon *
                        noVetoElectron
                        )

electronVeto = cms.Sequence(exactlyOneVetoElectron *
                            noVetoMuon
                            )

QCDPreselection = cms.Sequence(## ## produce good muons
##                                trackMuons *
##                                goodMuons *
##                                ## produce good electrons
##                                isolatedElectrons *
##                                goodElectrons *
                               ## produce good jets
                               looseJets *
                               ## produce good METs
                               looseMETs *
                               ## preselection
                               filterLooseHT *
                               oneLooseMET
                               )
