from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.useTriggerEventWeight = True

analyzeSUSY1m_1 = analyzeSUSY.clone()
analyzeSUSY1m_2 = analyzeSUSY.clone()
analyzeSUSY1m_3 = analyzeSUSY.clone()
analyzeSUSY1m_4 = analyzeSUSY.clone()
analyzeSUSY1m_5 = analyzeSUSY.clone()
analyzeSUSY1m_6 = analyzeSUSY.clone()

analyzeSUSY1m_noCuts = analyzeSUSY.clone()
analyzeSUSY1m_preselection = analyzeSUSY.clone()
analyzeSUSY1m_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1m_jetSelection = analyzeSUSY.clone()
analyzeSUSY1m_oneTightJet = analyzeSUSY.clone()
analyzeSUSY1m_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY1m_metSelection = analyzeSUSY.clone()
analyzeSUSY1m_HTSelection = analyzeSUSY.clone()
analyzeSUSY1m_mTSelection = analyzeSUSY.clone()

analyzeSUSY1m_nminus1_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1m_nminus1_jetSelection = analyzeSUSY.clone()
analyzeSUSY1m_nminus1_oneTightJet = analyzeSUSY.clone()
analyzeSUSY1m_nminus1_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY1m_nminus1_metSelection = analyzeSUSY.clone()
analyzeSUSY1m_nminus1_HTSelection = analyzeSUSY.clone()

analyzeSUSY1e_noCuts = analyzeSUSY.clone()
analyzeSUSY1e_preselection = analyzeSUSY.clone()
analyzeSUSY1e_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1e_jetSelection = analyzeSUSY.clone()
analyzeSUSY1e_oneTightJet = analyzeSUSY.clone()
analyzeSUSY1e_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY1e_metSelection = analyzeSUSY.clone()
analyzeSUSY1e_HTSelection = analyzeSUSY.clone()
analyzeSUSY1e_mTSelection = analyzeSUSY.clone()

analyzeSUSY1e_nminus1_leptonSelection = analyzeSUSY.clone()
analyzeSUSY1e_nminus1_jetSelection = analyzeSUSY.clone()
analyzeSUSY1e_nminus1_oneTightJet = analyzeSUSY.clone()
analyzeSUSY1e_nminus1_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY1e_nminus1_metSelection = analyzeSUSY.clone()
analyzeSUSY1e_nminus1_HTSelection = analyzeSUSY.clone()

analyzeSUSY1e_1 = analyzeSUSY.clone()
analyzeSUSY1e_2 = analyzeSUSY.clone()
analyzeSUSY1e_3 = analyzeSUSY.clone()
analyzeSUSY1e_4 = analyzeSUSY.clone()
analyzeSUSY1e_5 = analyzeSUSY.clone()
analyzeSUSY1e_6 = analyzeSUSY.clone()

analyzeSUSY1b_1 = analyzeSUSY.clone()
analyzeSUSY1b_2 = analyzeSUSY.clone()
analyzeSUSY1b_3 = analyzeSUSY.clone()
analyzeSUSY1b_4 = analyzeSUSY.clone()
analyzeSUSY1b_5 = analyzeSUSY.clone()
analyzeSUSY1b_6 = analyzeSUSY.clone()

analyzeSUSY2b_1 = analyzeSUSY.clone()
analyzeSUSY2b_2 = analyzeSUSY.clone()
analyzeSUSY2b_3 = analyzeSUSY.clone()
analyzeSUSY2b_4 = analyzeSUSY.clone()
analyzeSUSY2b_5 = analyzeSUSY.clone()
analyzeSUSY2b_6 = analyzeSUSY.clone()

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
    
analyzeSUSY4b1m_1 = analyzeSUSY.clone()
analyzeSUSY4b1m_2 = analyzeSUSY.clone()
analyzeSUSY4b1m_3 = analyzeSUSY.clone()
analyzeSUSY4b1m_4 = analyzeSUSY.clone()
analyzeSUSY4b1m_5 = analyzeSUSY.clone()
analyzeSUSY4b1m_6 = analyzeSUSY.clone()

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

analyzeSUSY4b1e_1 = analyzeSUSY.clone()
analyzeSUSY4b1e_2 = analyzeSUSY.clone()
analyzeSUSY4b1e_3 = analyzeSUSY.clone()
analyzeSUSY4b1e_4 = analyzeSUSY.clone()
analyzeSUSY4b1e_5 = analyzeSUSY.clone()
analyzeSUSY4b1e_6 = analyzeSUSY.clone()

analyzeSUSY3b_1 = analyzeSUSY.clone()
analyzeSUSY3b_2 = analyzeSUSY.clone()
analyzeSUSY3b_3 = analyzeSUSY.clone()
analyzeSUSY3b_4 = analyzeSUSY.clone()
analyzeSUSY3b_5 = analyzeSUSY.clone()
analyzeSUSY3b_6 = analyzeSUSY.clone()

analyzeSUSY4b_1 = analyzeSUSY.clone()
analyzeSUSY4b_2 = analyzeSUSY.clone()
analyzeSUSY4b_3 = analyzeSUSY.clone()
analyzeSUSY4b_4 = analyzeSUSY.clone()
analyzeSUSY4b_5 = analyzeSUSY.clone()
analyzeSUSY4b_6 = analyzeSUSY.clone()

from SUSYAnalysis.SUSYAnalyzer.BjetsAnalyzer_cfi import *
analyzeBjets.jets = "goodJets"
analyzeBjets.muons = "goodMuons"
analyzeBjets.electrons = "goodElectrons"
analyzeBjets.looseTrackHighEffBjets = "looseTrackHighEffBjets"
analyzeBjets.mediumTrackHighEffBjets = "mediumTrackHighEffBjets"
analyzeBjets.tightTrackHighEffBjets = "tightTrackHighEffBjets"
analyzeBjets.looseTrackHighPurBjets = "looseTrackHighPurBjets"
analyzeBjets.mediumTrackHighPurBjets = "mediumTrackHighPurBjets"
analyzeBjets.tightTrackHighPurBjets = "tightTrackHighPurBjets"
analyzeBjets.useTriggerEventWeight = True

analyzeBjets1m_1 = analyzeBjets.clone()
analyzeBjets1m_2 = analyzeBjets.clone()
analyzeBjets1m_3 = analyzeBjets.clone()
analyzeBjets1m_4 = analyzeBjets.clone()
analyzeBjets1m_5 = analyzeBjets.clone()
analyzeBjets1m_6 = analyzeBjets.clone()

analyzeBjets1m_noCuts = analyzeBjets.clone()
analyzeBjets1m_preselection = analyzeBjets.clone()
analyzeBjets1m_leptonSelection = analyzeBjets.clone()
analyzeBjets1m_jetSelection = analyzeBjets.clone()
analyzeBjets1m_oneTightJet = analyzeBjets.clone()
analyzeBjets1m_twoMediumJets = analyzeBjets.clone()
analyzeBjets1m_metSelection = analyzeBjets.clone()
analyzeBjets1m_HTSelection = analyzeBjets.clone()
analyzeBjets1m_mTSelection = analyzeBjets.clone()

