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

## create loose muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
looseMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                    cut =
                                    'pt > 10. &'
                                    'abs(eta) < 2.5'
                                    )
## create loose electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
looseElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                            cut =
                                            'pt > 20. &'
                                            'abs(eta) < 2.5 '
                                            )
#------------------------------
# matched-lepton collections 
#------------------------------

## genLepton.pdgId is not working for the moment, so modules are commented out in cmsSequence "matchedGoodObjects" defined in the end

## create collection of good muons that can be matched to a generator muon
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
matchedMuons = selectedPatMuons.clone(src = 'goodMuons',
                                      cut =  'genLepton.pdgId &'
                                      'abs(genLepton.pdgId) = 13'
                                      )

## create collection of good electrons that can be matched to a generator electron
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
matchedElectrons = selectedPatMuons.clone(src = 'goodMuons',
                                          cut = 'genLepton.pdgId &'
                                          'abs(genLepton.pdgId) = 11'
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
    
## create good jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
goodJets = selectedPatJets.clone(src = 'looseJets',
                                 cut =
                                 'pt > 30.'
                                 )
## create good jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
mediumJets = selectedPatJets.clone(src = 'goodJets',
                                   cut =
                                   'pt > 50.'
                                   )
## create good jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
tightJets = selectedPatJets.clone(src = 'goodJets',
                                  cut =
                                  'pt > 100.'
                                  )

#------------------------------------
# bjet collections, input: goodJets
#------------------------------------

## create looseTrackHighPurBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
looseTrackHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighPurBJetTags\") > 1.19'
                                               )

## create mediumTrackHighPurBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
mediumTrackHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                                cut = 'bDiscriminator(\"trackCountingHighPurBJetTags\") > 1.93'
                                                )

## create tightTrackHighPurBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
tightTrackHighPurBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighPurBJetTags\") > 3.41'
                                               )
## create looseTrackHighEffBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
looseTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 1.7'
                                               )

## create mediumTrackHighEffBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
mediumTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                                cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                )

## create mediumTrackHighEffBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
lightJets = selectedPatJets.clone(src = 'goodJets',
                                  cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") < 3.3'
                                  )

## create tightTrackHighEffBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
tightTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                               cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 10.2'
                                               )

#------------------------------
# matched-jet collections
#------------------------------

## create collection of good jets that can be matched to a generator b-quark
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
matchedBjets = selectedPatJets.clone(src = 'goodJets',
                                     cut = 'abs(partonFlavour())=5'
                                     )

## create jet collection that can be matched to a generator light quark
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
matchedLightJets = selectedPatJets.clone(src = 'goodJets',
                                         cut = 'abs(partonFlavour())<5'
                                         )

#------------------------------
# MET collection
#------------------------------

## create MET collection
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
looseMETs = selectedPatMET.clone(src = 'patMETsPF',
                                 cut =
                                 'et > 20.'
                                 )
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


## select events with at least one loose muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneLooseMuon = countPatMuons.clone(src = 'looseMuons',
                                   minNumber = 1
                                   )

## select events with at least one vertex muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneVertexMuon = countPatMuons.clone(src = 'vertexMuons',
                                    minNumber = 1
                                    )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                  minNumber = 1
                                  )

## select events with exactly one good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
exactlyOneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )
## select events with no good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
noGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                 maxNumber = 0
                                 )

## select events with at least two good muons
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
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
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneIsolatedElectron = countPatElectrons.clone(src = 'isolatedElectrons',
                                              minNumber = 1
                                              )

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                          minNumber = 1
                                          )

## select events with exactly one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
exactlyOneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1
                                                 )

## select events with no good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
noGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                         maxNumber = 0
                                         )

## select events with at least two good electrons
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
twoGoodElectrons = countPatElectrons.clone(src = 'goodElectrons',
                                           minNumber = 2
                                           )
#------------------------------
# veto-lepton countFilter
#------------------------------

