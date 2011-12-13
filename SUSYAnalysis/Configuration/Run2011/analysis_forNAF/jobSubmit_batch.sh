#!/bin/zsh

ini autoproxy
export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}

##################CMSSW Environment##########################
export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
source ${VO_CMS_SW_DIR}/cmsset_default.sh

export CMSSWDIR=/afs/naf.desy.de/user/c/cakir/cmssw_dir/RA4bAnalysis/CMSSW_4_2_8_patch7/src/SUSYAnalysis/Configuration/Run2011/analysis_forNAF


cd $CMSSWDIR
cmsenv

######################XfileX##########################################

nafJobSplitter.pl -q 12 8 RA4b_LM3_cfg.py
#nafJobSplitter.pl -q 12 31 RA4b_LM4_cfg.py
#nafJobSplitter.pl -q 12 27 RA4b_LM6_cfg.py
nafJobSplitter.pl -q 12 8 RA4b_LM8_cfg.py
nafJobSplitter.pl -q 12 17 RA4b_LM9_cfg.py
nafJobSplitter.pl -q 12 32 RA4b_LM13_cfg.py

nafJobSplitter.pl -q 12 235 RA4b_TTJets_cfg.py

nafJobSplitter.pl -q 12 40 RA4b_Tbar_tW_cfg.py
nafJobSplitter.pl -q 12 8 RA4b_Tbar_sChannel_cfg.py
nafJobSplitter.pl -q 12 98 RA4b_Tbar_tChannel_cfg.py
nafJobSplitter.pl -q 12 37 RA4b_Top_tW_cfg.py
nafJobSplitter.pl -q 12 196 RA4b_Top_tChannel_cfg.py

nafJobSplitter.pl -q 12 218 RA4b_QCD1_cfg.py
nafJobSplitter.pl -q 12 231 RA4b_QCD2_cfg.py

nafJobSplitter.pl -q 12 221 RA4b_MuHad_May10thReReco_cfg.py
nafJobSplitter.pl -q 12 209 RA4b_MuHad_PromtReco4_cfg_1.py
nafJobSplitter.pl -q 12 201 RA4b_MuHad_PromtReco4_cfg_2.py
nafJobSplitter.pl -q 12 111 RA4b_MuHad_Aug05thReReco_cfg.py
nafJobSplitter.pl -q 12 176 RA4b_MuHad_PromtReco6_cfg.py
nafJobSplitter.pl -q 12 207 RA4b_MuHad1_v1_2011_cfg.py
nafJobSplitter.pl -q 12 205 RA4b_MuHad2_v1_2011_cfg.py
nafJobSplitter.pl -q 12 192 RA4b_MuHad3_v1_2011_cfg.py
nafJobSplitter.pl -q 12 197 RA4b_MuHad4_v1_2011_cfg.py

nafJobSplitter.pl -q 12 203 RA4b_ElHad_May10_cfg.py
nafJobSplitter.pl -q 12 230 RA4b_ElHad1_v4_cfg.py
nafJobSplitter.pl -q 12 243 RA4b_ElHad2_v4_cfg.py
nafJobSplitter.pl -q 12 101 RA4b_ElHad_Aug05_cfg.py
nafJobSplitter.pl -q 12 167 RA4b_ElHad_v6_cfg.py
nafJobSplitter.pl -q 12 230 RA4b_ElHad1_v1_Run2011B_cfg.py
nafJobSplitter.pl -q 12 230 RA4b_ElHad2_v1_Run2011B_cfg.py
nafJobSplitter.pl -q 12 220 RA4b_ElHad3_v1_Run2011B_cfg.py

nafJobSplitter.pl -q 12 225 RA4b_WJets_cfg_1.py 
nafJobSplitter.pl -q 12 213 RA4b_WJets_cfg_2.py
nafJobSplitter.pl -q 12 145 RA4b_WJets_HT300_cfg.py

nafJobSplitter.pl -q 12 232 RA4b_ZJets_cfg_1.py
nafJobSplitter.pl -q 12 227 RA4b_ZJets_cfg_2.py

nafJobSplitter.pl -q 12 48 RA4b_TTJets_ScaleUp.py
nafJobSplitter.pl -q 12 50 RA4b_TTJets_ScaleDown.py
nafJobSplitter.pl -q 12 55 RA4b_TTJets_MatchingDown.py
nafJobSplitter.pl -q 12 54 RA4b_TTJets_MatchingUp.py 

while [ `qstat| fgrep cakir | fgrep j_RA4b_ | wc -l` -ge 1 ]
do
sleep 60
done


nafJobSplitter.pl check naf_RA4b_*


while [ `qstat| fgrep cakir | fgrep j_RA4b_ |  wc -l` -ge 1 ]
do
sleep 60
done

nafJobSplitter.pl -j check naf_RA4b_*




