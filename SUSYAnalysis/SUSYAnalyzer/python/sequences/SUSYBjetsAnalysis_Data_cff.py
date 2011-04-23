from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.electrons = "goodElectrons"


analyzeSUSY1l_1 = analyzeSUSY.clone()
analyzeSUSY1l_2 = analyzeSUSY.clone()
analyzeSUSY1l_3 = analyzeSUSY.clone()
analyzeSUSY1l_4 = analyzeSUSY.clone()
analyzeSUSY1l_5 = analyzeSUSY.clone()
analyzeSUSY1l_noCuts = analyzeSUSY.clone()
analyzeSUSY1l_preselection = analyzeSUSY.clone()
analyzeSUSY1l_oneGoodMuon = analyzeSUSY.clone()
analyzeSUSY1l_fourGoodJets = analyzeSUSY.clone()
analyzeSUSY1l_oneTightJet = analyzeSUSY.clone()
analyzeSUSY1l_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY1l_metSelection = analyzeSUSY.clone()
analyzeSUSY1l_HTSelection = analyzeSUSY.clone()

analyzeSUSY1l_nminus1_oneGoodMuon = analyzeSUSY.clone()
analyzeSUSY1l_nminus1_fourGoodJets = analyzeSUSY.clone()
analyzeSUSY1l_nminus1_oneTightJet = analyzeSUSY.clone()
analyzeSUSY1l_nminus1_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY1l_nminus1_metSelection = analyzeSUSY.clone()
analyzeSUSY1l_nminus1_HTSelection = analyzeSUSY.clone()

analyzeSUSY2l_1 = analyzeSUSY.clone()
analyzeSUSY2l_2 = analyzeSUSY.clone()
analyzeSUSY2l_3 = analyzeSUSY.clone()
analyzeSUSY2l_4 = analyzeSUSY.clone()
analyzeSUSY2l_5 = analyzeSUSY.clone()
analyzeSUSY2l_noCuts = analyzeSUSY.clone()
analyzeSUSY2l_preselection = analyzeSUSY.clone()
analyzeSUSY2l_twoGoodLeptons = analyzeSUSY.clone()
analyzeSUSY2l_threeGoodJets = analyzeSUSY.clone()
analyzeSUSY2l_oneTightJet = analyzeSUSY.clone()
analyzeSUSY2l_twoMediumJets = analyzeSUSY.clone()
analyzeSUSY2l_metSelection = analyzeSUSY.clone()
analyzeSUSY2l_HTSelection = analyzeSUSY.clone()

analyzeSUSY1b_1 = analyzeSUSY.clone()
analyzeSUSY1b_2 = analyzeSUSY.clone()
analyzeSUSY1b_3 = analyzeSUSY.clone()
analyzeSUSY1b_4 = analyzeSUSY.clone()
analyzeSUSY1b_5 = analyzeSUSY.clone()

analyzeSUSY2b_1 = analyzeSUSY.clone()
analyzeSUSY2b_2 = analyzeSUSY.clone()
analyzeSUSY2b_3 = analyzeSUSY.clone()
analyzeSUSY2b_4 = analyzeSUSY.clone()
analyzeSUSY2b_5 = analyzeSUSY.clone()

analyzeSUSY1b1l_1 = analyzeSUSY.clone()
analyzeSUSY1b1l_2 = analyzeSUSY.clone()
analyzeSUSY1b1l_3 = analyzeSUSY.clone()
analyzeSUSY1b1l_4 = analyzeSUSY.clone()
analyzeSUSY1b1l_5 = analyzeSUSY.clone()

analyzeSUSY2b1l_1 = analyzeSUSY.clone()
analyzeSUSY2b1l_2 = analyzeSUSY.clone()
analyzeSUSY2b1l_3 = analyzeSUSY.clone()
analyzeSUSY2b1l_4 = analyzeSUSY.clone()
analyzeSUSY2b1l_5 = analyzeSUSY.clone()

analyzeSUSY3b1l_1 = analyzeSUSY.clone()
analyzeSUSY3b1l_2 = analyzeSUSY.clone()
analyzeSUSY3b1l_3 = analyzeSUSY.clone()
analyzeSUSY3b1l_4 = analyzeSUSY.clone()
analyzeSUSY3b1l_5 = analyzeSUSY.clone()

analyzeSUSY4b1l_1 = analyzeSUSY.clone()
analyzeSUSY4b1l_2 = analyzeSUSY.clone()
analyzeSUSY4b1l_3 = analyzeSUSY.clone()
analyzeSUSY4b1l_4 = analyzeSUSY.clone()
analyzeSUSY4b1l_5 = analyzeSUSY.clone()

