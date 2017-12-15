#!/bin/bash
##after lium finished ,use this
ilp_dir=/home/zzpp220/Documents/ILP_RAR/LIUM-master/test_out
ilpfile_dir=/home/zzpp220/Documents/score/ilp_out
cp -f $ilp_dir/630_21/*.ev_is.120.seg $ilpfile_dir
## make ilp2rttm--sys_rttm
source ~/Templates/tools/zx_ilp2rttm.sh
##move sys_rttm to score/sys_tmp
mv -f $ilpfile_dir/*.sys.rttm $ilpfile_dir/../sys_tmp

##make chain_ref dir
#cp /home/zzpp220/Documents/mobile/DATA/chain/*/t*/*.ref.rttm $ilpfile_dir/../chain_ref/
##reference.list 
source $ilpfile_dir/../useage.sh
