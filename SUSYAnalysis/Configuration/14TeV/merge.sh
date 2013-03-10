#!/bin/bash

hadd TTJets.root naf_*_TTJets_cfg/$1

hadd QCD.root naf_QCD*_cfg/$1
