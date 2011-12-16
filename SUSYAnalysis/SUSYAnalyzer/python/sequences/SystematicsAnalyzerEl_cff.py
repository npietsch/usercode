import FWCore.ParameterSet.Config as cms

from SUSYAnalysis.SUSYAnalyzer.SystematicsAnalyzer_cfi import *

## set default settings
analyzeSystematics.useEventWeight = True
analyzeSystematics.useBtagEventWeight = True

##-----------------------------------
## Create clones for 0 btag bin
##-----------------------------------

analyzeSystematicsEl0b                     = analyzeSystematics.clone()
analyzeSystematicsEl0b.btagBin             = 0
analyzeSystematicsEl0b.BtagEventWeights    = "btagEventWeightEl:RA4bSFEventWeights"
analyzeSystematicsEl0b.jets                = "goodJets"
analyzeSystematicsEl0b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsEl0b.met                 = "patMETsPF"

analyzeSystematicsEl0bJER                  = analyzeSystematics.clone()
analyzeSystematicsEl0bJER.btagBin          = 0
analyzeSystematicsEl0bJER.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSystematicsEl0bJER.jets             = "smearedGoodJets"
analyzeSystematicsEl0bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsEl0bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsEl0bJECUp          = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bJECDown        = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bJERUp          = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bJERDown        = analyzeSystematicsEl0bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsEl0bLepUp          = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bLepDown        = analyzeSystematicsEl0bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsEl0bMETUp          = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bMETDown        = analyzeSystematicsEl0bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl0bBtagSFUp       = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bBtagSFDown     = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bMistagSFUp     = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bMistagSFDown   = analyzeSystematicsEl0bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsEl0bPUUp           = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bPUDown         = analyzeSystematicsEl0bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl0bWUp            = analyzeSystematicsEl0bJER.clone()
analyzeSystematicsEl0bWDown          = analyzeSystematicsEl0bJER.clone()

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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsEl0bLepUp.electrons      = "goodElectronsUp"
analyzeSystematicsEl0bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsEl"

analyzeSystematicsEl0bLepDown.electrons    = "goodElectronsDown"
analyzeSystematicsEl0bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsEl"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsEl0bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsEl0bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl0bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl0bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl0bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl0bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsEl0bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl0bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study W polatization uncertainty
## ...


##-----------------------------------
## Create clones for 1 btag bin
##-----------------------------------

analyzeSystematicsEl1b                     = analyzeSystematics.clone()
analyzeSystematicsEl1b.btagBin             = 1
analyzeSystematicsEl1b.BtagEventWeights    = "btagEventWeightEl:RA4bSFEventWeights"
analyzeSystematicsEl1b.jets                = "goodJets"
analyzeSystematicsEl1b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsEl1b.met                 = "patMETsPF"

analyzeSystematicsEl1bJER                  = analyzeSystematics.clone()
analyzeSystematicsEl1bJER.btagBin          = 1
analyzeSystematicsEl1bJER.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSystematicsEl1bJER.jets             = "smearedGoodJets"
analyzeSystematicsEl1bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsEl1bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsEl1bJECUp          = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bJECDown        = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bJERUp          = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bJERDown        = analyzeSystematicsEl1bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsEl1bLepUp          = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bLepDown        = analyzeSystematicsEl1bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsEl1bMETUp          = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bMETDown        = analyzeSystematicsEl1bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl1bBtagSFUp       = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bBtagSFDown     = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bMistagSFUp     = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bMistagSFDown   = analyzeSystematicsEl1bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsEl1bPUUp           = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bPUDown         = analyzeSystematicsEl1bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl1bWUp            = analyzeSystematicsEl1bJER.clone()
analyzeSystematicsEl1bWDown          = analyzeSystematicsEl1bJER.clone()


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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsEl1bLepUp.electrons      = "goodElectronsUp"
analyzeSystematicsEl1bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsEl"

analyzeSystematicsEl1bLepDown.electrons    = "goodElectronsDown"
analyzeSystematicsEl1bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsEl"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsEl1bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsEl1bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl1bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl1bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl1bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl1bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsEl1bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl1bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study W polatization uncertainty
## ...


##-----------------------------------
## Create clones for 2 btag bin
##-----------------------------------

analyzeSystematicsEl2b                     = analyzeSystematics.clone()
analyzeSystematicsEl2b.btagBin             = 2
analyzeSystematicsEl2b.BtagEventWeights    = "btagEventWeightEl:RA4bSFEventWeights"
analyzeSystematicsEl2b.jets                = "goodJets"
analyzeSystematicsEl2b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsEl2b.met                 = "patMETsPF"

