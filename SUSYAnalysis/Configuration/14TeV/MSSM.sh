#!/bin/zsh

ini autoproxy

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}

export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
source ${VO_CMS_SW_DIR}/cmsset_default.sh

export CMSSWDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4
export WORKDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV/___MODEL___
export FILEDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV
export STORAGE=/scratch/hh/lustre/cms/user/npietsch/Storage

mkdir ${WORKDIR}
cd ${WORKDIR}
cd ${CMSSWDIR}/src
cmsenv
cd -

cp ${FILEDIR}/Point___MODEL____cfg.py .
cp ${FILEDIR}/Point___MODEL___.slha .
cp ${FILEDIR}/MSSM.model .

cmsRun -p Point___MODEL____cfg.py &> log___MODEL___.txt
