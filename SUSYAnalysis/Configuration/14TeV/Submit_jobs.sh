#!/bin/zsh

nafJobSplitter.pl 2 A1_cfg.py

nafJobSplitter.pl 1 SemiLepTTJets_cfg.py
nafJobSplitter.pl 1 FullHadTTJets_cfg.py

nafJobSplitter.pl 3 ZJets_cfg.py
nafJobSplitter.pl 3 WJets_cfg.py

nafJobSplitter.pl 100 QCD_cfg.py

