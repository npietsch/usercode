from SUSYAnalysis.SUSYAnalyzer.EventTopology_cfi import *

analyzeEventTopology.met = "goodMETs"
analyzeEventTopology.jets = "goodJets"
analyzeEventTopology.muons = "goodMuons"
analyzeEventTopology.electrons = "goodElectrons"


## 1 lepton

analyzeEventTopology1l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1l_1 = cms.Sequence(analyzeEventTopology1l_looseTCHE_1*
                                        analyzeEventTopology1l_mediumTCHE_1 *
                                        analyzeEventTopology1l_tightTCHE_1 *
                                        analyzeEventTopology1l_looseTCHP_1 *
                                        analyzeEventTopology1l_mediumTCHP_1 *
                                        analyzeEventTopology1l_tightTCHP_1
                                        )

analyzeEventTopology1l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1l_2 = cms.Sequence(analyzeEventTopology1l_looseTCHE_2*
                                        analyzeEventTopology1l_mediumTCHE_2 *
                                        analyzeEventTopology1l_tightTCHE_2 *
                                        analyzeEventTopology1l_looseTCHP_2 *
                                        analyzeEventTopology1l_mediumTCHP_2 *
                                        analyzeEventTopology1l_tightTCHP_2
                                        )

analyzeEventTopology1l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1l_3 = cms.Sequence(analyzeEventTopology1l_looseTCHE_3*
                                        analyzeEventTopology1l_mediumTCHE_3 *
                                        analyzeEventTopology1l_tightTCHE_3 *
                                        analyzeEventTopology1l_looseTCHP_3 *
                                        analyzeEventTopology1l_mediumTCHP_3 *
                                        analyzeEventTopology1l_tightTCHP_3
                                        )

analyzeEventTopology1l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1l_4 = cms.Sequence(analyzeEventTopology1l_looseTCHE_4*
                                        analyzeEventTopology1l_mediumTCHE_4 *
                                        analyzeEventTopology1l_tightTCHE_4 *
                                        analyzeEventTopology1l_looseTCHP_4 *
                                        analyzeEventTopology1l_mediumTCHP_4 *
                                        analyzeEventTopology1l_tightTCHP_4
                                        )

analyzeEventTopology1l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1l_5 = cms.Sequence(analyzeEventTopology1l_looseTCHE_5*
                                        analyzeEventTopology1l_mediumTCHE_5 *
                                        analyzeEventTopology1l_tightTCHE_5 *
                                        analyzeEventTopology1l_looseTCHP_5 *
                                        analyzeEventTopology1l_mediumTCHP_5 *
                                        analyzeEventTopology1l_tightTCHP_5
                                        )

analyzeEventTopology1l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1l_6 = cms.Sequence(analyzeEventTopology1l_looseTCHE_6*
                                        analyzeEventTopology1l_mediumTCHE_6 *
                                        analyzeEventTopology1l_tightTCHE_6 *
                                        analyzeEventTopology1l_looseTCHP_6 *
                                        analyzeEventTopology1l_mediumTCHP_6 *
                                        analyzeEventTopology1l_tightTCHP_6
                                        )

## 1 lepton + 1 bjet

analyzeEventTopology1b1l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b1l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b1l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b1l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b1l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b1l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b1l_1 = cms.Sequence(analyzeEventTopology1b1l_looseTCHE_1*
                                        analyzeEventTopology1b1l_mediumTCHE_1 *
                                        analyzeEventTopology1b1l_tightTCHE_1 *
                                        analyzeEventTopology1b1l_looseTCHP_1 *
                                        analyzeEventTopology1b1l_mediumTCHP_1 *
                                        analyzeEventTopology1b1l_tightTCHP_1
                                        )

