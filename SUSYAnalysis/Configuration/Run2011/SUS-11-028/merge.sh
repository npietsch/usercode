#!/bin/bash

rm *root

#cp naf_RA4b_TTJets_cfg/$1 ./TTJetsSummer11_new.root

#hadd TTJetsFall11_new.root naf_RA4b_Fall11_TTJets?_cfg/*$1

#hadd SingleTop_new.root naf_RA4b_Top_*/$1 naf_RA4b_Tbar_*/$1

#hadd QCD_new.root naf_RA4b_QCD?_cfg/$1

#hadd WJetsHT250_new.root naf_RA4b_WJets_HT250*/$1

#hadd WJetsHT300_new.root naf_RA4b_WJets_HT300*/$1

#hadd WJetsHT_new.root naf_RA4b_WJets_HT*/$1

#hadd WJets_new.root naf_RA4b_WJets_cfg_*/$1

#hadd ZJets_new.root naf_RA4b_ZJets_cfg_*/$1

#cp naf_RA4b_LM6_noPFCheck_cfg/$1 ./LM6_new.root

#cp naf_RA4b_LM8_noPFCheck_cfg/$1 ./LM8_new.root

#cp naf_RA4b_LM9_noPFCheck_cfg/$1 ./LM9_new.root

#cp naf_RA4b_LM6_StopPair_noPFCheck_cfg/$1 ./LM6_StopPair_new.root
#cp naf_RA4b_LM6_SbottomPair_noPFCheck_cfg/$1 ./LM6_SbottomPair_new.root
#cp naf_RA4b_LM6_GluinoPair_noPFCheck_cfg/$1 ./LM6_GluinoPair_new.root
#cp naf_RA4b_LM6_SquarkPair_noPFCheck_cfg/$1 ./LM6_SquarkPair_new.root
#cp naf_RA4b_LM6_GluinoSquark_noPFCheck_cfg/$1 ./LM6_GluinoSquark_new.root
#cp naf_RA4b_LM6_Other_noPFCheck_cfg/$1 ./LM6_Other_new.root

#cp naf_RA4b_LM8_StopPair_noPFCheck_cfg/$1 ./LM8_StopPair_new.root
#cp naf_RA4b_LM8_SbottomPair_noPFCheck_cfg/$1 ./LM8_SbottomPair_new.root
#cp naf_RA4b_LM8_GluinoPair_noPFCheck_cfg/$1 ./LM8_GluinoPair_new.root
#cp naf_RA4b_LM8_SquarkPair_noPFCheck_cfg/$1 ./LM8_SquarkPair_new.root
#cp naf_RA4b_LM8_GluinoSquark_noPFCheck_cfg/$1 ./LM8_GluinoSquark_new.root
#cp naf_RA4b_LM8_Other_noPFCheck_cfg/$1 ./LM8_Other_new.root

#cp naf_RA4b_LM9_StopPair_noPFCheck_cfg/$1 ./LM9_StopPair_new.root
#cp naf_RA4b_LM9_SbottomPair_noPFCheck_cfg/$1 ./LM9_SbottomPair_new.root
#cp naf_RA4b_LM9_GluinoPair_noPFCheck_cfg/$1 ./LM9_GluinoPair_new.root
#cp naf_RA4b_LM9_SquarkPair_noPFCheck_cfg/$1 ./LM9_SquarkPair_new.root
#cp naf_RA4b_LM9_GluinoSquark_noPFCheck_cfg/$1 ./LM9_GluinoSquark_new.root
#cp naf_RA4b_LM9_Other_noPFCheck_cfg/$1 ./LM9_Other_new.root

#hadd MuHad_new.root naf_RA4b_MuHad*/$1

#hadd ElHad_new.root naf_RA4b_ElHad*/*$1

hadd SemiLepElMuTTJets_new.root naf_RA4b_SemiLepElMuTTJets*/$1

hadd SemiLepTauTTJets_new.root naf_RA4b_SemiLepTauTTJets*/$1

hadd DiLepTTJets_new.root naf_RA4b_DiLepTTJets*/$1

hadd FullHadTTJets_new.root naf_RA4b_FullHadTTJets*/$1


