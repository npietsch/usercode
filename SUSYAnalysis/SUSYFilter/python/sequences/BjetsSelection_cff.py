import FWCore.ParameterSet.Config as cms

#------------------------------------------------------------------------------
# Configure modules to produce collections of good objects and veto leptons
#------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
from PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *

from TopAnalysis.TopFilter.sequences.MuonVertexDistanceSelector_cfi import *
from TopAnalysis.TopFilter.sequences.ElectronVertexDistanceSelector_cfi import *


## configure module to produce collection of good muons
muons = selectedPatMuons.clone(src = "selectedPatMuons",
                               cut =
                               'isGlobalMuon() &'
                               'isPFMuon() &'
                               'pt >= 20. &'
                               'abs(eta) <= 2.4 &'
                               '(pfIsolationR03().sumChargedHadronPt+'
                               'max(0., pfIsolationR03().sumNeutralHadronEt+'
                               'pfIsolationR03().sumPhotonEt - 0.5*pfIsolationR03().sumPUPt))/'
                               'pt()<0.12 &'
                               'globalTrack().chi2()/globalTrack().ndof() < 11 &'
                               'globalTrack().hitPattern().numberOfValidMuonHits > 0 &'
                               'numberOfMatchedStations() &'
                               'innerTrack().hitPattern().numberOfValidPixelHits() > 0 &'
                               'track().hitPattern().trackerLayersWithMeasurement() > 5 &'
                               'abs(dB(\"PV2D\")) < 0.02'
                               )

goodMuons = vertexSelectedMuons.clone(src = "muons",
                                      cutValue = 0.5#,
                                      #dxy_cut = True
                                      )
          
## configure module to produce collection of veto muons
looseMuons = selectedPatMuons.clone(src = "selectedPatMuons",
                                    cut =
                                    'isGlobalMuon() || isTrackerMuon() &'
                                    'isPFMuon() &'
                                    'pt >= 15. &'
                                    'abs(eta) <= 2.5 &'
                                    '(pfIsolationR03().sumChargedHadronPt+'
                                    'max(0., pfIsolationR03().sumNeutralHadronEt+'
                                    'pfIsolationR03().sumPhotonEt - 0.5*pfIsolationR03().sumPUPt))/'
                                    'pt()<0.2 &'
                                    'abs(dB(\"PV2D\")) < 0.2'
                                    )

vetoMuons = vertexSelectedMuons.clone(src = "looseMuons",
                                      cutValue = 0.5#,
                                      #dxy_cut = True,
                                      #dxy = 0.2
                                      )

## configure module to produce collection of good electrons
goodElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt >= 20. &'
                                           'abs(eta) <= 2.5 &'
                                           '(abs(superCluster.eta) < 1.4442 | abs(superCluster.eta) > 1.566)'
##                                            'electronID(\"simpleEleId80relIso\")=7 &'
##                                            'fbrem() > 0.15 | (fbrem() < 0.15 & abs(eta) < 1 & eSuperClusterOverP() > 0.95) &'
##                                            'abs(dB) < 0.02 &'
##                                            'abs(track().dz()) < 0.1 &'
##                                            #'(dr03TkSumPt() + dr03EcalRecHitSumEt() + dr03HcalTowerSumEt())/pt < 0.15 '
##                                            '((dr03TkSumPt() + dr03EcalRecHitSumEt() + dr03HcalTowerSumEt())/pt < 0.15 & abs(eta) > 1.479) | ((dr03TkSumPt() + max(0, dr03EcalRecHitSumEt()-1) + dr03HcalTowerSumEt())/pt < 0.15 & abs(eta) < 1.479) '
                                           )

## configure module to produce collection of veto electrons
vetoElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                           cut =
                                           'pt >= 20. &'
                                           'abs(eta) <= 2.5 &'
                                           '(abs(superCluster.eta) < 1.4442 | abs(superCluster.eta) > 1.566)'
 ##                                          'electronID(\"simpleEleId80relIso\")=7 &'
##                                            'fbrem() > 0.15 | (fbrem() < 0.15 & abs(eta) < 1 & eSuperClusterOverP() > 0.95) &'
##                                            'abs(dB) < 0.02 &'
##                                            'abs(track().dz()) < 0.1 &'
##                                            #'(dr03TkSumPt() + dr03EcalRecHitSumEt() + dr03HcalTowerSumEt())/pt < 0.15 '
##                                            '((dr03TkSumPt() + dr03EcalRecHitSumEt() + dr03HcalTowerSumEt())/pt < 0.15 & abs(eta) > 1.479) | ((dr03TkSumPt() + max(0, dr03EcalRecHitSumEt()-1) + dr03HcalTowerSumEt())/pt < 0.15 & abs(eta) < 1.479) '
                                           )