analyzeBjets1m_nminus1_leptonSelection = analyzeBjets.clone()
analyzeBjets1m_nminus1_jetSelection = analyzeBjets.clone()
analyzeBjets1m_nminus1_oneTightJet = analyzeBjets.clone()
analyzeBjets1m_nminus1_twoMediumJets = analyzeBjets.clone()
analyzeBjets1m_nminus1_metSelection = analyzeBjets.clone()
analyzeBjets1m_nminus1_HTSelection = analyzeBjets.clone()

analyzeBjets1e_noCuts = analyzeBjets.clone()
analyzeBjets1e_preselection = analyzeBjets.clone()
analyzeBjets1e_leptonSelection = analyzeBjets.clone()
analyzeBjets1e_jetSelection = analyzeBjets.clone()
analyzeBjets1e_oneTightJet = analyzeBjets.clone()
analyzeBjets1e_twoMediumJets = analyzeBjets.clone()
analyzeBjets1e_metSelection = analyzeBjets.clone()
analyzeBjets1e_HTSelection = analyzeBjets.clone()
analyzeBjets1e_mTSelection = analyzeBjets.clone()

analyzeBjets1e_nminus1_leptonSelection = analyzeBjets.clone()
analyzeBjets1e_nminus1_jetSelection = analyzeBjets.clone()
analyzeBjets1e_nminus1_oneTightJet = analyzeBjets.clone()
analyzeBjets1e_nminus1_twoMediumJets = analyzeBjets.clone()
analyzeBjets1e_nminus1_metSelection = analyzeBjets.clone()
analyzeBjets1e_nminus1_HTSelection = analyzeBjets.clone()

analyzeBjets1e_1 = analyzeBjets.clone()
analyzeBjets1e_2 = analyzeBjets.clone()
analyzeBjets1e_3 = analyzeBjets.clone()
analyzeBjets1e_4 = analyzeBjets.clone()
analyzeBjets1e_5 = analyzeBjets.clone()
analyzeBjets1e_6 = analyzeBjets.clone()

analyzeBjets1b_1 = analyzeBjets.clone()
analyzeBjets1b_2 = analyzeBjets.clone()
analyzeBjets1b_3 = analyzeBjets.clone()
analyzeBjets1b_4 = analyzeBjets.clone()
analyzeBjets1b_5 = analyzeBjets.clone()
analyzeBjets1b_6 = analyzeBjets.clone()

analyzeBjets2b_1 = analyzeBjets.clone()
analyzeBjets2b_2 = analyzeBjets.clone()
analyzeBjets2b_3 = analyzeBjets.clone()
analyzeBjets2b_4 = analyzeBjets.clone()
analyzeBjets2b_5 = analyzeBjets.clone()
analyzeBjets2b_6 = analyzeBjets.clone()

analyzeBjets1b1m_1 = analyzeBjets.clone()
analyzeBjets1b1m_2 = analyzeBjets.clone()
analyzeBjets1b1m_3 = analyzeBjets.clone()
analyzeBjets1b1m_4 = analyzeBjets.clone()
analyzeBjets1b1m_5 = analyzeBjets.clone()
analyzeBjets1b1m_6 = analyzeBjets.clone()

analyzeBjets2b1m_1 = analyzeBjets.clone()
analyzeBjets2b1m_2 = analyzeBjets.clone()
analyzeBjets2b1m_3 = analyzeBjets.clone()
analyzeBjets2b1m_4 = analyzeBjets.clone()
analyzeBjets2b1m_5 = analyzeBjets.clone()
analyzeBjets2b1m_6 = analyzeBjets.clone()
    
analyzeBjets3b1m_1 = analyzeBjets.clone()
analyzeBjets3b1m_2 = analyzeBjets.clone()
analyzeBjets3b1m_3 = analyzeBjets.clone()
analyzeBjets3b1m_4 = analyzeBjets.clone()
analyzeBjets3b1m_5 = analyzeBjets.clone()
analyzeBjets3b1m_6 = analyzeBjets.clone()

analyzeBjets4b1m_1 = analyzeBjets.clone()
analyzeBjets4b1m_2 = analyzeBjets.clone()
analyzeBjets4b1m_3 = analyzeBjets.clone()
analyzeBjets4b1m_4 = analyzeBjets.clone()
analyzeBjets4b1m_5 = analyzeBjets.clone()
analyzeBjets4b1m_6 = analyzeBjets.clone()

analyzeBjets1b1e_1 = analyzeBjets.clone()
analyzeBjets1b1e_2 = analyzeBjets.clone()
analyzeBjets1b1e_3 = analyzeBjets.clone()
analyzeBjets1b1e_4 = analyzeBjets.clone()
analyzeBjets1b1e_5 = analyzeBjets.clone()
analyzeBjets1b1e_6 = analyzeBjets.clone()

analyzeBjets2b1e_1 = analyzeBjets.clone()
analyzeBjets2b1e_2 = analyzeBjets.clone()
analyzeBjets2b1e_3 = analyzeBjets.clone()
analyzeBjets2b1e_4 = analyzeBjets.clone()
analyzeBjets2b1e_5 = analyzeBjets.clone()
analyzeBjets2b1e_6 = analyzeBjets.clone()
    
analyzeBjets3b1e_1 = analyzeBjets.clone()
analyzeBjets3b1e_2 = analyzeBjets.clone()
analyzeBjets3b1e_3 = analyzeBjets.clone()
analyzeBjets3b1e_4 = analyzeBjets.clone()
analyzeBjets3b1e_5 = analyzeBjets.clone()
analyzeBjets3b1e_6 = analyzeBjets.clone()

analyzeBjets4b1e_1 = analyzeBjets.clone()
analyzeBjets4b1e_2 = analyzeBjets.clone()
analyzeBjets4b1e_3 = analyzeBjets.clone()
analyzeBjets4b1e_4 = analyzeBjets.clone()
analyzeBjets4b1e_5 = analyzeBjets.clone()
analyzeBjets4b1e_6 = analyzeBjets.clone()

analyzeBjets3b_1 = analyzeBjets.clone()
analyzeBjets3b_2 = analyzeBjets.clone()
analyzeBjets3b_3 = analyzeBjets.clone()
analyzeBjets3b_4 = analyzeBjets.clone()
analyzeBjets3b_5 = analyzeBjets.clone()
analyzeBjets3b_6 = analyzeBjets.clone()

analyzeBjets4b_1 = analyzeBjets.clone()
analyzeBjets4b_2 = analyzeBjets.clone()
analyzeBjets4b_3 = analyzeBjets.clone()
analyzeBjets4b_4 = analyzeBjets.clone()
analyzeBjets4b_5 = analyzeBjets.clone()
analyzeBjets4b_6 = analyzeBjets.clone()
 
from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import *

analyzeSUSYGenEvt.jets = "goodJets"
analyzeSUSYGenEvt.bjets = "mediumTrackHighPurBjets"
analyzeSUSYGenEvt.matchedbjets = "matchedBjets"
analyzeSUSYGenEvt.matchedqjets = "matchedLightJets"
analyzeSUSYGenEvt.matchedmuons = "goodMuons"
analyzeSUSYGenEvt.matchedelectrons = "goodElectrons"

