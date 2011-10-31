#!/bin/bash

cp ../Btagging/Configuration/naf_TTJets_cfg/AnalyzeBtags.root ./TTJets.root

rm SingleTop.root
cp ../Btagging/Configuration/naf_Tbar_sChannel_cfg/AnalyzeBtags.root ./Top1.root
cp ../Btagging/Configuration/naf_Tbar_tChannel_cfg/AnalyzeBtags.root ./Top2.root
cp ../Btagging/Configuration/naf_Tbar_tW_cfg/AnalyzeBtags.root ./Top3.root
cp ../Btagging/Configuration/naf_Top_sChannel_cfg/AnalyzeBtags.root ./Top4.root
cp ../Btagging/Configuration/naf_Top_tChannel_cfg/AnalyzeBtags.root ./Top5.root
cp ../Btagging/Configuration/naf_Top_tW_cfg/AnalyzeBtags.root ./Top6.root

hadd SingleTop.root Top*.root 
rm Top*.root

rm WJets*.root
cp ../Btagging/Configuration/naf_WJets_cfg_1/AnalyzeBtags.root ./WJets_1.root
cp ../Btagging/Configuration/naf_WJets_cfg_2/AnalyzeBtags.root ./WJets_2.root
hadd WJets.root WJets_?.root
rm WJets_*.root

rm DY*.root
cp ../Btagging/Configuration/naf_DY_cfg_1/AnalyzeBtags.root ./DY_1.root
cp ../Btagging/Configuration/naf_DY_cfg_2/AnalyzeBtags.root ./DY_2.root
hadd DY.root DY_?.root
rm DY_*.root

rm QCD*.root
cp ../Btagging/Configuration/naf_QCD_cfg_1/AnalyzeBtags.root ./QCD_1.root
cp ../Btagging/Configuration/naf_QCD_cfg_2/AnalyzeBtags.root ./QCD_2.root
hadd QCD.root QCD_?.root
rm QCD_*.root 

rm MuHad*.root
cp ../Btagging/Configuration/naf_MuHad_May10_cfg/AnalyzeBtags.root ./MuHad_1.root
cp ../Btagging/Configuration/naf_MuHad1_v4_cfg/AnalyzeBtags.root ./MuHad_3.root
cp ../Btagging/Configuration/naf_MuHad2_v4_cfg/AnalyzeBtags.root ./MuHad_4.root
hadd MuHad.root MuHad_?.root
rm MuHad_*.root
