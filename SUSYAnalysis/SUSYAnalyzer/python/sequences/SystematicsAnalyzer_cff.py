import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

## set default settings
analyzeSystematics.useEventWeight = True
analyzeSystematics.useBtagEventWeight = True
analyzeSystematics.BtagEventWeights = "btagEventWeightMu:RA4bSFEventWeights"

##-----------------------------------
## Create clones for 0 btag bin
##-----------------------------------

analyzeSystematicsMu0b = analyzeSystematics.clone()

## clones to study jet energy scale uncertainties
analyzeSystematicsMu0bJECUp          = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bJECDown        = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bJERUp          = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bJERDown        = analyzeSystematicsMu0b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsMu0bMETUp          = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bMETDown        = analyzeSystematicsMu0b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu0bBtagSFUp       = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bBtagSFDown     = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bMistagSFUp     = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bMistagSFDown   = analyzeSystematicsMu0b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu0bWUp            = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bWDown          = analyzeSystematicsMu0b.clone()

## clones to study PU uncertainties
analyzeSystematicsMu0bPUUp           = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bPUDown         = analyzeSystematicsMu0b.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu0bPDF1           = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bPDF2           = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bPDF3           = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bPDF4           = analyzeSystematicsMu0b.clone()

##-----------------------------------
## Configure clones for 0 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu0bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsMu0bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsMu0bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsMu0bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsMu0bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsMu0bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsMu0bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsMu0bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsMu0bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsMu0bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsMu0bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsMu0bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu0bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu0bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu0bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu0bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsMu0bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsMu0bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study PDF uncertainties
## ...
