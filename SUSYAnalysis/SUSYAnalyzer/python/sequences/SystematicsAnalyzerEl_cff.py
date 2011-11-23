import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

## set default settings
analyzeSystematics.useEventWeight = True
analyzeSystematics.useBtagEventWeight = True
analyzeSystematics.BtagEventWeights = "btagEventWeightEl:RA4bSFEventWeights"

##-----------------------------------
## Create clones for 0 btag bin
##-----------------------------------

analyzeSystematicsEl0b = analyzeSystematics.clone()
analyzeSystematicsEl0b.btagBin = 0

## clones to study jet energy scale uncertainties
analyzeSystematicsEl0bJEC            = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bJECUp          = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bJECDown        = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bJERUp          = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bJERDown        = analyzeSystematicsEl0b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsEl0bMETUp          = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bMETDown        = analyzeSystematicsEl0b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl0bBtagSFUp       = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bBtagSFDown     = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bMistagSFUp     = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bMistagSFDown   = analyzeSystematicsEl0b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl0bWUp            = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bWDown          = analyzeSystematicsEl0b.clone()

## clones to study PU uncertainties
analyzeSystematicsEl0bPUUp           = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bPUDown         = analyzeSystematicsEl0b.clone()

## clones to study PDF uncertainties
analyzeSystematicsEl0bPDF1           = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bPDF2           = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bPDF3           = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bPDF4           = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bPDF5           = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl0bPDF6           = analyzeSystematicsEl0b.clone()

##-----------------------------------
## Configure clones for 0 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsEl0bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsEl0bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsEl0bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsEl0bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsEl0bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsEl0bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsEl0bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsEl0bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsEl0bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsEl0bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsEl0bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsEl0bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl0bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl0bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl0bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl0bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsEl0bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl0bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study PDF uncertainties
## ...


##-----------------------------------
## Create clones for 1 btag bin
##-----------------------------------

analyzeSystematicsEl1b = analyzeSystematics.clone()
analyzeSystematicsEl1b.btagBin = 1

## clones to study jet energy scale uncertainties
analyzeSystematicsEl1bJEC            = analyzeSystematicsEl0b.clone()
analyzeSystematicsEl1bJECUp          = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bJECDown        = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bJERUp          = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bJERDown        = analyzeSystematicsEl1b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsEl1bMETUp          = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bMETDown        = analyzeSystematicsEl1b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl1bBtagSFUp       = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bBtagSFDown     = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bMistagSFUp     = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bMistagSFDown   = analyzeSystematicsEl1b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl1bWUp            = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bWDown          = analyzeSystematicsEl1b.clone()

## clones to study PU uncertainties
analyzeSystematicsEl1bPUUp           = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bPUDown         = analyzeSystematicsEl1b.clone()

## clones to study PDF uncertainties
analyzeSystematicsEl1bPDF1           = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bPDF2           = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bPDF3           = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bPDF4           = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bPDF5           = analyzeSystematicsEl1b.clone()
analyzeSystematicsEl1bPDF6           = analyzeSystematicsEl1b.clone()

##-----------------------------------
## Configure clones for 1 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsEl1bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsEl1bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsEl1bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsEl1bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsEl1bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsEl1bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsEl1bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsEl1bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsEl1bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsEl1bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsEl1bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsEl1bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl1bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl1bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl1bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl1bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsEl1bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl1bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study PDF uncertainties
## ...


##-----------------------------------
## Create clones for 2 btag bin
##-----------------------------------

analyzeSystematicsEl2b = analyzeSystematics.clone()
analyzeSystematicsEl2b.btagBin = 2

## clones to study jet energy scale uncertainties
analyzeSystematicsEl2bJEC            = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bJECUp          = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bJECDown        = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bJERUp          = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bJERDown        = analyzeSystematicsEl2b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsEl2bMETUp          = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bMETDown        = analyzeSystematicsEl2b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl2bBtagSFUp       = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bBtagSFDown     = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bMistagSFUp     = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bMistagSFDown   = analyzeSystematicsEl2b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl2bWUp            = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bWDown          = analyzeSystematicsEl2b.clone()

## clones to study PU uncertainties
analyzeSystematicsEl2bPUUp           = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bPUDown         = analyzeSystematicsEl2b.clone()

## clones to study PDF uncertainties
analyzeSystematicsEl2bPDF1           = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bPDF2           = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bPDF3           = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bPDF4           = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bPDF5           = analyzeSystematicsEl2b.clone()
analyzeSystematicsEl2bPDF6           = analyzeSystematicsEl2b.clone()


##-----------------------------------
## Configure clones for 2 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsEl2bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsEl2bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsEl2bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsEl2bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsEl2bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsEl2bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsEl2bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsEl2bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsEl2bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsEl2bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsEl2bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsEl2bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl2bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl2bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl2bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl2bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsEl2bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl2bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


##-----------------------------------
## Create clones for 3 btag bin
##-----------------------------------

analyzeSystematicsEl3b = analyzeSystematics.clone()
analyzeSystematicsEl3b.btagBin = 3

## clones to study jet energy scale uncertainties
analyzeSystematicsEl3bJEC            = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bJECUp          = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bJECDown        = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bJERUp          = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bJERDown        = analyzeSystematicsEl3b.clone()

## clones to study remaining met scale uncertainties
analyzeSystematicsEl3bMETUp          = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bMETDown        = analyzeSystematicsEl3b.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl3bBtagSFUp       = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bBtagSFDown     = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bMistagSFUp     = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bMistagSFDown   = analyzeSystematicsEl3b.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl3bWUp            = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bWDown          = analyzeSystematicsEl3b.clone()

## clones to study PU uncertainties
analyzeSystematicsEl3bPUUp           = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bPUDown         = analyzeSystematicsEl3b.clone()

## clones to study PDF uncertainties
analyzeSystematicsEl3bPDF1           = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bPDF2           = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bPDF3           = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bPDF4           = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bPDF5           = analyzeSystematicsEl3b.clone()
analyzeSystematicsEl3bPDF6           = analyzeSystematicsEl3b.clone()


##-----------------------------------
## Configure clones for 3 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsEl3bJECUp.jets     = "goodJetsJECUp"
analyzeSystematicsEl3bJECUp.bjets    = "mediumTrackHighEffBjetsJECUp"
analyzeSystematicsEl3bJECUp.met      = "scaledJetEnergyJECUp:patMETsPF"

analyzeSystematicsEl3bJECDown.jets   = "goodJetsJECDown"
analyzeSystematicsEl3bJECDown.bjets  = "mediumTrackHighEffBjetsJECDown"
analyzeSystematicsEl3bJECDown.met    = "scaledJetEnergyJECDown:patMETsPF"

analyzeSystematicsEl3bJERUp.jets     = "goodJetsJERUp"
analyzeSystematicsEl3bJERUp.bjets    = "mediumTrackHighEffBjetsJERUp"
analyzeSystematicsEl3bJERUp.met      = "scaledJetEnergyJERUp:patMETsPF"

analyzeSystematicsEl3bJERDown.jets   = "goodJetsJERDown"
analyzeSystematicsEl3bJERDown.bjets  = "mediumTrackHighEffBjetsJERDown"
analyzeSystematicsEl3bJERDown.met    = "scaledJetEnergyJERDown:patMETsPF"

## configure clones to study  remaining met scale uncertainties
## ...

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl3bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl3bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl3bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl3bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study W polatization uncertainty
## ...

## configure clones to study PU uncertainties
analyzeSystematicsEl3bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl3bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"
