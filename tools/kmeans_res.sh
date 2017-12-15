#!/bin/bash
for file in /home/zzpp220/DATA/TRAIN/630/630clu_/*.txt
do
	python /home/zzpp220/DATA/TRAIN/kmeans.py $file
done