analyzeEventTopology1b1l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b1l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b1l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b1l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b1l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b1l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b1l_2 = cms.Sequence(analyzeEventTopology1b1l_looseTCHE_2*
                                        analyzeEventTopology1b1l_mediumTCHE_2 *
                                        analyzeEventTopology1b1l_tightTCHE_2 *
                                        analyzeEventTopology1b1l_looseTCHP_2 *
                                        analyzeEventTopology1b1l_mediumTCHP_2 *
                                        analyzeEventTopology1b1l_tightTCHP_2
                                        )

analyzeEventTopology1b1l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b1l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b1l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b1l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b1l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b1l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b1l_3 = cms.Sequence(analyzeEventTopology1b1l_looseTCHE_3*
                                        analyzeEventTopology1b1l_mediumTCHE_3 *
                                        analyzeEventTopology1b1l_tightTCHE_3 *
                                        analyzeEventTopology1b1l_looseTCHP_3 *
                                        analyzeEventTopology1b1l_mediumTCHP_3 *
                                        analyzeEventTopology1b1l_tightTCHP_3
                                        )

analyzeEventTopology1b1l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b1l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b1l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b1l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b1l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b1l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b1l_4 = cms.Sequence(analyzeEventTopology1b1l_looseTCHE_4*
                                        analyzeEventTopology1b1l_mediumTCHE_4 *
                                        analyzeEventTopology1b1l_tightTCHE_4 *
                                        analyzeEventTopology1b1l_looseTCHP_4 *
                                        analyzeEventTopology1b1l_mediumTCHP_4 *
                                        analyzeEventTopology1b1l_tightTCHP_4
                                        )

analyzeEventTopology1b1l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b1l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b1l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b1l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b1l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b1l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b1l_5 = cms.Sequence(analyzeEventTopology1b1l_looseTCHE_5*
                                        analyzeEventTopology1b1l_mediumTCHE_5 *
                                        analyzeEventTopology1b1l_tightTCHE_5 *
                                        analyzeEventTopology1b1l_looseTCHP_5 *
                                        analyzeEventTopology1b1l_mediumTCHP_5 *
                                        analyzeEventTopology1b1l_tightTCHP_5
                                        )

analyzeEventTopology1b1l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b1l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b1l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b1l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b1l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b1l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1b1l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b1l_6 = cms.Sequence(analyzeEventTopology1b1l_looseTCHE_6*
                                        analyzeEventTopology1b1l_mediumTCHE_6 *
                                        analyzeEventTopology1b1l_tightTCHE_6 *
                                        analyzeEventTopology1b1l_looseTCHP_6 *
                                        analyzeEventTopology1b1l_mediumTCHP_6 *
                                        analyzeEventTopology1b1l_tightTCHP_6
                                        )


## 1 lepton + 2 bjets

analyzeEventTopology2b1l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b1l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b1l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b1l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b1l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b1l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b1l_1 = cms.Sequence(analyzeEventTopology2b1l_looseTCHE_1*
                                        analyzeEventTopology2b1l_mediumTCHE_1 *
                                        analyzeEventTopology2b1l_tightTCHE_1 *
                                        analyzeEventTopology2b1l_looseTCHP_1 *
                                        analyzeEventTopology2b1l_mediumTCHP_1 *
                                        analyzeEventTopology2b1l_tightTCHP_1
                                        )

analyzeEventTopology2b1l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b1l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b1l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b1l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b1l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b1l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b1l_2 = cms.Sequence(analyzeEventTopology2b1l_looseTCHE_2*
                                        analyzeEventTopology2b1l_mediumTCHE_2 *
                                        analyzeEventTopology2b1l_tightTCHE_2 *
                                        analyzeEventTopology2b1l_looseTCHP_2 *
                                        analyzeEventTopology2b1l_mediumTCHP_2 *
                                        analyzeEventTopology2b1l_tightTCHP_2
                                        )

analyzeEventTopology2b1l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b1l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b1l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b1l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b1l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b1l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b1l_3 = cms.Sequence(analyzeEventTopology2b1l_looseTCHE_3*
                                        analyzeEventTopology2b1l_mediumTCHE_3 *
                                        analyzeEventTopology2b1l_tightTCHE_3 *
                                        analyzeEventTopology2b1l_looseTCHP_3 *
                                        analyzeEventTopology2b1l_mediumTCHP_3 *
                                        analyzeEventTopology2b1l_tightTCHP_3
                                        )

