#!/bin/zsh

export JOBID=`echo $PBS_JOBID | cut -d. -f1`
export RUNDIR=/tmp/pbs.${JOBID}
export VO_CMS_SW_DIR=/afs/naf.desy.de/group/cms/sw

models=( A1 B1 C1 D1 )

for i in "${models[@]}"
do echo $i
cat MSSM_14TeV_herwigpp_cff_py_GEN_FASTSIM_HLT.py | sed "s/___MODEL___/$i/g" > Point"$i"_cfg.py
cat MSSM.sh | sed "s/___MODEL___/$i/g" > Point"$i".sh
qsub -l h_vmem=2000M Point"$i".sh
done
