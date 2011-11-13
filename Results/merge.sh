#!/bin/bash

cp ../Btagging/Configuration/naf_TTJets_cfg/AnalyzeBtags.root ./TTJets.root

rm SingleTop.root
cp ../Btagging/Configuration/naf_Tbar_sChannel_cfg/AnalyzeBtags.root ./Top_1.root
cp ../Btagging/Configuration/naf_Tbar_tChannel_cfg/AnalyzeBtags.root ./Top_2.root
cp ../Btagging/Configuration/naf_Tbar_tW_cfg/AnalyzeBtags.root ./Top_3.root
cp ../Btagging/Configuration/naf_Top_sChannel_cfg/AnalyzeBtags.root ./Top_4.root
cp ../Btagging/Configuration/naf_Top_tChannel_cfg/AnalyzeBtags.root ./Top_5.root
cp ../Btagging/Configuration/naf_Top_tW_cfg/AnalyzeBtags.root ./Top_6.root
hadd SingleTop.root Top_?.root 
rm Top_*.root

rm WJets*.root
cp ../Btagging/Configuration/naf_WJets1_cfg/AnalyzeBtags.root ./WJets_1.root
cp ../Btagging/Configuration/naf_WJets2_cfg/AnalyzeBtags.root ./WJets_2.root
hadd WJets.root WJets_?.root
rm WJets_*.root

rm DY*.root
cp ../Btagging/Configuration/naf_DY1_cfg/AnalyzeBtags.root ./DY_1.root
cp ../Btagging/Configuration/naf_DY2_cfg/AnalyzeBtags.root ./DY_2.root
hadd DY.root DY_?.root
rm DY_*.root

rm QCD*.root
cp ../Btagging/Configuration/naf_QCD1_cfg/AnalyzeBtags.root ./QCD_1.root
cp ../Btagging/Configuration/naf_QCD2_cfg/AnalyzeBtags.root ./QCD_2.root
hadd QCD.root QCD_?.root
rm QCD_*.root

rm MuHad*.root
cp ../Btagging/Configuration/naf_MuHad_May10_cfg/AnalyzeBtags.root ./MuHad_1.root
cp ../Btagging/Configuration/naf_MuHad_PromptReco1_v4_cfg/AnalyzeBtags.root ./MuHad_2.root
cp ../Btagging/Configuration/naf_MuHad_PromptReco2_v4_cfg/AnalyzeBtags.root ./MuHad_3.root
cp ../Btagging/Configuration/naf_MuHad_Aug5_cfg/AnalyzeBtags.root ./MuHad_4.root
cp ../Btagging/Configuration/naf_MuHad_PromptReco_v6_cfg/AnalyzeBtags.root ./MuHad_5.root
cp ../Btagging/Configuration/naf_RA4b_MuHad_Promtv1_2011B_cfg_1/AnalyzeBtags.root ./MuHad_6.root
cp ../Btagging/Configuration/naf_RA4b_MuHad_Promtv1_2011B_cfg_2/AnalyzeBtags.root ./MuHad_7.root
hadd MuHad.root MuHad_?.root
rm MuHad_*.root

rm ElHad*.root
cp ../Btagging/Configuration/naf_ElHad_May10_cfg/AnalyzeBtags.root ./ElHad_1.root
cp ../Btagging/Configuration/naf_ElHad_PromptReco1_v4_cfg/AnalyzeBtags.root ./ElHad_2.root
cp ../Btagging/Configuration/naf_ElHad_PromptReco2_v4_cfg/AnalyzeBtags.root ./ElHad_3.root
cp ../Btagging/Configuration/naf_ElHad_Aug5_cfg/AnalyzeBtags.root ./ElHad_4.root
cp ../Btagging/Configuration/naf_ElHad_PromptReco_v6_cfg/AnalyzeBtags.root ./ElHad_5.root
cp ../Btagging/Configuration/naf_RA4b_ElHad1_v1_Run2011B_cfg/AnalyzeBtags.root ./ElHad_6.root
cp ../Btagging/Configuration/naf_RA4b_ElHad2_v1_Run2011B_cfg/AnalyzeBtags.root ./ElHad_7.root
hadd ElHad.root ElHad_?.root
rm ElHad_*.root