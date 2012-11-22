#----------------------------------------------------
# Clone and configure CorrelationAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.CorrelationAnalyzer_cfi import *

analyzeCorrelation.jets           = "goodJets"
analyzeCorrelation.muons          = "goodMuons"
analyzeCorrelation.electrons      = "goodElectrons"
analyzeCorrelation.met            = "scaledJetEnergy:patMETsPF"
analyzeCorrelation.useEventWeight = True

## clone modules for different nJets, HT and MET cuts
analyzeCorrelation1l_HT200To300       = analyzeCorrelation.clone()
analyzeCorrelation1l_HT200To300.HTCut = 200.,300.

## clone modules for muon channel
analyzeCorrelation1m_noCuts = analyzeCorrelation.clone()
analyzeCorrelation1m_preselection = analyzeCorrelation.clone()
analyzeCorrelation1m_leptonSelection = analyzeCorrelation.clone()
analyzeCorrelation1m_jetSelection = analyzeCorrelation.clone()

analyzeCorrelation1b1m_1 = analyzeCorrelation.clone()
analyzeCorrelation2b1m_1 = analyzeCorrelation.clone()
analyzeCorrelation3b1m_1 = analyzeCorrelation.clone()

analyzeCorrelation0b1m_2 = analyzeCorrelation.clone()
analyzeCorrelation1b1m_2 = analyzeCorrelation.clone()
analyzeCorrelation2b1m_2 = analyzeCorrelation.clone()

## configure modules for muon channel
analyzeCorrelation1b1m_1.useInclusiveBtagEventWeight = True
analyzeCorrelation1b1m_1.inclusiveBtagBin = 1
analyzeCorrelation1b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation1b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeCorrelation2b1m_1.useInclusiveBtagEventWeight = True
analyzeCorrelation2b1m_1.inclusiveBtagBin = 2
analyzeCorrelation2b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation2b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeCorrelation3b1m_1.useInclusiveBtagEventWeight = True
analyzeCorrelation3b1m_1.inclusiveBtagBin = 3
analyzeCorrelation3b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation3b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeCorrelation0b1m_2.useBtagEventWeight = True
analyzeCorrelation0b1m_2.btagBin = 0
analyzeCorrelation0b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation0b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeCorrelation1b1m_2.useBtagEventWeight = True
analyzeCorrelation1b1m_2.btagBin = 1
analyzeCorrelation1b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation1b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeCorrelation2b1m_2.useBtagEventWeight = True
analyzeCorrelation2b1m_2.btagBin = 2
analyzeCorrelation2b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation2b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

## clone modules for electron channel
analyzeCorrelation1e_noCuts = analyzeCorrelation.clone()
analyzeCorrelation1e_preselection = analyzeCorrelation.clone()
analyzeCorrelation1e_leptonSelection = analyzeCorrelation.clone()
analyzeCorrelation1e_jetSelection = analyzeCorrelation.clone()

analyzeCorrelation1b1e_1 = analyzeCorrelation.clone()
analyzeCorrelation2b1e_1 = analyzeCorrelation.clone()
analyzeCorrelation3b1e_1 = analyzeCorrelation.clone()

analyzeCorrelation0b1e_2 = analyzeCorrelation.clone()
analyzeCorrelation1b1e_2 = analyzeCorrelation.clone()
analyzeCorrelation2b1e_2 = analyzeCorrelation.clone()

## configure modules electron muon channel
analyzeCorrelation1b1e_1.useInclusiveBtagEventWeight = True
analyzeCorrelation1b1e_1.inclusiveBtagBin = 1
analyzeCorrelation1b1e_1.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeCorrelation1b1e_1.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeCorrelation2b1e_1.useInclusiveBtagEventWeight = True
analyzeCorrelation2b1e_1.inclusiveBtagBin = 2
analyzeCorrelation2b1e_1.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeCorrelation2b1e_1.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeCorrelation3b1e_1.useInclusiveBtagEventWeight = True
analyzeCorrelation3b1e_1.inclusiveBtagBin = 3
analyzeCorrelation3b1e_1.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeCorrelation3b1e_1.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeCorrelation0b1e_2.useBtagEventWeight = True
analyzeCorrelation0b1e_2.btagBin = 0
analyzeCorrelation0b1e_2.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeCorrelation0b1e_2.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeCorrelation1b1e_2.useBtagEventWeight = True
analyzeCorrelation1b1e_2.btagBin = 1
analyzeCorrelation1b1e_2.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeCorrelation1b1e_2.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeCorrelation2b1e_2.useBtagEventWeight = True
analyzeCorrelation2b1e_2.btagBin = 2
analyzeCorrelation2b1e_2.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeCorrelation2b1e_2.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

# clone modules for analysis of simulated TTJets events
analyzeCorrelation_TTJets        = analyzeCorrelation.clone()
analyzeCorrelation_TTJets.TTJets = True

analyzeCorrelation1m_noCuts_SemiLep          = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_preselection_SemiLep    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_leptonSelection_SemiLep = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_jetSelection_SemiLep    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_HTSelection_SemiLep     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_METSelection_SemiLep    = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1m_noCuts_DiLep            = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_preselection_DiLep      = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_leptonSelection_DiLep   = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_jetSelection_DiLep      = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_HTSelection_DiLep       = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_METSelection_DiLep      = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1m_noCuts_FullHad          = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_preselection_FullHad    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_leptonSelection_FullHad = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_jetSelection_FullHad    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_HTSelection_FullHad     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_METSelection_FullHad    = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1m_noCuts_Tau              = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_preselection_Tau        = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_leptonSelection_Tau     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_jetSelection_Tau        = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_HTSelection_Tau         = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1m_METSelection_Tau        = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1e_noCuts_SemiLep          = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_preselection_SemiLep    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_leptonSelection_SemiLep = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_jetSelection_SemiLep    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_HTSelection_SemiLep     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_METSelection_SemiLep    = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1e_noCuts_DiLep            = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_preselection_DiLep      = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_leptonSelection_DiLep   = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_jetSelection_DiLep      = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_HTSelection_DiLep       = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_METSelection_DiLep      = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1e_noCuts_FullHad          = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_preselection_FullHad    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_leptonSelection_FullHad = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_jetSelection_FullHad    = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_HTSelection_FullHad     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_METSelection_FullHad    = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1e_noCuts_Tau              = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_preselection_Tau        = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_leptonSelection_Tau     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_jetSelection_Tau        = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_HTSelection_Tau         = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1e_METSelection_Tau        = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1l_noCuts_SemiLep           = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1l_preselection_SemiLep     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1l_leptonSelection_SemiLep  = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1l_jetSelection_SemiLep     = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1l_HTSelection_SemiLep      = analyzeCorrelation_TTJets.clone()
analyzeCorrelation1l_METSelection_SemiLep     = analyzeCorrelation_TTJets.clone()

analyzeCorrelation1l_noCuts_TTJets           = analyzeCorrelation.clone()
analyzeCorrelation1l_preselection_TTJets     = analyzeCorrelation.clone()
analyzeCorrelation1l_leptonSelection_TTJets  = analyzeCorrelation.clone()
analyzeCorrelation1l_jetSelection_TTJets     = analyzeCorrelation.clone()
analyzeCorrelation1l_HTSelection_TTJets      = analyzeCorrelation.clone()
analyzeCorrelation1l_METSelection_TTJets     = analyzeCorrelation.clone()