analyzeSystematicsEl2bJER                  = analyzeSystematics.clone()
analyzeSystematicsEl2bJER.btagBin          = 2
analyzeSystematicsEl2bJER.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSystematicsEl2bJER.jets             = "smearedGoodJets"
analyzeSystematicsEl2bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsEl2bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsEl2bJECUp          = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bJECDown        = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bJERUp          = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bJERDown        = analyzeSystematicsEl2bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsEl2bLepUp          = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bLepDown        = analyzeSystematicsEl2bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsEl2bMETUp          = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bMETDown        = analyzeSystematicsEl2bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl2bBtagSFUp       = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bBtagSFDown     = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bMistagSFUp     = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bMistagSFDown   = analyzeSystematicsEl2bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsEl2bPUUp           = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bPUDown         = analyzeSystematicsEl2bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl2bWUp            = analyzeSystematicsEl2bJER.clone()
analyzeSystematicsEl2bWDown          = analyzeSystematicsEl2bJER.clone()

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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsEl2bLepUp.electrons      = "goodElectronsUp"
analyzeSystematicsEl2bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsEl"

analyzeSystematicsEl2bLepDown.electrons    = "goodElectronsDown"
analyzeSystematicsEl2bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsEl"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsEl2bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsEl2bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl2bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl2bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl2bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl2bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsEl2bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl2bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study W polatization uncertainty
## ...


##-----------------------------------
## Create clones for 3 btag bin
##-----------------------------------

analyzeSystematicsEl3b                     = analyzeSystematics.clone()
analyzeSystematicsEl3b.btagBin             = 3
analyzeSystematicsEl3b.BtagEventWeights    = "btagEventWeightEl:RA4bSFEventWeights"
analyzeSystematicsEl3b.jets                = "goodJets"
analyzeSystematicsEl3b.bjets               = "mediumTrackHighEffBjets"
analyzeSystematicsEl3b.met                 = "patMETsPF"

analyzeSystematicsEl3bJER                  = analyzeSystematics.clone()
analyzeSystematicsEl3bJER.btagBin          = 3
analyzeSystematicsEl3bJER.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSystematicsEl3bJER.jets             = "smearedGoodJets"
analyzeSystematicsEl3bJER.bjets            = "smearedMediumTrackHighEffBjets"
analyzeSystematicsEl3bJER.met              = "scaledJetEnergy:patMETsPF"

## clones to study jet energy scale uncertainties
analyzeSystematicsEl3bJECUp          = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bJECDown        = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bJERUp          = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bJERDown        = analyzeSystematicsEl3bJER.clone()

## clones to study lepton energy scale uncertainties
analyzeSystematicsEl3bLepUp          = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bLepDown        = analyzeSystematicsEl3bJER.clone()

## clones to study unclustered energy scale uncertainties
analyzeSystematicsEl3bMETUp          = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bMETDown        = analyzeSystematicsEl3bJER.clone()

## clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl3bBtagSFUp       = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bBtagSFDown     = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bMistagSFUp     = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bMistagSFDown   = analyzeSystematicsEl3bJER.clone()

## clones to study PU uncertainties
analyzeSystematicsEl3bPUUp           = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bPUDown         = analyzeSystematicsEl3bJER.clone()

## clones to study W polarization uncertainty
analyzeSystematicsEl3bWUp            = analyzeSystematicsEl3bJER.clone()
analyzeSystematicsEl3bWDown          = analyzeSystematicsEl3bJER.clone()

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

## configure clones to study lepton energy scale uncertainties
analyzeSystematicsEl3bLepUp.electrons      = "goodElectronsUp"
analyzeSystematicsEl3bLepUp.met        = "scaledLeptonEnergyUp:scaledMETsEl"

analyzeSystematicsEl3bLepDown.electrons    = "goodElectronsDown"
analyzeSystematicsEl3bLepDown.met      = "scaledLeptonEnergyDown:scaledMETsEl"

## configure clones to study unclustered energy scale uncertainties
analyzeSystematicsEl3bMETUp.met      = "scaledUnclusteredEnergyUp:scaledMETs"
analyzeSystematicsEl3bMETDown.met    = "scaledUnclusteredEnergyDown:scaledMETs"

## configure clones to study btag eff and mistag scale factor uncertainties
analyzeSystematicsEl3bBtagSFUp.BtagEventWeights     = "btagEventWeightElBtagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl3bBtagSFDown.BtagEventWeights   = "btagEventWeightElBtagSFDown:RA4bSFEventWeights"
analyzeSystematicsEl3bMistagSFUp.BtagEventWeights   = "btagEventWeightElMistagSFUp:RA4bSFEventWeights"
analyzeSystematicsEl3bMistagSFDown.BtagEventWeights = "btagEventWeightElMistagSFDown:RA4bSFEventWeights"

## configure clones to study PU uncertainties
analyzeSystematicsEl3bPUUp.PUWeight   =  "eventWeightPU:eventWeightPUUp"
analyzeSystematicsEl3bPUDown.PUWeight =  "eventWeightPU:eventWeightPUDown"


## configure clones to study W polatization uncertainty
## ...
