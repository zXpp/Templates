function htk2cmu_gz(header,filedir,destdir,suffix)
%%htk2cmu_gz('chain_v2.0_concate/htk_mfcc/','chain_v2.0_concate/htk_mfcc/','.fea');
%filedir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain_v2.0_concate/htk_mfcc/'
model_index=strcat(header,'*',suffix); %model_index=strcat(model_ids{j},'*_txt.gmsv');    
filelist=dir([filedir,model_index]);
filenum=length(filelist);
for k=1:filenum
 file=filelist(k).name;
  file_total=strcat(filedir,file);  
 data=READHTK(file_total);
 
 %data=load(file_total);
 
 data=data(:,1:50);
%  htkwrite(data_cut,strcat(destdir,file),839);%838=MFCC_E_D_A; 839=FBANK_E_D_A
 
 
dlmwrite(strcat(destdir,file),data,' ');%用分隔符空格写入 ，默认=为‘，’
    
end
%%
%   tc is the sum of the following values:
%  			0		WAVEFORM
%  			1		LPC
%  			2		LPREFC
%  			3		LPCEPSTRA
%  			4		LPDELCEP
%  			5		IREFC
%  			6		MFCC
%  			7		FBANK
%  			8		MELSPEC
%  			9		USER
%  			10		DISCRETE
%  			64		-E		Includes energy terms
%  			128	_N		Suppress absolute energy
%  			256	_D		Include delta coefs
%  			512	_A		Include acceleration coefs
%  			1024	_C		Compressed (not implemented yet)
%  			2048	_Z		Zero mean static coefs
%  			4096	_K		CRC checksum (not implemented yet)
%  			8192	_0		Include 0'th cepstral coef
%
