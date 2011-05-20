import FWCore.ParameterSet.Config as cms


#------------------------------
# Muon collections 
#------------------------------

## create good muon collection
#from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *

from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
from TopAnalysis.TopFilter.filters.MuonJetOverlapSelector_cfi import *
from TopAnalysis.TopFilter.sequences.MuonVertexDistanceSelector_cfi import *

globalPromptTightMuons = selectedPatMuons.clone(src = "selectedPatMuons",
                                                cut =
                                                ## Global Muon Prompt Tight
                                                ##---------------------------
                                                #'isGlobalMuon &'
                                                #'globalTrack.normalizedChi2 < 10.0 &'
                                                #'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                                'isGood("GlobalMuonPromptTight")'
                                                )

AllTrackerMuons = selectedPatMuons.clone(src = "globalPromptTightMuons",
                                         cut =
                                         ## Track Muon
                                         ##-------------
                                         #'isTrackerMuon &'
                                         'isGood("AllTrackerMuons")'
                                         )

ptMuons = selectedPatMuons.clone(src = "AllTrackerMuons",
                                 cut =
                                 'pt >= 20.'
                                 )

etaMuons = selectedPatMuons.clone(src = "ptMuons",
                                  cut =
                                  'abs(eta) <= 2.1'
                                  )

isolatedMuons = selectedPatMuons.clone(src = "etaMuons",
                                       cut =
                                       '(trackIso+hcalIso+ecalIso)/pt < 0.1'
                                       )

dBMuons = selectedPatMuons.clone(src = "isolatedMuons",
                                 cut =
                                 'abs(dB) < 0.02'
                                 ) 

validHitsMuons = selectedPatMuons.clone(src = "dBMuons",
                                        cut =
                                        'globalTrack.hitPattern.numberOfValidTrackerHits > 10 '
                                        )

matchesMuons = selectedPatMuons.clone(src = "validHitsMuons",
                                      cut =
                                      'numberOfMatches() > 1'
                                      )

pixelMuons = selectedPatMuons.clone(src = "matchesMuons",
                                    cut =
                                    'innerTrack.hitPattern.pixelLayersWithMeasurement >= 1'
                                    )

RA4Muons = vertexSelectedMuons.clone(src = "pixelMuons"
                                     )
#------------------------------
# Muon countFilter
#------------------------------

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneGlobalPromptTightMuon = countPatMuons.clone(src = 'globalPromptTightMuons',
                                               minNumber = 1
                                               )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneTrackMuon = countPatMuons.clone(src = 'AllTrackerMuons',
                                   minNumber = 1
                                   )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
onePtMuon = countPatMuons.clone(src = 'ptMuons',
                                minNumber = 1
                                )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneEtaMuon = countPatMuons.clone(src = 'etaMuons',
                                 minNumber = 1
                                 )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneIsolatedMuon = countPatMuons.clone(src = 'isolatedMuons',
                                      minNumber = 1
                                      )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneDBMuon = countPatMuons.clone(src = 'dBMuons',
                                minNumber = 1
                                )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneValidHitMuon = countPatMuons.clone(src = 'validHitsMuons',
                                      minNumber = 1
                                      )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneMatchesMuon = countPatMuons.clone(src = 'matchesMuons',
                                     minNumber = 1
                                     )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
onePixelMuon = countPatMuons.clone(src = 'pixelMuons',
                                   minNumber = 1
                                   )

## select events with at least good muon
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
oneRA4Muon = countPatMuons.clone(src = 'vertexSelMuons',
                                 minNumber = 1
                                 )

RA4MuonCollections = cms.Sequence(globalPromptTightMuons*
                                  AllTrackerMuons *
                                  ptMuons *
                                  etaMuons *
                                  isolatedMuons *
                                  dBMuons *
                                  validHitsMuons *
                                  matchesMuons *
                                  pixelMuons *
                                  RA4Muons
                                  )

#---------------------------------------------------------
# Modules for monitoring muon quality and kinematics 
#---------------------------------------------------------

## Muon quality
from TopAnalysis.TopAnalyzer.MuonQuality_cfi import *

analyzeMuonQualityPat = analyzeMuonQuality.clone()
analyzeMuonQualityPat.src = 'selectedPatMuons'

analyzeMuonQualityGlobal = analyzeMuonQuality.clone()
analyzeMuonQualityGlobal.src = 'globalPromptTightMuons'

