#!/bin/zsh

for i in {401..500}
do
echo "Copying naf_QCD_$i/SUSYPAT.root to Storage"
cp naf_QCD_"$i"/SUSYPAT.root ../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_"$i".root
done