#!/bin/zsh

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}
export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw

for i in {400..402}
do
cat PAT.sh | sed "s/___JOB___/$i/g" > PAT_"$i".sh
chmod +x PAT_"$i".sh
qsub -l h_vmem=10000M -l h_cpu=23:59:00 PAT_"$i".sh
done