analyzeSUSY1b2l_1 = analyzeSUSY.clone()
analyzeSUSY1b2l_2 = analyzeSUSY.clone()
analyzeSUSY1b2l_3 = analyzeSUSY.clone()
analyzeSUSY1b2l_4 = analyzeSUSY.clone()
analyzeSUSY1b2l_5 = analyzeSUSY.clone()
    
analyzeSUSY2b2l_1 = analyzeSUSY.clone()
analyzeSUSY2b2l_2 = analyzeSUSY.clone()
analyzeSUSY2b2l_3 = analyzeSUSY.clone()
analyzeSUSY2b2l_4 = analyzeSUSY.clone()
analyzeSUSY2b2l_5 = analyzeSUSY.clone()
    
analyzeSUSY3b2l_1 = analyzeSUSY.clone()
analyzeSUSY3b2l_2 = analyzeSUSY.clone()
analyzeSUSY3b2l_3 = analyzeSUSY.clone()
analyzeSUSY3b2l_4 = analyzeSUSY.clone()
analyzeSUSY3b2l_5 = analyzeSUSY.clone()

analyzeSUSY4b2l_1 = analyzeSUSY.clone()
analyzeSUSY4b2l_2 = analyzeSUSY.clone()
analyzeSUSY4b2l_3 = analyzeSUSY.clone()
analyzeSUSY4b2l_4 = analyzeSUSY.clone()
analyzeSUSY4b2l_5 = analyzeSUSY.clone()

analyzeSUSY3b_1 = analyzeSUSY.clone()
analyzeSUSY3b_2 = analyzeSUSY.clone()
analyzeSUSY3b_3 = analyzeSUSY.clone()
analyzeSUSY3b_4 = analyzeSUSY.clone()
analyzeSUSY3b_5 = analyzeSUSY.clone()

analyzeSUSY4b_1 = analyzeSUSY.clone()
analyzeSUSY4b_2 = analyzeSUSY.clone()
analyzeSUSY4b_3 = analyzeSUSY.clone()
analyzeSUSY4b_4 = analyzeSUSY.clone()
analyzeSUSY4b_5 = analyzeSUSY.clone()

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


analyzeBjets1l_1 = analyzeBjets.clone()
analyzeBjets1l_2 = analyzeBjets.clone()
analyzeBjets1l_3 = analyzeBjets.clone()
analyzeBjets1l_4 = analyzeBjets.clone()
analyzeBjets1l_5 = analyzeBjets.clone()
analyzeBjets1l_noCuts = analyzeBjets.clone()
analyzeBjets1l_preselection = analyzeBjets.clone()
analyzeBjets1l_oneGoodMuon = analyzeBjets.clone()
analyzeBjets1l_fourGoodJets = analyzeBjets.clone()
analyzeBjets1l_oneTightJet = analyzeBjets.clone()
analyzeBjets1l_twoMediumJets = analyzeBjets.clone()
analyzeBjets1l_metSelection = analyzeBjets.clone()
analyzeBjets1l_HTSelection = analyzeBjets.clone()

analyzeBjets1l_nminus1_oneGoodMuon = analyzeBjets.clone()
analyzeBjets1l_nminus1_fourGoodJets = analyzeBjets.clone()
analyzeBjets1l_nminus1_oneTightJet = analyzeBjets.clone()
analyzeBjets1l_nminus1_twoMediumJets = analyzeBjets.clone()
analyzeBjets1l_nminus1_metSelection = analyzeBjets.clone()
analyzeBjets1l_nminus1_HTSelection = analyzeBjets.clone()

analyzeBjets2l_1 = analyzeBjets.clone()
analyzeBjets2l_2 = analyzeBjets.clone()
analyzeBjets2l_3 = analyzeBjets.clone()
analyzeBjets2l_4 = analyzeBjets.clone()
analyzeBjets2l_5 = analyzeBjets.clone()
analyzeBjets2l_noCuts = analyzeBjets.clone()
analyzeBjets2l_preselection = analyzeBjets.clone()
analyzeBjets2l_twoGoodLeptons = analyzeBjets.clone()
analyzeBjets2l_threeGoodJets = analyzeBjets.clone()
analyzeBjets2l_oneTightJet = analyzeBjets.clone()
analyzeBjets2l_twoMediumJets = analyzeBjets.clone()
analyzeBjets2l_metSelection = analyzeBjets.clone()
analyzeBjets2l_HTSelection = analyzeBjets.clone()

analyzeBjets1b_1 = analyzeBjets.clone()
analyzeBjets1b_2 = analyzeBjets.clone()
analyzeBjets1b_3 = analyzeBjets.clone()
analyzeBjets1b_4 = analyzeBjets.clone()
analyzeBjets1b_5 = analyzeBjets.clone()

