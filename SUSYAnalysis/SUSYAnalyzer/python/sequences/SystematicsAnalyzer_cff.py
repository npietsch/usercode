import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

##-------------------------
## Create clones
##-------------------------

## clones to study jet energy scale uncertainties
analyzeSystematicsMuJECUp          = analyzeSystematics.clone()
analyzeSystematicsMuJECDown        = analyzeSystematics.clone()
analyzeSystematicsMuJERUp          = analyzeSystematics.clone()
analyzeSystematicsMuJERDown        = analyzeSystematics.clone()

## clones to study  remaining met scale uncertainties
analyzeSystematicsMuMETUp          = analyzeSystematics.clone()
analyzeSystematicsMuMETDown        = analyzeSystematics.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMuBtagSFUp       = analyzeSystematics.clone()
analyzeSystematicsMuBtagSFDown     = analyzeSystematics.clone()
analyzeSystematicsMuMistagSFUp     = analyzeSystematics.clone()
analyzeSystematicsMuMistagSFDown   = analyzeSystematics.clone()

## clones to study PU uncertainties
analyzeSystematicsMuPUUp           = analyzeSystematics.clone()
analyzeSystematicsMuPUDown         = analyzeSystematics.clone()

##-------------------------
## Configure clones 
##-------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMuJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsMuJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsMuJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsMuJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsMuJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsMuJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsMuJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsMuJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsMuJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsMuJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsMuJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsMuJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMuBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMuBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeight"
analyzeSystematicsMuMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMuMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeight"

## configure clones to study PU uncertainties
analyzeSystematicsMuPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUP"
analyzeSystematicsMuPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"
