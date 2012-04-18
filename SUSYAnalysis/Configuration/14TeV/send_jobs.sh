#!/bin/zsh

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}
export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw
export LHEFILES=/afs/naf.desy.de/user/c/cakir/workdir/cmssw/CMSSW_3_8_4/src/Scripts/Simple4lModel/New1/

for file in `ls ${LHEFILES} | fgrep .lhe`
do

cat Canlandir.sh | sed "s/XfileX/${file}/g" > ${file}.sh

qsub -l h_vmem=2500M ${file}.sh
#qsub -l h_cpu=120:00:00 ${file}.sh
#qsub script_pG_r${a}.sh
rm ${file}.sh
done