analyzeBjets2b_1 = analyzeBjets.clone()
analyzeBjets2b_2 = analyzeBjets.clone()
analyzeBjets2b_3 = analyzeBjets.clone()
analyzeBjets2b_4 = analyzeBjets.clone()
analyzeBjets2b_5 = analyzeBjets.clone()

analyzeBjets1b1l_1 = analyzeBjets.clone()
analyzeBjets1b1l_2 = analyzeBjets.clone()
analyzeBjets1b1l_3 = analyzeBjets.clone()
analyzeBjets1b1l_4 = analyzeBjets.clone()
analyzeBjets1b1l_5 = analyzeBjets.clone()

analyzeBjets2b1l_1 = analyzeBjets.clone()
analyzeBjets2b1l_2 = analyzeBjets.clone()
analyzeBjets2b1l_3 = analyzeBjets.clone()
analyzeBjets2b1l_4 = analyzeBjets.clone()
analyzeBjets2b1l_5 = analyzeBjets.clone()

analyzeBjets3b1l_1 = analyzeBjets.clone()
analyzeBjets3b1l_2 = analyzeBjets.clone()
analyzeBjets3b1l_3 = analyzeBjets.clone()
analyzeBjets3b1l_4 = analyzeBjets.clone()
analyzeBjets3b1l_5 = analyzeBjets.clone()
    
analyzeBjets4b1l_1 = analyzeBjets.clone()
analyzeBjets4b1l_2 = analyzeBjets.clone()
analyzeBjets4b1l_3 = analyzeBjets.clone()
analyzeBjets4b1l_4 = analyzeBjets.clone()
analyzeBjets4b1l_5 = analyzeBjets.clone()

analyzeBjets1b2l_1 = analyzeBjets.clone()
analyzeBjets1b2l_2 = analyzeBjets.clone()
analyzeBjets1b2l_3 = analyzeBjets.clone()
analyzeBjets1b2l_4 = analyzeBjets.clone()
analyzeBjets1b2l_5 = analyzeBjets.clone()

analyzeBjets2b2l_1 = analyzeBjets.clone()
analyzeBjets2b2l_2 = analyzeBjets.clone()
analyzeBjets2b2l_3 = analyzeBjets.clone()
analyzeBjets2b2l_4 = analyzeBjets.clone()
analyzeBjets2b2l_5 = analyzeBjets.clone()

analyzeBjets3b2l_1 = analyzeBjets.clone()
analyzeBjets3b2l_2 = analyzeBjets.clone()
analyzeBjets3b2l_3 = analyzeBjets.clone()
analyzeBjets3b2l_4 = analyzeBjets.clone()
analyzeBjets3b2l_5 = analyzeBjets.clone()

analyzeBjets4b2l_1 = analyzeBjets.clone()
analyzeBjets4b2l_2 = analyzeBjets.clone()
analyzeBjets4b2l_3 = analyzeBjets.clone()
analyzeBjets4b2l_4 = analyzeBjets.clone()
analyzeBjets4b2l_5 = analyzeBjets.clone()

analyzeBjets3b_1 = analyzeBjets.clone()
analyzeBjets3b_2 = analyzeBjets.clone()
analyzeBjets3b_3 = analyzeBjets.clone()
analyzeBjets3b_4 = analyzeBjets.clone()
analyzeBjets3b_5 = analyzeBjets.clone()

analyzeBjets4b_1 = analyzeBjets.clone()
analyzeBjets4b_2 = analyzeBjets.clone()
analyzeBjets4b_3 = analyzeBjets.clone()
analyzeBjets4b_4 = analyzeBjets.clone()
analyzeBjets4b_5 = analyzeBjets.clone()
    
from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import *

analyzeSUSYGenEvt.jets = "goodJets"
analyzeSUSYGenEvt.bjets = "mediumTrackHighPurBjets"
analyzeSUSYGenEvt.matchedbjets = "matchedBjets"
analyzeSUSYGenEvt.matchedqjets = "matchedLightJets"
analyzeSUSYGenEvt.matchedmuons = "goodMuons"
analyzeSUSYGenEvt.matchedelectrons = "goodElectrons"


analyzeSUSYGenEvt1l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_noCuts = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_preselection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_oneGoodMuon = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_fourGoodJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_HTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1l_nminus1_oneGoodMuon = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_nminus1_fourGoodJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_nminus1_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_nminus1_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_nminus1_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1l_nminus1_HTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt2l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_5 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_noCuts = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_preselection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_twoGoodLeptons = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_threeGoodJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_oneTightJet = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_twoMediumJets = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_metSelection = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2l_HTSelection = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt2b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt1b1l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b1l_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt2b1l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b1l_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt3b1l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b1l_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt4b1l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b1l_5 = analyzeSUSYGenEvt.clone()
    
