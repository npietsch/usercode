#!/bin/bash

rm -r datasets*

cp /afs/naf.desy.de/user/c/cakir/workdir/UserCode/cakir/scripts_ra4b/*sh ./
cp -r /afs/naf.desy.de/user/c/cakir/workdir/UserCode/cakir/scripts_ra4b/Templates ./

date=`date +%d%m%y`

datasetdir=datasets_${date}

mkdir $datasetdir
cd $datasetdir
mkdir DataFiles
cd DataFiles

cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_LM3_cfg/Bjets.root ./LM3.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_LM8_cfg/Bjets.root ./LM8.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_LM9_cfg/Bjets.root ./LM9.root

cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_TTJets_cfg/Bjets.root ./TTJets.root

rm WJets*.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_WJets_cfg_1/Bjets.root ./WJets_1.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_WJets_cfg_2/Bjets.root ./WJets_2.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_WJets_cfg_3/Bjets.root ./WJets_3.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_WJets_cfg_4/Bjets.root ./WJets_4.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_WJets_cfg_5/Bjets.root ./WJets_5.root
hadd WJets.root WJets_?.root
rm WJets_*.root

rm ZJets*.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_ZJets_cfg_1/Bjets.root ./ZJets_1.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_ZJets_cfg_2/Bjets.root ./ZJets_2.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_ZJets_cfg_3/Bjets.root ./ZJets_3.root
hadd ZJets.root ZJets_?.root
rm ZJets_*.root

rm QCD*.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_QCD_cfg_1/Bjets.root ./QCD_1.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_RA4b_QCD_cfg_2/Bjets.root ./QCD_2.root
hadd QCD.root QCD_?.root
rm QCD_*.root 

rm MuHad*.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_MuHad1_v1_cfg/Bjets.root ./MuHad_1.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_MuHad2_v1_cfg/Bjets.root ./MuHad_2.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_MuHad1_v4_cfg/Bjets.root ./MuHad_3.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_MuHad2_v4_cfg/Bjets.root ./MuHad_4.root
hadd MuHad.root MuHad_?.root
rm MuHad_*.root

rm ElectronHad*.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_ElHad1_v1_cfg/Bjets.root ./ElectronHad_1.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_ElHad2_v1_cfg/Bjets.root ./ElectronHad_2.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_ElHad1_v4_cfg/Bjets.root ./ElectronHad_3.root
cp ../../../SUSYAnalysis/Configuration/Run2011/naf_Bjets_ElHad2_v4_cfg/Bjets.root ./ElectronHad_4.root
hadd ElectronHad.root ElectronHad_?.root
rm ElectronHad_*.root