#!/bin/zsh

nafJobSplitter.pl -q 1 2 A1_cfg.py
nafJobSplitter.pl -q 1 2 B1_cfg.py
nafJobSplitter.pl -q 1 2 C1_cfg.py

nafJobSplitter.pl -q 1 2 SemiLepTTJets_cfg.py
nafJobSplitter.pl -q 1 1 DiLepTTJets_cfg.py
nafJobSplitter.pl -q 1 2 FullHadTTJets_cfg.py

nafJobSplitter.pl -q 1 3 ZJets_cfg.py

nafJobSplitter.pl -q 1 3 WJets_el_cfg.py
nafJobSplitter.pl -q 1 3 WJets_el_new_cfg.py
nafJobSplitter.pl -q 1 3 WJets_mu_cfg.py
nafJobSplitter.pl -q 1 3 WJets_tau_cfg.py

nafJobSplitter.pl -q 12 20 QCD1_1_cfg.py
nafJobSplitter.pl -q 12 20 QCD1_2_cfg.py
nafJobSplitter.pl -q 12 20 QCD2_1_cfg.py
nafJobSplitter.pl -q 12 18 QCD2_2_cfg.py
nafJobSplitter.pl -q 12 15 QCD3_1_cfg.py
nafJobSplitter.pl -q 12 15 QCD3_2_cfg.py
nafJobSplitter.pl -q 12 15 QCD4_1_cfg.py
nafJobSplitter.pl -q 12 11 QCD4_2_cfg.py

nafJobSplitter.pl -q 12 20 QCD5_1_cfg.py
nafJobSplitter.pl -q 12 20 QCD5_2_cfg.py

nafJobSplitter.pl -q 12 20 QCD6_1_cfg.py
nafJobSplitter.pl -q 12 20 QCD6_2_cfg.py

nafJobSplitter.pl -q 12 12 QCD7_1_cfg.py
nafJobSplitter.pl -q 12 16 QCD7_2_cfg.py

nafJobSplitter.pl -q 12 20 QCD8_1_cfg.py
nafJobSplitter.pl -q 12 14 QCD8_2_cfg.py

#nafJobSplitter.pl -q 1 200 QCD1_1_cfg.py
#nafJobSplitter.pl -q 1 197 QCD1_2_cfg.py
#nafJobSplitter.pl -q 1 200 QCD2_1_cfg.py
#nafJobSplitter.pl -q 1 174 QCD2_2_cfg.py
#nafJobSplitter.pl -q 1 150 QCD3_1_cfg.py
#nafJobSplitter.pl -q 1 146 QCD3_2_cfg.py
#nafJobSplitter.pl -q 1 150 QCD4_1_cfg.py
#nafJobSplitter.pl -q 1 107 QCD4_2_cfg.py

#nafJobSplitter.pl -q 1 200 QCD5_1_cfg.py
#nafJobSplitter.pl -q 1 200 QCD5_2_cfg.py

#nafJobSplitter.pl -q 1 200 QCD6_1_cfg.py
#nafJobSplitter.pl -q 1 200 QCD6_2_cfg.py

#nafJobSplitter.pl -q 1 198 QCD7_1_cfg.py
#nafJobSplitter.pl -q 1 152 QCD7_2_cfg.py

#nafJobSplitter.pl -q 1 200 QCD8_1_cfg.py
#nafJobSplitter.pl -q 1 133 QCD8_2_cfg.py