import FWCore.ParameterSet.Config as cms


#------------------------------
# lepton collections 
#------------------------------

## create good muon collection
from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *

goodMuons = cleanPatMuons.clone(preselection =
                                # Global Muon Prompt Tight
                                'isGlobalMuon &'
                                'globalTrack.normalizedChi2 < 10.0 &'
                                'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                # other requirements 
                                'isTrackerMuon &'
                                'pt > 20. &'
                                'abs(eta) < 2.1 &'
                                '(trackIso+caloIso)/pt < 0.05 &'
                                'abs(dB) < 0.02 &' # !! 'abs(track.d0) < 0.02 &' # abs(dB) = abs(dxy(Beam Spot))??
                                'globalTrack.hitPattern.numberOfValidTrackerHits > 10'
                                )

## Check good Muons for overlap with jets 
goodMuons.checkOverlaps = cms.PSet(
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
goodElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt > 20. &'
                                           'abs(eta) < 2.4 &'
                                           'electronID(\"simpleEleId80relIso\")=7'
                                           #'(abs(eta) < 1.47 | abs(eta) > 1.507) $'
                                           )

#------------------------------
# lepton-veto collections
#------------------------------

## create veto-muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
vetoMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                   cut =
                                   'isGlobalMuon &'
                                   'pt > 10. &'
                                   'abs(eta) < 2.5 &'
                                   '(trackIso+caloIso)/pt <  0.2'
                                   )

## create veto-electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
vetoElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt > 15. &'
                                           'abs(eta) < 2.5 &'
                                           #'(abs(eta) < 1.47 | abs(eta) > 1.507) $'
                                           '(dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/et<0.2 '
                                           )

#------------------------------
# jet collection
#------------------------------

## create jet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
goodJets = selectedPatJets.clone(src = 'selectedPatJets',
                                 cut =
                                 'abs(eta) < 2.4 &'
                                 'pt > 30. &'
                                 'emEnergyFraction > 0.01 &'
                                 'jetID.fHPD < 0.98 &'
                                 'jetID.n90Hits > 1'
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

#------------------------------
# filter
#------------------------------

## select events with at least good hard muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                  minNumber = 1
                                  )

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
oneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                          minNumber = 1
                                          )

## select events with no veto muon
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

## select events with one veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                         maxNumber = 0
                                         )

## select events with one veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                         maxNumber = 0
                                         )

## select events with 4 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 4
                                  )
## select events with good one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )

#------------------------------
# Define sequences
#------------------------------

muonSelection = cms.Sequence(#goodJets *
                             goodMuons *
                             goodElectrons *
                             oneGoodMuon
                             )

electronSelection = cms.Sequence(#goodJets *
                                 goodElectrons *
                                 goodMuons *
                                 oneGoodElectron
                                 )

jetSelection = cms.Sequence(goodJets *
                            fourGoodJets
                            )

metSelection = cms.Sequence(goodMETs *
                            oneGoodMET
                            )

muonVeto = cms.Sequence(vetoMuons *
                        vetoElectrons *
                        oneVetoMuon *
                        noVetoElectron
                        )

electronVeto = cms.Sequence(vetoMuons *
                            vetoElectrons *
                            oneVetoElectron *
                            noVetoMuon
                            )
