#!/bin/bash

export DATADIRS=$PWD
export STORAGE=$PWD/datasets

for file in `ls ${DATADIRS} | fgrep naf_RA4b_`
do
    echo $file
    export drop1=`echo $file | sed 's/naf_RA4b_//'`
    cd $file   
    cp Bjets.root $STORAGE/${drop1}.root
    cd -

done


for file1 in `ls ${STORAGE} | fgrep _cfg`
do
    echo $file1
    export drop2=`echo $file1 | sed 's/_cfg//'`
    cd $STORAGE
    echo $drop2

    mv $file1 ${drop2}
    cd -

done