analyzeSUSYGenEvt1m_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1m_noCuts = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_preselection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_leptonSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_jetSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_HTSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_mTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1m_nminus1_leptonSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_nminus1_jetSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_nminus1_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_nminus1_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_nminus1_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1m_nminus1_HTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1e_noCuts = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_preselection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_leptonSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_jetSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_HTSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_mTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1e_nminus1_leptonSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_nminus1_jetSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_nminus1_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_nminus1_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_nminus1_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_nminus1_HTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1e_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1e_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt2b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1b1m_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1m_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1m_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1m_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1m_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1m_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt2b1m_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1m_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1m_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1m_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1m_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1m_6 = analyzeSUSYGenEvt.clone()
    
analyzeSUSYGenEvt3b1m_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1m_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1m_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1m_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1m_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1m_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt4b1m_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1m_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1m_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1m_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1m_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1m_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1b1e_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1e_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1e_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1e_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1e_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1e_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt2b1e_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1e_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1e_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1e_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1e_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1e_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt3b1e_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1e_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1e_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1e_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1e_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1e_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt4b1e_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1e_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1e_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1e_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1e_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1e_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt3b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_6 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt4b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_6 = analyzeSUSYGenEvt.clone()

from TopAnalysis.TopAnalyzer.BTags_cfi import *

analyzeBTags.src = "goodJets"

analyzeBTags1m_1 = analyzeBTags.clone()
analyzeBTags1m_2 = analyzeBTags.clone()
analyzeBTags1m_3 = analyzeBTags.clone()
analyzeBTags1m_4 = analyzeBTags.clone()
analyzeBTags1m_5 = analyzeBTags.clone()
analyzeBTags1m_6 = analyzeBTags.clone()

analyzeBTags1m_noCuts = analyzeBTags.clone()
analyzeBTags1m_preselection = analyzeBTags.clone()
analyzeBTags1m_leptonSelection = analyzeBTags.clone()
analyzeBTags1m_jetSelection = analyzeBTags.clone()
analyzeBTags1m_oneTightJet = analyzeBTags.clone()
analyzeBTags1m_twoMediumJets = analyzeBTags.clone()
analyzeBTags1m_metSelection = analyzeBTags.clone()
analyzeBTags1m_HTSelection = analyzeBTags.clone()
analyzeBTags1m_mTSelection = analyzeBTags.clone()

analyzeBTags1m_nminus1_leptonSelection = analyzeBTags.clone()
analyzeBTags1m_nminus1_jetSelection = analyzeBTags.clone()
analyzeBTags1m_nminus1_oneTightJet = analyzeBTags.clone()
analyzeBTags1m_nminus1_twoMediumJets = analyzeBTags.clone()
analyzeBTags1m_nminus1_metSelection = analyzeBTags.clone()
analyzeBTags1m_nminus1_HTSelection = analyzeBTags.clone()

analyzeBTags1e_noCuts = analyzeBTags.clone()
analyzeBTags1e_preselection = analyzeBTags.clone()
analyzeBTags1e_leptonSelection = analyzeBTags.clone()
analyzeBTags1e_jetSelection = analyzeBTags.clone()
analyzeBTags1e_oneTightJet = analyzeBTags.clone()
analyzeBTags1e_twoMediumJets = analyzeBTags.clone()
analyzeBTags1e_metSelection = analyzeBTags.clone()
analyzeBTags1e_HTSelection = analyzeBTags.clone()
analyzeBTags1e_mTSelection = analyzeBTags.clone()

analyzeBTags1e_nminus1_leptonSelection = analyzeBTags.clone()
analyzeBTags1e_nminus1_jetSelection = analyzeBTags.clone()
analyzeBTags1e_nminus1_oneTightJet = analyzeBTags.clone()
analyzeBTags1e_nminus1_twoMediumJets = analyzeBTags.clone()
analyzeBTags1e_nminus1_metSelection = analyzeBTags.clone()
analyzeBTags1e_nminus1_HTSelection = analyzeBTags.clone()

analyzeBTags1e_1 = analyzeBTags.clone()
analyzeBTags1e_2 = analyzeBTags.clone()
analyzeBTags1e_3 = analyzeBTags.clone()
analyzeBTags1e_4 = analyzeBTags.clone()
analyzeBTags1e_5 = analyzeBTags.clone()
analyzeBTags1e_6 = analyzeBTags.clone()

analyzeBTags1b_1 = analyzeBTags.clone()
analyzeBTags1b_2 = analyzeBTags.clone()
analyzeBTags1b_3 = analyzeBTags.clone()
analyzeBTags1b_4 = analyzeBTags.clone()
analyzeBTags1b_5 = analyzeBTags.clone()
analyzeBTags1b_6 = analyzeBTags.clone()

analyzeBTags2b_1 = analyzeBTags.clone()
analyzeBTags2b_2 = analyzeBTags.clone()
analyzeBTags2b_3 = analyzeBTags.clone()
analyzeBTags2b_4 = analyzeBTags.clone()
analyzeBTags2b_5 = analyzeBTags.clone()
analyzeBTags2b_6 = analyzeBTags.clone()

analyzeBTags1b1m_1 = analyzeBTags.clone()
analyzeBTags1b1m_2 = analyzeBTags.clone()
analyzeBTags1b1m_3 = analyzeBTags.clone()
analyzeBTags1b1m_4 = analyzeBTags.clone()
analyzeBTags1b1m_5 = analyzeBTags.clone()
analyzeBTags1b1m_6 = analyzeBTags.clone()

analyzeBTags2b1m_1 = analyzeBTags.clone()
analyzeBTags2b1m_2 = analyzeBTags.clone()
analyzeBTags2b1m_3 = analyzeBTags.clone()
analyzeBTags2b1m_4 = analyzeBTags.clone()
analyzeBTags2b1m_5 = analyzeBTags.clone()
analyzeBTags2b1m_6 = analyzeBTags.clone()

analyzeBTags3b1m_1 = analyzeBTags.clone()
analyzeBTags3b1m_2 = analyzeBTags.clone()
analyzeBTags3b1m_3 = analyzeBTags.clone()
analyzeBTags3b1m_4 = analyzeBTags.clone()
analyzeBTags3b1m_5 = analyzeBTags.clone()
analyzeBTags3b1m_6 = analyzeBTags.clone()
    
analyzeBTags4b1m_1 = analyzeBTags.clone()
analyzeBTags4b1m_2 = analyzeBTags.clone()
analyzeBTags4b1m_3 = analyzeBTags.clone()
analyzeBTags4b1m_4 = analyzeBTags.clone()
analyzeBTags4b1m_5 = analyzeBTags.clone()
analyzeBTags4b1m_6 = analyzeBTags.clone()

