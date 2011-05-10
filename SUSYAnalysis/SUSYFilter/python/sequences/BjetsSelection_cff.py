import FWCore.ParameterSet.Config as cms


#------------------------------
# lepton collections 
#------------------------------

## create good muon collection
#from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *

from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
from TopAnalysis.TopFilter.filters.MuonJetOverlapSelector_cfi import *
from TopAnalysis.TopFilter.sequences.MuonVertexDistanceSelector_cfi import *

trackMuons = selectedPatMuons.clone(src = "selectedPatMuons",
                                    cut =
                                    ## Global Muon Prompt Tight
                                    ##---------------------------
                                    #'isGlobalMuon &'
                                    #'globalTrack.normalizedChi2 < 10.0 &'
                                    #'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                    'isGood("GlobalMuonPromptTight") &'
                                    ## Track Muon
                                    ##-------------
                                    #'isTrackerMuon &'
                                    'isGood("AllTrackerMuons") &'
                                    ## Other requirements
                                    ##---------------------
                                    'pt >= 20. &'
                                    'abs(eta) <= 2.1 &'
                                    '(trackIso+hcalIso+ecalIso)/pt < 0.1 &'
                                    'abs(dB) < 0.02 &' # !! 'abs(track.d0) < 0.02 &' # abs(dB) = abs(dxy(Beam Spot))??
                                    'globalTrack.hitPattern.numberOfValidTrackerHits > 10 &'
                                    'numberOfMatches() > 1 &'
                                    'innerTrack().hitPattern().pixelLayersWithMeasurement() >= 1 '
                                    #'abs( innerTrack().vertex().z() - PV().z()) < 1'
                                   )

vertexMuons = vertexSelectedMuons.clone(src = "trackMuons"
                                        )

goodMuons = checkJetOverlapMuons.clone(muons = "vertexMuons",
                                       jets =  "goodJets" ,
                                       deltaR  = cms.double(0.3),
                                       overlap = cms.bool(False)
                                       )

## Check good muons for overlap with jets 
## goodMuons.checkOverlaps = cms.PSet(
##     jets = cms.PSet(src       = cms.InputTag("goodJets"),
##                     algorithm = cms.string("byDeltaR"),
##                     preselection        = cms.string(""),
##                     deltaR              = cms.double(0.3),
##                     checkRecoComponents = cms.bool(False),
##                     pairCut             = cms.string(""),
##                     requireNoOverlaps   = cms.bool(True),
##                     )
##     )

## create good electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
goodElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt >= 20. &'
                                           'abs(eta) <= 2.4 &'
                                           'electronID(\"simpleEleId80relIso\")=7 &'
                                           '(abs(eta) < 1.4442 | abs(eta) > 1.566)'
                                           )

## create veto-muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
looseMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                   cut =
                                   'pt > 10.'
                                   #'abs(eta) < 2.5'
                                   )

## create veto-electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
looseElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt > 10.'
                                           #'abs(eta) < 2.5 '
                                           )

#------------------------------
# matched-lepton collections 
#------------------------------

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
# lepton-veto collections
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
                                           #'(abs(eta) < 1.4442 | abs(eta) > 1.566) &'
                                           'electronID(\"simpleEleId95relIso\")=7 '
                                           )

#------------------------------
# jet collections
#------------------------------

## create good jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
goodJets = selectedPatJets.clone(src = 'selectedPatJets',
                                 cut =
                                 'abs(eta) < 2.4 &'
                                 'pt > 30. &'
                                 'emEnergyFraction > 0.01 &'
                                 'jetID.fHPD < 0.98 &'
                                 'jetID.n90Hits > 1'
                                 )

## goodJets.checkOverlaps.muons.src = "goodMuons"
## goodJets.checkOverlaps.muons.deltaR = 0.3
## goodJets.checkOverlaps.muons.requireNoOverlaps = False

## goodJets.checkOverlaps.electrons.src = "goodElectrons"
## goodJets.checkOverlaps.electrons.deltaR = 0.3
## goodJets.checkOverlaps.electrons.requireNoOverlaps = False

## goodJets.checkOverlaps.photons.src = "goodElectrons"
## goodJets.checkOverlaps.photons.requireNoOverlaps = False

## goodJets.checkOverlaps.taus.src = "goodElectrons"
## goodJets.checkOverlaps.taus.requireNoOverlaps = False

## goodJets.checkOverlaps.tkIsoElectrons.src = "goodElectrons"
## goodJets.checkOverlaps.tkIsoElectrons.requireNoOverlaps = False