## configure module to produce collection of good jets
goodJets = cleanPatJets.clone(src = 'selectedPatJetsAK5PF',
                              preselection =
                              'pt > 40. &'
                              'abs(eta) < 2.4 &'
                              'neutralHadronEnergyFraction < 0.99 &'
                              'neutralEmEnergyFraction     < 0.99 &'
                              'nConstituents               > 1 &'
                              'chargedHadronEnergyFraction > 0.0 &'
                              'chargedMultiplicity         > 0 &'
                              'chargedEmEnergyFraction     < 0.99 &'
                              '(chargedMultiplicity + neutralMultiplicity + muonMultiplicity) > 1'
                              )

## reject jets close to selected leptons
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
## configure module to produce collection of good METs
goodMETs = selectedPatMET.clone(src = 'patMETsPF',
                                cut =
                                'et > 100.'
                                )

#------------------------------------------------------------------------------
# Configure filter modules for selection of events based on number of objects
#------------------------------------------------------------------------------

from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *

## configure module to select events with exactly one good muon 
exactlyOneGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )

## configure module to select events with no one good muon 
noGoodMuon = countPatMuons.clone(src = 'goodMuons',
                                 minNumber = 0,
                                 maxNumber = 0
                                 )

## configure module to select events with exactly veto good muon 
exactlyOneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                         minNumber = 1,
                                         maxNumber = 1
                                         )

## configure module to select events with exactly one good electron 
exactlyOneGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1
                                                 )

## configure module to select events with exactly no good electron 
noGoodElectron = countPatElectrons.clone(src = 'goodElectrons',
                                         minNumber = 0,
                                         maxNumber = 0
                                         )

## configure module to select events with exactly one veto electron 
exactlyOneVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                                 minNumber = 1,
                                                 maxNumber = 1
                                                 )

## configure module to select events with maximal one veto lepton
exactlyOneVetoLepton = countPatLeptons.clone()
exactlyOneVetoLepton.electronSource = "vetoElectrons"
exactlyOneVetoLepton.muonSource = "vetoMuons"                           
exactlyOneVetoLepton.minNumber = 1
exactlyOneVetoLepton.maxNumber = 1

## configure module to select events with at least four good jets
fourGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 4
                                  )

## configure module to select events with at least one good Muons
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )


#------------------------------------------------------------------------------
# Configure other filter modules
#------------------------------------------------------------------------------

## HT filter
from SUSYAnalysis.SUSYFilter.filters.HTFilter_cfi import *
filterGoodHT = filterHT.clone()
filterGoodHT.jets = "goodJets"
filterGoodHT.Cut = 300

## MHT filter
from SUSYAnalysis.SUSYFilter.filters.MHTFilter_cfi import *
filterMediumMHT = filterMHT.clone()
filterMediumMHT.jets = "goodJets"
filterMediumMHT.Cut = 100

## DiLepton Filter
from TopAnalysis.TopFilter.filters.DiLeptonFilter_cfi import *

## Transverse mass filter
from SUSYAnalysis.SUSYFilter.filters.TransverseMassFilter_cfi import *
filterMT = filterTransverseMass.clone()
filterMT.muons = "goodMuons"
filterMT.electrons = "goodElectrons"

#------------------------------------------------------------------------------
# Define producer and filter sequences
#------------------------------------------------------------------------------

createObjects = cms.Sequence(muons *
                             goodMuons *
                             looseMuons *
                             vetoMuons *
                             goodElectrons *
                             vetoElectrons *
                             goodJets *
                             goodMETs
                             )

from SUSYAnalysis.SUSYFilter.filters.PFMuonConsistency_cfi import *
pfMuonConsistency.muons = "goodMuons"

muonSelection = cms.Sequence(exactlyOneGoodMuon *
                             #pfMuonConsistency *
                             noGoodElectron *
                             exactlyOneVetoMuon *
                             exactlyOneVetoLepton
                             )

electronSelection = cms.Sequence(exactlyOneGoodElectron *
                                 noGoodMuon *
                                 exactlyOneVetoElectron *
                                 exactlyOneVetoLepton
                                 )

jetSelection = cms.Sequence(fourGoodJets)

HTSelection = cms.Sequence(filterGoodHT)

metSelection = cms.Sequence(oneGoodMET
                            )
