#!/bin/zsh

ini autoproxy

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}

export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
source ${VO_CMS_SW_DIR}/cmsset_default.sh

export CMSSWDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4
export WORKDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV/C1
export FILEDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV
export STORAGE=/scratch/hh/lustre/cms/user/npietsch/Storage

mkdir ${WORKDIR}
cd ${WORKDIR}
cd ${CMSSWDIR}/src
cmsenv
cd -

cp ${FILEDIR}/PointC1_cfg.py .
cp ${FILEDIR}/PointC1.slha .
cp ${FILEDIR}/MSSM.model .

cmsRun -p PointC1_cfg.py &> logC1.txt
