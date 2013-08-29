#----------------------------------------------------
# Clone and configure CorrelationAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.CorrelationAnalyzer_cfi import *

## default configuration
analyzeCorrelation.jets           = "goodJets"
analyzeCorrelation.muons          = "goodMuons"
analyzeCorrelation.electrons      = "goodElectrons"
analyzeCorrelation.met            = "scaledJetEnergy:patMETsPF"
analyzeCorrelation.useEventWeight = True
analyzeCorrelation.TTJets         = True

## clone and configure modules for different inclusive MET cuts
analyzeCorrelation1m_MET60ToInf  = analyzeCorrelation.clone()
analyzeCorrelation1m_MET100ToInf = analyzeCorrelation.clone()
analyzeCorrelation1m_MET150ToInf = analyzeCorrelation.clone()
analyzeCorrelation1m_MET200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1m_MET250ToInf = analyzeCorrelation.clone()

analyzeCorrelation1m_MET60ToInf.METCut  = 60.,9999.
analyzeCorrelation1m_MET100ToInf.METCut = 100.,9999.
analyzeCorrelation1m_MET150ToInf.METCut = 150.,9999.
analyzeCorrelation1m_MET200ToInf.METCut = 200.,9999.
analyzeCorrelation1m_MET250ToInf.METCut = 250.,9999.

analyzeCorrelation1e_MET60ToInf  = analyzeCorrelation.clone()
analyzeCorrelation1e_MET100ToInf = analyzeCorrelation.clone()
analyzeCorrelation1e_MET150ToInf = analyzeCorrelation.clone()
analyzeCorrelation1e_MET200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1e_MET250ToInf = analyzeCorrelation.clone()

analyzeCorrelation1e_MET60ToInf.METCut  = 60.,9999.
analyzeCorrelation1e_MET100ToInf.METCut = 100.,9999.
analyzeCorrelation1e_MET150ToInf.METCut = 150.,9999.
analyzeCorrelation1e_MET200ToInf.METCut = 200.,9999.
analyzeCorrelation1e_MET250ToInf.METCut = 250.,9999.

## clone and configure modules for different nJets cuts
analyzeCorrelation1m_nJets1To1   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets2To2   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets3To3   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets4ToInf = analyzeCorrelation.clone()

analyzeCorrelation1m_nJets1To1.nJetsCut     = 1,1
analyzeCorrelation1m_nJets2To2.nJetsCut     = 2,2
analyzeCorrelation1m_nJets3To3.nJetsCut     = 3,3
analyzeCorrelation1m_nJets4ToInf.nJetsCut   = 4,999

analyzeCorrelation1e_nJets1To1   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets2To2   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets3To3   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets4ToInf = analyzeCorrelation.clone()

analyzeCorrelation1e_nJets1To1.nJetsCut     = 1,1
analyzeCorrelation1e_nJets2To2.nJetsCut     = 2,2
analyzeCorrelation1e_nJets3To3.nJetsCut     = 3,3
analyzeCorrelation1e_nJets4ToInf.nJetsCut   = 4,999
