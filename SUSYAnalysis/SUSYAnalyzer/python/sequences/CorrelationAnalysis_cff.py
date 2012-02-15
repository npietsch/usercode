from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.useEventWeight = True

##--------------------------------
## Create SUSYAnalyzer clones
##--------------------------------

analyzeSUSY1m_noCuts = analyzeSUSY.clone()
analyzeSUSY1m_preselection = analyzeSUSY.clone()
analyzeSUSY1m_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1m_jetSelection = analyzeSUSY.clone()
analyzeSUSY1m_metSelection = analyzeSUSY.clone()
analyzeSUSY1m_HTSelection = analyzeSUSY.clone()
analyzeSUSY1m_mTSelection = analyzeSUSY.clone()

analyzeSUSY1m_1 = analyzeSUSY.clone()
analyzeSUSY1m_2 = analyzeSUSY.clone()
analyzeSUSY1m_3 = analyzeSUSY.clone()
analyzeSUSY1m_4 = analyzeSUSY.clone()
analyzeSUSY1m_5 = analyzeSUSY.clone()
analyzeSUSY1m_6 = analyzeSUSY.clone()

analyzeSUSY1b1m_1 = analyzeSUSY.clone()
analyzeSUSY1b1m_2 = analyzeSUSY.clone()
analyzeSUSY1b1m_3 = analyzeSUSY.clone()
analyzeSUSY1b1m_4 = analyzeSUSY.clone()
analyzeSUSY1b1m_5 = analyzeSUSY.clone()
analyzeSUSY1b1m_6 = analyzeSUSY.clone()

analyzeSUSY2b1m_1 = analyzeSUSY.clone()
analyzeSUSY2b1m_2 = analyzeSUSY.clone()
analyzeSUSY2b1m_3 = analyzeSUSY.clone()
analyzeSUSY2b1m_4 = analyzeSUSY.clone()
analyzeSUSY2b1m_5 = analyzeSUSY.clone()
analyzeSUSY2b1m_6 = analyzeSUSY.clone()

analyzeSUSY3b1m_1 = analyzeSUSY.clone()
analyzeSUSY3b1m_2 = analyzeSUSY.clone()
analyzeSUSY3b1m_3 = analyzeSUSY.clone()
analyzeSUSY3b1m_4 = analyzeSUSY.clone()
analyzeSUSY3b1m_5 = analyzeSUSY.clone()
analyzeSUSY3b1m_6 = analyzeSUSY.clone()

analyzeSUSY1e_noCuts = analyzeSUSY.clone()
analyzeSUSY1e_preselection = analyzeSUSY.clone()
analyzeSUSY1e_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1e_jetSelection = analyzeSUSY.clone()
analyzeSUSY1e_metSelection = analyzeSUSY.clone()
analyzeSUSY1e_HTSelection = analyzeSUSY.clone()
analyzeSUSY1e_mTSelection = analyzeSUSY.clone()

analyzeSUSY1e_1 = analyzeSUSY.clone()
analyzeSUSY1e_2 = analyzeSUSY.clone()
analyzeSUSY1e_3 = analyzeSUSY.clone()
analyzeSUSY1e_4 = analyzeSUSY.clone()
analyzeSUSY1e_5 = analyzeSUSY.clone()
analyzeSUSY1e_6 = analyzeSUSY.clone()
    
analyzeSUSY1b1e_1 = analyzeSUSY.clone()
analyzeSUSY1b1e_2 = analyzeSUSY.clone()
analyzeSUSY1b1e_3 = analyzeSUSY.clone()
analyzeSUSY1b1e_4 = analyzeSUSY.clone()
analyzeSUSY1b1e_5 = analyzeSUSY.clone()
analyzeSUSY1b1e_6 = analyzeSUSY.clone()
 
analyzeSUSY2b1e_1 = analyzeSUSY.clone()
analyzeSUSY2b1e_2 = analyzeSUSY.clone()
analyzeSUSY2b1e_3 = analyzeSUSY.clone()
analyzeSUSY2b1e_4 = analyzeSUSY.clone()
analyzeSUSY2b1e_5 = analyzeSUSY.clone()
analyzeSUSY2b1e_6 = analyzeSUSY.clone()

analyzeSUSY3b1e_1 = analyzeSUSY.clone()
analyzeSUSY3b1e_2 = analyzeSUSY.clone()
analyzeSUSY3b1e_3 = analyzeSUSY.clone()
analyzeSUSY3b1e_4 = analyzeSUSY.clone()
analyzeSUSY3b1e_5 = analyzeSUSY.clone()
analyzeSUSY3b1e_6 = analyzeSUSY.clone()