analyzeEventTopology2b1l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b1l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b1l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b1l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b1l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b1l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b1l_4 = cms.Sequence(analyzeEventTopology2b1l_looseTCHE_4*
                                        analyzeEventTopology2b1l_mediumTCHE_4 *
                                        analyzeEventTopology2b1l_tightTCHE_4 *
                                        analyzeEventTopology2b1l_looseTCHP_4 *
                                        analyzeEventTopology2b1l_mediumTCHP_4 *
                                        analyzeEventTopology2b1l_tightTCHP_4
                                        )

analyzeEventTopology2b1l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b1l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b1l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b1l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b1l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b1l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b1l_5 = cms.Sequence(analyzeEventTopology2b1l_looseTCHE_5*
                                        analyzeEventTopology2b1l_mediumTCHE_5 *
                                        analyzeEventTopology2b1l_tightTCHE_5 *
                                        analyzeEventTopology2b1l_looseTCHP_5 *
                                        analyzeEventTopology2b1l_mediumTCHP_5 *
                                        analyzeEventTopology2b1l_tightTCHP_5
                                        )

analyzeEventTopology2b1l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b1l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b1l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b1l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b1l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b1l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2b1l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b1l_6 = cms.Sequence(analyzeEventTopology2b1l_looseTCHE_6*
                                        analyzeEventTopology2b1l_mediumTCHE_6 *
                                        analyzeEventTopology2b1l_tightTCHE_6 *
                                        analyzeEventTopology2b1l_looseTCHP_6 *
                                        analyzeEventTopology2b1l_mediumTCHP_6 *
                                        analyzeEventTopology2b1l_tightTCHP_6
                                        )

## 1 lepton + 3 bjets

analyzeEventTopology3b1l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b1l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b1l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b1l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b1l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b1l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b1l_1 = cms.Sequence(analyzeEventTopology3b1l_looseTCHE_1*
                                        analyzeEventTopology3b1l_mediumTCHE_1 *
                                        analyzeEventTopology3b1l_tightTCHE_1 *
                                        analyzeEventTopology3b1l_looseTCHP_1 *
                                        analyzeEventTopology3b1l_mediumTCHP_1 *
                                        analyzeEventTopology3b1l_tightTCHP_1
                                        )

analyzeEventTopology3b1l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b1l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b1l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b1l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b1l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b1l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b1l_2 = cms.Sequence(analyzeEventTopology3b1l_looseTCHE_2*
                                        analyzeEventTopology3b1l_mediumTCHE_2 *
                                        analyzeEventTopology3b1l_tightTCHE_2 *
                                        analyzeEventTopology3b1l_looseTCHP_2 *
                                        analyzeEventTopology3b1l_mediumTCHP_2 *
                                        analyzeEventTopology3b1l_tightTCHP_2
                                        )

analyzeEventTopology3b1l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b1l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b1l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b1l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b1l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b1l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b1l_3 = cms.Sequence(analyzeEventTopology3b1l_looseTCHE_3*
                                        analyzeEventTopology3b1l_mediumTCHE_3 *
                                        analyzeEventTopology3b1l_tightTCHE_3 *
                                        analyzeEventTopology3b1l_looseTCHP_3 *
                                        analyzeEventTopology3b1l_mediumTCHP_3 *
                                        analyzeEventTopology3b1l_tightTCHP_3
                                        )

analyzeEventTopology3b1l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b1l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b1l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b1l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b1l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b1l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b1l_4 = cms.Sequence(analyzeEventTopology3b1l_looseTCHE_4*
                                        analyzeEventTopology3b1l_mediumTCHE_4 *
                                        analyzeEventTopology3b1l_tightTCHE_4 *
                                        analyzeEventTopology3b1l_looseTCHP_4 *
                                        analyzeEventTopology3b1l_mediumTCHP_4 *
                                        analyzeEventTopology3b1l_tightTCHP_4
                                        )

