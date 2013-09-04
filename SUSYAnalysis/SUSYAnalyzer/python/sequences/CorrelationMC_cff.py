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


## clone and configure modules for different event selection steps
analyzeCorrelation1m_leptonSelection  = analyzeCorrelation.clone()
analyzeCorrelation1m_jetSelection     = analyzeCorrelation.clone()

analyzeCorrelation1e_leptonSelection  = analyzeCorrelation.clone()
analyzeCorrelation1e_jetSelection     = analyzeCorrelation.clone()

## clone and configure modules for different inclusive MET cuts
analyzeCorrelation1m_MET60To100  = analyzeCorrelation.clone()
analyzeCorrelation1m_MET100To150 = analyzeCorrelation.clone()
analyzeCorrelation1m_MET150To200 = analyzeCorrelation.clone()
analyzeCorrelation1m_MET200To300 = analyzeCorrelation.clone()
analyzeCorrelation1m_MET300ToInf = analyzeCorrelation.clone()

analyzeCorrelation1m_MET60To100.METCut  = 60.,100.
analyzeCorrelation1m_MET100To150.METCut = 100.,150.
analyzeCorrelation1m_MET150To200.METCut = 150.,200.
analyzeCorrelation1m_MET200To300.METCut = 200.,300.
analyzeCorrelation1m_MET300ToInf.METCut = 300.,9999.

analyzeCorrelation1e_MET60To100  = analyzeCorrelation.clone()
analyzeCorrelation1e_MET100To150 = analyzeCorrelation.clone()
analyzeCorrelation1e_MET150To200 = analyzeCorrelation.clone()
analyzeCorrelation1e_MET200To300 = analyzeCorrelation.clone()
analyzeCorrelation1e_MET300ToInf = analyzeCorrelation.clone()

analyzeCorrelation1e_MET60To100.METCut  = 60.,100.
analyzeCorrelation1e_MET100To150.METCut = 100.,150.
analyzeCorrelation1e_MET150To200.METCut = 150.,200.
analyzeCorrelation1e_MET200To300.METCut = 200.,300.
analyzeCorrelation1e_MET300ToInf.METCut = 300.,9999.

## clone and configure modules for different nJets cuts
analyzeCorrelation1m_nJets1To1   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets2To2   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets3To3   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets4To4   = analyzeCorrelation.clone()
analyzeCorrelation1m_nJets5To5   = analyzeCorrelation.clone()

analyzeCorrelation1m_nJets1To1.nJetsCut   = 1,1
analyzeCorrelation1m_nJets2To2.nJetsCut   = 2,2
analyzeCorrelation1m_nJets3To3.nJetsCut   = 3,3
analyzeCorrelation1m_nJets4To4.nJetsCut   = 4,4
analyzeCorrelation1m_nJets5To5.nJetsCut   = 5,5

analyzeCorrelation1e_nJets1To1   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets2To2   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets3To3   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets4To4   = analyzeCorrelation.clone()
analyzeCorrelation1e_nJets5To5   = analyzeCorrelation.clone()

analyzeCorrelation1e_nJets1To1.nJetsCut   = 1,1
analyzeCorrelation1e_nJets2To2.nJetsCut   = 2,2
analyzeCorrelation1e_nJets3To3.nJetsCut   = 3,3
analyzeCorrelation1e_nJets4To4.nJetsCut   = 4,4
analyzeCorrelation1e_nJets5To5.nJetsCut   = 5,5

#----------------------------------------------------
# Clone and configure TtGenEventAnalyzer modules
#----------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.TtGenEventAnalyzer_cfi import *

analyzeTtGenEvent1m_noCuts           = analyzeTtGenEvent.clone()
analyzeTtGenEvent1m_preselection     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1m_leptonSelection  = analyzeTtGenEvent.clone()
analyzeTtGenEvent1m_jetSelection     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1m_HTSelection      = analyzeTtGenEvent.clone()
analyzeTtGenEvent1m_METSelection     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1m_mTSelection      = analyzeTtGenEvent.clone()

analyzeTtGenEvent1e_noCuts           = analyzeTtGenEvent.clone()
analyzeTtGenEvent1e_preselection     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1e_leptonSelection  = analyzeTtGenEvent.clone()
analyzeTtGenEvent1e_jetSelection     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1e_HTSelection      = analyzeTtGenEvent.clone()
analyzeTtGenEvent1e_METSelection     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1e_mTSelection      = analyzeTtGenEvent.clone()
