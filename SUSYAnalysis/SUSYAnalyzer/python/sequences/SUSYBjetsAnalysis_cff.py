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

analyzeSUSY0b1m_2 = analyzeSUSY.clone()
analyzeSUSY1b1m_2 = analyzeSUSY.clone()
analyzeSUSY2b1m_2 = analyzeSUSY.clone()

## configure modules for muon channel
analyzeSUSY1b1m_1.useInclusiveBtagEventWeight = True
analyzeSUSY1b1m_1.inclusiveBtagBin = 1
analyzeSUSY1b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSUSY1b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeSUSY2b1m_1.useInclusiveBtagEventWeight = True
analyzeSUSY2b1m_1.inclusiveBtagBin = 2
analyzeSUSY2b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSUSY2b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeSUSY3b1m_1.useInclusiveBtagEventWeight = True
analyzeSUSY3b1m_1.inclusiveBtagBin = 3
analyzeSUSY3b1m_1.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSUSY3b1m_1.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeSUSY0b1m_2.useBtagEventWeight = True
analyzeSUSY0b1m_2.btagBin = 0
analyzeSUSY0b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSUSY0b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeSUSY1b1m_2.useBtagEventWeight = True
analyzeSUSY1b1m_2.btagBin = 1
analyzeSUSY1b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSUSY1b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeSUSY2b1m_2.useBtagEventWeight = True
analyzeSUSY2b1m_2.btagBin = 2
analyzeSUSY2b1m_2.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeSUSY2b1m_2.BtagJetWeights   = "btagEventWeightMuJER:RA4bSFJetWeights"

## clone modules for electron channel
analyzeSUSY1e_noCuts = analyzeSUSY.clone()
analyzeSUSY1e_preselection = analyzeSUSY.clone()
analyzeSUSY1e_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1e_jetSelection = analyzeSUSY.clone()

analyzeSUSY1b1e_1 = analyzeSUSY.clone()
analyzeSUSY2b1e_1 = analyzeSUSY.clone()
analyzeSUSY3b1e_1 = analyzeSUSY.clone()

analyzeSUSY0b1e_2 = analyzeSUSY.clone()
analyzeSUSY1b1e_2 = analyzeSUSY.clone()
analyzeSUSY2b1e_2 = analyzeSUSY.clone()

## configure modules electron muon channel
analyzeSUSY1b1e_1.useInclusiveBtagEventWeight = True
analyzeSUSY1b1e_1.inclusiveBtagBin = 1
analyzeSUSY1b1e_1.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSUSY1b1e_1.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeSUSY2b1e_1.useInclusiveBtagEventWeight = True
analyzeSUSY2b1e_1.inclusiveBtagBin = 2
analyzeSUSY2b1e_1.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSUSY2b1e_1.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeSUSY3b1e_1.useInclusiveBtagEventWeight = True
analyzeSUSY3b1e_1.inclusiveBtagBin = 3
analyzeSUSY3b1e_1.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSUSY3b1e_1.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeSUSY0b1e_2.useBtagEventWeight = True
analyzeSUSY0b1e_2.btagBin = 0
analyzeSUSY0b1e_2.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSUSY0b1e_2.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeSUSY1b1e_2.useBtagEventWeight = True
analyzeSUSY1b1e_2.btagBin = 1
analyzeSUSY1b1e_2.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSUSY1b1e_2.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

analyzeSUSY2b1e_2.useBtagEventWeight = True
analyzeSUSY2b1e_2.btagBin = 2
analyzeSUSY2b1e_2.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"
analyzeSUSY2b1e_2.BtagJetWeights   = "btagEventWeightElJER:RA4bSFJetWeights"

# clone modules for analysis of simulated TTJets events
analyzeSUSY_TTJets        = analyzeSUSY.clone()
analyzeSUSY_TTJets.TTJets = True

analyzeSUSY1m_noCuts_SemiLep          = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_preselection_SemiLep    = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_leptonSelection_SemiLep = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_jetSelection_SemiLep    = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_HTSelection_SemiLep     = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_METSelection_SemiLep    = analyzeSUSY_TTJets.clone()

analyzeSUSY1m_noCuts_DiLep            = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_preselection_DiLep      = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_leptonSelection_DiLep   = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_jetSelection_DiLep      = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_HTSelection_DiLep       = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_METSelection_DiLep      = analyzeSUSY_TTJets.clone()

