#!/bin/bash

hadd TTJets.root naf_*TTJets_cfg/$1

hadd QCD.root naf_QCD*_cfg/$1

hadd WJets.root naf_WJets*_cfg/$1

hadd ZJets.root naf_ZJets*_cfg/$1

cp naf_A1_cfg/$1 ./A1.root

cp naf_B1_cfg/$1 ./B1.root

cp naf_C1_cfg/$1 ./C1.root
