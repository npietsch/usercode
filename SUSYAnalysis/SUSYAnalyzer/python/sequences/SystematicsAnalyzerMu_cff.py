import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

## set default settings
analyzeSystematics.useEventWeight = True
analyzeSystematics.useBtagEventWeight = True
analyzeSystematics.BtagEventWeights = "btagEventWeightMu:RA4bSFEventWeights"
analyzeSystematics.jets     = "smearedGoodJets"
analyzeSystematics.bjets    = "smearedMediumTrackHighEffBjets"
analyzeSystematics.met      = "smearedGoodMETs"


##-----------------------------------
## Create clones for 0 btag bin
##-----------------------------------

analyzeSystematicsMu0bJER = analyzeSystematics.clone()
analyzeSystematicsMu0bJER.btagBin = 0

## clones to study jet energy scale uncertainties
analyzeSystematicsMu0b               = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bJER            = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bJECUp          = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bJECDown        = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bJERUp          = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bJERDown        = analyzeSystematicsMu0bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu0bLepUp          = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bLepDown        = analyzeSystematicsMu0bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu0bMETUp          = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bMETDown        = analyzeSystematicsMu0bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu0bBtagSFUp       = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bBtagSFDown     = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bMistagSFUp     = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bMistagSFDown   = analyzeSystematicsMu0bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu0bPUUp           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPUDown         = analyzeSystematicsMu0bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu0bWUp            = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bWDown          = analyzeSystematicsMu0bJER.clone()

##-----------------------------------
## Configure clones for 0 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu0b.jets     = "goodJets"
analyzeSystematicsMu0b.bjets    = "mediumTrackHighEffBjets"
analyzeSystematicsMu0b.met      = "patMETsPF"

analyzeSystematicsMu0bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsMu0bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsMu0bJECUp.met      = "goodMETsJECUp"

analyzeSystematicsMu0bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsMu0bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsMu0bJECDown.met    = "goodMETsJECDown"

analyzeSystematicsMu0bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsMu0bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsMu0bJERUp.met      = "goodMETsJERUp"

analyzeSystematicsMu0bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsMu0bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsMu0bJERDown.met    = "goodMETsJERDown"

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu0bLepUp.muons      = "goodMuonsUp"
analyzeSystematicsMu0bLepUp.met        = "LeptonEnergyUp:scaledMETsMu"

analyzeSystematicsMu0bLepDown.muons    = "goodMuonsDown"
analyzeSystematicsMu0bLepDown.met      = "LeptonEnergyDown:scaledMETsMu"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu0bMETUp.met      = "unclusteredEnergyUp:scaledMETs"
analyzeSystematicsMu0bMETDown.met    = "unclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu0bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu0bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu0bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu0bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsMu0bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsMu0bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study W polatization uncertainty
## ...