##--------------------------------
## Configure SUSYAnalyzer clones
##--------------------------------

analyzeSUSY1b1m_4.useInclusiveBtagEventWeight = True
analyzeSUSY1b1m_4.inclusiveBtagBin = 1
analyzeSUSY1b1m_4.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

analyzeSUSY1b1m_6.useBtagEventWeight = True
analyzeSUSY1b1m_6.btagBin = 1
analyzeSUSY1b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

analyzeSUSY2b1m_6.useBtagEventWeight = True
analyzeSUSY2b1m_6.btagBin = 2
analyzeSUSY2b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

analyzeSUSY3b1m_6.useBtagEventWeight = True
analyzeSUSY3b1m_6.btagBin = 3
analyzeSUSY3b1m_6.BtagEventWeights = "btagEventWeightMuJER:RA4bSFEventWeights"

analyzeSUSY1b1e_4.useInclusiveBtagEventWeight = True
analyzeSUSY1b1e_4.inclusiveBtagBin = 1
analyzeSUSY1b1e_4.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

analyzeSUSY1b1e_6.useBtagEventWeight = True
analyzeSUSY1b1e_6.btagBin = 1
analyzeSUSY1b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

analyzeSUSY2b1e_6.useBtagEventWeight = True
analyzeSUSY2b1e_6.btagBin = 2
analyzeSUSY2b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

analyzeSUSY3b1e_6.useBtagEventWeight = True
analyzeSUSY3b1e_6.btagBin = 3
analyzeSUSY3b1e_6.BtagEventWeights = "btagEventWeightElJER:RA4bSFEventWeights"

##--------------------------------
## Create SUSYAnalyzer clones
##--------------------------------

analyzeSUSY1b1m_4_JER10Up = analyzeSUSY1b1m_4.clone()
analyzeSUSY1b1m_4_JER20Up = analyzeSUSY1b1m_4.clone()
analyzeSUSY1b1m_4_JER30Up = analyzeSUSY1b1m_4.clone()
analyzeSUSY1b1m_4_JER10Down = analyzeSUSY1b1m_4.clone()
analyzeSUSY1b1m_4_JER20Down = analyzeSUSY1b1m_4.clone()
analyzeSUSY1b1m_4_JER30Down = analyzeSUSY1b1m_4.clone()

analyzeSUSY1b1m_6_JER10Up = analyzeSUSY1b1m_6.clone()
analyzeSUSY1b1m_6_JER20Up = analyzeSUSY1b1m_6.clone()
analyzeSUSY1b1m_6_JER30Up = analyzeSUSY1b1m_6.clone()
analyzeSUSY1b1m_6_JER10Down = analyzeSUSY1b1m_6.clone()
analyzeSUSY1b1m_6_JER20Down = analyzeSUSY1b1m_6.clone()
analyzeSUSY1b1m_6_JER30Down = analyzeSUSY1b1m_6.clone()

analyzeSUSY2b1m_6_JER10Up = analyzeSUSY2b1m_6.clone()
analyzeSUSY2b1m_6_JER20Up = analyzeSUSY2b1m_6.clone()
analyzeSUSY2b1m_6_JER30Up = analyzeSUSY2b1m_6.clone()
analyzeSUSY2b1m_6_JER10Down = analyzeSUSY2b1m_6.clone()
analyzeSUSY2b1m_6_JER20Down = analyzeSUSY2b1m_6.clone()
analyzeSUSY2b1m_6_JER30Down = analyzeSUSY2b1m_6.clone()

analyzeSUSY3b1m_6_JER10Up = analyzeSUSY3b1m_6.clone()
analyzeSUSY3b1m_6_JER20Up = analyzeSUSY3b1m_6.clone()
analyzeSUSY3b1m_6_JER30Up = analyzeSUSY3b1m_6.clone()
analyzeSUSY3b1m_6_JER10Down = analyzeSUSY3b1m_6.clone()
analyzeSUSY3b1m_6_JER20Down = analyzeSUSY3b1m_6.clone()
analyzeSUSY3b1m_6_JER30Down = analyzeSUSY3b1m_6.clone()

analyzeSUSY1b1e_4_JER10Up = analyzeSUSY1b1e_4.clone()
analyzeSUSY1b1e_4_JER20Up = analyzeSUSY1b1e_4.clone()
analyzeSUSY1b1e_4_JER30Up = analyzeSUSY1b1e_4.clone()
analyzeSUSY1b1e_4_JER10Down = analyzeSUSY1b1e_4.clone()
analyzeSUSY1b1e_4_JER20Down = analyzeSUSY1b1e_4.clone()
analyzeSUSY1b1e_4_JER30Down = analyzeSUSY1b1e_4.clone()

