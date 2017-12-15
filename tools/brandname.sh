for file in /home/zzpp220/Documents/mobile/DATA/mix_data02/*.wav
do
	if [ -f "$file" ]
	then
		basename "$file" _train2.wav >>brandnamelist.txt
	fi
done