analyzeSUSY1m_noCuts_FullHad          = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_preselection_FullHad    = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_leptonSelection_FullHad = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_jetSelection_FullHad    = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_HTSelection_FullHad     = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_METSelection_FullHad    = analyzeSUSY_TTJets.clone()

analyzeSUSY1m_noCuts_Tau              = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_preselection_Tau        = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_leptonSelection_Tau     = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_jetSelection_Tau        = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_HTSelection_Tau         = analyzeSUSY_TTJets.clone()
analyzeSUSY1m_METSelection_Tau        = analyzeSUSY_TTJets.clone()

analyzeSUSY1e_noCuts_SemiLep          = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_preselection_SemiLep    = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_leptonSelection_SemiLep = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_jetSelection_SemiLep    = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_HTSelection_SemiLep     = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_METSelection_SemiLep    = analyzeSUSY_TTJets.clone()

analyzeSUSY1e_noCuts_DiLep            = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_preselection_DiLep      = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_leptonSelection_DiLep   = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_jetSelection_DiLep      = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_HTSelection_DiLep       = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_METSelection_DiLep      = analyzeSUSY_TTJets.clone()

analyzeSUSY1e_noCuts_FullHad          = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_preselection_FullHad    = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_leptonSelection_FullHad = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_jetSelection_FullHad    = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_HTSelection_FullHad     = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_METSelection_FullHad    = analyzeSUSY_TTJets.clone()

analyzeSUSY1e_noCuts_Tau              = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_preselection_Tau        = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_leptonSelection_Tau     = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_jetSelection_Tau        = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_HTSelection_Tau         = analyzeSUSY_TTJets.clone()
analyzeSUSY1e_METSelection_Tau        = analyzeSUSY_TTJets.clone()

analyzeSUSY1l_noCuts_SemiLep           = analyzeSUSY_TTJets.clone()
analyzeSUSY1l_preselection_SemiLep     = analyzeSUSY_TTJets.clone()
analyzeSUSY1l_leptonSelection_SemiLep  = analyzeSUSY_TTJets.clone()
analyzeSUSY1l_jetSelection_SemiLep     = analyzeSUSY_TTJets.clone()
analyzeSUSY1l_HTSelection_SemiLep      = analyzeSUSY_TTJets.clone()
analyzeSUSY1l_METSelection_SemiLep     = analyzeSUSY_TTJets.clone()

analyzeSUSY1l_noCuts_TTJets           = analyzeSUSY.clone()
analyzeSUSY1l_preselection_TTJets     = analyzeSUSY.clone()
analyzeSUSY1l_leptonSelection_TTJets  = analyzeSUSY.clone()
analyzeSUSY1l_jetSelection_TTJets     = analyzeSUSY.clone()
analyzeSUSY1l_HTSelection_TTJets      = analyzeSUSY.clone()
analyzeSUSY1l_METSelection_TTJets     = analyzeSUSY.clone()

#----------------------------------------------------
# Clone and configure SUSYGenEventAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import *

analyzeSUSYGenEvent = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvent.jets             = "goodJets"
analyzeSUSYGenEvent.bjets            = "mediumTrackHighPurBjets"
analyzeSUSYGenEvent.matchedbjets     = "matchedBjets"
analyzeSUSYGenEvent.matchedqjets     = "matchedLightJets"
analyzeSUSYGenEvent.matchedmuons     = "goodMuons"
analyzeSUSYGenEvent.matchedelectrons = "goodElectrons"

## clone modules for muon channel
analyzeSUSYGenEvent1m_noCuts = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1m_preselection = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1m_leptonSelection = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1m_jetSelection = analyzeSUSYGenEvent.clone()

analyzeSUSYGenEvent1b1m_1 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent2b1m_1 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent3b1m_1 = analyzeSUSYGenEvent.clone()

analyzeSUSYGenEvent0b1m_2 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1b1m_2 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent2b1m_2 = analyzeSUSYGenEvent.clone()

## clone modules for electron channel
analyzeSUSYGenEvent1e_noCuts = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1e_preselection = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1e_leptonSelection = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1e_jetSelection = analyzeSUSYGenEvent.clone()

analyzeSUSYGenEvent1b1e_1 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent2b1e_1 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent3b1e_1 = analyzeSUSYGenEvent.clone()

analyzeSUSYGenEvent0b1e_2 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent1b1e_2 = analyzeSUSYGenEvent.clone()
analyzeSUSYGenEvent2b1e_2 = analyzeSUSYGenEvent.clone()