analyzeSUSY1b1e_6_JER10Up = analyzeSUSY1b1e_6.clone()
analyzeSUSY1b1e_6_JER20Up = analyzeSUSY1b1e_6.clone()
analyzeSUSY1b1e_6_JER30Up = analyzeSUSY1b1e_6.clone()
analyzeSUSY1b1e_6_JER10Down = analyzeSUSY1b1e_6.clone()
analyzeSUSY1b1e_6_JER20Down = analyzeSUSY1b1e_6.clone()
analyzeSUSY1b1e_6_JER30Down = analyzeSUSY1b1e_6.clone()

analyzeSUSY2b1e_6_JER10Up = analyzeSUSY2b1e_6.clone()
analyzeSUSY2b1e_6_JER20Up = analyzeSUSY2b1e_6.clone()
analyzeSUSY2b1e_6_JER30Up = analyzeSUSY2b1e_6.clone()
analyzeSUSY2b1e_6_JER10Down = analyzeSUSY2b1e_6.clone()
analyzeSUSY2b1e_6_JER20Down = analyzeSUSY2b1e_6.clone()
analyzeSUSY2b1e_6_JER30Down = analyzeSUSY2b1e_6.clone()

analyzeSUSY3b1e_6_JER10Up = analyzeSUSY3b1e_6.clone()
analyzeSUSY3b1e_6_JER20Up = analyzeSUSY3b1e_6.clone()
analyzeSUSY3b1e_6_JER30Up = analyzeSUSY3b1e_6.clone()
analyzeSUSY3b1e_6_JER10Down = analyzeSUSY3b1e_6.clone()
analyzeSUSY3b1e_6_JER20Down = analyzeSUSY3b1e_6.clone()
analyzeSUSY3b1e_6_JER30Down = analyzeSUSY3b1e_6.clone()


## configuration for muon channel
analyzeSUSY1b1m_4_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY1b1m_4_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY1b1m_4_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY1b1m_4_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY1b1m_4_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY1b1m_4_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY1b1m_4_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY1b1m_4_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY1b1m_4_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY1b1m_4_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY1b1m_4_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY1b1m_4_JER30Down.met = "goodMETsJER30Down"

analyzeSUSY1b1m_6_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY1b1m_6_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY1b1m_6_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY1b1m_6_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY1b1m_6_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY1b1m_6_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY1b1m_6_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY1b1m_6_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY1b1m_6_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY1b1m_6_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY1b1m_6_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY1b1m_6_JER30Down.met = "goodMETsJER30Down"

analyzeSUSY2b1m_6_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY2b1m_6_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY2b1m_6_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY2b1m_6_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY2b1m_6_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY2b1m_6_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY2b1m_6_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY2b1m_6_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY2b1m_6_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY2b1m_6_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY2b1m_6_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY2b1m_6_JER30Down.met = "goodMETsJER30Down"

analyzeSUSY3b1m_6_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY3b1m_6_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY3b1m_6_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY3b1m_6_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY3b1m_6_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY3b1m_6_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY3b1m_6_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY3b1m_6_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY3b1m_6_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY3b1m_6_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY3b1m_6_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY3b1m_6_JER30Down.met = "goodMETsJER30Down"


## configuration for electron channel
analyzeSUSY1b1e_4_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY1b1e_4_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY1b1e_4_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY1b1e_4_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY1b1e_4_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY1b1e_4_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY1b1e_4_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY1b1e_4_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY1b1e_4_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY1b1e_4_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY1b1e_4_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY1b1e_4_JER30Down.met = "goodMETsJER30Down"

analyzeSUSY1b1e_6_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY1b1e_6_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY1b1e_6_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY1b1e_6_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY1b1e_6_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY1b1e_6_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY1b1e_6_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY1b1e_6_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY1b1e_6_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY1b1e_6_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY1b1e_6_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY1b1e_6_JER30Down.met = "goodMETsJER30Down"

analyzeSUSY2b1e_6_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY2b1e_6_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY2b1e_6_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY2b1e_6_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY2b1e_6_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY2b1e_6_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY2b1e_6_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY2b1e_6_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY2b1e_6_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY2b1e_6_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY2b1e_6_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY2b1e_6_JER30Down.met = "goodMETsJER30Down"

