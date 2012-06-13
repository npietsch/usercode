#!/bin/bash

nafJobSplitter.pl -q 1 8 RA4b_LM3_cfg.py
nafJobSplitter.pl -q 1 8 RA4b_LM8_cfg.py
nafJobSplitter.pl -q 1 32 RA4b_LM13_cfg.py

nafJobSplitter.pl -q 1 235 RA4b_TTJets_cfg.py

nafJobSplitter.pl -q 12 50 RA4b_Fall11_TTJets1_cfg.py
nafJobSplitter.pl -q 12 50 RA4b_Fall11_TTJets2cfg.py
nafJobSplitter.pl -q 12 50 RA4b_Fall11_TTJets3_cfg.py
nafJobSplitter.pl -q 12 50 RA4b_Fall11_TTJets4_cfg.py
nafJobSplitter.pl -q 12 50 RA4b_Fall11_TTJets5_cfg.py

nafJobSplitter.pl -q 1 40 RA4b_Tbar_tW_cfg.py
nafJobSplitter.pl -q 1 8 RA4b_Tbar_sChannel_cfg.py
nafJobSplitter.pl -q 1 98 RA4b_Tbar_tChannel_cfg.py
nafJobSplitter.pl -q 1 37 RA4b_Top_tW_cfg.py
nafJobSplitter.pl -q 1 196 RA4b_Top_tChannel_cfg.py
nafJobSplitter.pl -q 1 14 RA4b_Top_sChannel_cfg.py

nafJobSplitter.pl -q 1 218 RA4b_QCD1_cfg.py
nafJobSplitter.pl -q 1 231 RA4b_QCD2_cfg.py

nafJobSplitter.pl -q 1 225 RA4b_WJets_cfg_1.py 
nafJobSplitter.pl -q 1 213 RA4b_WJets_cfg_2.py
nafJobSplitter.pl -q 12 142 RA4b_WJets_HT300_cfg.py
nafJobSplitter.pl -q 12 235 RA4b_WJets_HT250_300_cfg_1.py
nafJobSplitter.pl -q 12 210 RA4b_WJets_HT250_300_cfg_2.py

nafJobSplitter.pl -q 1 232 RA4b_ZJets_cfg_1.py
nafJobSplitter.pl -q 1 227 RA4b_ZJets_cfg_2.py
