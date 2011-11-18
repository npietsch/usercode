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
analyzeSystematicsMu0b.btagBin = 0

## clones to study jet energy scale uncertainties
analyzeSystematicsMu0bJEC            = analyzeSystematicsMu0b.clone()
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
analyzeSystematicsMu0bPDF5           = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu0bPDF6           = analyzeSystematicsMu0b.clone()

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


##-----------------------------------
## Create clones for 1 btag bin
##-----------------------------------

analyzeSystematicsMu1b = analyzeSystematics.clone()
analyzeSystematicsMu1b.btagBin = 1

## clones to study jet energy scale uncertainties
analyzeSystematicsMu1bJEC            = analyzeSystematicsMu0b.clone()
analyzeSystematicsMu1bJECUp          = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bJECDown        = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bJERUp          = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bJERDown        = analyzeSystematicsMu1b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsMu1bMETUp          = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bMETDown        = analyzeSystematicsMu1b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu1bBtagSFUp       = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bBtagSFDown     = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bMistagSFUp     = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bMistagSFDown   = analyzeSystematicsMu1b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu1bWUp            = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bWDown          = analyzeSystematicsMu1b.clone()

## clones to study PU uncertainties
analyzeSystematicsMu1bPUUp           = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bPUDown         = analyzeSystematicsMu1b.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu1bPDF1           = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bPDF2           = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bPDF3           = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bPDF4           = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bPDF5           = analyzeSystematicsMu1b.clone()
analyzeSystematicsMu1bPDF6           = analyzeSystematicsMu1b.clone()

##-----------------------------------
## Configure clones for 1 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu1bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsMu1bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsMu1bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsMu1bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsMu1bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsMu1bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsMu1bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsMu1bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsMu1bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsMu1bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsMu1bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsMu1bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu1bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu1bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu1bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu1bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsMu1bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsMu1bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study PDF uncertainties
## ...


##-----------------------------------
## Create clones for 2 btag bin
##-----------------------------------

analyzeSystematicsMu2b = analyzeSystematics.clone()
analyzeSystematicsMu2b.btagBin = 2

## clones to study jet energy scale uncertainties
analyzeSystematicsMu2bJEC            = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bJECUp          = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bJECDown        = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bJERUp          = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bJERDown        = analyzeSystematicsMu2b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsMu2bMETUp          = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bMETDown        = analyzeSystematicsMu2b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu2bBtagSFUp       = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bBtagSFDown     = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bMistagSFUp     = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bMistagSFDown   = analyzeSystematicsMu2b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu2bWUp            = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bWDown          = analyzeSystematicsMu2b.clone()

## clones to study PU uncertainties
analyzeSystematicsMu2bPUUp           = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bPUDown         = analyzeSystematicsMu2b.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu2bPDF1           = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bPDF2           = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bPDF3           = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bPDF4           = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bPDF5           = analyzeSystematicsMu2b.clone()
analyzeSystematicsMu2bPDF6           = analyzeSystematicsMu2b.clone()


##-----------------------------------
## Configure clones for 2 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu2bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsMu2bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsMu2bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsMu2bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsMu2bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsMu2bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsMu2bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsMu2bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsMu2bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsMu2bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsMu2bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsMu2bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu2bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu2bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu2bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu2bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsMu2bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsMu2bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


##-----------------------------------
## Create clones for 3 btag bin
##-----------------------------------

analyzeSystematicsMu3b = analyzeSystematics.clone()
analyzeSystematicsMu3b.btagBin = 3

## clones to study jet energy scale uncertainties
analyzeSystematicsMu3bJEC            = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bJECUp          = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bJECDown        = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bJERUp          = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bJERDown        = analyzeSystematicsMu3b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsMu3bMETUp          = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bMETDown        = analyzeSystematicsMu3b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu3bBtagSFUp       = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bBtagSFDown     = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bMistagSFUp     = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bMistagSFDown   = analyzeSystematicsMu3b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu3bWUp            = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bWDown          = analyzeSystematicsMu3b.clone()

## clones to study PU uncertainties
analyzeSystematicsMu3bPUUp           = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bPUDown         = analyzeSystematicsMu3b.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu3bPDF1           = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bPDF2           = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bPDF3           = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bPDF4           = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bPDF5           = analyzeSystematicsMu3b.clone()
analyzeSystematicsMu3bPDF6           = analyzeSystematicsMu3b.clone()


##-----------------------------------
## Configure clones for 3 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu3bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsMu3bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsMu3bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsMu3bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsMu3bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsMu3bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsMu3bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsMu3bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsMu3bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsMu3bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsMu3bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsMu3bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu3bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu3bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu3bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu3bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsMu3bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsMu3bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"
