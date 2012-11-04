#!/bin/bash

rm LM3.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_LM3_noPFCheck_cfg/$1 ./LM3.root

rm LM6.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_LM6_noPFCheck_cfg/$1 ./LM6.root

rm LM8.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_LM8_noPFCheck_cfg/$1 ./LM8.root

rm LM13.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_LM13_noPFCheck_cfg/$1 ./LM13.root

rm TTJetsFall11.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Fall11_TTJets1_cfg/$1 ./TTJetsFall11_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Fall11_TTJets2_cfg/$1 ./TTJetsFall11_2.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Fall11_TTJets3_cfg/$1 ./TTJetsFall11_3.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Fall11_TTJets4_cfg/$1 ./TTJetsFall11_4.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Fall11_TTJets5_cfg/$1 ./TTJetsFall11_5.root
hadd TTJetsFall11.root TTJetsFall11_?.root
rm TTJetsFall11_?.root

rm SingleTop.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Tbar_sChannel_cfg/$1 ./Top_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Tbar_tChannel_cfg/$1 ./Top_2.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Tbar_tW_cfg/$1       ./Top_3.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Top_sChannel_cfg/$1  ./Top_4.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Top_tChannel_cfg/$1  ./Top_5.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_Top_tW_cfg/$1        ./Top_6.root
hadd SingleTop.root Top_?.root 
rm Top_*.root

rm WJetsHT*.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_WJets_HT250_300_cfg_1/$1 ./WJetsHT_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_WJets_HT250_300_cfg_2/$1 ./WJetsHT_2.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_WJets_HT300_cfg_1/$1     ./WJetsHT_3.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_WJets_HT300_cfg_2/$1     ./WJetsHT_4.root
hadd WJetsHT.root WJetsHT_?.root
rm WJetsHT_*.root

rm ZJets*.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ZJets_cfg_1/$1 ./ZJets_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ZJets_cfg_2/$1 ./ZJets_2.root
hadd ZJets.root ZJets_?.root
rm ZJets_*.root

rm QCD*.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_QCD1_cfg/$1 ./QCD_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_QCD2_cfg/$1 ./QCD_2.root
hadd QCD.root QCD_?.root
rm QCD_*.root

rm MuHad*.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad_May10thReReco_cfg/$1 ./MuHad_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad_PromtReco4_cfg_1/$1  ./MuHad_2.root    
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad_PromtReco4_cfg_2/$1  ./MuHad_3.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad_Aug05thReReco_cfg/$1 ./MuHad_4.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad_PromtReco6_cfg/$1    ./MuHad_5.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad1_v1_2011_cfg/$1      ./MuHad_6.root   
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad2_v1_2011_cfg/$1      ./MuHad_7.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad3_v1_2011_cfg/$1      ./MuHad_8.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_MuHad4_v1_2011_cfg/$1      ./MuHad_9.root
hadd MuHad.root MuHad_?.root
rm MuHad_*.root


rm ElHad*.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad_May10_cfg/$1        ./ElHad_1.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad1_v4_cfg/$1          ./ElHad_2.root    
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad2_v4_cfg/$1          ./ElHad_3.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad_Aug05_cfg/$1        ./ElHad_4.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad_v6_cfg/$1           ./ElHad_5.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad1_v1_Run2011B_cfg/$1 ./ElHad_6.root   
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad2_v1_Run2011B_cfg/$1 ./ElHad_7.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad3_v1_Run2011B_cfg/$1 ./ElHad_8.root
cp ../SUSYAnalysis/Configuration/Run2011/SUS-11-028/naf_RA4b_ElHad4_v1_Run2011B_cfg/$1 ./ElHad_9.root
hadd ElHad.root ElHad_*.root
rm ElHad_*.root