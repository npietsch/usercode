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

## b-tag configuration
analyzeCorrelation.useInclusiveBtagEventWeight = True
analyzeCorrelation.inclusiveBtagBin            = 3
analyzeCorrelation.BtagEventWeights            = "btagEventWeightMuJER:RA4bSFEventWeights"
analyzeCorrelation.BtagJetWeights              = "btagEventWeightMuJER:RA4bSFJetWeights"

analyzeCorrelation1l              = analyzeCorrelation.clone()

## clone and configure modules for different nJets cuts
analyzeCorrelation1l_nJets3To4   = analyzeCorrelation.clone()
analyzeCorrelation1l_nJets5To6   = analyzeCorrelation.clone()
analyzeCorrelation1l_nJets7ToInf = analyzeCorrelation.clone()

analyzeCorrelation1l_nJets3To4.nJetsCut   = 3,4
analyzeCorrelation1l_nJets5To6.nJetsCut   = 5,6
analyzeCorrelation1l_nJets7ToInf.nJetsCut = 7,99

## clone and configure modules for different inclusive HT cuts
analyzeCorrelation1l_HT200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT300ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT700ToInf = analyzeCorrelation.clone()

analyzeCorrelation1l_HT200ToInf.HTCut   = 200.,9999.
analyzeCorrelation1l_HT300ToInf.HTCut   = 300.,9999.
analyzeCorrelation1l_HT400ToInf.HTCut   = 400.,9999.
analyzeCorrelation1l_HT500ToInf.HTCut   = 500.,9999.
analyzeCorrelation1l_HT600ToInf.HTCut   = 600.,9999.
analyzeCorrelation1l_HT700ToInf.HTCut   = 600.,9999.

## clone and configure modules for different exclusive HT cuts
analyzeCorrelation1l_HT200To300 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT300To400 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400To500 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500To600 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600To700 = analyzeCorrelation.clone()

analyzeCorrelation1l_HT200To300.HTCut = 200.,300.
analyzeCorrelation1l_HT300To400.HTCut = 300.,400.
analyzeCorrelation1l_HT400To500.HTCut = 400.,500.
analyzeCorrelation1l_HT500To600.HTCut = 500.,600.
analyzeCorrelation1l_HT600To700.HTCut = 600.,700.

## clone and configure modules for different inclusive MET cuts
analyzeCorrelation1l_MET0ToInf   = analyzeCorrelation.clone()
analyzeCorrelation1l_MET50ToInf  = analyzeCorrelation.clone()
analyzeCorrelation1l_MET100ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_MET150ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_MET200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_MET250ToInf = analyzeCorrelation.clone()

analyzeCorrelation1l_MET0ToInf.METCut   = 0.,9999.
analyzeCorrelation1l_MET50ToInf.METCut  = 50.,9999.
analyzeCorrelation1l_MET100ToInf.METCut = 100.,9999.
analyzeCorrelation1l_MET150ToInf.METCut = 150.,9999.
analyzeCorrelation1l_MET200ToInf.METCut = 200.,9999.
analyzeCorrelation1l_MET250ToInf.METCut = 250.,9999.

## clone and configure modules for different exclusive MET cuts
analyzeCorrelation1l_MET0To50    = analyzeCorrelation.clone()
analyzeCorrelation1l_MET50To100  = analyzeCorrelation.clone()
analyzeCorrelation1l_MET100To150 = analyzeCorrelation.clone()
analyzeCorrelation1l_MET150To200 = analyzeCorrelation.clone()
analyzeCorrelation1l_MET200To250 = analyzeCorrelation.clone()

analyzeCorrelation1l_MET0To50.METCut    = 0.,50.
analyzeCorrelation1l_MET50To100.METCut  = 50.,100.
analyzeCorrelation1l_MET100To150.METCut = 100.,150.
analyzeCorrelation1l_MET150To200.METCut = 150.,200.
analyzeCorrelation1l_MET200To250.METCut = 200.,250.

