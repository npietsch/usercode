import FWCore.ParameterSet.Config as cms


#------------------------------
# lepton collections 
#------------------------------

## create good muon collection
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
goodMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                   cut =
                                   'isGlobalMuon &'
                                   'isTrackerMuon &'
                                   'globalTrack.normalizedChi2 < 10 &'
                                   'globalTrack.hitPattern.numberOfValidTrackerHits > 10 &'
                                   'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                   'abs(eta) < 2.4 &'
                                   'pt > 5. &'
                                   'abs(dB) < 0.02 &' ## =abs(dxy) zum beam spot
                                   'ecalIsoDeposit.candEnergy < 4 &'
                                   'hcalIsoDeposit.candEnergy < 6 &'
                                   '(trackIso+caloIso)/pt < 0.15'
                                   )
## create good electron collection
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
goodElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt > 20. &'
                                           'abs(eta) < 2.4 &'
                                           'electronID(\"simpleEleId80relIso\")=7 '
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
                                           #'(abs(eta) < 1.47 | abs(eta) > 1.507) &'
                                           '(dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/et<0.2 '
                                           )

#------------------------------
# jet collection
#------------------------------

## create jet collection
from PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi import *
goodJets = cleanPatJets.clone(src = cms.InputTag("selectedPatJetsAK5PF"),
                              preselection = cms.string('(pt > 30. &'
                                                        'abs(eta) < 2.4 &'
                                                        'neutralHadronEnergyFraction < 0.99 &'
                                                        'neutralEmEnergyFraction     < 0.99 &'
                                                        'nConstituents > 1 ) ||'
                                                        
                                                        '(pt > 30. &'
                                                        'abs(eta) < 2.4 &'
                                                        'neutralHadronEnergyFraction < 0.99 &'
                                                        'neutralEmEnergyFraction     < 0.99 &'
                                                        'nConstituents > 1 &'
                                                        'chargedHadronEnergyFraction > 0.0  &'
                                                        'chargedMultiplicity > 0            &'
                                                        'chargedEmEnergyFraction     < 0.99)'
                                                        )
                              )
goodJets.checkOverlaps = cms.PSet(
    muons = cms.PSet(src = cms.InputTag("goodMuons"),
                     preselection        = cms.string(""),
                     algorithm = cms.string("byDeltaR"),
                     deltaR              = cms.double(0.4),
                     checkRecoComponents = cms.bool(False),
                     pairCut             = cms.string(""),
                     requireNoOverlaps   = cms.bool(True),
                     ),
    electrons = cms.PSet(src = cms.InputTag("goodElectrons"),
                         preselection        = cms.string(""),
                         algorithm = cms.string("byDeltaR"),
                         deltaR              = cms.double(0.4),
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
                                'et > 30.'
                                )

#------------------------------
# count Filter
#------------------------------

## select events with at least good hard muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
countGoodMuons = countPatMuons.clone(src = 'goodMuons',
                                     minNumber = 2
                                     )
## select events with no veto muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
countVetoMuons = countPatMuons.clone(src = 'vetoMuons',
                                     maxNumber = 2
                                     )
## select events with one veto electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
countVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                            maxNumber = 0
                                            )
## select events with 2 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
countGoodJets = countPatJets.clone(src = 'goodJets',
                                   minNumber = 2
                                   )
## select events with good one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
countGoodMET = countPatMET.clone(src = 'goodMETs',
                                 minNumber = 1
                                 )

#------------------------------
# Event Filter
#------------------------------

#from SUSYAnalysis.SUSYFilter.selections.HTSelection_cff import *
from SUSYAnalysis.SUSYFilter.filters.HTFilter_cfi import *
filterHT.jets= "goodJets"

from TopAnalysis.TopFilter.filters.DiMuonFilter_cfi import *
SSignMuMuFilter = filterMuonPair.clone()
mLowVeto5 = filterMuonPair.clone()
ZVeto = filterMuonPair.clone()

#------------------------------
# Define sequences
#------------------------------

muonSelection = cms.Sequence(goodMuons *
                             countGoodMuons *
                             SSignMuMuFilter *
                             mLowVeto5 *
                             ZVeto
                             )

jetSelection = cms.Sequence(goodElectrons *
                            goodJets *
                            countGoodJets
                            )

metSelection = cms.Sequence(goodMETs *
                            countGoodMET
                            )

HTSelection = cms.Sequence(filterHT)