analyzeSUSYGenEvt1b2l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b2l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b2l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b2l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt1b2l_5 = analyzeSUSYGenEvt.clone()
    
analyzeSUSYGenEvt2b2l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b2l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b2l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b2l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt2b2l_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt3b2l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b2l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b2l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b2l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b2l_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt4b2l_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b2l_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b2l_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b2l_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b2l_5 = analyzeSUSYGenEvt.clone()
    
analyzeSUSYGenEvt3b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt3b_5 = analyzeSUSYGenEvt.clone()

analyzeSUSYGenEvt4b_1 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_2 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_3 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_4 = analyzeSUSYGenEvt.clone()
analyzeSUSYGenEvt4b_5 = analyzeSUSYGenEvt.clone()

from TopAnalysis.TopAnalyzer.BTags_cfi import *

analyzeBTags.src = "goodJets"

analyzeBTags1l_1 = analyzeBTags.clone()
analyzeBTags1l_2 = analyzeBTags.clone()
analyzeBTags1l_3 = analyzeBTags.clone()
analyzeBTags1l_4 = analyzeBTags.clone()
analyzeBTags1l_5 = analyzeBTags.clone()
analyzeBTags1l_noCuts = analyzeBTags.clone()
analyzeBTags1l_preselection = analyzeBTags.clone()
analyzeBTags1l_oneGoodMuon = analyzeBTags.clone()
analyzeBTags1l_fourGoodJets = analyzeBTags.clone()
analyzeBTags1l_oneTightJet = analyzeBTags.clone()
analyzeBTags1l_twoMediumJets = analyzeBTags.clone()
analyzeBTags1l_metSelection = analyzeBTags.clone()
analyzeBTags1l_HTSelection = analyzeBTags.clone()

analyzeBTags1l_nminus1_oneGoodMuon = analyzeBTags.clone()
analyzeBTags1l_nminus1_fourGoodJets = analyzeBTags.clone()
analyzeBTags1l_nminus1_oneTightJet = analyzeBTags.clone()
analyzeBTags1l_nminus1_twoMediumJets = analyzeBTags.clone()
analyzeBTags1l_nminus1_metSelection = analyzeBTags.clone()
analyzeBTags1l_nminus1_HTSelection = analyzeBTags.clone()

analyzeBTags2l_1 = analyzeBTags.clone()
analyzeBTags2l_2 = analyzeBTags.clone()
analyzeBTags2l_3 = analyzeBTags.clone()
analyzeBTags2l_4 = analyzeBTags.clone()
analyzeBTags2l_5 = analyzeBTags.clone()
analyzeBTags2l_noCuts = analyzeBTags.clone()
analyzeBTags2l_preselection = analyzeBTags.clone()
analyzeBTags2l_twoGoodLeptons = analyzeBTags.clone()
analyzeBTags2l_threeGoodJets = analyzeBTags.clone()
analyzeBTags2l_oneTightJet = analyzeBTags.clone()
analyzeBTags2l_twoMediumJets = analyzeBTags.clone()
analyzeBTags2l_metSelection = analyzeBTags.clone()
analyzeBTags2l_HTSelection = analyzeBTags.clone()

analyzeBTags1b_1 = analyzeBTags.clone()
analyzeBTags1b_2 = analyzeBTags.clone()
analyzeBTags1b_3 = analyzeBTags.clone()
analyzeBTags1b_4 = analyzeBTags.clone()
analyzeBTags1b_5 = analyzeBTags.clone()

analyzeBTags2b_1 = analyzeBTags.clone()
analyzeBTags2b_2 = analyzeBTags.clone()
analyzeBTags2b_3 = analyzeBTags.clone()
analyzeBTags2b_4 = analyzeBTags.clone()
analyzeBTags2b_5 = analyzeBTags.clone()

analyzeBTags1b1l_1 = analyzeBTags.clone()
analyzeBTags1b1l_2 = analyzeBTags.clone()
analyzeBTags1b1l_3 = analyzeBTags.clone()
analyzeBTags1b1l_4 = analyzeBTags.clone()
analyzeBTags1b1l_5 = analyzeBTags.clone()

analyzeBTags2b1l_1 = analyzeBTags.clone()
analyzeBTags2b1l_2 = analyzeBTags.clone()
analyzeBTags2b1l_3 = analyzeBTags.clone()
analyzeBTags2b1l_4 = analyzeBTags.clone()
analyzeBTags2b1l_5 = analyzeBTags.clone()