analyzeSUSY3b1e_6_JER10Up.jets = "goodJetsJER10Up"
analyzeSUSY3b1e_6_JER10Up.met = "goodMETsJER10Up"
analyzeSUSY3b1e_6_JER20Up.jets = "goodJetsJER20Up"
analyzeSUSY3b1e_6_JER20Up.met = "goodMETsJER20Up"
analyzeSUSY3b1e_6_JER30Up.jets = "goodJetsJER30Up"
analyzeSUSY3b1e_6_JER30Up.met = "goodMETsJER30Up"

analyzeSUSY3b1e_6_JER10Down.jets = "goodJetsJER10Down"
analyzeSUSY3b1e_6_JER10Down.met = "goodMETsJER10Down"
analyzeSUSY3b1e_6_JER20Down.jets = "goodJetsJER20Down"
analyzeSUSY3b1e_6_JER20Down.met = "goodMETsJER20Down"
analyzeSUSY3b1e_6_JER30Down.jets = "goodJetsJER30Down"
analyzeSUSY3b1e_6_JER30Down.met = "goodMETsJER30Down"

# define sequnces

analyzeCorrelation1b1m_4 = cms.Sequence(analyzeSUSY1b1m_4_JER10Up *
                                         analyzeSUSY1b1m_4_JER20Up *
                                         analyzeSUSY1b1m_4_JER30Up *
                                         analyzeSUSY1b1m_4_JER10Down *
                                         analyzeSUSY1b1m_4_JER20Down *
                                         analyzeSUSY1b1m_4_JER30Down
                                         )

analyzeCorrelation1b1m_6 = cms.Sequence(analyzeSUSY1b1m_6_JER10Up *
                                         analyzeSUSY1b1m_6_JER20Up *
                                         analyzeSUSY1b1m_6_JER30Up *
                                         analyzeSUSY1b1m_6_JER10Down *
                                         analyzeSUSY1b1m_6_JER20Down *
                                         analyzeSUSY1b1m_6_JER30Down
                                         )

analyzeCorrelation2b1m_6 = cms.Sequence(analyzeSUSY2b1m_6_JER10Up *
                                         analyzeSUSY2b1m_6_JER20Up *
                                         analyzeSUSY2b1m_6_JER30Up *
                                         analyzeSUSY2b1m_6_JER10Down *
                                         analyzeSUSY2b1m_6_JER20Down *
                                         analyzeSUSY2b1m_6_JER30Down
                                         )

analyzeCorrelation3b1m_6 = cms.Sequence(analyzeSUSY3b1m_6_JER10Up *
                                         analyzeSUSY3b1m_6_JER20Up *
                                         analyzeSUSY3b1m_6_JER30Up *
                                         analyzeSUSY3b1m_6_JER10Down *
                                         analyzeSUSY3b1m_6_JER20Down *
                                         analyzeSUSY3b1m_6_JER30Down
                                         )


analyzeCorrelation1b1e_4 = cms.Sequence(analyzeSUSY1b1e_4_JER10Up *
                                         analyzeSUSY1b1e_4_JER20Up *
                                         analyzeSUSY1b1e_4_JER30Up *
                                         analyzeSUSY1b1e_4_JER10Down *
                                         analyzeSUSY1b1e_4_JER20Down *
                                         analyzeSUSY1b1e_4_JER30Down
                                         )

analyzeCorrelation1b1e_6 = cms.Sequence(analyzeSUSY1b1e_6_JER10Up *
                                         analyzeSUSY1b1e_6_JER20Up *
                                         analyzeSUSY1b1e_6_JER30Up *
                                         analyzeSUSY1b1e_6_JER10Down *
                                         analyzeSUSY1b1e_6_JER20Down *
                                         analyzeSUSY1b1e_6_JER30Down
                                         )

analyzeCorrelation2b1e_6 = cms.Sequence(analyzeSUSY2b1e_6_JER10Up *
                                         analyzeSUSY2b1e_6_JER20Up *
                                         analyzeSUSY2b1e_6_JER30Up *
                                         analyzeSUSY2b1e_6_JER10Down *
                                         analyzeSUSY2b1e_6_JER20Down *
                                         analyzeSUSY2b1e_6_JER30Down
                                         )

analyzeCorrelation3b1e_6 = cms.Sequence(analyzeSUSY3b1e_6_JER10Up *
                                         analyzeSUSY3b1e_6_JER20Up *
                                         analyzeSUSY3b1e_6_JER30Up *
                                         analyzeSUSY3b1e_6_JER10Down *
                                         analyzeSUSY3b1e_6_JER20Down *
                                         analyzeSUSY3b1e_6_JER30Down
                                         )
