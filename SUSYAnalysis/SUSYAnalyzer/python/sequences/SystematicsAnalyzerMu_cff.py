import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

## set default settings
analyzeSystematics.useEventWeight = True
analyzeSystematics.useBtagEventWeight = True
analyzeSystematics.BtagEventWeights = "btagEventWeightMu:RA4bSFEventWeights"
analyzeSystematics.jets     = "goodJetsJER"
analyzeSystematics.bjets    = "mediumTrackHighEffBjetsJER"
analyzeSystematics.met      = "scaledJetEnergy:patMETsPF"


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

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu0bMETUp          = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bMETDown        = analyzeSystematicsMu0bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu0bLECUp          = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bLECDown        = analyzeSystematicsMu0bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu0bBtagSFUp       = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bBtagSFDown     = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bMistagSFUp     = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bMistagSFDown   = analyzeSystematicsMu0bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu0bWUp            = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bWDown          = analyzeSystematicsMu0bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu0bPUUp           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPUDown         = analyzeSystematicsMu0bJER.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu0bPDF1           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPDF2           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPDF3           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPDF4           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPDF5           = analyzeSystematicsMu0bJER.clone()
analyzeSystematicsMu0bPDF6           = analyzeSystematicsMu0bJER.clone()

##-----------------------------------
## Configure clones for 0 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu0b.jets     = "goodJets"
analyzeSystematicsMu0b.bjets    = "mediumTrackHighEffBjets"
analyzeSystematicsMu0b.met      = "patMETsPF"

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

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu0bMETUp.met      = "unclusteredEnergyUp:scaledMET"
analyzeSystematicsMu0bMETDown.met    = "unclusteredEnergyDown:scaledMET"

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu0bLECUp.muons      = "goodMuons"
analyzeSystematicsMu0bLECDown.muons    = "goodMuons"

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

analyzeSystematicsMu1bJER = analyzeSystematics.clone()
analyzeSystematicsMu1bJER.btagBin = 0

## clones to study jet energy scale uncertainties
analyzeSystematicsMu1b               = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJER            = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJECUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJECDown        = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJERUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJERDown        = analyzeSystematicsMu1bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu1bMETUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bMETDown        = analyzeSystematicsMu1bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu1bLECUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bLECDown        = analyzeSystematicsMu1bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu1bBtagSFUp       = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bBtagSFDown     = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bMistagSFUp     = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bMistagSFDown   = analyzeSystematicsMu1bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu1bWUp            = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bWDown          = analyzeSystematicsMu1bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu1bPUUp           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPUDown         = analyzeSystematicsMu1bJER.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu1bPDF1           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPDF2           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPDF3           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPDF4           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPDF5           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPDF6           = analyzeSystematicsMu1bJER.clone()

##-----------------------------------
## Configure clones for 1 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu1b.jets     = "goodJets"
analyzeSystematicsMu1b.bjets    = "mediumTrackHighEffBjets"
analyzeSystematicsMu1b.met      = "patMETsPF"

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

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu1bMETUp.met      = "unclusteredEnergyUp:scaledMET"
analyzeSystematicsMu1bMETDown.met    = "unclusteredEnergyDown:scaledMET"

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu1bLECUp.muons      = "goodMuons"
analyzeSystematicsMu1bLECDown.muons    = "goodMuons"

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

analyzeSystematicsMu2bJER = analyzeSystematics.clone()
analyzeSystematicsMu2bJER.btagBin = 0

## clones to study jet energy scale uncertainties
analyzeSystematicsMu2b               = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJER            = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJECUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJECDown        = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJERUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJERDown        = analyzeSystematicsMu2bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu2bMETUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bMETDown        = analyzeSystematicsMu2bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu2bLECUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bLECDown        = analyzeSystematicsMu2bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu2bBtagSFUp       = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bBtagSFDown     = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bMistagSFUp     = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bMistagSFDown   = analyzeSystematicsMu2bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu2bWUp            = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bWDown          = analyzeSystematicsMu2bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu2bPUUp           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPUDown         = analyzeSystematicsMu2bJER.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu2bPDF1           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPDF2           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPDF3           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPDF4           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPDF5           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPDF6           = analyzeSystematicsMu2bJER.clone()

##-----------------------------------
## Configure clones for 2 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu2b.jets     = "goodJets"
analyzeSystematicsMu2b.bjets    = "mediumTrackHighEffBjets"
analyzeSystematicsMu2b.met      = "patMETsPF"

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

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu2bMETUp.met      = "unclusteredEnergyUp:scaledMET"
analyzeSystematicsMu2bMETDown.met    = "unclusteredEnergyDown:scaledMET"

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu2bLECUp.muons      = "goodMuons"
analyzeSystematicsMu2bLECDown.muons    = "goodMuons"

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


## configure clones to study PDF uncertainties
## ...


##-----------------------------------
## Create clones for 3 btag bin
##-----------------------------------

analyzeSystematicsMu3bJER = analyzeSystematics.clone()
analyzeSystematicsMu3bJER.btagBin = 0

## clones to study jet energy scale uncertainties
analyzeSystematicsMu3b               = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJER            = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJECUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJECDown        = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJERUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJERDown        = analyzeSystematicsMu3bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu3bMETUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bMETDown        = analyzeSystematicsMu3bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu3bLECUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bLECDown        = analyzeSystematicsMu3bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu3bBtagSFUp       = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bBtagSFDown     = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bMistagSFUp     = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bMistagSFDown   = analyzeSystematicsMu3bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu3bWUp            = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bWDown          = analyzeSystematicsMu3bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu3bPUUp           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPUDown         = analyzeSystematicsMu3bJER.clone()

## clones to study PDF uncertainties
analyzeSystematicsMu3bPDF1           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPDF2           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPDF3           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPDF4           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPDF5           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPDF6           = analyzeSystematicsMu3bJER.clone()

##-----------------------------------
## Configure clones for 3 btag bin
##-----------------------------------

## configure clones to study jet energy scale uncertainties
analyzeSystematicsMu3b.jets     = "goodJets"
analyzeSystematicsMu3b.bjets    = "mediumTrackHighEffBjets"
analyzeSystematicsMu3b.met      = "patMETsPF"

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

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu3bMETUp.met      = "unclusteredEnergyUp:scaledMET"
analyzeSystematicsMu3bMETDown.met    = "unclusteredEnergyDown:scaledMET"

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu3bLECUp.muons      = "goodMuons"
analyzeSystematicsMu3bLECDown.muons    = "goodMuons"

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


## configure clones to study PDF uncertainties
## ...