analyzeEventTopology3b1l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b1l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b1l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b1l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b1l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b1l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b1l_5 = cms.Sequence(analyzeEventTopology3b1l_looseTCHE_5*
                                        analyzeEventTopology3b1l_mediumTCHE_5 *
                                        analyzeEventTopology3b1l_tightTCHE_5 *
                                        analyzeEventTopology3b1l_looseTCHP_5 *
                                        analyzeEventTopology3b1l_mediumTCHP_5 *
                                        analyzeEventTopology3b1l_tightTCHP_5
                                        )

analyzeEventTopology3b1l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b1l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b1l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b1l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b1l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b1l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology3b1l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b1l_6 = cms.Sequence(analyzeEventTopology3b1l_looseTCHE_6*
                                        analyzeEventTopology3b1l_mediumTCHE_6 *
                                        analyzeEventTopology3b1l_tightTCHE_6 *
                                        analyzeEventTopology3b1l_looseTCHP_6 *
                                        analyzeEventTopology3b1l_mediumTCHP_6 *
                                        analyzeEventTopology3b1l_tightTCHP_6
                                        )


## 2 lepton

analyzeEventTopology2l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2l_1 = cms.Sequence(analyzeEventTopology2l_looseTCHE_1*
                                        analyzeEventTopology2l_mediumTCHE_1 *
                                        analyzeEventTopology2l_tightTCHE_1 *
                                        analyzeEventTopology2l_looseTCHP_1 *
                                        analyzeEventTopology2l_mediumTCHP_1 *
                                        analyzeEventTopology2l_tightTCHP_1
                                        )

analyzeEventTopology2l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2l_2 = cms.Sequence(analyzeEventTopology2l_looseTCHE_2*
                                        analyzeEventTopology2l_mediumTCHE_2 *
                                        analyzeEventTopology2l_tightTCHE_2 *
                                        analyzeEventTopology2l_looseTCHP_2 *
                                        analyzeEventTopology2l_mediumTCHP_2 *
                                        analyzeEventTopology2l_tightTCHP_2
                                        )

analyzeEventTopology2l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2l_3 = cms.Sequence(analyzeEventTopology2l_looseTCHE_3*
                                        analyzeEventTopology2l_mediumTCHE_3 *
                                        analyzeEventTopology2l_tightTCHE_3 *
                                        analyzeEventTopology2l_looseTCHP_3 *
                                        analyzeEventTopology2l_mediumTCHP_3 *
                                        analyzeEventTopology2l_tightTCHP_3
                                        )

analyzeEventTopology2l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2l_4 = cms.Sequence(analyzeEventTopology2l_looseTCHE_4*
                                        analyzeEventTopology2l_mediumTCHE_4 *
                                        analyzeEventTopology2l_tightTCHE_4 *
                                        analyzeEventTopology2l_looseTCHP_4 *
                                        analyzeEventTopology2l_mediumTCHP_4 *
                                        analyzeEventTopology2l_tightTCHP_4
                                        )

analyzeEventTopology2l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2l_5 = cms.Sequence(analyzeEventTopology2l_looseTCHE_5*
                                        analyzeEventTopology2l_mediumTCHE_5 *
                                        analyzeEventTopology2l_tightTCHE_5 *
                                        analyzeEventTopology2l_looseTCHP_5 *
                                        analyzeEventTopology2l_mediumTCHP_5 *
                                        analyzeEventTopology2l_tightTCHP_5
                                        )

analyzeEventTopology2l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2l_6 = cms.Sequence(analyzeEventTopology2l_looseTCHE_6*
                                        analyzeEventTopology2l_mediumTCHE_6 *
                                        analyzeEventTopology2l_tightTCHE_6 *
                                        analyzeEventTopology2l_looseTCHP_6 *
                                        analyzeEventTopology2l_mediumTCHP_6 *
                                        analyzeEventTopology2l_tightTCHP_6
                                        )

