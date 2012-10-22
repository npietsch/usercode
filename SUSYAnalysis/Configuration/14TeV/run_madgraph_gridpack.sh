#!/bin/bash

#set -o verbose

echo "   ______________________________________     "
echo "         Running Madgraph5                    "
echo "   ______________________________________     "

repo=${1}
echo "%MSG-MG5 repository = $repo"

name=${2} 
echo "%MSG-MG5 gridpack = $name"

nevt=${3}
echo "%MSG-MG5 number of events requested = $nevt"

decay=${4}
echo "%MSG-MG5 run decay = $decay"

replace=${5}
echo "%MSG-MG5 replace = $replace"

process=${6}
echo "%MSG-MG5 process = $process"

maxjetflavor=${7}
echo "%MSG-MG5 maxjetflavor = $maxjetflavor"

qcut=${8}
echo "%MSG-MG5 qcut = $qcut"

minmax_jet=${9}
echo "%MSG-MG5 minmax_jet = $minmax_jet"

min_jets=${10}
max_jets=${11}
echo "%MSG-MG5 min/max jet multiplicity = $min_jets / $max_jets"

rnum=${12}
echo "%MSG-MG5 random seed used for the run = $rnum"

# retrieve the wanted gridpack from the official repository 

wget --no-check-certificate http://cms-project-generators.web.cern.ch/cms-project-generators/${repo}/${name}_gridpack.tar.gz 

# force the f77 compiler to be the CMS defined one

ln -s `which gfortran` f77
ln -s `which gfortran` g77
PATH=`pwd`:${PATH}

tar xzf ${name}_gridpack.tar.gz ; rm -f ${name}_gridpack.tar.gz ; cd madevent

# run the production stage
./bin/compile
./bin/clean4grid
cd ..
./run.sh ${nevt} ${rnum}

file="events"

if [ ! -f ${file}.lhe.gz ]; then
        echo "%MSG-MG5 events.lhe.gz file is not in the same folder with run.sh script, abort  !!! "
        exit
fi

cp ${file}.lhe.gz ${file}_orig.lhe.gz
gzip -d ${file}.lhe.gz

#_______________________________________________________________________________________
# check the seed number in LHE file.

echo "   ______________________________________     "
echo "         post processing started              "
echo "   ______________________________________     "

echo 
if [ -f ${file}.lhe ] ; then
        seed=`awk 'BEGIN{FS=" = gseed  "}/gseed/{print $1}' ${file}.lhe`
        number_event=`grep -c "</event>" ${file}.lhe`
fi

if [ $seed -eq $rnum ] ;then
                echo "GSEED  :$seed"
                if [ $number_event -eq $nevt ] ;then
                        echo "NEVENT :  $nevt "
                else
                        echo "%MSG-MG5 Error: The are less events ( $number_event ) Post Production is cancelled."
                        # TO-DO You might want to save the events in case of inspection the events.
                        exit 1
                fi
else
        echo "%MSG-MG5 Error: Seed numbers doesnt match ( $seed )"
        exit 1
fi

echo Test1

#_______________________________________________________________________________________
# post-process the LHE file.

#__________________________________________
# DECAY process
if [ "${decay}" == true ] ; then

    echo "%MSG-MG5 Running DECAY..."
	sed -i 's/  5 0.000000 # b : 0/  5  4.700000 # b/g' ${file}.lhe
    
	# if you want to do not-inclusive top-decays you have to modify the switch in the decay_1.in and decay_2.in
	for (( i = 1; i <=2; i++)) ; do
		madevent/bin/decay < decay_$i\.in
	done
fi

echo Test2

#__________________________________________
# REPLACE process
# REPLACE will replace el with el/mu/taus by default, if you need something else you need to edit the replace_card1.dat

cat > replace_card1.dat <<EOF
# Enter here any particles you want replaced in the event file after ME run
# In the syntax PID : PID1 PID2 PID3 ...
# End with "done" or <newline>
11:11 13 15
-12: -12 -14 -16
-11:-11 -13 -15
12: 12 14 16
done
EOF

if [ ${replace} == true ] ; then
    echo "%MSG-MG5 Runnig REPLACE..."
	if [ -f ${file}.lhe ] ; then
		mv ${file}.lhe ${file}_in.lhe
	fi
	perl madevent/bin/replace.pl ${file}_in.lhe ${file}.lhe < replace_card1.dat
fi	

echo Test3

#__________________________________________
# wjets/zjets
if [[ ${process} == wjets || ${process} == zjets ]] ; then
	echo "%MSG-MG5 process V+jets"
	python madevent/bin/mgPostProcv2.py -o ${file}_qcut${qcut}_mgPostv2.lhe -m -w -j ${maxjetflavor} -q ${qcut} -e 5 -s ${file}.lhe
fi

# qcd 
if [ ${process} == qcd ] ; then
	echo "%MSG-MG5 process QCD"
	python madevent/bin/mgPostProcv2.py -o ${file}_qcut${qcut}_mgPostv2.lhe -q ${qcut} -j ${maxjetflavor} -e 5 -s ${file}.lhe
fi

# ttbar
if [ ${process} == ttbar ] ; then
	echo "%MSG-MG5 process ttbar"
	python madevent/bin/mgPostProcv2.py -o ${file}_qcut${qcut}_mgPostv2.lhe  -m -w -t -j ${maxjetflavor} -q ${qcut} -e 5 -s ${file}.lhe
	echo Test3A
	sed -i -e '/Rnd seed/d'  -e '/MC partial width/d' -e '/Number of Events/d' -e '/Max wgt/d' -e '/Average wgt/d'   -e '/Integrated weight/d' ${file}_qcut${qcut}_mgPostv2.lhe
fi

echo Test4

#__________________________________________
# If you have HT binned samples min/max jets might be different from file to file. 
# So you can override the min/max jets decision and put by hand these from the command line 

if [ $minmax_jet == true ] ;then

	sed -i "s/ [0-9]* = minjets    ! Smallest number of additional light flavour jets/ $min_jets = minjets    ! Smallest number of additional light flavour jets/g" \
	${file}_qcut${qcut}_mgPostv2.lhe 
	sed -i "s/ [0-9]* = maxjets    ! Largest number (inclusive ktMLM matching multipl.)/ $max_jets = maxjets    ! Largest number  (inclusive ktMLM matching multipl.)/g" \
	${file}_qcut${qcut}_mgPostv2.lhe 
fi

mv ${file}_qcut${qcut}_mgPostv2.lhe ${file}.lhe 

ls -l
echo

exit 0