analyzeBTags3b1l_1 = analyzeBTags.clone()
analyzeBTags3b1l_2 = analyzeBTags.clone()
analyzeBTags3b1l_3 = analyzeBTags.clone()
analyzeBTags3b1l_4 = analyzeBTags.clone()
analyzeBTags3b1l_5 = analyzeBTags.clone()

analyzeBTags4b1l_1 = analyzeBTags.clone()
analyzeBTags4b1l_2 = analyzeBTags.clone()
analyzeBTags4b1l_3 = analyzeBTags.clone()
analyzeBTags4b1l_4 = analyzeBTags.clone()
analyzeBTags4b1l_5 = analyzeBTags.clone()

analyzeBTags1b2l_1 = analyzeBTags.clone()
analyzeBTags1b2l_2 = analyzeBTags.clone()
analyzeBTags1b2l_3 = analyzeBTags.clone()
analyzeBTags1b2l_4 = analyzeBTags.clone()
analyzeBTags1b2l_5 = analyzeBTags.clone()

analyzeBTags2b2l_1 = analyzeBTags.clone()
analyzeBTags2b2l_2 = analyzeBTags.clone()
analyzeBTags2b2l_3 = analyzeBTags.clone()
analyzeBTags2b2l_4 = analyzeBTags.clone()
analyzeBTags2b2l_5 = analyzeBTags.clone()

analyzeBTags3b2l_1 = analyzeBTags.clone()
analyzeBTags3b2l_2 = analyzeBTags.clone()
analyzeBTags3b2l_3 = analyzeBTags.clone()
analyzeBTags3b2l_4 = analyzeBTags.clone()
analyzeBTags3b2l_5 = analyzeBTags.clone()

analyzeBTags4b2l_1 = analyzeBTags.clone()
analyzeBTags4b2l_2 = analyzeBTags.clone()
analyzeBTags4b2l_3 = analyzeBTags.clone()
analyzeBTags4b2l_4 = analyzeBTags.clone()
analyzeBTags4b2l_5 = analyzeBTags.clone()

analyzeBTags3b_1 = analyzeBTags.clone()
analyzeBTags3b_2 = analyzeBTags.clone()
analyzeBTags3b_3 = analyzeBTags.clone()
analyzeBTags3b_4 = analyzeBTags.clone()
analyzeBTags3b_5 = analyzeBTags.clone()

analyzeBTags4b_1 = analyzeBTags.clone()
analyzeBTags4b_2 = analyzeBTags.clone()
analyzeBTags4b_3 = analyzeBTags.clone()
analyzeBTags4b_4 = analyzeBTags.clone()
analyzeBTags4b_5 = analyzeBTags.clone()



## 1 lepton
analyzeSUSYBjets1l_noCuts = cms.Sequence(analyzeSUSY1l_noCuts *
                                         analyzeBjets1l_noCuts
                                         )
analyzeSUSYBjets1l_preselection = cms.Sequence(analyzeSUSY1l_preselection *
                                               analyzeBjets1l_preselection
                                               )
analyzeSUSYBjets1l_oneGoodMuon = cms.Sequence(analyzeSUSY1l_oneGoodMuon *
                                              analyzeBjets1l_oneGoodMuon
                                              )
analyzeSUSYBjets1l_fourGoodJets = cms.Sequence(analyzeSUSY1l_fourGoodJets *
                                               analyzeBjets1l_fourGoodJets
                                               )
analyzeSUSYBjets1l_oneTightJet = cms.Sequence(analyzeSUSY1l_oneTightJet *
                                              analyzeBjets1l_oneTightJet
                                              )
analyzeSUSYBjets1l_twoMediumJets = cms.Sequence(analyzeSUSY1l_twoMediumJets *
                                                analyzeBjets1l_twoMediumJets
                                                )
analyzeSUSYBjets1l_metSelection = cms.Sequence(analyzeSUSY1l_metSelection *
                                               analyzeBjets1l_metSelection
                                               )
analyzeSUSYBjets1l_HTSelection = cms.Sequence(analyzeSUSY1l_HTSelection *
                                              analyzeBjets1l_HTSelection
                                              )

analyzeSUSYBjets1l_nminus1_oneGoodMuon = cms.Sequence(analyzeSUSY1l_nminus1_oneGoodMuon *
                                                      analyzeBjets1l_nminus1_oneGoodMuon
                                                      )
analyzeSUSYBjets1l_nminus1_fourGoodJets = cms.Sequence(analyzeSUSY1l_nminus1_fourGoodJets *
                                                       analyzeBjets1l_nminus1_fourGoodJets
                                                       )
