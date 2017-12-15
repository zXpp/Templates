#!/bin/bash

for file in ~/DATA/TRAIN/WAV/*.wav
do
	echo $file	
	basename $file .wav >> ~/DATA/TRAIN/ubm.lst
done
