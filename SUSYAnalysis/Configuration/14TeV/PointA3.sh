#!/bin/zsh

ini autoproxy

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}

export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
source ${VO_CMS_SW_DIR}/cmsset_default.sh

export CMSSWDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4

export WORKDIR=/scratch/hh/lustre/cms/user/npietsch/CMSSW_4_4_4/src/SUSYAnalysis/Configuration/14TeV/Temp

export PYDIR=${CMSSWDIR}/src/SUSYAnalysis/Configuration/14TeV

export STORAGE=/scratch/hh/lustre/cms/user/npietsch/Storage

mkdir ${WORKDIR}
cd ${WORKDIR}
cd ${CMSSWDIR}/src
cmsenv
cd -

cp ${PYDIR}/PointA3_cfg.py .
cp ${PYDIR}/PointA3.slha .
cp ${PYDIR}/MSSM.model .

cmsRun -p PointA3_cfg.py &> LogFile

#mv ${WORKDIR}/PointA3.root ${STORAGE}
#mv ${WORKDIR}/LogFile ${STORAGE}

