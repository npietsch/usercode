#!/bin/zsh

nafJobSplitter.pl -q 1 2 A1_cfg.py
nafJobSplitter.pl -q 1 2 B1_cfg.py
nafJobSplitter.pl -q 1 2 C1_cfg.py
nafJobSplitter.pl -q 1 2 D1_cfg.py

nafJobSplitter.pl -q 1 1 SemiLepTTJets_cfg.py
nafJobSplitter.pl -q 1 1 FullHadTTJets_cfg.py

nafJobSplitter.pl -q 1 3 ZJets_cfg.py
nafJobSplitter.pl -q 1 3 WJets_cfg.py

nafJobSplitter.pl -q 1 100 QCD_cfg.py