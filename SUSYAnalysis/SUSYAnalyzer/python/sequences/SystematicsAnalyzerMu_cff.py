import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

## set default settings
analyzeSystematics.useEventWeight = True
analyzeSystematics.useBtagEventWeight = True

##-----------------------------------
## Create clones for 0 btag bin
##-----------------------------------

analyzeSystematicsMu0b                     = analyzeSystematics.clone()
analyzeSystematicsMu0b.btagBin             = 0
analyzeSystematicsMu0b.BtagEventWeights    = "btagEventWeightMu:RA4bSFEventWeights"
analyzeSystematicsMu0b.jets                = "goodJets"
analyzeSystematicsMu0b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsMu0b.met                 = "patMETsPF"

analyzeSystematicsMu0bJER                  = analyzeSystematics.clone()
analyzeSystematicsMu0bJER.btagBin          = 0
analyzeSystematicsMu0bJER.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSystematicsMu0bJER.jets             = "smearedGoodJets"
analyzeSystematicsMu0bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsMu0bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu0bLepUp.muons      = "goodMuonsUp"
analyzeSystematicsMu0bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsMu"

analyzeSystematicsMu0bLepDown.muons    = "goodMuonsDown"
analyzeSystematicsMu0bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsMu"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu0bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsMu0bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu0bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu0bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu0bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu0bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsMu0bPUUp.PUWeight   =  "eventWeightPUUp:eventWeightPU"
analyzeSystematicsMu0bPUDown.PUWeight =  "eventWeightPUDown:eventWeightPU"


## configure clones to study W polatization uncertainty
## ...


##-----------------------------------
## Create clones for 1 btag bin
##-----------------------------------

analyzeSystematicsMu1b                     = analyzeSystematics.clone()
analyzeSystematicsMu1b.btagBin             = 1
analyzeSystematicsMu1b.BtagEventWeights    = "btagEventWeightMu:RA4bSFEventWeights"
analyzeSystematicsMu1b.jets                = "goodJets"
analyzeSystematicsMu1b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsMu1b.met                 = "patMETsPF"

analyzeSystematicsMu1bJER                  = analyzeSystematics.clone()
analyzeSystematicsMu1bJER.btagBin          = 1
analyzeSystematicsMu1bJER.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSystematicsMu1bJER.jets             = "smearedGoodJets"
analyzeSystematicsMu1bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsMu1bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsMu1bJECUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJECDown        = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJERUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bJERDown        = analyzeSystematicsMu1bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu1bLepUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bLepDown        = analyzeSystematicsMu1bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu1bMETUp          = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bMETDown        = analyzeSystematicsMu1bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu1bBtagSFUp       = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bBtagSFDown     = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bMistagSFUp     = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bMistagSFDown   = analyzeSystematicsMu1bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu1bPUUp           = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bPUDown         = analyzeSystematicsMu1bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu1bWUp            = analyzeSystematicsMu1bJER.clone()
analyzeSystematicsMu1bWDown          = analyzeSystematicsMu1bJER.clone()


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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu1bLepUp.muons      = "goodMuonsUp"
analyzeSystematicsMu1bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsMu"

analyzeSystematicsMu1bLepDown.muons    = "goodMuonsDown"
analyzeSystematicsMu1bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsMu"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu1bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsMu1bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu1bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu1bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu1bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu1bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsMu1bPUUp.PUWeight   =  "eventWeightPUUp:eventWeightPU"
analyzeSystematicsMu1bPUDown.PUWeight =  "eventWeightPUDown:eventWeightPU"


## configure clones to study W polatization uncertainty
## ...


##-----------------------------------
## Create clones for 2 btag bin
##-----------------------------------

analyzeSystematicsMu2b                     = analyzeSystematics.clone()
analyzeSystematicsMu2b.btagBin             = 2
analyzeSystematicsMu2b.BtagEventWeights    = "btagEventWeightMu:RA4bSFEventWeights"
analyzeSystematicsMu2b.jets                = "goodJets"
analyzeSystematicsMu2b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsMu2b.met                 = "patMETsPF"

