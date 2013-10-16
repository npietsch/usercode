
#----------------------------------------------------
# Clone and configure SUSYAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets           = "goodJets"
analyzeSUSY.muons          = "goodMuons"
analyzeSUSY.electrons      = "goodElectrons"
analyzeSUSY.useTriggerEventWeight = True

## clone and configure modules for muon channel
analyzeSUSY1m_noCuts = analyzeSUSY.clone()
analyzeSUSY1m_preselectionLepton = analyzeSUSY.clone()
analyzeSUSY1m_preselectionHT = analyzeSUSY.clone()
analyzeSUSY1m_preselectionMET = analyzeSUSY.clone()
analyzeSUSY1m_preselection = analyzeSUSY.clone()
analyzeSUSY1m_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1m_jetSelection = analyzeSUSY.clone()

analyzeSUSY1m_nJets1 = analyzeSUSY.clone()
analyzeSUSY1m_nJets2 = analyzeSUSY.clone()
analyzeSUSY1m_nJets3 = analyzeSUSY.clone()
analyzeSUSY1m_nJets4 = analyzeSUSY.clone()
analyzeSUSY1m_nJets5 = analyzeSUSY.clone()
analyzeSUSY1m_nJets6 = analyzeSUSY.clone()

analyzeSUSY1b1m_1 = analyzeSUSY.clone()
analyzeSUSY2b1m_1 = analyzeSUSY.clone()
analyzeSUSY3b1m_1 = analyzeSUSY.clone()

analyzeSUSY0b1m_2 = analyzeSUSY.clone()
analyzeSUSY1b1m_2 = analyzeSUSY.clone()
analyzeSUSY2b1m_2 = analyzeSUSY.clone()

analyzeSUSY1m_nJets1.nJetsCut = 1,1
analyzeSUSY1m_nJets2.nJetsCut = 2,2
analyzeSUSY1m_nJets3.nJetsCut = 3,3
analyzeSUSY1m_nJets4.nJetsCut = 4,4
analyzeSUSY1m_nJets5.nJetsCut = 5,5
analyzeSUSY1m_nJets6.nJetsCut = 6,6

## clone and configure modules for electron channel
analyzeSUSY1e_noCuts = analyzeSUSY.clone()
analyzeSUSY1e_preselectionLepton = analyzeSUSY.clone()
analyzeSUSY1e_preselectionHT = analyzeSUSY.clone()
analyzeSUSY1e_preselectionMET = analyzeSUSY.clone()
analyzeSUSY1e_preselection = analyzeSUSY.clone()
analyzeSUSY1e_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1e_jetSelection = analyzeSUSY.clone()

analyzeSUSY1e_nJets1 = analyzeSUSY.clone()
analyzeSUSY1e_nJets2 = analyzeSUSY.clone()
analyzeSUSY1e_nJets3 = analyzeSUSY.clone()
analyzeSUSY1e_nJets4 = analyzeSUSY.clone()
analyzeSUSY1e_nJets5 = analyzeSUSY.clone()
analyzeSUSY1e_nJets6 = analyzeSUSY.clone()

analyzeSUSY1b1e_1 = analyzeSUSY.clone()
analyzeSUSY2b1e_1 = analyzeSUSY.clone()
analyzeSUSY3b1e_1 = analyzeSUSY.clone()

analyzeSUSY0b1e_2 = analyzeSUSY.clone()
analyzeSUSY1b1e_2 = analyzeSUSY.clone()
analyzeSUSY2b1e_2 = analyzeSUSY.clone()

analyzeSUSY1e_nJets1.nJetsCut = 1,1
analyzeSUSY1e_nJets2.nJetsCut = 2,2
analyzeSUSY1e_nJets3.nJetsCut = 3,3
analyzeSUSY1e_nJets4.nJetsCut = 4,4
analyzeSUSY1e_nJets5.nJetsCut = 5,5
analyzeSUSY1e_nJets6.nJetsCut = 6,6

#----------------------------------------------------
# Define analyzer sequences
#----------------------------------------------------

analyzeSUSYBjets1m_noCuts = cms.Sequence(analyzeSUSY1m_noCuts
                                         )

analyzeSUSYBjets1m_preselection = cms.Sequence(analyzeSUSY1m_preselection
                                               )

analyzeSUSYBjets1m_leptonSelection = cms.Sequence(analyzeSUSY1m_leptonSelection
                                                  )

analyzeSUSYBjets1m_jetSelection = cms.Sequence(analyzeSUSY1m_jetSelection
                                               )


analyzeSUSYBjets1b1m_1 = cms.Sequence(analyzeSUSY1b1m_1 
                                      )

analyzeSUSYBjets2b1m_1 = cms.Sequence(analyzeSUSY2b1m_1
                                      )

analyzeSUSYBjets3b1m_1 = cms.Sequence(analyzeSUSY3b1m_1
                                      )

analyzeSUSYBjets0b1m_2 = cms.Sequence(analyzeSUSY0b1m_2
                                      )

analyzeSUSYBjets1b1m_2 = cms.Sequence(analyzeSUSY1b1m_2
                                      )

analyzeSUSYBjets2b1m_2 = cms.Sequence(analyzeSUSY2b1m_2
                                      )


analyzeSUSYBjets1e_noCuts = cms.Sequence(analyzeSUSY1e_noCuts
                                         )

analyzeSUSYBjets1e_preselection = cms.Sequence(analyzeSUSY1e_preselection
                                               )

analyzeSUSYBjets1e_leptonSelection = cms.Sequence(analyzeSUSY1e_leptonSelection
                                                  )

analyzeSUSYBjets1e_jetSelection = cms.Sequence(analyzeSUSY1e_jetSelection
                                               )


analyzeSUSYBjets1b1e_1 = cms.Sequence(analyzeSUSY1b1e_1
                                      )

analyzeSUSYBjets2b1e_1 = cms.Sequence(analyzeSUSY2b1e_1
                                      )

analyzeSUSYBjets3b1e_1 = cms.Sequence(analyzeSUSY3b1e_1
                                      )

analyzeSUSYBjets0b1e_2 = cms.Sequence(analyzeSUSY0b1e_2
                                      )

analyzeSUSYBjets1b1e_2 = cms.Sequence(analyzeSUSY1b1e_2
                                      )

analyzeSUSYBjets2b1e_2 = cms.Sequence(analyzeSUSY2b1e_2
                                      )