## 2 lepton + 1 bjet

analyzeEventTopology1b2l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b2l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b2l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b2l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b2l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b2l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b2l_1 = cms.Sequence(analyzeEventTopology1b2l_looseTCHE_1*
                                        analyzeEventTopology1b2l_mediumTCHE_1 *
                                        analyzeEventTopology1b2l_tightTCHE_1 *
                                        analyzeEventTopology1b2l_looseTCHP_1 *
                                        analyzeEventTopology1b2l_mediumTCHP_1 *
                                        analyzeEventTopology1b2l_tightTCHP_1
                                        )

analyzeEventTopology1b2l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b2l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b2l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b2l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b2l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b2l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b2l_2 = cms.Sequence(analyzeEventTopology1b2l_looseTCHE_2*
                                        analyzeEventTopology1b2l_mediumTCHE_2 *
                                        analyzeEventTopology1b2l_tightTCHE_2 *
                                        analyzeEventTopology1b2l_looseTCHP_2 *
                                        analyzeEventTopology1b2l_mediumTCHP_2 *
                                        analyzeEventTopology1b2l_tightTCHP_2
                                        )

analyzeEventTopology1b2l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b2l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b2l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b2l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b2l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b2l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b2l_3 = cms.Sequence(analyzeEventTopology1b2l_looseTCHE_3*
                                        analyzeEventTopology1b2l_mediumTCHE_3 *
                                        analyzeEventTopology1b2l_tightTCHE_3 *
                                        analyzeEventTopology1b2l_looseTCHP_3 *
                                        analyzeEventTopology1b2l_mediumTCHP_3 *
                                        analyzeEventTopology1b2l_tightTCHP_3
                                        )

analyzeEventTopology1b2l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b2l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b2l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b2l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b2l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b2l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b2l_4 = cms.Sequence(analyzeEventTopology1b2l_looseTCHE_4*
                                        analyzeEventTopology1b2l_mediumTCHE_4 *
                                        analyzeEventTopology1b2l_tightTCHE_4 *
                                        analyzeEventTopology1b2l_looseTCHP_4 *
                                        analyzeEventTopology1b2l_mediumTCHP_4 *
                                        analyzeEventTopology1b2l_tightTCHP_4
                                        )

analyzeEventTopology1b2l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b2l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b2l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b2l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b2l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b2l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b2l_5 = cms.Sequence(analyzeEventTopology1b2l_looseTCHE_5*
                                        analyzeEventTopology1b2l_mediumTCHE_5 *
                                        analyzeEventTopology1b2l_tightTCHE_5 *
                                        analyzeEventTopology1b2l_looseTCHP_5 *
                                        analyzeEventTopology1b2l_mediumTCHP_5 *
                                        analyzeEventTopology1b2l_tightTCHP_5
                                        )

analyzeEventTopology1b2l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology1b2l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology1b2l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology1b2l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology1b2l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology1b2l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology1b2l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology1b2l_6 = cms.Sequence(analyzeEventTopology1b2l_looseTCHE_6*
                                        analyzeEventTopology1b2l_mediumTCHE_6 *
                                        analyzeEventTopology1b2l_tightTCHE_6 *
                                        analyzeEventTopology1b2l_looseTCHP_6 *
                                        analyzeEventTopology1b2l_mediumTCHP_6 *
                                        analyzeEventTopology1b2l_tightTCHP_6
                                        )


## 2 lepton + 2 bjets

analyzeEventTopology2b2l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b2l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b2l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b2l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b2l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b2l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b2l_1 = cms.Sequence(analyzeEventTopology2b2l_looseTCHE_1*
                                        analyzeEventTopology2b2l_mediumTCHE_1 *
                                        analyzeEventTopology2b2l_tightTCHE_1 *
                                        analyzeEventTopology2b2l_looseTCHP_1 *
                                        analyzeEventTopology2b2l_mediumTCHP_1 *
                                        analyzeEventTopology2b2l_tightTCHP_1
                                        )

