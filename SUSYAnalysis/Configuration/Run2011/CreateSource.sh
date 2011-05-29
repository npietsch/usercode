#!/bin/bash

rm temp.txt
touch temp.txt

for i in `ls /pnfs/desy.de/cms/tier2/store/$1`
do

for j in `ls /pnfs/desy.de/cms/tier2/store/$1/$i`
do
echo \'/store/$1/$i/$j\', >> temp.txt

done
done
