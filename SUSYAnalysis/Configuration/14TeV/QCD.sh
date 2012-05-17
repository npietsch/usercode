#!/bin/zsh

ini autoproxy

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}

export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
source ${VO_CMS_SW_DIR}/cmsset_default.sh

export CMSSWDIR=/scratch/hh/lustre/cms/user/npietsch/TTJets/CMSSW_4_4_4
export FILEDIR=/scratch/hh/lustre/cms/user/npietsch/TTJets/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV
export WORKDIR=/scratch/hh/lustre/cms/user/npietsch/TTJets/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV/naf_QCD____JOB___

mkdir ${WORKDIR}
cd ${WORKDIR}
cd ${CMSSWDIR}/src
cmsenv
cd -

number=$RANDOM

cp ${FILEDIR}/QCD_template_cfg.py .
cat QCD_template_cfg.py | sed "s/___RND___/$number/g" > QCD_"$number"_cfg.py
rm QCD_template_cfg.py
cmsRun -p QCD_"$number"_cfg.py &> log_"$number".py
