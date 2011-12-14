import FWCore.ParameterSet.Config as cms


##======================================================================
##========================= DEFINE GOOD OBJECTS ========================
##======================================================================


#-------------------------------
# collections of good leptons
#-------------------------------

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
                                    'innerTrack().hitPattern().pixelLayersWithMeasurement() >= 1 &'
                                    '(globalTrack.ptError)/(pt*pt) < 0.001'
                                    )

goodMuons = vertexSelectedMuons.clone(src = "trackMuons"
                                      )

## create good electron collection
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

#-------------------------------
# collections of veto leptons
#-------------------------------

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
# collections of loose leptons
#------------------------------

## create collection of loose muons
looseMuons = selectedPatMuons.clone(src = 'selectedPatMuons',
                                    cut =
                                    'pt > 20. &'
                                    'abs(eta) < 2.5'
                                    )

## create collection of loose electrons
looseElectrons = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                            cut =
                                            'pt > 20. &'
                                            'abs(eta) < 2.5 '
                                            )

#-------------------------------
# collections of good jets
#-------------------------------

## create collection of good Jets
from PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi import *
goodJets = cleanPatJets.clone(src = 'selectedPatJetsAK5PF',
                              preselection =
                              'abs(eta) < 2.4 &'
                              'pt > 40. &'
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

#-----------------------------------------------------
# create collection of good b-tagged jets
#-----------------------------------------------------

## create mediumTrackHighEffBjet collection
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
mediumTrackHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                                cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                )

## create mediumSSVHighEffBjet collection
mediumSSVHighEffBjets = selectedPatJets.clone(src = 'goodJets',
                                              cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                              )

#-------------------------------
# collections of good METs
#-------------------------------

## create collection of good METs
from PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi import *
goodMETs = selectedPatMET.clone(src = 'patMETsPF',
                                cut =
                                'et > 80.'
                                )

## create collection of RA4 METs
RA4METs = selectedPatMET.clone(src = 'patMETsPF',
                               cut =
                               'et > 100.'
                               )

#--------------------------------------------------------------------------------------------
# collections of good jets, good  b-tagged jets and METs with jet energy scaled up and down
#--------------------------------------------------------------------------------------------

## create collection of good Jets with scaled up jet energy corrections
goodJetsJECUp = goodJets.clone()
goodJetsJECUp.src = "scaledJetEnergyJECUp:selectedPatJetsAK5PF"

## create collection of good Jets with scaled down jet energy corrections
goodJetsJECDown = goodJets.clone()
goodJetsJECDown.src = "scaledJetEnergyJECDown:selectedPatJetsAK5PF"

## create collection of good Jets with smeared jet energy
goodJetsJER = goodJets.clone()
goodJetsJER.src = "scaledJetEnergy:selectedPatJetsAK5PF"

## create collection of good Jets with scaled up jet energy resolution
goodJetsJERUp = goodJets.clone()
goodJetsJERUp.src = "scaledJetEnergyJERUp:selectedPatJetsAK5PF"

## create collection of good Jets with scaled down jet energy resolution
goodJetsJERDown = goodJets.clone()
goodJetsJERDown.src = "scaledJetEnergyJERDown:selectedPatJetsAK5PF"


## create collection of good METs with scaled up jet energy corrections
goodMETsJECUp = goodMETs.clone()
goodMETsJECUp.src = "scaledJetEnergyJECUp:patMETsPF"

## create collection of good METs with scaled down jet energy corrections
goodMETsJECDown = goodMETs.clone()
goodMETsJECDown.src = "scaledJetEnergyJECDown:patMETsPF"

## create collection of good METs with smeared jet energy 
goodMETsJER = goodMETs.clone()
goodMETsJER.src = "scaledJetEnergy:patMETsPF"

## create collection of good METs with scaled up jet energy resolution
goodMETsJERUp = goodMETs.clone()
goodMETsJERUp.src = "scaledJetEnergyJERUp:patMETsPF"

## create collection of good METs with scaled down jet energy resolution
goodMETsJERDown = goodMETs.clone()
goodMETsJERDown.src = "scaledJetEnergyJERDown:patMETsPF"


## create mediumTrackHighEffBjet collection with scaled up jet energy corrections
mediumTrackHighEffBjetsJECUp = selectedPatJets.clone(src = 'goodJetsJECUp',
                                                     cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                     )

## create mediumTrackHighEffBjet collection with scaled down jet energy corrections
mediumTrackHighEffBjetsJECDown = selectedPatJets.clone(src = 'goodJetsJECDown',
                                                       cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                       )

