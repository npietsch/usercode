#!/bin/bash

#rm *root

#cp naf_RA4b_TTJets_cfg/$1 ./TTJetsSummer11.root

hadd TTJetsFall11.root naf_RA4b_Fall11_TTJets?_cfg/$1

hadd SingleTop.root naf_RA4b_Top_*/$1 naf_RA4b_Tbar_*/$1

hadd QCD.root naf_RA4b_QCD?_cfg/$1

hadd WJetsHT250.root naf_RA4b_WJets_HT250*/$1

hadd WJetsHT300.root naf_RA4b_WJets_HT300*/$1

hadd WJetsHT.root naf_RA4b_WJets_HT*/$1

hadd WJets.root naf_RA4b_WJets_cfg_*/$1

hadd ZJets.root naf_RA4b_ZJets_cfg_*/$1

cp naf_RA4b_LM3_cfg/$1 ./LM3.root

cp naf_RA4b_LM8_noPFCheck_cfg/$1 ./LM8.root



#cp naf_RA4b_LM6_noPFCheck_cfg/$1 ./LM6.root

#cp naf_RA4b_LM13_cfg/$1 ./LM13.root

