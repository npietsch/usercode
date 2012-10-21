#!/bin/zsh

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}
export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw

rm -r naf_QCD_?
rm QCD_?.sh

for i in {401..420}
do
cat QCD.sh | sed "s/___JOB___/$i/g" > QCD_"$i".sh
chmod +x QCD_"$i".sh
#qsub -l h_vmem=10000M -l h_cpu=47:59:00 QCD_"$i".sh
qsub -l h_vmem=1000M -l h_cpu=11:59:00 QCD_"$i".sh
done