## create mediumTrackHighEffBjet collection with smeared jet energy
mediumTrackHighEffBjetsJER = selectedPatJets.clone(src = 'goodJetsJER',
                                                   cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                   )

## create mediumTrackHighEffBjet collection with scaled up jet energy resolution
mediumTrackHighEffBjetsJERUp = selectedPatJets.clone(src = 'goodJetsJERUp',
                                                     cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                     )

## create mediumTrackHighEffBjet collection with scaled down jet energy resolution
mediumTrackHighEffBjetsJERDown = selectedPatJets.clone(src = 'goodJetsJERDown',
                                                       cut = 'bDiscriminator(\"trackCountingHighEffBJetTags\") > 3.3'
                                                       )


## create mediumSSVHighEffBjet collection with scaled up jet energy corrections
mediumSSVHighEffBjetsJECUp = selectedPatJets.clone(src = 'goodJetsJECUp',
                                                   cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                                   )

## create mediumSSVHighEffBjet collection with scaled down jet energy corrections
mediumSSVHighEffBjetsJECDown = selectedPatJets.clone(src = 'goodJetsJECDown',
                                                     cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                                     )

## create mediumSSVHighEffBjet collection with smeared jet energy
mediumSSVHighEffBjetsJER = selectedPatJets.clone(src = 'goodJetsJER',
                                                 cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                                 )

## create mediumSSVHighEffBjet collection with scaled up jet energy resoltuion
mediumSSVHighEffBjetsJERUp = selectedPatJets.clone(src = 'goodJetsJERUp',
                                                   cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                                   )

## create mediumSSVHighEffBjet collection with scaled down jet energy resolution
mediumSSVHighEffBjetsJERDown = selectedPatJets.clone(src = 'goodJetsJERDown',
                                                     cut = 'bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") > 1.74 '
                                                     )


#--------------------------------------------------------------------------------------------
# collections of METs with unclustered energy scaled up and down
#--------------------------------------------------------------------------------------------

## create collection of good METs with scaled up unclustered energy
goodMETsMETUp = goodMETs.clone()
goodMETsMETUp.src = "unclusteredEnergyUp:scaledMET"

## create collection of good METs with scaled down unclustered energy
goodMETsMETDown = goodMETs.clone()
goodMETsMETDown.src = "unclusteredEnergyDown:scaledMET"



##======================================================================
##========================== COUNT GOOD OBJECTS ========================
##======================================================================


#------------------------------
# muon countFilter
#------------------------------

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
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
#------------------------------
# electron countFilter
#------------------------------

## select events with at least one good electron
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
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
#------------------------------
# veto lepton countFilter
#------------------------------

## select events with exactly one veto muon
oneVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  minNumber = 1,
                                  maxNumber = 1
                                  )

## select events with no veto muon
noVetoMuon = countPatMuons.clone(src = 'vetoMuons',
                                  maxNumber = 0
                                  )

## select events with exactly one veto electron
oneVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                          minNumber = 1,
                                          maxNumber = 1
                                          )
## select events with no veto electron
noVetoElectron = countPatElectrons.clone(src = 'vetoElectrons',
                                         maxNumber = 0
                                         )
#------------------------------
# loos lepton countFilter
#------------------------------

## select events with at least one loose muon
oneLooseMuon = countPatMuons.clone(src = 'looseMuons',
                                   minNumber = 1
                                   )

## select events with at least one loose electron
oneLooseElectron = countPatElectrons.clone(src = 'looseElectrons',
                                           minNumber = 1
                                           )
#------------------------------
# jet countFilter
#------------------------------

## select events with 4 good jets
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *
fourGoodJets = countPatJets.clone(src = 'goodJets',
                                  minNumber = 4
                                  )
#------------------------------
# met countFilter
#------------------------------

## select events with one good MET
from PhysicsTools.PatAlgos.selectionLayer1.metCountFilter_cfi import *
oneGoodMET = countPatMET.clone(src = 'goodMETs',
                               minNumber = 1
                               )

## select events with one RA4 MET
oneRA4MET = countPatMET.clone(src = 'RA4METs',
                              minNumber = 1
                              )

#----------------------------------------------------------------------------
# filter on number of good jets and METs with jet energy scaled up and down
#----------------------------------------------------------------------------

## select events with 4 good Jets with scaled up jet energy corrections
fourGoodJetsJECUp = countPatJets.clone(src = 'goodJetsJECUp',
                                       minNumber = 4
                                       )

