#!/bin/zsh

ini autoproxy

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}

export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
source ${VO_CMS_SW_DIR}/cmsset_default.sh

export CMSSWDIR=/scratch/hh/lustre/cms/user/npietsch/Analysis/CMSSW_4_4_4
export FILEDIR=/scratch/hh/lustre/cms/user/npietsch/Analysis/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV
export WORKDIR=/scratch/hh/lustre/cms/user/npietsch/Analysis/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV/naf_QCD____JOB___

cd ${WORKDIR}
cd ${CMSSWDIR}/src
cmsenv
cd -

cp ${FILEDIR}/SUSY_pattuple_cfg.py ./
cmsRun -p SUSY_pattuple_cfg.py &> log.txt
