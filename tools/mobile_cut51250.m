filedir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chainv3.0/test/FBANK_51/';% #path must be full with the last #"/" 
destdir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chainv3.0/test/FBANK_50/';
header='test_chain';
suffix='.fea';
htk2cmu_gz(header,filedir,destdir,suffix)