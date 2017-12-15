%%��mfcc�ļ�ת����mlf�ļ�
%ת����ɺ������޿��У�Linux�µ��ļ���ʽ������Ҫת��Ϊunix.
fid = fopen('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/lists/model_all.lst', 'rt');
%fid = fopen('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/data_Sets/14cellphones/LATEST_DATA/brandnamelist.txt', 'rt');
C = textscan(fid, '%s %s');
fclose(fid);
fidout=fopen('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TEST/Mobile_Timit/test_e_d_26.mlf','wb');  %��һ���ļ�����д 
fprintf(fidout,'%s\n','#!MLF!#');
%[C,IA,IC] = unique(A,'stable') returns the values of C in the same order that they appear in A
model_ids = unique(C{1}, 'stable');%
model_files = C{2};
nspks = length(model_ids);
for spk = 1 : nspks,
mydir='/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TEST/Mobile_Timit/MFCC_E_D_26/';%mydir='/home/zzpp220/DATA/TEST/MFCC/';
getname=strcat(model_ids{spk},'*.mfcc');
filelist=dir([mydir,getname]);
filenum=length(filelist);
%zznewname=strcat(model_ids{spk},'.mlf');

for k=1:filenum
  filename=[mydir,filelist(k).name];
  [D,FP,DT,TC,T]=READHTK(filename)
  findchar=strfind(filename,'.mfcc');%�����ַ��λ��
  begpos=length(mydir);
  tmpname=filename(begpos+1:findchar-1);
  newname=strcat(tmpname,'.lab"');
  fprintf(fidout,'"*/%s\n',newname);
 
  [row col] = size(D);  %ȡ�������������к���
  begtime=0;
  endtime=row*FP*10000000;
  fprintf(fidout,'%d %s %s\n',begtime,int2str(endtime),model_ids{spk});
  fprintf(fidout,'%s\n','.');
end
end
fclose(fidout);