analyzeSUSYBjets1l_nminus1_oneTightJet = cms.Sequence(analyzeSUSY1l_nminus1_oneTightJet *
                                                      analyzeBjets1l_nminus1_oneTightJet
                                                      )
analyzeSUSYBjets1l_nminus1_twoMediumJets = cms.Sequence(analyzeSUSY1l_nminus1_twoMediumJets *
                                                        analyzeBjets1l_nminus1_twoMediumJets
                                                        )
analyzeSUSYBjets1l_nminus1_metSelection = cms.Sequence(analyzeSUSY1l_nminus1_metSelection *
                                                       analyzeBjets1l_nminus1_metSelection
                                                       )
analyzeSUSYBjets1l_nminus1_HTSelection = cms.Sequence(analyzeSUSY1l_nminus1_HTSelection *
                                                      analyzeBjets1l_nminus1_HTSelection
                                                      )

analyzeSUSYBjets1l_1 = cms.Sequence(analyzeSUSY1l_1 *
                                    analyzeBjets1l_1
                                    )
analyzeSUSYBjets1l_2 = cms.Sequence(analyzeSUSY1l_2 *
                                    analyzeBjets1l_2
                                    )
analyzeSUSYBjets1l_3 = cms.Sequence(analyzeSUSY1l_3 *
                                    analyzeBjets1l_3
                                    )
analyzeSUSYBjets1l_4 = cms.Sequence(analyzeSUSY1l_4 *
                                    analyzeBjets1l_4
                                    )
analyzeSUSYBjets1l_5 = cms.Sequence(analyzeSUSY1l_5 *
                                    analyzeBjets1l_5
                                    )

## 2 leptons
analyzeSUSYBjets2l_1 = cms.Sequence(analyzeSUSY2l_1 *
                                    analyzeBjets2l_1
                                    )
analyzeSUSYBjets2l_2 = cms.Sequence(analyzeSUSY2l_2 *
                                    analyzeBjets2l_2
                                    )
analyzeSUSYBjets2l_3 = cms.Sequence(analyzeSUSY2l_3 *
                                    analyzeBjets2l_3
                                    )
analyzeSUSYBjets2l_4 = cms.Sequence(analyzeSUSY2l_4 *
                                    analyzeBjets2l_4
                                    )
analyzeSUSYBjets2l_5 = cms.Sequence(analyzeSUSY2l_5 *
                                    analyzeBjets2l_5
                                    )

analyzeSUSYBjets2l_noCuts = cms.Sequence(analyzeSUSY2l_noCuts *
                                         analyzeBjets2l_noCuts
                                         )
analyzeSUSYBjets2l_preselection = cms.Sequence(analyzeSUSY2l_preselection *
                                               analyzeBjets2l_preselection
                                               )
analyzeSUSYBjets2l_twoGoodLeptons = cms.Sequence(analyzeSUSY2l_twoGoodLeptons *
                                                 analyzeBjets2l_twoGoodLeptons
                                                 )
analyzeSUSYBjets2l_threeGoodJets = cms.Sequence(analyzeSUSY2l_threeGoodJets *
                                                analyzeBjets2l_threeGoodJets
                                                )
analyzeSUSYBjets2l_oneTightJet = cms.Sequence(analyzeSUSY2l_oneTightJet *
                                              analyzeBjets2l_oneTightJet
                                              )
analyzeSUSYBjets2l_twoMediumJets = cms.Sequence(analyzeSUSY2l_twoMediumJets *
                                                analyzeBjets2l_twoMediumJets
                                                )
analyzeSUSYBjets2l_metSelection = cms.Sequence(analyzeSUSY2l_metSelection *
                                               analyzeBjets2l_metSelection
                                               )
analyzeSUSYBjets2l_HTSelection = cms.Sequence(analyzeSUSY2l_HTSelection *
                                              analyzeBjets2l_HTSelection
                                              )
## 1 bjet
analyzeSUSYBjets1b_1 = cms.Sequence(analyzeSUSY1b_1 *
                                    analyzeBjets1b_1
                                    )
analyzeSUSYBjets1b_2 = cms.Sequence(analyzeSUSY1b_2 *
                                    analyzeBjets1b_2
                                    )
analyzeSUSYBjets1b_3 = cms.Sequence(analyzeSUSY1b_3 *
                                    analyzeBjets1b_3
                                    )
analyzeSUSYBjets1b_4 = cms.Sequence(analyzeSUSY1b_4 *
                                    analyzeBjets1b_4
                                    )
analyzeSUSYBjets1b_5 = cms.Sequence(analyzeSUSY1b_5 *
                                    analyzeBjets1b_5
                                    )

