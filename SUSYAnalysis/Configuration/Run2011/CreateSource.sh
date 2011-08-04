#!/bin/bash

rm temp.txt
touch temp.txt

for i in `ls /pnfs/desy.de/cms/tier2/store/$1`
do

echo \'/store/$1/$i\', >> temp.txt

done