## select events with 4 good Jets with scaled down jet energy corrections
fourGoodJetsJECDown = countPatJets.clone(src = 'goodJetsJECDown',
                                         minNumber = 4
                                         )

## select events with 4 good jets with smeared jet energy
fourGoodJetsJER = countPatJets.clone(src = 'goodJetsJER',
                                     minNumber = 4
                                     )

## select events with 4 good Jets with scaled up jet energy resolutions
fourGoodJetsJERUp = countPatJets.clone(src = 'goodJetsJERUp',
                                       minNumber = 4
                                       )

## select events with 4 good Jets with scaled down jet energy resolutions
fourGoodJetsJERDown = countPatJets.clone(src = 'goodJetsJERDown',
                                         minNumber = 4
                                         )


## select events with 1 good MET with scaled up jet energy corrections
oneGoodMETJECUp = countPatMET.clone(src = 'goodMETsJECUp',
                                    minNumber = 1
                                    )

## select events with 1 good MET with scaled down jet energy corrections
oneGoodMETJECDown = countPatMET.clone(src = 'goodMETsJECDown',
                                      minNumber = 1
                                      )

## select events with 1 good MET with smeared jet energy
oneGoodMETJER = countPatMET.clone(src = 'goodMETsJER',
                                  minNumber = 1
                                  )

## select events with 1 good MET with scaled up jet energy resolutions
oneGoodMETJERUp = countPatMET.clone(src = 'goodMETsJERUp',
                                    minNumber = 1
                                    )

## select events with 1 good MET with scaled down jet energy resolutions
oneGoodMETJERDown = countPatMET.clone(src = 'goodMETsJERDown',
                                      minNumber = 1
                                      )


#----------------------------------------------------------------------------
# filter on number of METs with unclustered energy scaled up and down
#----------------------------------------------------------------------------

## select events with 1 good MET with scaled up unclustered energy
oneGoodMETMETUp = countPatMET.clone(src = 'goodMETsMETUp',
                                    minNumber = 1
                                    )

## select events with 1 good MET with scaled down unclustered energy
oneGoodMETMETDown = countPatMET.clone(src = 'goodMETsMETDown',
                                      minNumber = 1
                                      )

##======================================================================
##======================== DEFINE EVENT FILTER =========================
##======================================================================


#-----------------------------
# HT Filter
#-----------------------------

from SUSYAnalysis.SUSYFilter.filters.HTFilter_cfi import *

## select events with one good HT
oneGoodHT = filterHT.clone()
oneGoodHT.jets = "goodJets"
oneGoodHT.Cut = 300

## select events with one good HT with scaled up jet energy corrections
oneGoodHTJECUp = filterHT.clone()
oneGoodHTJECUp.jets = "goodJetsJECUp"
oneGoodHTJECUp.Cut = 300

## select events with one good HT with scaled down jet energy corrections
oneGoodHTJECDown = filterHT.clone()
oneGoodHTJECDown.jets = "goodJetsJECDown"
oneGoodHTJECDown.Cut = 300

## select events with one good HT with smeared jet energy
oneGoodHTJER = filterHT.clone()
oneGoodHTJER.jets = "goodJetsJER"
oneGoodHTJER.Cut = 300

## select events with one good HT with scaled up jet energy corrections
oneGoodHTJERUp = filterHT.clone()
oneGoodHTJERUp.jets = "goodJetsJERUp"
oneGoodHTJERUp.Cut = 300

## select events with one good HT with scaled down jet energy corrections
oneGoodHTJERDown = filterHT.clone()
oneGoodHTJERDown.jets = "goodJetsJERDown"
oneGoodHTJERDown.Cut = 300


##======================================================================
##===================== DEFINE SELECTION SEQUENCES =====================
##======================================================================