## select events with exactly one veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  minNumber = 1,
                                  maxNumber = 1
                                  )
## select events with no veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
noVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  maxNumber = 0
                                  )
## select events with exactly one veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                          minNumber = 1,
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


## select events with at least 1 loose jet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneLooseJet = countPatJets.clone(src = 'looseJets',
                                 minNumber = 1
                                 )
## select events with at least 2 loose jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoLooseJets = countPatJets.clone(src = 'looseJets',
                                  minNumber = 2
                                  )
## select events with at least 3 loose jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeLooseJets = countPatJets.clone(src = 'looseJets',
                                    minNumber = 3
                                    )
## select events with at least 4 loose jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourLooseJets = countPatJets.clone(src = 'looseJets',
                                   minNumber = 4
                                   )

## select events with 2 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneGoodJet = countPatJets.clone(src = 'goodJets',
                                minNumber = 1
                                )
## select events with 2 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 2
                                  )
## select events with 3 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 3
                                  )
## select events with 4 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 4
                                  )


## select events with 2 medium jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoMediumJets = countPatJets.clone(src = 'mediumJets',
                                   minNumber = 2
                                   )

## select events with 3 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneTightJet = countPatJets.clone(src = 'tightJets',
                                 minNumber = 1
                                 )

#------------------------------
# trackHighEffBjet countFilter
#------------------------------

## select events with 1 medium bjet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneLooseTrackHighEffBjet = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                              minNumber = 1
                                              )
## select events with 2 loose bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoLooseTrackHighEffBjets = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                               minNumber = 2 
                                               )
## select events with 3 loose bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeLooseTrackHighEffBjets = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                                 minNumber = 3
                                                 ) 
## select events with 4 loose bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourLooseTrackHighEffBjets = countPatJets.clone(src = 'looseTrackHighEffBjets',
                                                minNumber = 4
                                                )

## select events with 1 medium bjet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneMediumTrackHighEffBjet = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                               minNumber = 1
                                               )
## select events with 2 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                minNumber = 2
                                                )
## select events with 3 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                  minNumber = 3
                                                  )
## select events with 4 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                 minNumber = 4
                                                 )

## select events with exactly 1 medium bjet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
exactlyOneMediumTrackHighEffBjet = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                    minNumber = 1,
                                                    maxNumber = 1
                                                    )
## select events with exactly 2 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
exactlyTwoMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                     minNumber = 2,
                                                     maxNumber = 2
                                                     )
## select events with exactly 3 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
exactlyThreeMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                       minNumber = 3,
                                                       maxNumber = 3
                                                       )
## select events with exactly 4 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
exactlyFourMediumTrackHighEffBjets = countPatJets.clone(src = 'mediumTrackHighEffBjets',
                                                      minNumber = 4,
                                                      maxNumber = 4
                                                      )
#------------------------------
# trackHighPurBjet countFilter
#------------------------------

## select events with 1 medium bjet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneLooseTrackHighPurBjet = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                              minNumber = 1
                                              )
## select events with 2 loose bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoLooseTrackHighPurBjets = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                               minNumber = 2
                                               )
## select events with 3 loose bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeLooseTrackHighPurBjets = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                                 minNumber = 3
                                                 )
## select events with 4 loose bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourLooseTrackHighPurBjets = countPatJets.clone(src = 'looseTrackHighPurBjets',
                                                minNumber = 4
                                                )

## select events with 1 medium bjet
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneMediumTrackHighPurBjet = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                               minNumber = 1
                                               )
## select events with 2 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoMediumTrackHighPurBjetss = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                                 minNumber = 2
                                                 )
## select events with 3 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
threeMediumTrackHighPurBjets = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                                  minNumber = 3
                                                  )
## select events with 4 medium bjets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourMediumTrackHighPurBjets = countPatJets.clone(src = 'mediumTrackHighPurBjets',
                                                 minNumber = 4
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
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )
## select events with one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
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
filterLooseHT.Cut = 250

