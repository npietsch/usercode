#!/bin/bash

cp naf_Bjets_LM8_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_LM8.root
cp naf_Bjets_LM3_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_LM3.root
cp naf_Bjets_LM1_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_LM1.root
cp naf_Bjets_TTJets_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_TTJets.root
cp naf_Bjets_QCDMu_cfg/Bjets.root ./Bjets_QCDMu1.root
cp naf_Bjets_QCDMu2_cfg/Bjets.root ./Bjets_QCDMu2.root
hadd Bjets_QCDMu.root Bjets_QCDMu?.root
cp naf_Bjets_QCDMu_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_QCDMu.root
cp naf_Bjets_Wjets_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_Wjets.root
cp naf_Bjets_Zjets_cfg/Bjets.root ~/CMSSW_4_1_4/src/mSUGRA_Plots/Bjets_Zjets.root