## clone and configure modules for different exclusive YMET cuts
analyzeCorrelation1l_YMET10To15 = analyzeCorrelation.clone()
analyzeCorrelation1l_YMET15To20 = analyzeCorrelation.clone()
analyzeCorrelation1l_YMET20To25 = analyzeCorrelation.clone()
analyzeCorrelation1l_YMET25To30 = analyzeCorrelation.clone()
analyzeCorrelation1l_YMET30To35 = analyzeCorrelation.clone()
analyzeCorrelation1l_YMET35To40 = analyzeCorrelation.clone()

analyzeCorrelation1l_YMET10To15.YMETCut = 1.,1.5
analyzeCorrelation1l_YMET15To20.YMETCut = 1.5,2.
analyzeCorrelation1l_YMET20To25.YMETCut = 2.,2.5
analyzeCorrelation1l_YMET25To30.YMETCut = 2.5,3.
analyzeCorrelation1l_YMET30To35.YMETCut = 3.,3.5
analyzeCorrelation1l_YMET35To40.YMETCut = 3.5,4.

## clone and configure modules for HT > 400 und different inclusive MET cuts
analyzeCorrelation1l_HT400ToInf_MET0ToInf   = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET50ToInf  = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET100ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET150ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET250ToInf = analyzeCorrelation.clone()
    
analyzeCorrelation1l_HT400ToInf_MET0ToInf.HTCut    = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET0ToInf.METCut   = 0.,9999.

analyzeCorrelation1l_HT400ToInf_MET50ToInf.HTCut   = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET50ToInf.METCut  = 50.,9999.

analyzeCorrelation1l_HT400ToInf_MET100ToInf.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET100ToInf.METCut = 100.,9999.

analyzeCorrelation1l_HT400ToInf_MET150ToInf.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET150ToInf.METCut = 150.,9999.

analyzeCorrelation1l_HT400ToInf_MET200ToInf.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET200ToInf.METCut = 200.,9999.

analyzeCorrelation1l_HT400ToInf_MET250ToInf.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET250ToInf.METCut = 250.,9999.

## clone and configure modules for HT > 400 und different exclusive MET cuts
analyzeCorrelation1l_HT400ToInf_MET0To50    = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET50To100  = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET100To150 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET150To200 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400ToInf_MET200To250 = analyzeCorrelation.clone()
    
analyzeCorrelation1l_HT400ToInf_MET0To50.HTCut     = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET0To50.METCut    = 0.,50.

analyzeCorrelation1l_HT400ToInf_MET50To100.HTCut   = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET50To100.METCut  = 50.,100.

analyzeCorrelation1l_HT400ToInf_MET100To150.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET100To150.METCut = 100.,150.

analyzeCorrelation1l_HT400ToInf_MET150To200.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET150To200.METCut = 150.,200.

analyzeCorrelation1l_HT400ToInf_MET200To250.HTCut  = 400.,9999.
analyzeCorrelation1l_HT400ToInf_MET200To250.METCut = 200.,250.

## clone and configure modules for HT > 500 und different inclusive MET cuts
analyzeCorrelation1l_HT500ToInf_MET0ToInf   = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET50ToInf  = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET100ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET150ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET250ToInf = analyzeCorrelation.clone()
    
analyzeCorrelation1l_HT500ToInf_MET0ToInf.HTCut    = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET0ToInf.METCut   = 0.,9999.

analyzeCorrelation1l_HT500ToInf_MET50ToInf.HTCut   = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET50ToInf.METCut  = 50.,9999.

analyzeCorrelation1l_HT500ToInf_MET100ToInf.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET100ToInf.METCut = 100.,9999.

analyzeCorrelation1l_HT500ToInf_MET150ToInf.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET150ToInf.METCut = 150.,9999.

analyzeCorrelation1l_HT500ToInf_MET200ToInf.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET200ToInf.METCut = 200.,9999.

