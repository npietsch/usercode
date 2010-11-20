import FWCore.ParameterSet.Config as cms

#------------------------------------------------
# Modules for analysis of single objects
#------------------------------------------------


## analyze muons
from TopAnalysis.TopAnalyzer.MuonKinematics_cfi import *
analyzeMuonKinematics.src = "goodMuons"

## analyze electrons
from TopAnalysis.TopAnalyzer.ElectronKinematics_cfi import *
analyzeElectronKinematics.src = "goodElectrons"

## analyze jets
from TopAnalysis.TopAnalyzer.JetKinematics_cfi import *
analyzeJetKinematics.src = "goodJets"

## analyze MET
from TopAnalysis.TopAnalyzer.METKinematics_cfi import *
analyzeMETKinematics.srcA = "goodMETs"

#------------------------------------------------
# Define Sequences
#------------------------------------------------

singleObjectsAnalysis = cms.Sequence(analyzeMuonKinematics *
                                     analyzeElectronKinematics *
                                     analyzeJetKinematics *
                                     analyzeMETKinematics
                                     )