#----------------------------------------------------
# Define analyzer sequences
#----------------------------------------------------

analyzeSUSYBjets1m_noCuts = cms.Sequence(analyzeSUSY1m_noCuts *
                                         analyzeSUSYGenEvent1m_noCuts
                                         )

analyzeSUSYBjets1m_preselection = cms.Sequence(analyzeSUSY1m_preselection *
                                               analyzeSUSYGenEvent1m_preselection
                                               )

analyzeSUSYBjets1m_leptonSelection = cms.Sequence(analyzeSUSY1m_leptonSelection *
                                                  analyzeSUSYGenEvent1m_leptonSelection
                                                  )

analyzeSUSYBjets1m_jetSelection = cms.Sequence(analyzeSUSY1m_jetSelection *
                                               analyzeSUSYGenEvent1m_jetSelection
                                               )

analyzeSUSYBjets1b1m_1 = cms.Sequence(analyzeSUSY1b1m_1 *
                                      analyzeSUSYGenEvent1b1m_1
                                      )

analyzeSUSYBjets2b1m_1 = cms.Sequence(analyzeSUSY2b1m_1 *
                                      analyzeSUSYGenEvent2b1m_1
                                      )

analyzeSUSYBjets3b1m_1 = cms.Sequence(analyzeSUSY3b1m_1 *
                                      analyzeSUSYGenEvent3b1m_1
                                      )

analyzeSUSYBjets0b1m_2 = cms.Sequence(analyzeSUSY0b1m_2 *
                                      analyzeSUSYGenEvent0b1m_2
                                      )

analyzeSUSYBjets1b1m_2 = cms.Sequence(analyzeSUSY1b1m_2 *
                                      analyzeSUSYGenEvent1b1m_2
                                      )

analyzeSUSYBjets2b1m_2 = cms.Sequence(analyzeSUSY2b1m_2 *
                                      analyzeSUSYGenEvent2b1m_2
                                      )



analyzeSUSYBjets1e_noCuts = cms.Sequence(analyzeSUSY1e_noCuts *
                                         analyzeSUSYGenEvent1e_noCuts
                                         )

analyzeSUSYBjets1e_preselection = cms.Sequence(analyzeSUSY1e_preselection *
                                               analyzeSUSYGenEvent1e_preselection
                                               )

analyzeSUSYBjets1e_leptonSelection = cms.Sequence(analyzeSUSY1e_leptonSelection *
                                                  analyzeSUSYGenEvent1e_leptonSelection
                                                  )

analyzeSUSYBjets1e_jetSelection = cms.Sequence(analyzeSUSY1e_jetSelection *
                                               analyzeSUSYGenEvent1e_jetSelection
                                               )

analyzeSUSYBjets1b1e_1 = cms.Sequence(analyzeSUSY1b1e_1 *
                                      analyzeSUSYGenEvent1b1e_1
                                      )

analyzeSUSYBjets2b1e_1 = cms.Sequence(analyzeSUSY2b1e_1 *
                                      analyzeSUSYGenEvent2b1e_1
                                      )

analyzeSUSYBjets3b1e_1 = cms.Sequence(analyzeSUSY3b1e_1 *
                                      analyzeSUSYGenEvent3b1e_1
                                      )

analyzeSUSYBjets0b1e_2 = cms.Sequence(analyzeSUSY0b1e_2 *
                                      analyzeSUSYGenEvent0b1e_2
                                      )

analyzeSUSYBjets1b1e_2 = cms.Sequence(analyzeSUSY1b1e_2 *
                                      analyzeSUSYGenEvent1b1e_2
                                      )

analyzeSUSYBjets2b1e_2 = cms.Sequence(analyzeSUSY2b1e_2 *
                                      analyzeSUSYGenEvent2b1e_2
                                      )

#----------------------------------------------------
# Clone and configure TtGenEventAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.TtGenEventAnalyzer_cfi import *

analyzeTtGenEvent1l_noCuts_TTJets           = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_preselection_TTJets     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_leptonSelection_TTJets  = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_jetSelection_TTJets     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_HTSelection_TTJets      = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_METSelection_TTJets     = analyzeTtGenEvent.clone()

analyzeTtGenEvent1l_noCuts_SemiLep          = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_preselection_SemiLep    = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_leptonSelection_SemiLep = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_jetSelection_SemiLep    = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_HTSelection_SemiLep     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_METSelection_SemiLep    = analyzeTtGenEvent.clone()