analyzeSystematicsMu2bJER                  = analyzeSystematics.clone()
analyzeSystematicsMu2bJER.btagBin          = 2
analyzeSystematicsMu2bJER.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSystematicsMu2bJER.jets             = "smearedGoodJets"
analyzeSystematicsMu2bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsMu2bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsMu2bJECUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJECDown        = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJERUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bJERDown        = analyzeSystematicsMu2bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu2bLepUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bLepDown        = analyzeSystematicsMu2bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu2bMETUp          = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bMETDown        = analyzeSystematicsMu2bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu2bBtagSFUp       = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bBtagSFDown     = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bMistagSFUp     = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bMistagSFDown   = analyzeSystematicsMu2bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu2bPUUp           = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bPUDown         = analyzeSystematicsMu2bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu2bWUp            = analyzeSystematicsMu2bJER.clone()
analyzeSystematicsMu2bWDown          = analyzeSystematicsMu2bJER.clone()

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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu2bLepUp.muons      = "goodMuonsUp"
analyzeSystematicsMu2bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsMu"

analyzeSystematicsMu2bLepDown.muons    = "goodMuonsDown"
analyzeSystematicsMu2bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsMu"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu2bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsMu2bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu2bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu2bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu2bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu2bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsMu2bPUUp.PUWeight   =  "eventWeightPUUp:eventWeightPU"
analyzeSystematicsMu2bPUDown.PUWeight =  "eventWeightPUDown:eventWeightPU"


## configure clones to study W polatization uncertainty
## ...


##-----------------------------------
## Create clones for 3 btag bin
##-----------------------------------

analyzeSystematicsMu3b                     = analyzeSystematics.clone()
analyzeSystematicsMu3b.btagBin             = 3
analyzeSystematicsMu3b.BtagEventWeights    = "btagEventWeightMu:RA4bSFEventWeights"
analyzeSystematicsMu3b.jets                = "goodJets"
analyzeSystematicsMu3b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsMu3b.met                 = "patMETsPF"

analyzeSystematicsMu3bJER                  = analyzeSystematics.clone()
analyzeSystematicsMu3bJER.btagBin          = 3
analyzeSystematicsMu3bJER.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSystematicsMu3bJER.jets             = "smearedGoodJets"
analyzeSystematicsMu3bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsMu3bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsMu3bJECUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJECDown        = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJERUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bJERDown        = analyzeSystematicsMu3bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsMu3bLepUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bLepDown        = analyzeSystematicsMu3bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsMu3bMETUp          = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bMETDown        = analyzeSystematicsMu3bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu3bBtagSFUp       = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bBtagSFDown     = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bMistagSFUp     = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bMistagSFDown   = analyzeSystematicsMu3bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsMu3bPUUp           = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bPUDown         = analyzeSystematicsMu3bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsMu3bWUp            = analyzeSystematicsMu3bJER.clone()
analyzeSystematicsMu3bWDown          = analyzeSystematicsMu3bJER.clone()

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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsMu3bLepUp.muons      = "goodMuonsUp"
analyzeSystematicsMu3bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsMu"

analyzeSystematicsMu3bLepDown.muons    = "goodMuonsDown"
analyzeSystematicsMu3bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsMu"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsMu3bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsMu3bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsMu3bBtagSFUp.BtagEventWeights     = "btagEventWeightMuBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu3bBtagSFDown.BtagEventWeights   = "btagEventWeightMuBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsMu3bMistagSFUp.BtagEventWeights   = "btagEventWeightMuMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsMu3bMistagSFDown.BtagEventWeights = "btagEventWeightMuMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsMu3bPUUp.PUWeight   =  "eventWeightPUUp:eventWeightPU"
analyzeSystematicsMu3bPUDown.PUWeight =  "eventWeightPUDown:eventWeightPU"


## configure clones to study W polatization uncertainty
## ...