## 2 bjets
analyzeSUSYBjets2b_1 = cms.Sequence(analyzeSUSY2b_1 *
                                    analyzeBjets2b_1
                                    )
analyzeSUSYBjets2b_2 = cms.Sequence(analyzeSUSY2b_2 *
                                    analyzeBjets2b_2
                                    )
analyzeSUSYBjets2b_3 = cms.Sequence(analyzeSUSY2b_3 *
                                    analyzeBjets2b_3
                                    )
analyzeSUSYBjets2b_4 = cms.Sequence(analyzeSUSY2b_4 *
                                    analyzeBjets2b_4
                                    )
analyzeSUSYBjets2b_5 = cms.Sequence(analyzeSUSY2b_5 *
                                    analyzeBjets2b_5
                                    )
## 1 bjet, 1 lepton
analyzeSUSYBjets1b1l_1 = cms.Sequence(analyzeSUSY1b1l_1 *
                                      analyzeBjets1b1l_1
                                      )
analyzeSUSYBjets1b1l_2 = cms.Sequence(analyzeSUSY1b1l_2 *
                                      analyzeBjets1b1l_2
                                      )
analyzeSUSYBjets1b1l_3 = cms.Sequence(analyzeSUSY1b1l_3 *
                                      analyzeBjets1b1l_3
                                      )
analyzeSUSYBjets1b1l_4 = cms.Sequence(analyzeSUSY1b1l_4 *
                                      analyzeBjets1b1l_4
                                      )
analyzeSUSYBjets1b1l_5 = cms.Sequence(analyzeSUSY1b1l_5 *
                                      analyzeBjets1b1l_5
                                      )

## 2 bjets, 1 lepton
analyzeSUSYBjets2b1l_1 = cms.Sequence(analyzeSUSY2b1l_1 *
                                      analyzeBjets2b1l_1
                                      )
analyzeSUSYBjets2b1l_2 = cms.Sequence(analyzeSUSY2b1l_2 *
                                      analyzeBjets2b1l_2
                                      )
analyzeSUSYBjets2b1l_3 = cms.Sequence(analyzeSUSY2b1l_3 *
                                      analyzeBjets2b1l_3
                                      )
analyzeSUSYBjets2b1l_4 = cms.Sequence(analyzeSUSY2b1l_4 *
                                      analyzeBjets2b1l_4
                                      )
analyzeSUSYBjets2b1l_5 = cms.Sequence(analyzeSUSY2b1l_5 *
                                      analyzeBjets2b1l_5
                                      )

## 3 bjets, 1 lepton
analyzeSUSYBjets3b1l_1 = cms.Sequence(analyzeSUSY3b1l_1 *
                                      analyzeBjets3b1l_1
                                      )
analyzeSUSYBjets3b1l_2 = cms.Sequence(analyzeSUSY3b1l_2 *
                                      analyzeBjets3b1l_2
                                      )
analyzeSUSYBjets3b1l_3 = cms.Sequence(analyzeSUSY3b1l_3 *
                                      analyzeBjets3b1l_3
                                      )
analyzeSUSYBjets3b1l_4 = cms.Sequence(analyzeSUSY3b1l_4 *
                                      analyzeBjets3b1l_4
                                      )
analyzeSUSYBjets3b1l_5 = cms.Sequence(analyzeSUSY3b1l_5 *
                                      analyzeBjets3b1l_5
                                      )

## 4 bjets, 1 lepton
analyzeSUSYBjets4b1l_1 = cms.Sequence(analyzeSUSY4b1l_1 *
                                      analyzeBjets4b1l_1
                                      )
analyzeSUSYBjets4b1l_2 = cms.Sequence(analyzeSUSY4b1l_2 *
                                      analyzeBjets4b1l_2
                                      )
analyzeSUSYBjets4b1l_3 = cms.Sequence(analyzeSUSY4b1l_3 *
                                      analyzeBjets4b1l_3
                                      )
analyzeSUSYBjets4b1l_4 = cms.Sequence(analyzeSUSY4b1l_4 *
                                      analyzeBjets4b1l_4
                                      )
analyzeSUSYBjets4b1l_5 = cms.Sequence(analyzeSUSY4b1l_5 *
                                      analyzeBjets4b1l_5
                                      )

## 1 bjet, 2 leptons
analyzeSUSYBjets1b2l_1 = cms.Sequence(analyzeSUSY1b2l_1 *
                                      analyzeBjets1b2l_1
                                      )
analyzeSUSYBjets1b2l_2 = cms.Sequence(analyzeSUSY1b2l_2 *
                                      analyzeBjets1b2l_2
                                      )