## goodJets.checkOverlap = cms.PSet(
##         muons = cms.PSet(
##            src       = cms.InputTag("goodMuons"),
##            algorithm = cms.string("byDeltaR"),
##            preselection        = cms.string(""),
##            deltaR              = cms.double(0.3),
##            checkRecoComponents = cms.bool(False),
##            pairCut             = cms.string(""),
##            requireNoOverlaps   = cms.bool(True),
##         ),
##         electrons = cms.PSet(
##            src       = cms.InputTag("goodElectrons"),
##            algorithm = cms.string("byDeltaR"),
##            preselection        = cms.string(""),
##            deltaR              = cms.double(0.3),
##            checkRecoComponents = cms.bool(False),
##            pairCut             = cms.string(""),
##            requireNoOverlaps   = cms.bool(True),
##        )
## )

## create good jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
mediumJets = selectedPatJets.clone(src = 'goodJets',
                                   cut =
                                   'pt > 60.'
                                   )

## create good jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
tightJets = selectedPatJets.clone(src = 'selectedPatJets',
                                  cut =
                                  'pt > 100.'
                                  )

#------------------------------
# bjet collections
#------------------------------

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
goodMETs = selectedPatMET.clone(src = 'patMETs',
                                cut =
                                'et > 100.'
                                )

## create MET collection
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
looseMETs = selectedPatMET.clone(src = 'patMETs',
                                 cut =
                                 'et > 50.'
                                 )

#------------------------------
# muon countFilter
#------------------------------

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                  minNumber = 1
                                  )

## select events with at least two good muons
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
twoGoodMuons = countPatMuons.clone(src = 'goodMuons',
                                   minNumber = 2
                                   )

## select events with at least two good muons
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneLooseMuon = countPatMuons.clone(src = 'looseMuons',
                                   minNumber = 1
                                   )

#------------------------------
# electron countFilter
#------------------------------

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                          minNumber = 1
                                          )
## select events with at least two good electrons
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
twoGoodElectrons = countPatElectrons.clone(src = 'goodElectrons',
                                           minNumber = 2
                                           )

#------------------------------
# veto-lepton countFilter
#------------------------------

## select events with one veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  maxNumber = 1
                                  )
## select events with no veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
noVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  maxNumber = 0
                                  )
## select events with one veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
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


## select events with 3 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
oneTightJet = countPatJets.clone(src = 'tightJets',
                                 minNumber = 1
                                 )
## select events with 2 medium jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
twoMediumJets = countPatJets.clone(src = 'mediumJets',
                                   minNumber = 2
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
## select events with 5 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fiveGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 5
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
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )

## select events with one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneLooseMET = countPatMET.clone(src = 'looseMETs',
                                minNumber = 1
                                )

#-----------------------------
# Event Filter
#-----------------------------

from SUSYAnalysis.SUSYFilter.filters.HTFilter_cfi import *

filterHT1 = filterHT.clone()
filterHT1.jets = "goodJets"
filterHT1.Cut = 300

filterHT2 = filterHT.clone()
filterHT2.jets = "goodJets"
filterHT2.Cut = 350

filterHT3 = filterHT.clone()
filterHT3.jets = "goodJets"
filterHT3.Cut = 220

from TopAnalysis.TopFilter.filters.DiMuonFilter_cfi import *
SSignMuMuFilter = filterMuonPair.clone()
ZVetoMu = filterMuonPair.clone()
ZVetoMu.isVeto = True

from TopAnalysis.TopFilter.filters.DiElectronFilter_cfi import *          

SSignElElFilter = filterElecPair.clone()
ZVetoEl = filterElecPair.clone()
ZVetoEl.isVeto = True

from PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi import *

oneLepton = countPatLeptons.clone()                           
oneLepton.minNumber = 1

twoLeptons = countPatLeptons.clone()                           
twoLeptons.minNumber = 2

oneGoodLepton = countPatLeptons.clone()
oneGoodLepton.electronSource = "goodElectrons"
oneGoodLepton.muonSource = "goodMuons"                           
oneGoodLepton.minNumber = 1

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

goodObjects = cms.Sequence(goodJets *
                           trackMuons *
                           vertexMuons *
                           goodMuons *
                           goodElectrons*
                           goodMETs *
                           looseMETs *
                           vetoMuons *
                           vetoElectrons *
                           #goodJets *
                           mediumJets *
                           tightJets *
                           looseMuons *
                           looseElectrons *
                           looseTrackHighPurBjets *
                           mediumTrackHighPurBjets *
                           tightTrackHighPurBjets *
                           looseTrackHighEffBjets *
                           mediumTrackHighEffBjets *
                           tightTrackHighEffBjets
                           )

muonSelection = cms.Sequence(oneGoodMuon
                             )

electronSelection = cms.Sequence(oneGoodElectron
                                 )

metSelection = cms.Sequence(oneGoodMET
                            )

looseMetSelection = cms.Sequence(oneLooseMET
                                 )

HTSelection = cms.Sequence(filterHT1)

tightHTSelection = cms.Sequence(filterHT2)

MuHadSelection = cms.Sequence(filterHT3 *
                              oneLooseMuon
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
