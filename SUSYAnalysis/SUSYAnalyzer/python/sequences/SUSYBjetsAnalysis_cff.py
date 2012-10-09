
#----------------------------------------------------
# Clone and configure SUSYAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets           = "goodJets"
analyzeSUSY.muons          = "goodMuons"
analyzeSUSY.electrons      = "goodElectrons"
analyzeSUSY.met            = "scaledJetEnergy:patMETsPF"
analyzeSUSY.useEventWeight = True

## clone modules for muon channel
analyzeSUSY1m_noCuts = analyzeSUSY.clone()
analyzeSUSY1m_preselection = analyzeSUSY.clone()
analyzeSUSY1m_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1m_jetSelection = analyzeSUSY.clone()

analyzeSUSY1b1m_1 = analyzeSUSY.clone()
analyzeSUSY2b1m_1 = analyzeSUSY.clone()
analyzeSUSY3b1m_1 = analyzeSUSY.clone()

analyzeSUSY1b1m_2 = analyzeSUSY.clone()
analyzeSUSY2b1m_2 = analyzeSUSY.clone()

## configure modules for muon channel
analyzeSUSY1b1m_1.useInclusiveBtagEventWeight = True
analyzeSUSY1b1m_1.inclusiveBtagBin = 1
analyzeSUSY1b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
analyzeSUSY1b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

analyzeSUSY2b1m_1.useInclusiveBtagEventWeight = True
analyzeSUSY2b1m_1.inclusiveBtagBin = 2
analyzeSUSY2b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
analyzeSUSY2b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

analyzeSUSY3b1m_1.useInclusiveBtagEventWeight = True
analyzeSUSY3b1m_1.inclusiveBtagBin = 3
analyzeSUSY3b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
analyzeSUSY3b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

analyzeSUSY1b1m_2.useInclusiveBtagEventWeight = True
analyzeSUSY1b1m_2.btagBin = 1
analyzeSUSY1b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
analyzeSUSY1b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

analyzeSUSY2b1m_2.useInclusiveBtagEventWeight = True
analyzeSUSY2b1m_2.btagBin = 2
analyzeSUSY2b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bEventWeights"
analyzeSUSY2b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bJetWeights"

#----------------------------------------------------
# Clone and configure SUSYGenEventAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import *

analyzeSUSYGenEvent.jets             = "goodJets"
analyzeSUSYGenEvent.bjets            = "mediumTrackHighPurBjets"
analyzeSUSYGenEvent.matchedbjets     = "matchedBjets"
analyzeSUSYGenEvent.matchedqjets     = "matchedLightJets"
analyzeSUSYGenEvent.matchedmuons     = "goodMuons"
analyzeSUSYGenEvent.matchedelectrons = "goodElectrons"

## clone modules 
analyzeSUSYGenEvent1m_noCuts = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1m_preselection = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1m_leptonSelection = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1m_jetSelection = analyzeSUSYGenEvent.clone()

analyzeSUSYGenEvent1b1m_1 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent2b1m_1 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent3b1m_1 = analyzeSUSYGenEvent.clone()

analyzeSUSYGenEvent1b1m_2 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent2b1m_2 = analyzeSUSYGenEvent.clone()