analyzeMuonQualityTrack = analyzeMuonQuality.clone()
analyzeMuonQualityTrack.src = 'AllTrackerMuons'

analyzeMuonQualityPt = analyzeMuonQuality.clone()
analyzeMuonQualityPt.src = 'ptMuons'

analyzeMuonQualityEta = analyzeMuonQuality.clone()
analyzeMuonQualityEta.src = 'etaMuons'

analyzeMuonQualityIso = analyzeMuonQuality.clone()
analyzeMuonQualityIso.src = 'isolatedMuons'

analyzeMuonQualityDB = analyzeMuonQuality.clone()
analyzeMuonQualityDB.src = 'dBMuons'

analyzeMuonQualityHits = analyzeMuonQuality.clone()
analyzeMuonQualityHits.src = 'validHitsMuons'

analyzeMuonQualityMatches = analyzeMuonQuality.clone()
analyzeMuonQualityMatches.src = 'matchesMuons'

analyzeMuonQualityPixel = analyzeMuonQuality.clone()
analyzeMuonQualityPixel.src = 'pixelMuons'

analyzeMuonQualityRA4 = analyzeMuonQuality.clone()
analyzeMuonQualityRA4.src = 'RA4Muons'

## Muon kinematics
from TopAnalysis.TopAnalyzer.MuonKinematics_cfi import *

analyzeMuonKinematicsPat = analyzeMuonKinematics.clone()
analyzeMuonKinematicsPat.src = 'selectedPatMuons'

analyzeMuonKinematicsGlobal = analyzeMuonKinematics.clone()
analyzeMuonKinematicsGlobal.src = 'globalPromptTightMuons'

analyzeMuonKinematicsTrack = analyzeMuonKinematics.clone()
analyzeMuonKinematicsTrack.src = 'AllTrackerMuons'

analyzeMuonKinematicsPt = analyzeMuonKinematics.clone()
analyzeMuonKinematicsPt.src = 'ptMuons'

analyzeMuonKinematicsEta = analyzeMuonKinematics.clone()
analyzeMuonKinematicsEta.src = 'etaMuons'

analyzeMuonKinematicsIso = analyzeMuonKinematics.clone()
analyzeMuonKinematicsIso.src = 'isolatedMuons'

analyzeMuonKinematicsDB = analyzeMuonKinematics.clone()
analyzeMuonKinematicsDB.src = 'dBMuons'

analyzeMuonKinematicsHits = analyzeMuonKinematics.clone()
analyzeMuonKinematicsHits.src = 'validHitsMuons'

analyzeMuonKinematicsMatches = analyzeMuonKinematics.clone()
analyzeMuonKinematicsMatches.src = 'matchesMuons'

analyzeMuonKinematicsPixel = analyzeMuonKinematics.clone()
analyzeMuonKinematicsPixel.src = 'pixelMuons'

analyzeMuonKinematicsRA4 = analyzeMuonKinematics.clone()
analyzeMuonKinematicsRA4.src = 'RA4Muons'

## RA4MuonSelection
RA4MuonSelection = cms.Sequence(analyzeMuonQualityPat *
                                analyzeMuonKinematicsPat *
                                oneGlobalPromptTightMuon *
                                analyzeMuonQualityGlobal *
                                analyzeMuonKinematicsGlobal *
                                oneTrackMuon *
                                analyzeMuonQualityTrack *
                                analyzeMuonKinematicsTrack *
                                onePtMuon *
                                analyzeMuonQualityPt *
                                analyzeMuonKinematicsPt *
                                oneEtaMuon *
                                analyzeMuonQualityEta *
                                analyzeMuonKinematicsEta *
                                oneIsolatedMuon *
                                analyzeMuonQualityIso *
                                analyzeMuonKinematicsIso *
                                oneDBMuon *
                                analyzeMuonQualityDB *
                                analyzeMuonKinematicsDB *
                                oneValidHitMuon *
                                analyzeMuonQualityHits *
                                analyzeMuonKinematicsHits *
                                oneMatchesMuon *
                                analyzeMuonQualityMatches *
                                analyzeMuonKinematicsMatches *
                                onePixelMuon *
                                analyzeMuonQualityPixel *
                                analyzeMuonKinematicsPixel *
                                oneRA4Muon *
                                analyzeMuonQualityRA4 *
                                analyzeMuonKinematicsRA4
                                )