analyzeCorrelation1l_HT500ToInf_MET250ToInf.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET250ToInf.METCut = 250.,9999.

## clone and configure modules for HT > 500 und different exclusive MET cuts
analyzeCorrelation1l_HT500ToInf_MET0To50    = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET50To100  = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET100To150 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET150To200 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500ToInf_MET200To250 = analyzeCorrelation.clone()
    
analyzeCorrelation1l_HT500ToInf_MET0To50.HTCut     = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET0To50.METCut    = 0.,50.

analyzeCorrelation1l_HT500ToInf_MET50To100.HTCut   = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET50To100.METCut  = 50.,100.

analyzeCorrelation1l_HT500ToInf_MET100To150.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET100To150.METCut = 100.,150.

analyzeCorrelation1l_HT500ToInf_MET150To200.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET150To200.METCut = 150.,200.

analyzeCorrelation1l_HT500ToInf_MET200To250.HTCut  = 500.,9999.
analyzeCorrelation1l_HT500ToInf_MET200To250.METCut = 200.,250.

## clone and configure modules for HT > 600 und different inclusive MET cuts
analyzeCorrelation1l_HT600ToInf_MET0ToInf   = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET50ToInf  = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET100ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET150ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET200ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET250ToInf = analyzeCorrelation.clone()

analyzeCorrelation1l_HT600ToInf_MET0ToInf.HTCut    = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET0ToInf.METCut   = 0.,9999.

analyzeCorrelation1l_HT600ToInf_MET50ToInf.HTCut   = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET50ToInf.METCut  = 50.,9999.

analyzeCorrelation1l_HT600ToInf_MET100ToInf.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET100ToInf.METCut = 100.,9999.

analyzeCorrelation1l_HT600ToInf_MET150ToInf.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET150ToInf.METCut = 150.,9999.

analyzeCorrelation1l_HT600ToInf_MET200ToInf.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET200ToInf.METCut = 200.,9999.

analyzeCorrelation1l_HT600ToInf_MET250ToInf.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET250ToInf.METCut = 250.,9999.

## clone and configure modules for HT > 600 und different exclusive MET cuts
analyzeCorrelation1l_HT600ToInf_MET0To50    = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET50To100  = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET100To150 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET150To200 = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET200To250 = analyzeCorrelation.clone()
    
analyzeCorrelation1l_HT600ToInf_MET0To50.HTCut     = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET0To50.METCut    = 0.,50.

analyzeCorrelation1l_HT600ToInf_MET50To100.HTCut   = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET50To100.METCut  = 50.,100.

analyzeCorrelation1l_HT600ToInf_MET100To150.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET100To150.METCut = 100.,150.

analyzeCorrelation1l_HT600ToInf_MET150To200.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET150To200.METCut = 150.,200.

analyzeCorrelation1l_HT600ToInf_MET200To250.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET200To250.METCut = 200.,250.

## clone and configure modules for different exclusive HT and exclusive MET cuts
analyzeCorrelation1l_HT300To400_MET0To50      = analyzeCorrelation.clone()
analyzeCorrelation1l_HT300To400_MET50To100    = analyzeCorrelation.clone()
analyzeCorrelation1l_HT300To400_MET100To150   = analyzeCorrelation.clone()

analyzeCorrelation1l_HT400To500_MET0To50      = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400To500_MET50To100    = analyzeCorrelation.clone()
analyzeCorrelation1l_HT400To500_MET100To150   = analyzeCorrelation.clone()

analyzeCorrelation1l_HT500To600_MET0To50      = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500To600_MET50To100    = analyzeCorrelation.clone()
analyzeCorrelation1l_HT500To600_MET100To150   = analyzeCorrelation.clone()

analyzeCorrelation1l_HT300To400_MET0To50.HTCut     = 300.,400.
analyzeCorrelation1l_HT300To400_MET0To50.METCut    = 0.,50.