analyzeBTags1b1e_1 = analyzeBTags.clone()
analyzeBTags1b1e_2 = analyzeBTags.clone()
analyzeBTags1b1e_3 = analyzeBTags.clone()
analyzeBTags1b1e_4 = analyzeBTags.clone()
analyzeBTags1b1e_5 = analyzeBTags.clone()
analyzeBTags1b1e_6 = analyzeBTags.clone()

analyzeBTags2b1e_1 = analyzeBTags.clone()
analyzeBTags2b1e_2 = analyzeBTags.clone()
analyzeBTags2b1e_3 = analyzeBTags.clone()
analyzeBTags2b1e_4 = analyzeBTags.clone()
analyzeBTags2b1e_5 = analyzeBTags.clone()
analyzeBTags2b1e_6 = analyzeBTags.clone()

analyzeBTags3b1e_1 = analyzeBTags.clone()
analyzeBTags3b1e_2 = analyzeBTags.clone()
analyzeBTags3b1e_3 = analyzeBTags.clone()
analyzeBTags3b1e_4 = analyzeBTags.clone()
analyzeBTags3b1e_5 = analyzeBTags.clone()
analyzeBTags3b1e_6 = analyzeBTags.clone()

analyzeBTags4b1e_1 = analyzeBTags.clone()
analyzeBTags4b1e_2 = analyzeBTags.clone()
analyzeBTags4b1e_3 = analyzeBTags.clone()
analyzeBTags4b1e_4 = analyzeBTags.clone()
analyzeBTags4b1e_5 = analyzeBTags.clone()
analyzeBTags4b1e_6 = analyzeBTags.clone()

analyzeBTags3b_1 = analyzeBTags.clone()
analyzeBTags3b_2 = analyzeBTags.clone()
analyzeBTags3b_3 = analyzeBTags.clone()
analyzeBTags3b_4 = analyzeBTags.clone()
analyzeBTags3b_5 = analyzeBTags.clone()
analyzeBTags3b_6 = analyzeBTags.clone()

analyzeBTags4b_1 = analyzeBTags.clone()
analyzeBTags4b_2 = analyzeBTags.clone()
analyzeBTags4b_3 = analyzeBTags.clone()
analyzeBTags4b_4 = analyzeBTags.clone()
analyzeBTags4b_5 = analyzeBTags.clone()
analyzeBTags4b_6 = analyzeBTags.clone()

## 1 muon
analyzeSUSYBjets1m_noCuts = cms.Sequence(analyzeSUSY1m_noCuts *
                                         analyzeBjets1m_noCuts #*
                                         #analyzeSUSYGenEvt1m_noCuts *
                                         #analyzeBTags1m_noCuts
                                         )
analyzeSUSYBjets1m_preselection = cms.Sequence(analyzeSUSY1m_preselection *
                                               analyzeBjets1m_preselection #*
                                               #analyzeSUSYGenEvt1m_preselection #*
                                               #analyzeBTags1m_preselection
                                               )
analyzeSUSYBjets1m_leptonSelection = cms.Sequence(analyzeSUSY1m_leptonSelection *
                                                  analyzeBjets1m_leptonSelection #*
                                                  #analyzeSUSYGenEvt1m_leptonSelection *
                                                  #analyzeBTags1m_leptonSelection
                                                  )
analyzeSUSYBjets1m_jetSelection = cms.Sequence(analyzeSUSY1m_jetSelection *
                                               analyzeBjets1m_jetSelection #*
                                               #analyzeSUSYGenEvt1m_jetSelection *
                                               #analyzeBTags1m_jetSelection
                                               )
analyzeSUSYBjets1m_oneTightJet = cms.Sequence(analyzeSUSY1m_oneTightJet *
                                              analyzeBjets1m_oneTightJet #*
                                              #analyzeSUSYGenEvt1m_oneTightJet *
                                              #analyzeBTags1m_oneTightJet
                                              )
analyzeSUSYBjets1m_twoMediumJets = cms.Sequence(analyzeSUSY1m_twoMediumJets *
                                                analyzeBjets1m_twoMediumJets #*
                                                #analyzeSUSYGenEvt1m_twoMediumJets *
                                                #analyzeBTags1m_twoMediumJets
                                                )
analyzeSUSYBjets1m_metSelection = cms.Sequence(analyzeSUSY1m_metSelection *
                                               analyzeBjets1m_metSelection #*
                                               #analyzeSUSYGenEvt1m_metSelection *
                                               #analyzeBTags1m_metSelection
                                               )
analyzeSUSYBjets1m_HTSelection = cms.Sequence(analyzeSUSY1m_HTSelection *
                                              analyzeBjets1m_HTSelection #*
                                              #analyzeSUSYGenEvt1m_HTSelection *
                                              #analyzeBTags1m_HTSelection
                                              )
analyzeSUSYBjets1m_mTSelection = cms.Sequence(analyzeSUSY1m_mTSelection *
                                              analyzeBjets1m_mTSelection #*
                                              #analyzeSUSYGenEvt1m_mTSelection *
                                              #analyzeBTags1m_mTSelection
                                              )


## 1 electron
analyzeSUSYBjets1e_noCuts = cms.Sequence(analyzeSUSY1e_noCuts *
                                         analyzeBjets1e_noCuts #*
                                         #analyzeSUSYGenEvt1e_noCuts *
                                         #analyzeBTags1e_noCuts
                                         )
analyzeSUSYBjets1e_preselection = cms.Sequence(analyzeSUSY1e_preselection *
                                               analyzeBjets1e_preselection #*
                                               #analyzeSUSYGenEvt1e_preselection *
                                               #analyzeBTags1e_preselection
                                               )
analyzeSUSYBjets1e_leptonSelection = cms.Sequence(analyzeSUSY1e_leptonSelection *
                                                  analyzeBjets1e_leptonSelection #*
                                                  #analyzeSUSYGenEvt1e_leptonSelection *
                                                  #analyzeBTags1e_leptonSelection
                                                  )
analyzeSUSYBjets1e_jetSelection = cms.Sequence(analyzeSUSY1e_jetSelection *
                                               analyzeBjets1e_jetSelection #*
                                               #analyzeSUSYGenEvt1e_jetSelection *
                                               #analyzeBTags1e_jetSelection
                                               )
analyzeSUSYBjets1e_oneTightJet = cms.Sequence(analyzeSUSY1e_oneTightJet *
                                              analyzeBjets1e_oneTightJet #*
                                              #analyzeSUSYGenEvt1e_oneTightJet *
                                              #analyzeBTags1e_oneTightJet
                                              )
analyzeSUSYBjets1e_twoMediumJets = cms.Sequence(analyzeSUSY1e_twoMediumJets *
                                                analyzeBjets1e_twoMediumJets #*
                                                #analyzeSUSYGenEvt1e_twoMediumJets *
                                                #analyzeBTags1e_twoMediumJets
                                                )
analyzeSUSYBjets1e_metSelection = cms.Sequence(analyzeSUSY1e_metSelection *
                                               analyzeBjets1e_metSelection #*
                                               #analyzeSUSYGenEvt1e_metSelection *
                                               #analyzeBTags1e_metSelection
                                               )
