#!/bin/bash

##$ -N TNET_EXAMPLE
#$ -o _$JOB_NAME.out
#$ -e _$JOB_NAME.err
#$ -cwd

#$ -q long.q@@pco203,long.q@pcspeech-gpu
##$ -l gpu=1

if [ $SGE_O_WORKDIR ]; then cd $SGE_O_WORKDIR; fi

hostname

########################################################
# SELECT TNET LOCATION
#TNET_ROOT='/mnt/matylda5/iveselyk/Tools/TNet/'
TNET_ROOT='/mnt/matylda5/iveselyk/DEVEL/TNet_PACKAGE/TNet/trunk/'



########################################################
# CONFIG
#
OutputDir='_tdecode'
MONOSTATES='/mnt/matylda5/iveselyk/DATABASE/SPEECHDAT/HU/labels/monostates_hu_phn62_3s'
SCP='test_post.scp'
MLF_REF='/mnt/matylda5/iveselyk/DATABASE/SPEECHDAT/HU/labels/ref_realign-it6_LCRC1500.mlf'

LMSCALE=0.0
WIP=-2.85585
#
########################################################



mkdir -p $OutputDir

##########################################
#prepare decoder

# create HMM model for STK decoder with posterior input
cp $MONOSTATES ${OutputDir}/monostates
cat ${OutputDir}/monostates | sed 's|__[2-4]||' | uniq > ${OutputDir}/hmmlist

# create dictonary
awk '{print $1 " " $1}' ${OutputDir}/hmmlist > ${OutputDir}/dict

#create recognition net
HBuild ${OutputDir}/hmmlist ${OutputDir}/monophones_lnet.hvite

# generate hmm model with GMM bypass input
${TNET_ROOT}/tools/decode/gen_HTK_gmmbypass.sh ${OutputDir}/monostates ${OutputDir}/hmmdefs.htk



##########################################
# DECODE TEST DATA

#decode
HVite \
  -A -D -T 1 -y 'rec' \
  -S $SCP \
  -H ${OutputDir}/hmmdefs.htk \
  -i ${SCP%.scp}.mlf \
  -l '*' \
  -s $LMSCALE \
  -w ${OutputDir}/monophones_lnet.hvite \
  -p ${WIP:-0.0} \
  ${OutputDir}/dict \
  ${OutputDir}/hmmlist

#score
if [ $MLF_REF ]; then
HResults -p -I $MLF_REF ${OutputDir}/hmmlist ${SCP%.scp}.mlf | \
  tee ${SCP%.scp}.res
fi