analyzeCorrelation1l_HT300To400_MET50To100.HTCut   = 300.,400.
analyzeCorrelation1l_HT300To400_MET50To100.METCut  = 50.,100.

analyzeCorrelation1l_HT300To400_MET100To150.HTCut  = 300.,400.
analyzeCorrelation1l_HT300To400_MET100To150.METCut = 100.,150.

analyzeCorrelation1l_HT400To500_MET0To50.HTCut     = 400.,500.
analyzeCorrelation1l_HT400To500_MET0To50.METCut    = 0.,50.

analyzeCorrelation1l_HT400To500_MET50To100.HTCut   = 400.,500.
analyzeCorrelation1l_HT400To500_MET50To100.METCut  = 50.,100.

analyzeCorrelation1l_HT400To500_MET100To150.HTCut  = 400.,500.
analyzeCorrelation1l_HT400To500_MET100To150.METCut = 100.,150.

analyzeCorrelation1l_HT500To600_MET0To50.HTCut     = 500.,600.
analyzeCorrelation1l_HT500To600_MET0To50.METCut    = 0.,50.

analyzeCorrelation1l_HT500To600_MET50To100.HTCut   = 500.,600.
analyzeCorrelation1l_HT500To600_MET50To100.METCut  = 50.,100.

analyzeCorrelation1l_HT500To600_MET100To150.HTCut  = 500.,600.
analyzeCorrelation1l_HT500To600_MET100To150.METCut = 100.,150.

## clone and configure modules for HT > 600, MET > 150 and different inclusive nJets cuts
analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets3ToInf = analyzeCorrelation.clone()
analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets4ToInf = analyzeCorrelation.clone()

analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets3ToInf.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets3ToInf.METCut = 150.,9999.
analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets3ToInf.nJetsCut = 3,99

analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets4ToInf.HTCut  = 600.,9999.
analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets4ToInf.METCut = 150.,9999.
analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets4ToInf.nJetsCut = 4,99

## clone and configure modules for analysis after kin fit
analyzeCorrelation1m_KinFitHadWMass           = analyzeCorrelation.clone()
analyzeCorrelation1m_KinFitHadWMass.TTJetsHyp = True
analyzeCorrelation1m_KinFitHadWMass.TtSemiLepEvent = "ttSemiLepEventHadWMass"

analyzeCorrelation1m_KinFitHadWMass_nJets4 = analyzeCorrelation1m_KinFitHadWMass.clone()
analyzeCorrelation1m_KinFitHadWMass_nJets5 = analyzeCorrelation1m_KinFitHadWMass.clone()
analyzeCorrelation1m_KinFitHadWMass_nJets6 = analyzeCorrelation1m_KinFitHadWMass.clone()

analyzeCorrelation1m_KinFitHadWMass_nJets4.nJetsCut = 4,4
analyzeCorrelation1m_KinFitHadWMass_nJets5.nJetsCut = 5,5
analyzeCorrelation1m_KinFitHadWMass_nJets6.nJetsCut = 6,6

## clone modules for muon channel
analyzeCorrelation1m_noCuts          = analyzeCorrelation.clone()
analyzeCorrelation1m_preselection    = analyzeCorrelation.clone()
analyzeCorrelation1m_leptonSelection = analyzeCorrelation.clone()
analyzeCorrelation1m_jetSelection    = analyzeCorrelation.clone()

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

# clone modules for muon channel
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

# clone modules for electron channel
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
analyzeTtGenEvent1l_mTSelection_TTJets      = analyzeTtGenEvent.clone()

analyzeTtGenEvent1l_noCuts_SemiLep          = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_preselection_SemiLep    = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_leptonSelection_SemiLep = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_jetSelection_SemiLep    = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_HTSelection_SemiLep     = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_METSelection_SemiLep    = analyzeTtGenEvent.clone()
analyzeTtGenEvent1l_mTSelection_SemiLep     = analyzeTtGenEvent.clone()