analyzeSUSYBjets1e_HTSelection = cms.Sequence(analyzeSUSY1e_HTSelection *
                                              analyzeBjets1e_HTSelection #*
                                              #analyzeSUSYGenEvt1e_HTSelection *
                                              #analyzeBTags1e_HTSelection
                                              )
analyzeSUSYBjets1e_mTSelection = cms.Sequence(analyzeSUSY1e_mTSelection *
                                              analyzeBjets1e_mTSelection #*
                                              #analyzeSUSYGenEvt1e_mTSelection *
                                              #analyzeBTags1e_mTSelection
                                              )

## 1 muon n-1
analyzeSUSYBjets1m_nminus1_leptonSelection = cms.Sequence(analyzeSUSY1m_nminus1_leptonSelection *
                                                          analyzeBjets1m_nminus1_leptonSelection #*
                                                          #analyzeSUSYGenEvt1m_nminus1_leptonSelection *
                                                          #analyzeBTags1m_nminus1_leptonSelection
                                                          )
analyzeSUSYBjets1m_nminus1_jetSelection = cms.Sequence(analyzeSUSY1m_nminus1_jetSelection *
                                                       analyzeBjets1m_nminus1_jetSelection #*
                                                       #analyzeSUSYGenEvt1m_nminus1_jetSelection *
                                                       #analyzeBTags1m_nminus1_jetSelection
                                                       )
analyzeSUSYBjets1m_nminus1_oneTightJet = cms.Sequence(analyzeSUSY1m_nminus1_oneTightJet *
                                                      analyzeBjets1m_nminus1_oneTightJet #*
                                                      #analyzeSUSYGenEvt1m_nminus1_oneTightJet *
                                                      #analyzeBTags1m_nminus1_oneTightJet
                                                      )
analyzeSUSYBjets1m_nminus1_twoMediumJets = cms.Sequence(analyzeSUSY1m_nminus1_twoMediumJets *
                                                        analyzeBjets1m_nminus1_twoMediumJets #*
                                                        #analyzeSUSYGenEvt1m_nminus1_twoMediumJets *
                                                        #analyzeBTags1m_nminus1_twoMediumJets
                                                        )
analyzeSUSYBjets1m_nminus1_metSelection = cms.Sequence(analyzeSUSY1m_nminus1_metSelection *
                                                       analyzeBjets1m_nminus1_metSelection #*
                                                       #analyzeSUSYGenEvt1m_nminus1_metSelection *
                                                       #analyzeBTags1m_nminus1_metSelection
                                                       )
analyzeSUSYBjets1m_nminus1_HTSelection = cms.Sequence(analyzeSUSY1m_nminus1_HTSelection *
                                                      analyzeBjets1m_nminus1_HTSelection #*
                                                      #analyzeSUSYGenEvt1m_nminus1_HTSelection *
                                                      #analyzeBTags1m_nminus1_HTSelection
                                                      )

## 1 electron n-1
analyzeSUSYBjets1e_nminus1_leptonSelection = cms.Sequence(analyzeSUSY1e_nminus1_leptonSelection *
                                                          analyzeBjets1e_nminus1_leptonSelection #*
                                                          #analyzeSUSYGenEvt1e_nminus1_leptonSelection *
                                                          #analyzeBTags1e_nminus1_leptonSelection
                                                          )
analyzeSUSYBjets1e_nminus1_jetSelection = cms.Sequence(analyzeSUSY1e_nminus1_jetSelection *
                                                       analyzeBjets1e_nminus1_jetSelection #*
                                                       #analyzeSUSYGenEvt1e_nminus1_jetSelection *
                                                       #analyzeBTags1e_nminus1_jetSelection
                                                       )
analyzeSUSYBjets1e_nminus1_oneTightJet = cms.Sequence(analyzeSUSY1e_nminus1_oneTightJet *
                                                      analyzeBjets1e_nminus1_oneTightJet #*
                                                      #analyzeSUSYGenEvt1e_nminus1_oneTightJet *
                                                      #analyzeBTags1e_nminus1_oneTightJet
                                                      )
analyzeSUSYBjets1e_nminus1_twoMediumJets = cms.Sequence(analyzeSUSY1e_nminus1_twoMediumJets *
                                                        analyzeBjets1e_nminus1_twoMediumJets #*
                                                        #analyzeSUSYGenEvt1e_nminus1_twoMediumJets #*
                                                        #analyzeBTags1e_nminus1_twoMediumJets
                                                        )
analyzeSUSYBjets1e_nminus1_metSelection = cms.Sequence(analyzeSUSY1e_nminus1_metSelection *
                                                       analyzeBjets1e_nminus1_metSelection #*
                                                       #analyzeSUSYGenEvt1e_nminus1_metSelection #*
                                                       #analyzeBTags1e_nminus1_metSelection
                                                       )
analyzeSUSYBjets1e_nminus1_HTSelection = cms.Sequence(analyzeSUSY1e_nminus1_HTSelection *
                                                      analyzeBjets1e_nminus1_HTSelection #*
                                                      #analyzeSUSYGenEvt1e_nminus1_HTSelection *
                                                      #analyzeBTags1e_nminus1_HTSelection
                                                      )
## 1 muon
analyzeSUSYBjets1m_1 = cms.Sequence(analyzeSUSY1m_1 *
                                    analyzeBjets1m_1 #*
                                    #analyzeSUSYGenEvt1m_1 *
                                    #analyzeBTags1m_1
                                    )
analyzeSUSYBjets1m_2 = cms.Sequence(analyzeSUSY1m_2 *
                                    analyzeBjets1m_2 #*
                                    #analyzeSUSYGenEvt1m_2 *
                                    #analyzeBTags1m_2
                                    )
analyzeSUSYBjets1m_3 = cms.Sequence(analyzeSUSY1m_3 *
                                    analyzeBjets1m_3 #*
                                    #analyzeSUSYGenEvt1m_3 *
                                    #analyzeBTags1m_3
                                    )
analyzeSUSYBjets1m_4 = cms.Sequence(analyzeSUSY1m_4 *
                                    analyzeBjets1m_4 #*
                                    #analyzeSUSYGenEvt1m_4 *
                                    #analyzeBTags1m_4
                                    )
analyzeSUSYBjets1m_5 = cms.Sequence(analyzeSUSY1m_5 *
                                    analyzeBjets1m_5 #*
                                    #analyzeSUSYGenEvt1m_5 *
                                    #analyzeBTags1m_5
                                    )
analyzeSUSYBjets1m_6 = cms.Sequence(analyzeSUSY1m_6 *
                                    analyzeBjets1m_6 #*
                                    #analyzeSUSYGenEvt1m_6 *
                                    #analyzeBTags1m_6
                                    )

## 1 electron
analyzeSUSYBjets1e_1 = cms.Sequence(analyzeSUSY1e_1 *
                                    analyzeBjets1e_1 #*
                                    #analyzeSUSYGenEvt1e_1 *
                                    #analyzeBTags1e_1
                                    )
analyzeSUSYBjets1e_2 = cms.Sequence(analyzeSUSY1e_2 *
                                    analyzeBjets1e_2 #*
                                    #analyzeSUSYGenEvt1e_2 *
                                    #analyzeBTags1e_2
                                    )