filterMediumHT = filterHT.clone()
filterMediumHT.jets = "goodJets"
filterMediumHT.Cut = 300

filterTightHT = filterHT.clone()
filterTightHT.jets = "goodJets"
filterTightHT.Cut = 350

## DiLepton Filter
from TopAnalysis.TopFilter.filters.DiMuonFilter_cfi import *
SSignMuMuFilter = filterMuonPair.clone()
ZVetoMu = filterMuonPair.clone()
ZVetoMu.isVeto = True

from TopAnalysis.TopFilter.filters.DiElectronFilter_cfi import *          

SSignElElFilter = filterElecPair.clone()
ZVetoEl = filterElecPair.clone()
ZVetoEl.isVeto = True

from PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi import *

oneLooseLepton = countPatLeptons.clone()
oneLooseLepton.electronSource = "looseElectrons"
oneLooseLepton.muonSource = "looseMuons"  
oneLooseLepton.minNumber = 1

oneGoodLepton = countPatLeptons.clone()
oneGoodLepton.electronSource = "goodElectrons"
oneGoodLepton.muonSource = "goodMuons"                           
oneGoodLepton.minNumber = 1
oneGoodLepton.maxNumber = 1

atLeastOneGoodLepton = countPatLeptons.clone()
atLeastOneGoodLepton.electronSource = "goodElectrons"
atLeastOneGoodLepton.muonSource = "goodMuons"                           
atLeastOneGoodLepton.minNumber = 1

twoGoodLeptons = countPatLeptons.clone()
twoGoodLeptons.electronSource = "goodElectrons"
twoGoodLeptons.muonSource = "goodMuons"                           
twoGoodLeptons.minNumber = 2

leptonVeto = countPatLeptons.clone()

#------------------------------
# Define sequences
#------------------------------

matchedGoodObjects = cms.Sequence(matchedBjets *
                                  matchedLightJets ## *
##                                   matchedMuons  *
##                                   matchedElectrons
                                  )

goodObjects = cms.Sequence(looseMuons *
                           looseElectrons *
                           trackMuons *
                           vertexMuons *
                           vetoMuons *
                           vetoElectrons *
                           isolatedElectrons *
                           goodElectrons*
                           looseJets *
                           goodJets *
                           lightJets *
                           mediumJets *
                           tightJets *
                           goodMuons *
                           looseMETs *
                           goodMETs *
                           tightMETs *
                           looseTrackHighPurBjets *
                           mediumTrackHighPurBjets *
                           tightTrackHighPurBjets *
                           looseTrackHighEffBjets *
                           mediumTrackHighEffBjets *
                           tightTrackHighEffBjets
                           )

muonSelection = cms.Sequence(oneGoodMuon *
                             exactlyOneGoodMuon *
                             noGoodElectron
                             )

electronSelection = cms.Sequence(oneGoodElectron *
                                 exactlyOneGoodElectron *
                                 noGoodMuon
                                 )

leptonSelection = cms.Sequence(oneGoodLepton
                               )

jetSelection = cms.Sequence(fourLooseJets ##*
##                             twoMediumJets
##                             oneTightJet
                            )

metSelection = cms.Sequence(oneGoodMET
                            )

HTSelection = cms.Sequence(filterMediumHT)

tightHTSelection = cms.Sequence(filterTightHT)

MuHadSelection = cms.Sequence(filterMediumHT *
                              oneLooseMuon
                              )

ElHadSelection = cms.Sequence(filterMediumHT *
                              oneLooseElectron
                              )

LepHadSelection = cms.Sequence(filterMediumHT *
                               oneLooseLepton
                               )

muonVeto = cms.Sequence(oneVetoMuon *
                        noVetoElectron
                        )

electronVeto = cms.Sequence(oneVetoElectron *
                            noVetoMuon
                            )

makeObjects = cms.Sequence(goodObjects *
                           matchedGoodObjects
                           )