analyzeSUSYBjets1b2l_3 = cms.Sequence(analyzeSUSY1b2l_3 *
                                      analyzeBjets1b2l_3
                                      )
analyzeSUSYBjets1b2l_4 = cms.Sequence(analyzeSUSY1b2l_4 *
                                      analyzeBjets1b2l_4
                                      )
analyzeSUSYBjets1b2l_5 = cms.Sequence(analyzeSUSY1b2l_5 *
                                      analyzeBjets1b2l_5
                                      )

## 2 bjets, 2 leptons
analyzeSUSYBjets2b2l_1 = cms.Sequence(analyzeSUSY2b2l_1 *
                                      analyzeBjets2b2l_1
                                      )
analyzeSUSYBjets2b2l_2 = cms.Sequence(analyzeSUSY2b2l_2 *
                                      analyzeBjets2b2l_2
                                      )
analyzeSUSYBjets2b2l_3 = cms.Sequence(analyzeSUSY2b2l_3 *
                                      analyzeBjets2b2l_3
                                      )
analyzeSUSYBjets2b2l_4 = cms.Sequence(analyzeSUSY2b2l_4 *
                                      analyzeBjets2b2l_4
                                      )
analyzeSUSYBjets2b2l_5 = cms.Sequence(analyzeSUSY2b2l_5 *
                                      analyzeBjets2b2l_5
                                      )

## 3 bjets, 2 leptons
analyzeSUSYBjets3b2l_1 = cms.Sequence(analyzeSUSY3b2l_1 *
                                      analyzeBjets3b2l_1
                                      )
analyzeSUSYBjets3b2l_2 = cms.Sequence(analyzeSUSY3b2l_2 *
                                      analyzeBjets3b2l_2
                                      )
analyzeSUSYBjets3b2l_3 = cms.Sequence(analyzeSUSY3b2l_3 *
                                      analyzeBjets3b2l_3
                                      )
analyzeSUSYBjets3b2l_4 = cms.Sequence(analyzeSUSY3b2l_4 *
                                      analyzeBjets3b2l_4
                                      )
analyzeSUSYBjets3b2l_5 = cms.Sequence(analyzeSUSY3b2l_5 *
                                      analyzeBjets3b2l_5
                                      )

## 4 bjets, 2 leptons
analyzeSUSYBjets4b2l_1 = cms.Sequence(analyzeSUSY4b2l_1 *
                                      analyzeBjets4b2l_1
                                      )
analyzeSUSYBjets4b2l_2 = cms.Sequence(analyzeSUSY4b2l_2 *
                                      analyzeBjets4b2l_2
                                      )
analyzeSUSYBjets4b2l_3 = cms.Sequence(analyzeSUSY4b2l_3 *
                                      analyzeBjets4b2l_3
                                      )
analyzeSUSYBjets4b2l_4 = cms.Sequence(analyzeSUSY4b2l_4 *
                                      analyzeBjets4b2l_4
                                      )
analyzeSUSYBjets4b2l_5 = cms.Sequence(analyzeSUSY4b2l_5 *
                                      analyzeBjets4b2l_5
                                      )

## 3 bjets
analyzeSUSYBjets3b_1 = cms.Sequence(analyzeSUSY3b_1 *
                                    analyzeBjets3b_1
                                    )
analyzeSUSYBjets3b_2 = cms.Sequence(analyzeSUSY3b_2 *
                                    analyzeBjets3b_2
                                    )
analyzeSUSYBjets3b_3 = cms.Sequence(analyzeSUSY3b_3 *
                                    analyzeBjets3b_3
                                    )
analyzeSUSYBjets3b_4 = cms.Sequence(analyzeSUSY3b_4 *
                                    analyzeBjets3b_4
                                    )
analyzeSUSYBjets3b_5 = cms.Sequence(analyzeSUSY3b_5 *
                                    analyzeBjets3b_5
                                    )

## 4 bjets
analyzeSUSYBjets4b_1 = cms.Sequence(analyzeSUSY4b_1 *
                                    analyzeBjets4b_1
                                    )
analyzeSUSYBjets4b_2 = cms.Sequence(analyzeSUSY4b_2 *
                                    analyzeBjets4b_2
                                    )
analyzeSUSYBjets4b_3 = cms.Sequence(analyzeSUSY4b_3 *
                                    analyzeBjets4b_3
                                    )
analyzeSUSYBjets4b_4 = cms.Sequence(analyzeSUSY4b_4 *
                                    analyzeBjets4b_4
                                    )
analyzeSUSYBjets4b_5 = cms.Sequence(analyzeSUSY4b_5 *
                                    analyzeBjets4b_5
                                    )
