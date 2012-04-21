#!/bin/zsh

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}
export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw

#qsub -l h_vmem=15000M PointA1.sh   ## former A3

qsub -l h_vmem=15000M PointB1.sh

qsub -l h_vmem=15000M PointC1.sh

qsub -l h_vmem=15000M PointD1.sh