analyzeSUSYBjets1e_3 = cms.Sequence(analyzeSUSY1e_3 *
                                    analyzeBjets1e_3 #*
                                    #analyzeSUSYGenEvt1e_3 *
                                    #analyzeBTags1e_3
                                    )
analyzeSUSYBjets1e_4 = cms.Sequence(analyzeSUSY1e_4 *
                                    analyzeBjets1e_4 #*
                                    #analyzeSUSYGenEvt1e_4 *
                                    #analyzeBTags1e_4
                                    )
analyzeSUSYBjets1e_5 = cms.Sequence(analyzeSUSY1e_5 *
                                    analyzeBjets1e_5 #*
                                    #analyzeSUSYGenEvt1e_5 *
                                    #analyzeBTags1e_5
                                    )
analyzeSUSYBjets1e_6 = cms.Sequence(analyzeSUSY1e_6 *
                                    analyzeBjets1e_6 #*
                                    #analyzeSUSYGenEvt1e_6 *
                                    #analyzeBTags1e_6
                                    )

## 1 bjet
analyzeSUSYBjets1b_1 = cms.Sequence(analyzeSUSY1b_1 *
                                    analyzeBjets1b_1 #*
                                    #analyzeSUSYGenEvt1b_1 *
                                    #analyzeBTags1b_1
                                    )
analyzeSUSYBjets1b_2 = cms.Sequence(analyzeSUSY1b_2 *
                                    analyzeBjets1b_2 #*
                                    #analyzeSUSYGenEvt1b_2 *
                                    #analyzeBTags1b_2
                                    )
analyzeSUSYBjets1b_3 = cms.Sequence(analyzeSUSY1b_3 *
                                    analyzeBjets1b_3 #*
                                    #analyzeSUSYGenEvt1b_3 *
                                    #analyzeBTags1b_3
                                    )
analyzeSUSYBjets1b_4 = cms.Sequence(analyzeSUSY1b_4 *
                                    analyzeBjets1b_4 #*
                                    #analyzeSUSYGenEvt1b_4 *
                                    #analyzeBTags1b_4
                                    )
analyzeSUSYBjets1b_5 = cms.Sequence(analyzeSUSY1b_5 *
                                    analyzeBjets1b_5 #*
                                    #analyzeSUSYGenEvt1b_5 *
                                    #analyzeBTags1b_5
                                    )
analyzeSUSYBjets1b_6 = cms.Sequence(analyzeSUSY1b_6 *
                                    analyzeBjets1b_6 #*
                                    #analyzeSUSYGenEvt1b_6 *
                                    #analyzeBTags1b_6
                                    )

## 2 bjets
analyzeSUSYBjets2b_1 = cms.Sequence(analyzeSUSY2b_1 *
                                    analyzeBjets2b_1 #*
                                    #analyzeSUSYGenEvt2b_1 *
                                    #analyzeBTags2b_1
                                    )
analyzeSUSYBjets2b_2 = cms.Sequence(analyzeSUSY2b_2 *
                                    analyzeBjets2b_2 #*
                                    #analyzeSUSYGenEvt2b_2 *
                                    #analyzeBTags2b_2
                                    )
analyzeSUSYBjets2b_3 = cms.Sequence(analyzeSUSY2b_3 *
                                    analyzeBjets2b_3 #*
                                    #analyzeSUSYGenEvt2b_3 *
                                    #analyzeBTags2b_3
                                    )
analyzeSUSYBjets2b_4 = cms.Sequence(analyzeSUSY2b_4 *
                                    analyzeBjets2b_4 #*
                                    #analyzeSUSYGenEvt2b_4 *
                                    #analyzeBTags2b_4
                                    )
analyzeSUSYBjets2b_5 = cms.Sequence(analyzeSUSY2b_5 * 
                                    analyzeBjets2b_5 #*
                                    #analyzeSUSYGenEvt2b_5 *
                                    #analyzeBTags2b_5
                                    )
analyzeSUSYBjets2b_6 = cms.Sequence(analyzeSUSY2b_6 *
                                    analyzeBjets2b_6 #*
                                    #analyzeSUSYGenEvt2b_6 *
                                    #analyzeBTags2b_6
                                    )

## 1 bjet, 1 muon
analyzeSUSYBjets1b1m_1 = cms.Sequence(analyzeSUSY1b1m_1 *
                                      analyzeBjets1b1m_1 #*
                                      #analyzeSUSYGenEvt1b1m_1 *
                                      #analyzeBTags1b1m_1
                                      )
analyzeSUSYBjets1b1m_2 = cms.Sequence(analyzeSUSY1b1m_2 *
                                      analyzeBjets1b1m_2 #*
                                      #analyzeSUSYGenEvt1b1m_2 *
                                      #analyzeBTags1b1m_2
                                      )
analyzeSUSYBjets1b1m_3 = cms.Sequence(analyzeSUSY1b1m_3 *
                                      analyzeBjets1b1m_3 #*
                                      #analyzeSUSYGenEvt1b1m_3 *
                                      #analyzeBTags1b1m_3
                                      )
analyzeSUSYBjets1b1m_4 = cms.Sequence(analyzeSUSY1b1m_4 *
                                      analyzeBjets1b1m_4 #*
                                      #analyzeSUSYGenEvt1b1m_4 *
                                      #analyzeBTags1b1m_4
                                      )
analyzeSUSYBjets1b1m_5 = cms.Sequence(analyzeSUSY1b1m_5 *
                                      analyzeBjets1b1m_5 #*
                                      #analyzeSUSYGenEvt1b1m_5 *
                                      #analyzeBTags1b1m_5
                                      )
analyzeSUSYBjets1b1m_6 = cms.Sequence(analyzeSUSY1b1m_6 *
                                      analyzeBjets1b1m_6 #*
                                      #analyzeSUSYGenEvt1b1m_6 *
                                      #analyzeBTags1b1m_6
                                      )

## 2 bjets, 1 muon
analyzeSUSYBjets2b1m_1 = cms.Sequence(analyzeSUSY2b1m_1 *
                                      analyzeBjets2b1m_1 #*
                                      #analyzeSUSYGenEvt2b1m_1 *
                                      #analyzeBTags2b1m_1
                                      )
analyzeSUSYBjets2b1m_2 = cms.Sequence(analyzeSUSY2b1m_2 *
                                      analyzeBjets2b1m_2 #*
                                      #analyzeSUSYGenEvt2b1m_2 *
                                      #analyzeBTags2b1m_2
                                      )
analyzeSUSYBjets2b1m_3 = cms.Sequence(analyzeSUSY2b1m_3 *
                                      analyzeBjets2b1m_3 #*
                                      #analyzeSUSYGenEvt2b1m_3 *
                                      #analyzeBTags2b1m_3
                                      )
analyzeSUSYBjets2b1m_4 = cms.Sequence(analyzeSUSY2b1m_4 *
                                      analyzeBjets2b1m_4 #*
                                      #analyzeSUSYGenEvt2b1m_4 *
                                      #analyzeBTags2b1m_4
                                      )
