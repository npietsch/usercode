import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

HCalAnalyzerSequence = cms.Sequence(analyzeHCal)
