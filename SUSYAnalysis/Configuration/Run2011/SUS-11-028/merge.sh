#!/bin/bash

#rm *root

#cp naf_RA4b_TTJets_cfg/$1 ./TTJetsSummer11.root

#hadd TTJetsFall11.root naf_RA4b_Fall11_TTJets?_cfg/$1

#hadd SingleTop.root naf_RA4b_Top_*/$1 naf_RA4b_Tbar_*/$1

#hadd QCD.root naf_RA4b_QCD?_cfg/$1

#hadd WJetsHT250.root naf_RA4b_WJets_HT250*/$1

#hadd WJetsHT300.root naf_RA4b_WJets_HT300*/$1

#hadd WJetsHT.root naf_RA4b_WJets_HT*/$1

#hadd WJets.root naf_RA4b_WJets_cfg_*/$1

#hadd ZJets.root naf_RA4b_ZJets_cfg_*/$1

#cp naf_RA4b_LM3_noPFCheck_cfg/$1 ./LM3.root

#cp naf_RA4b_LM8_noPFCheck_cfg/$1 ./LM8.root

#hadd MuHad.root naf_RA4b_MuHad*/$1

#hadd ElHad.root naf_RA4b_ElHad*/$1

hadd SemiLepElMuTTJets.root naf_RA4b_SemiLepElMuTTJets*/$1

hadd SemiLepTauTTJets.root naf_RA4b_SemiLepTauTTJets*/$1

hadd DiLepTTJets.root naf_RA4b_DiLepTTJets*/$1

hadd FullHadTTJets.root naf_RA4b_FullHadTTJets*/$1