analyzeSUSYBjets2b1m_5 = cms.Sequence(analyzeSUSY2b1m_5 *
                                      analyzeBjets2b1m_5 #*
                                      #analyzeSUSYGenEvt2b1m_5 *
                                      #analyzeBTags2b1m_5
                                      )
analyzeSUSYBjets2b1m_6 = cms.Sequence(analyzeSUSY2b1m_6 *
                                      analyzeBjets2b1m_6 #*
                                      #analyzeSUSYGenEvt2b1m_6 *
                                      #analyzeBTags2b1m_6
                                      )

## 3 bjets, 1 muon
analyzeSUSYBjets3b1m_1 = cms.Sequence(analyzeSUSY3b1m_1 *
                                      analyzeBjets3b1m_1 #*
                                      #analyzeSUSYGenEvt3b1m_1 *
                                      #analyzeBTags3b1m_1
                                      )
analyzeSUSYBjets3b1m_2 = cms.Sequence(analyzeSUSY3b1m_2 *
                                      analyzeBjets3b1m_2 #*
                                      #analyzeSUSYGenEvt3b1m_2 *
                                      #analyzeBTags3b1m_2
                                      )
analyzeSUSYBjets3b1m_3 = cms.Sequence(analyzeSUSY3b1m_3 *
                                      analyzeBjets3b1m_3 #*
                                      #analyzeSUSYGenEvt3b1m_3 *
                                      #analyzeBTags3b1m_3
                                      )
analyzeSUSYBjets3b1m_4 = cms.Sequence(analyzeSUSY3b1m_4 *
                                      analyzeBjets3b1m_4 #*
                                      #analyzeSUSYGenEvt3b1m_4 *
                                      #analyzeBTags3b1m_4
                                      )
analyzeSUSYBjets3b1m_5 = cms.Sequence(analyzeSUSY3b1m_5 *
                                      analyzeBjets3b1m_5 #*
                                      #analyzeSUSYGenEvt3b1m_5 *
                                      #analyzeBTags3b1m_5
                                      )
analyzeSUSYBjets3b1m_6 = cms.Sequence(analyzeSUSY3b1m_6 *
                                      analyzeBjets3b1m_6 #*
                                      #analyzeSUSYGenEvt3b1m_6 *
                                      #analyzeBTags3b1m_6
                                      )

## 4 bjets, 1 muon
analyzeSUSYBjets4b1m_1 = cms.Sequence(analyzeSUSY4b1m_1 *
                                      analyzeBjets4b1m_1 #*
                                      #analyzeSUSYGenEvt4b1m_1 *
                                      #analyzeBTags4b1m_1
                                      )
analyzeSUSYBjets4b1m_2 = cms.Sequence(analyzeSUSY4b1m_2 *
                                      analyzeBjets4b1m_2 #*
                                      #analyzeSUSYGenEvt4b1m_2 *
                                      #analyzeBTags4b1m_2
                                      )
analyzeSUSYBjets4b1m_3 = cms.Sequence(analyzeSUSY4b1m_3 *
                                      analyzeBjets4b1m_3 #*
                                      #analyzeSUSYGenEvt4b1m_3 *
                                      #analyzeBTags4b1m_3
                                      )
analyzeSUSYBjets4b1m_4 = cms.Sequence(analyzeSUSY4b1m_4 *
                                      analyzeBjets4b1m_4 #*
                                      #analyzeSUSYGenEvt4b1m_4 *
                                      #analyzeBTags4b1m_4
                                      )
analyzeSUSYBjets4b1m_5 = cms.Sequence(analyzeSUSY4b1m_5 *
                                      analyzeBjets4b1m_5 #*
                                      #analyzeSUSYGenEvt4b1m_5 *
                                      #analyzeBTags4b1m_5
                                      )
analyzeSUSYBjets4b1m_6 = cms.Sequence(analyzeSUSY4b1m_6 *
                                      analyzeBjets4b1m_6 #*
                                      #analyzeSUSYGenEvt4b1m_6 *
                                      #analyzeBTags4b1m_6
                                      )

## 1 bjet, 1 electron
analyzeSUSYBjets1b1e_1 = cms.Sequence(analyzeSUSY1b1e_1 *
                                      analyzeBjets1b1e_1 #*
                                      #analyzeSUSYGenEvt1b1e_1 *
                                      #analyzeBTags1b1e_1
                                      )
analyzeSUSYBjets1b1e_2 = cms.Sequence(analyzeSUSY1b1e_2 *
                                      analyzeBjets1b1e_2 #*
                                      #analyzeSUSYGenEvt1b1e_2 *
                                      #analyzeBTags1b1e_2
                                      )
analyzeSUSYBjets1b1e_3 = cms.Sequence(analyzeSUSY1b1e_3 *
                                      analyzeBjets1b1e_3 #*
                                      #analyzeSUSYGenEvt1b1e_3 *
                                      #analyzeBTags1b1e_3
                                      )
analyzeSUSYBjets1b1e_4 = cms.Sequence(analyzeSUSY1b1e_4 *
                                      analyzeBjets1b1e_4 #*
                                      #analyzeSUSYGenEvt1b1e_4 *
                                      #analyzeBTags1b1e_4
                                      )
analyzeSUSYBjets1b1e_5 = cms.Sequence(analyzeSUSY1b1e_5 *
                                      analyzeBjets1b1e_5 #*
                                      #analyzeSUSYGenEvt1b1e_5 *
                                      #analyzeBTags1b1e_5
                                      )
analyzeSUSYBjets1b1e_6 = cms.Sequence(analyzeSUSY1b1e_6 *
                                      analyzeBjets1b1e_6 #*
                                      #analyzeSUSYGenEvt1b1e_6 *
                                      #analyzeBTags1b1e_6
                                      )

## 2 bjets, 1 electron
analyzeSUSYBjets2b1e_1 = cms.Sequence(analyzeSUSY2b1e_1 *
                                      analyzeBjets2b1e_1 #*
                                      #analyzeSUSYGenEvt2b1e_1 *
                                      #analyzeBTags2b1e_1
                                      )
analyzeSUSYBjets2b1e_2 = cms.Sequence(analyzeSUSY2b1e_2 *
                                      analyzeBjets2b1e_2 #*
                                      #analyzeSUSYGenEvt2b1e_2 *
                                      #analyzeBTags2b1e_2
                                      )
analyzeSUSYBjets2b1e_3 = cms.Sequence(analyzeSUSY2b1e_3 *
                                      analyzeBjets2b1e_3 #*
                                      #analyzeSUSYGenEvt2b1e_3 *
                                      #analyzeBTags2b1e_3
                                      )
analyzeSUSYBjets2b1e_4 = cms.Sequence(analyzeSUSY2b1e_4 *
                                      analyzeBjets2b1e_4 #*
                                      #analyzeSUSYGenEvt2b1e_4 *
                                      #analyzeBTags2b1e_4
                                      )