## sequence to create good objects
createGoodObjects = cms.Sequence(## muons
                                 looseMuons *
                                 trackMuons *
                                 goodMuons *
                                 trackVetoMuons *
                                 vetoMuons *
                                 ## electrons
                                 looseElectrons *
                                 isolatedElectrons *
                                 goodElectrons*
                                 looseVetoElectrons *
                                 vetoElectrons *
                                 ## jets
                                 goodJets *
                                 goodJetsJECUp *
                                 goodJetsJECDown *
                                 goodJetsJER *
                                 goodJetsJERUp *
                                 goodJetsJERDown *
                                 ## bjets
                                 mediumTrackHighEffBjets *
                                 mediumTrackHighEffBjetsJECUp *
                                 mediumTrackHighEffBjetsJECDown *
                                 mediumTrackHighEffBjetsJER *
                                 mediumTrackHighEffBjetsJERUp *
                                 mediumTrackHighEffBjetsJERDown *
                                 mediumSSVHighEffBjets *
                                 mediumSSVHighEffBjetsJECUp *
                                 mediumSSVHighEffBjetsJECDown *
                                 mediumSSVHighEffBjetsJER *
                                 mediumSSVHighEffBjetsJERUp *
                                 mediumSSVHighEffBjetsJERDown *
                                 ## METs
                                 goodMETs *
                                 goodMETsJECUp *
                                 goodMETsJECDown *
                                 goodMETsJER *
                                 goodMETsJERUp *
                                 goodMETsJERDown *
                                 goodMETsMETUp *
                                 goodMETsMETDown *
                                 RA4METs
                                 )

## sequences to match different triggers for muon selections
MuHadSelection = cms.Sequence(oneGoodHT *
                              oneGoodMET *
                              oneLooseMuon
                              )

MuHadSelectionJECUp = cms.Sequence(oneGoodHTJECUp *
                                   oneGoodMETJECUp *
                                   oneLooseMuon
                                   )

MuHadSelectionJECDown = cms.Sequence(oneGoodHTJECDown *
                                     oneGoodMETJECDown *
                                     oneLooseMuon
                                     )

MuHadSelectionJER = cms.Sequence(oneGoodHTJER *
                                 oneGoodMETJER *
                                 oneLooseMuon
                                 )

MuHadSelectionJERUp = cms.Sequence(oneGoodHTJERUp *
                                   oneGoodMETJERUp *
                                   oneLooseMuon
                                   )

MuHadSelectionJERDown = cms.Sequence(oneGoodHTJERDown *
                                     oneGoodMETJERDown *
                                     oneLooseMuon
                                     )

MuHadSelectionMETUp = cms.Sequence(oneGoodHTJER *
                                   oneGoodMETMETUp *
                                   oneLooseMuon
                                   )

MuHadSelectionMETDown = cms.Sequence(oneGoodHTJER *
                                     oneGoodMETMETDown *
                                     oneLooseMuon
                                     )

## sequences to match different triggers for electron selections
ElHadSelection = cms.Sequence(oneGoodHT *
                              oneGoodMET *
                              oneLooseElectron
                              )

ElHadSelectionJECUp = cms.Sequence(oneGoodHTJECUp *
                                   oneGoodMETJECUp *
                                   oneLooseElectron
                                   )

ElHadSelectionJECDown = cms.Sequence(oneGoodHTJECDown *
                                     oneGoodMETJECDown *
                                     oneLooseElectron
                                     )

ElHadSelectionJER = cms.Sequence(oneGoodHTJER *
                                 oneGoodMETJER *
                                 oneLooseElectron
                                 )

ElHadSelectionJERUp = cms.Sequence(oneGoodHTJERUp *
                                   oneGoodMETJERUp *
                                   oneLooseElectron
                                   )

ElHadSelectionJERDown = cms.Sequence(oneGoodHTJERDown *
                                     oneGoodMETJERDown *
                                     oneLooseElectron
                                     )

ElHadSelectionMETUp = cms.Sequence(oneGoodHTJER *
                                   oneGoodMETMETUp *
                                   oneLooseElectron
                                   )

ElHadSelectionMETDown = cms.Sequence(oneGoodHTJER *
                                     oneGoodMETMETDown *
                                     oneLooseElectron
                                     )

## muon selection sequence
from SUSYAnalysis.SUSYFilter.filters.PFMuonConsistency_cfi import *
muonSelection = cms.Sequence(oneGoodMuon *
                             exactlyOneGoodMuon *
                             pfMuonConsistency *
                             noGoodElectron *
                             oneVetoMuon *
                             noVetoElectron
                             )

## electron selection sequence
electronSelection = cms.Sequence(oneGoodElectron *
                                 exactlyOneGoodElectron *
                                 noGoodMuon *
                                 oneVetoElectron *
                                 noVetoMuon
                                 )

## jet selection sequence
jetSelection = cms.Sequence(fourGoodJets)

jetSelectionJECUp = cms.Sequence(fourGoodJetsJECUp)

jetSelectionJECDown = cms.Sequence(fourGoodJetsJECDown)

jetSelectionJER = cms.Sequence(fourGoodJetsJERUp)

jetSelectionJERUp = cms.Sequence(fourGoodJetsJERUp)

jetSelectionJERDown = cms.Sequence(fourGoodJetsJERDown)



