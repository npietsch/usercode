#!/bin/bash

#cp naf_Bjets_LM12_cfg/Bjets.root $1/Bjets_LM12.root
cp naf_Bjets_LM9_cfg/Bjets.root $1/Bjets_LM9.root
cp naf_Bjets_LM8_cfg/Bjets.root $1/Bjets_LM8.root
#cp naf_Bjets_LM7_cfg/Bjets.root $1/Bjets_LM7.root
cp naf_Bjets_LM3_cfg/Bjets.root $1/Bjets_LM3.root
cp naf_Bjets_LM1_cfg/Bjets.root $1/Bjets_LM1.root

#cp naf_Bjets_GluinoOSET400_cfg/Bjets.root $1/Bjets_GluinoOSET400.root
#cp naf_Bjets_GluinoOSET450_cfg/Bjets.root $1/Bjets_GluinoOSET450.root
#cp naf_Bjets_GluinoOSET500_cfg/Bjets.root $1/Bjets_GluinoOSET500.root
#cp naf_Bjets_GluinoOSET550_cfg/Bjets.root $1/Bjets_GluinoOSET550.root
#cp naf_Bjets_GluinoOSET600_cfg/Bjets.root $1/Bjets_GluinoOSET600.root
#cp naf_Bjets_GluinoOSET650_cfg/Bjets.root $1/Bjets_GluinoOSET650.root
#cp naf_Bjets_GluinoOSET700_cfg/Bjets.root $1/Bjets_GluinoOSET700.root
#cp naf_Bjets_GluinoOSET750_cfg/Bjets.root $1/Bjets_GluinoOSET750.root
#cp naf_Bjets_GluinoOSET800_cfg/Bjets.root $1/Bjets_GluinoOSET800.root

#cp naf_Bjets_tbGluinoOSET400_cfg/Bjets.root $1/Bjets_tbGluinoOSET400.root
#cp naf_Bjets_tbGluinoOSET450_cfg/Bjets.root $1/Bjets_tbGluinoOSET450.root
#cp naf_Bjets_tbGluinoOSET500_cfg/Bjets.root $1/Bjets_tbGluinoOSET500.root
#cp naf_Bjets_tbGluinoOSET550_cfg/Bjets.root $1/Bjets_tbGluinoOSET550.root
#cp naf_Bjets_tbGluinoOSET600_cfg/Bjets.root $1/Bjets_tbGluinoOSET600.root
#cp naf_Bjets_tbGluinoOSET650_cfg/Bjets.root $1/Bjets_tbGluinoOSET650.root
#cp naf_Bjets_tbGluinoOSET700_cfg/Bjets.root $1/Bjets_tbGluinoOSET700.root
#cp naf_Bjets_tbGluinoOSET750_cfg/Bjets.root $1/Bjets_tbGluinoOSET750.root
#cp naf_Bjets_tbGluinoOSET800_cfg/Bjets.root $1/Bjets_tbGluinoOSET800.root

cp naf_Bjets_TTJets_cfg/Bjets.root $1/Bjets_TTJets.root
cp naf_Bjets_TTJetsSemiMuon_cfg/Bjets.root $1/Bjets_TTJetsSemiMuon.root
cp naf_Bjets_TTJetsOther_cfg/Bjets.root $1/Bjets_TTJetsOther.root
cp naf_Bjets_Wjets_cfg/Bjets.root $1/Bjets_Wjets.root
cp naf_Bjets_Zjets_cfg/Bjets.root $1/Bjets_Zjets.root

cp naf_Bjets_QCDMu_cfg/Bjets.root ./Bjets_QCDMu1.root
cp naf_Bjets_QCDMu2_cfg/Bjets.root ./Bjets_QCDMu2.root
hadd Bjets_QCDMu.root Bjets_QCDMu?.root
cp Bjets_QCDMu.root $1/Bjets_QCDMu.root
rm Bjets_QCDMu.root
rm Bjets_QCDMu1.root
rm Bjets_QCDMu2.root

cp naf_Bjets_MuHad_v1_cfg/Bjets.root ./Bjets_MuHad1.root
cp naf_Bjets_MuHad_v2_cfg/Bjets.root ./Bjets_MuHad2.root
cp naf_Bjets_MuHad2_v2_cfg/Bjets.root ./Bjets_MuHad3.root
hadd Bjets_Mu.root Bjets_MuHad*.root
cp Bjets_Mu.root $1/Bjets_Mu.root
rm Bjets_Mu.root
rm Bjets_MuHad1.root
rm Bjets_MuHad2.root
rm Bjets_MuHad3.root