analyzeSUSYBjets2b1e_5 = cms.Sequence(analyzeSUSY2b1e_5 *
                                      analyzeBjets2b1e_5 #*
                                      #analyzeSUSYGenEvt2b1e_5 *
                                      #analyzeBTags2b1e_5
                                      )
analyzeSUSYBjets2b1e_6 = cms.Sequence(analyzeSUSY2b1e_6 *
                                      analyzeBjets2b1e_6 #*
                                      #analyzeSUSYGenEvt2b1e_6 *
                                      #analyzeBTags2b1e_6
                                      )

## 3 bjets, 1 electron
analyzeSUSYBjets3b1e_1 = cms.Sequence(analyzeSUSY3b1e_1 *
                                      analyzeBjets3b1e_1 #*
                                      #analyzeSUSYGenEvt3b1e_1 *
                                      #analyzeBTags3b1e_1
                                      )
analyzeSUSYBjets3b1e_2 = cms.Sequence(analyzeSUSY3b1e_2 *
                                      analyzeBjets3b1e_2 #*
                                      #analyzeSUSYGenEvt3b1e_2 *
                                      #analyzeBTags3b1e_2
                                      )
analyzeSUSYBjets3b1e_3 = cms.Sequence(analyzeSUSY3b1e_3 *
                                      analyzeBjets3b1e_3 #*
                                      #analyzeSUSYGenEvt3b1e_3 *
                                      #analyzeBTags3b1e_3
                                      )
analyzeSUSYBjets3b1e_4 = cms.Sequence(analyzeSUSY3b1e_4 *
                                      analyzeBjets3b1e_4 #*
                                      #analyzeSUSYGenEvt3b1e_4 *
                                      #analyzeBTags3b1e_4
                                      )
analyzeSUSYBjets3b1e_5 = cms.Sequence(analyzeSUSY3b1e_5 *
                                      analyzeBjets3b1e_5 #*
                                      #analyzeSUSYGenEvt3b1e_5 *
                                      #analyzeBTags3b1e_5
                                      )
analyzeSUSYBjets3b1e_6 = cms.Sequence(analyzeSUSY3b1e_6 *
                                      analyzeBjets3b1e_6 #*
                                      #analyzeSUSYGenEvt3b1e_6 *
                                      #analyzeBTags3b1e_6
                                      )

## 4 bjets, 1 electron
analyzeSUSYBjets4b1e_1 = cms.Sequence(analyzeSUSY4b1e_1 *
                                      analyzeBjets4b1e_1 #*
                                      #analyzeSUSYGenEvt4b1e_1 *
                                      #analyzeBTags4b1e_1
                                      )
analyzeSUSYBjets4b1e_2 = cms.Sequence(analyzeSUSY4b1e_2 *
                                      analyzeBjets4b1e_2 #*
                                      #analyzeSUSYGenEvt4b1e_2 *
                                      #analyzeBTags4b1e_2
                                      )
analyzeSUSYBjets4b1e_3 = cms.Sequence(analyzeSUSY4b1e_3 *
                                      analyzeBjets4b1e_3 #*
                                      #analyzeSUSYGenEvt4b1e_3 *
                                      #analyzeBTags4b1e_3
                                      )
analyzeSUSYBjets4b1e_4 = cms.Sequence(analyzeSUSY4b1e_4 *
                                      analyzeBjets4b1e_4 #*
                                      #analyzeSUSYGenEvt4b1e_4 *
                                      #analyzeBTags4b1e_4
                                      )
analyzeSUSYBjets4b1e_5 = cms.Sequence(analyzeSUSY4b1e_5 *
                                      analyzeBjets4b1e_5 #*
                                      #analyzeSUSYGenEvt4b1e_5 *
                                      #analyzeBTags4b1e_5
                                      )
analyzeSUSYBjets4b1e_6 = cms.Sequence(analyzeSUSY4b1e_6 *
                                      analyzeBjets4b1e_6 #*
                                      #analyzeSUSYGenEvt4b1e_6 *
                                      #analyzeBTags4b1e_6
                                      )

## 3 bjets
analyzeSUSYBjets3b_1 = cms.Sequence(analyzeSUSY3b_1 *
                                    analyzeBjets3b_1 #*
                                    #analyzeSUSYGenEvt3b_1 *
                                    #analyzeBTags3b_1
                                    )
analyzeSUSYBjets3b_2 = cms.Sequence(analyzeSUSY3b_2 *
                                    analyzeBjets3b_2 #*
                                    #analyzeSUSYGenEvt3b_2 *
                                    #analyzeBTags3b_2
                                    )
analyzeSUSYBjets3b_3 = cms.Sequence(analyzeSUSY3b_3 *
                                    analyzeBjets3b_3 #*
                                    #analyzeSUSYGenEvt3b_3 *
                                    #analyzeBTags3b_3
                                    )
analyzeSUSYBjets3b_4 = cms.Sequence(analyzeSUSY3b_4 *
                                    analyzeBjets3b_4 #*
                                    #analyzeSUSYGenEvt3b_4 *
                                    #analyzeBTags3b_4
                                    )
analyzeSUSYBjets3b_5 = cms.Sequence(analyzeSUSY3b_5 *
                                    analyzeBjets3b_5 #*
                                    #analyzeSUSYGenEvt3b_5 *
                                    #analyzeBTags3b_5
                                    )
analyzeSUSYBjets3b_6 = cms.Sequence(analyzeSUSY3b_6 *
                                    analyzeBjets3b_6 #*
                                    #analyzeSUSYGenEvt3b_6 *
                                    #analyzeBTags3b_6
                                    )

## 4 bjets
analyzeSUSYBjets4b_1 = cms.Sequence(analyzeSUSY4b_1 *
                                    analyzeBjets4b_1 #*
                                    #analyzeSUSYGenEvt4b_1 *
                                    #analyzeBTags4b_1
                                    )
analyzeSUSYBjets4b_2 = cms.Sequence(analyzeSUSY4b_2 *
                                    analyzeBjets4b_2 #*
                                    #analyzeSUSYGenEvt4b_2 *
                                    #analyzeBTags4b_2
                                    )
analyzeSUSYBjets4b_3 = cms.Sequence(analyzeSUSY4b_3 *
                                    analyzeBjets4b_3 #*
                                    #analyzeSUSYGenEvt4b_3 *
                                    #analyzeBTags4b_3
                                    )
analyzeSUSYBjets4b_4 = cms.Sequence(analyzeSUSY4b_4 *
                                    analyzeBjets4b_4 #*
                                    #analyzeSUSYGenEvt4b_4 *
                                    #analyzeBTags4b_4
                                    )
analyzeSUSYBjets4b_5 = cms.Sequence(analyzeSUSY4b_5 *
                                    analyzeBjets4b_5 #*
                                    #analyzeSUSYGenEvt4b_5 *
                                    #analyzeBTags4b_5
                                    )
analyzeSUSYBjets4b_6 = cms.Sequence(analyzeSUSY4b_6 *
                                    analyzeBjets4b_6 #*
                                    #analyzeSUSYGenEvt4b_6 *
                                    #analyzeBTags4b_6
                                    )