analyzeEventTopology2b2l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b2l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b2l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b2l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b2l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b2l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b2l_2 = cms.Sequence(analyzeEventTopology2b2l_looseTCHE_2*
                                        analyzeEventTopology2b2l_mediumTCHE_2 *
                                        analyzeEventTopology2b2l_tightTCHE_2 *
                                        analyzeEventTopology2b2l_looseTCHP_2 *
                                        analyzeEventTopology2b2l_mediumTCHP_2 *
                                        analyzeEventTopology2b2l_tightTCHP_2
                                        )

analyzeEventTopology2b2l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b2l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b2l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b2l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b2l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b2l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b2l_3 = cms.Sequence(analyzeEventTopology2b2l_looseTCHE_3*
                                        analyzeEventTopology2b2l_mediumTCHE_3 *
                                        analyzeEventTopology2b2l_tightTCHE_3 *
                                        analyzeEventTopology2b2l_looseTCHP_3 *
                                        analyzeEventTopology2b2l_mediumTCHP_3 *
                                        analyzeEventTopology2b2l_tightTCHP_3
                                        )

analyzeEventTopology2b2l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b2l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b2l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b2l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b2l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b2l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b2l_4 = cms.Sequence(analyzeEventTopology2b2l_looseTCHE_4*
                                        analyzeEventTopology2b2l_mediumTCHE_4 *
                                        analyzeEventTopology2b2l_tightTCHE_4 *
                                        analyzeEventTopology2b2l_looseTCHP_4 *
                                        analyzeEventTopology2b2l_mediumTCHP_4 *
                                        analyzeEventTopology2b2l_tightTCHP_4
                                        )

analyzeEventTopology2b2l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b2l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b2l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b2l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b2l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b2l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b2l_5 = cms.Sequence(analyzeEventTopology2b2l_looseTCHE_5*
                                        analyzeEventTopology2b2l_mediumTCHE_5 *
                                        analyzeEventTopology2b2l_tightTCHE_5 *
                                        analyzeEventTopology2b2l_looseTCHP_5 *
                                        analyzeEventTopology2b2l_mediumTCHP_5 *
                                        analyzeEventTopology2b2l_tightTCHP_5
                                        )

analyzeEventTopology2b2l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology2b2l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology2b2l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology2b2l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology2b2l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology2b2l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology2b2l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology2b2l_6 = cms.Sequence(analyzeEventTopology2b2l_looseTCHE_6*
                                        analyzeEventTopology2b2l_mediumTCHE_6 *
                                        analyzeEventTopology2b2l_tightTCHE_6 *
                                        analyzeEventTopology2b2l_looseTCHP_6 *
                                        analyzeEventTopology2b2l_mediumTCHP_6 *
                                        analyzeEventTopology2b2l_tightTCHP_6
                                        )

## 2 lepton + 3 bjets

analyzeEventTopology3b2l_looseTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHE_1.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b2l_mediumTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHE_1.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b2l_tightTCHE_1 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHE_1.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b2l_looseTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHP_1.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b2l_mediumTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHP_1.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b2l_tightTCHP_1 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHP_1.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b2l_1 = cms.Sequence(analyzeEventTopology3b2l_looseTCHE_1*
                                        analyzeEventTopology3b2l_mediumTCHE_1 *
                                        analyzeEventTopology3b2l_tightTCHE_1 *
                                        analyzeEventTopology3b2l_looseTCHP_1 *
                                        analyzeEventTopology3b2l_mediumTCHP_1 *
                                        analyzeEventTopology3b2l_tightTCHP_1
                                        )

