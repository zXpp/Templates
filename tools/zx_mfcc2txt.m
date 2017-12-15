mydir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/wav/';%mydir='/home/zzpp220/DATA/TEST/MFCC/';
suffix ='.fea'
getname=strcat('scut_test_chain','*.fea');
filelist=dir([mydir,getname]);
filenum=length(filelist);
%zznewname=strcat(model_ids{spk},'.mlf');

for k=1:filenum
  name=filelist(k).name;  
  filename=strcat(mydir,name);
  [D,FP,DT,TC,T]=READHTK(filename);
  prefix=strfind(filelist(k).name,suffix);
  dlmwrite(strcat(mydir,name(1:prefix),'feat'),D,' ');
end















