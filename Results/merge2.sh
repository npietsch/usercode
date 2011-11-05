#!/bin/bash

rm BtagEff_TTJets.root
cp ../Btagging/Configuration/naf_TTJets_cfg/BtagEff.root ./BtagEff_TTJets.root

rm BtagEff_SingleTop.root
cp ../Btagging/Configuration/naf_Tbar_sChannel_cfg/BtagEff.root ./Top_1.root
cp ../Btagging/Configuration/naf_Tbar_tChannel_cfg/BtagEff.root ./Top_2.root
cp ../Btagging/Configuration/naf_Tbar_tW_cfg/BtagEff.root ./Top_3.root
cp ../Btagging/Configuration/naf_Top_sChannel_cfg/BtagEff.root ./Top_4.root
cp ../Btagging/Configuration/naf_Top_tChannel_cfg/BtagEff.root ./Top_5.root
cp ../Btagging/Configuration/naf_Top_tW_cfg/BtagEff.root ./Top_6.root
hadd BtagEff_SingleTop.root Top_?.root 
rm Top_*.root

rm BtagEff_WJets*.root
cp ../Btagging/Configuration/naf_WJets1_cfg/BtagEff.root ./WJets_1.root
cp ../Btagging/Configuration/naf_WJets2_cfg/BtagEff.root ./WJets_2.root
hadd BtagEff_WJets.root WJets_?.root
rm WJets_*.root

rm BtagEff_DY*.root
cp ../Btagging/Configuration/naf_DY1_cfg/BtagEff.root ./DY_1.root
cp ../Btagging/Configuration/naf_DY2_cfg/BtagEff.root ./DY_2.root
hadd BtagEff_DY.root DY_?.root
rm DY_*.root

rm BtagEff_QCD*.root
cp ../Btagging/Configuration/naf_QCD1_cfg/BtagEff.root ./QCD_1.root
cp ../Btagging/Configuration/naf_QCD2_cfg/BtagEff.root ./QCD_2.root
hadd BtagEff_QCD.root QCD_?.root
rm QCD_*.root