analyzeEventTopology3b2l_looseTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHE_2.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b2l_mediumTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHE_2.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b2l_tightTCHE_2 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHE_2.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b2l_looseTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHP_2.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b2l_mediumTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHP_2.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b2l_tightTCHP_2 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHP_2.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b2l_2 = cms.Sequence(analyzeEventTopology3b2l_looseTCHE_2*
                                        analyzeEventTopology3b2l_mediumTCHE_2 *
                                        analyzeEventTopology3b2l_tightTCHE_2 *
                                        analyzeEventTopology3b2l_looseTCHP_2 *
                                        analyzeEventTopology3b2l_mediumTCHP_2 *
                                        analyzeEventTopology3b2l_tightTCHP_2
                                        )

analyzeEventTopology3b2l_looseTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHE_3.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b2l_mediumTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHE_3.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b2l_tightTCHE_3 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHE_3.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b2l_looseTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHP_3.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b2l_mediumTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHP_3.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b2l_tightTCHP_3 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHP_3.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b2l_3 = cms.Sequence(analyzeEventTopology3b2l_looseTCHE_3*
                                        analyzeEventTopology3b2l_mediumTCHE_3 *
                                        analyzeEventTopology3b2l_tightTCHE_3 *
                                        analyzeEventTopology3b2l_looseTCHP_3 *
                                        analyzeEventTopology3b2l_mediumTCHP_3 *
                                        analyzeEventTopology3b2l_tightTCHP_3
                                        )

analyzeEventTopology3b2l_looseTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHE_4.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b2l_mediumTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHE_4.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b2l_tightTCHE_4 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHE_4.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b2l_looseTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHP_4.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b2l_mediumTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHP_4.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b2l_tightTCHP_4 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHP_4.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b2l_4 = cms.Sequence(analyzeEventTopology3b2l_looseTCHE_4*
                                        analyzeEventTopology3b2l_mediumTCHE_4 *
                                        analyzeEventTopology3b2l_tightTCHE_4 *
                                        analyzeEventTopology3b2l_looseTCHP_4 *
                                        analyzeEventTopology3b2l_mediumTCHP_4 *
                                        analyzeEventTopology3b2l_tightTCHP_4
                                        )

analyzeEventTopology3b2l_looseTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHE_5.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b2l_mediumTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHE_5.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b2l_tightTCHE_5 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHE_5.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b2l_looseTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHP_5.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b2l_mediumTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHP_5.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b2l_tightTCHP_5 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHP_5.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b2l_5 = cms.Sequence(analyzeEventTopology3b2l_looseTCHE_5*
                                        analyzeEventTopology3b2l_mediumTCHE_5 *
                                        analyzeEventTopology3b2l_tightTCHE_5 *
                                        analyzeEventTopology3b2l_looseTCHP_5 *
                                        analyzeEventTopology3b2l_mediumTCHP_5 *
                                        analyzeEventTopology3b2l_tightTCHP_5
                                        )

analyzeEventTopology3b2l_looseTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHE_6.bjets = "looseTrackHighEffBjets"
analyzeEventTopology3b2l_mediumTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHE_6.bjets = "mediumTrackHighEffBjets"
analyzeEventTopology3b2l_tightTCHE_6 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHE_6.bjets = "tightTrackHighEffBjets"
analyzeEventTopology3b2l_looseTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_looseTCHP_6.bjets = "looseTrackHighPurBjets"
analyzeEventTopology3b2l_mediumTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_mediumTCHP_6.bjets = "mediumTrackHighPurBjets"
analyzeEventTopology3b2l_tightTCHP_6 = analyzeEventTopology.clone()
analyzeEventTopology3b2l_tightTCHP_6.bjets = "tightTrackHighPurBjets"
analyzeEventTopology3b2l_6 = cms.Sequence(analyzeEventTopology3b2l_looseTCHE_6*
                                        analyzeEventTopology3b2l_mediumTCHE_6 *
                                        analyzeEventTopology3b2l_tightTCHE_6 *
                                        analyzeEventTopology3b2l_looseTCHP_6 *
                                        analyzeEventTopology3b2l_mediumTCHP_6 *
                                        analyzeEventTopology3b2l_tightTCHP_6
                                        )
