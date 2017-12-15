%%��mfcc�ļ�ת����mlf�ļ�
%ת����ɺ������޿��У�Linux�µ��ļ���ʽ������Ҫת��Ϊunix.
fid = fopen('/home/zzpp220/DATA/TRAIN/lists/model_all.lst', 'rt');
C = textscan(fid, '%s %s');
fclose(fid);
%[C,IA,IC] = unique(A,'stable') returns the values of C in the same order that they appear in A
model_ids = unique(C{1}, 'stable');%
model_files = C{2};
nspks = length(model_ids);
for spk = 1 : nspks,
mydir='/home/zzpp220/zx/nn.mob_mfcc/fx/mfcc_13_bn/';%mydir='/home/zzpp220/DATA/TEST/MFCC/';
getname=strcat(model_ids{spk},'*.bn');
filelist=dir([mydir,getname]);
filenum=length(filelist);
%zznewname=strcat(model_ids{spk},'.mlf');
%fidout=fopen(zznewname,'wb');  %��һ���ļ�����д 
%fprintf(fidout,'%s\n','#!MLF!#');
for k=1:filenum
  filename=[mydir,filelist(k).name];
  [D,FP,DT,TC,T]=READHTK(filename);
  findchar=strfind(filename,'.bn');%�����ַ��λ��
  begpos=length(mydir);
  tmpname=filename(begpos+1:findchar-1);
  %newname=strcat(tmpname,'.lab"');
  lblname=strcat(tmpname,'lbl');
  lbl=fopen(lblname,'wb');
  %fprintf(lbl,'%s\n','#!MLF!#');
  %fprintf(lbl,'"*/%s\n',newname);
 
  [row col] = size(D);  %ȡ�������������к���
  begtime=0;
  endtime=row*FP;%endtime=row*FP*10000000;
  fprintf(lbl,'%d %s %s\n',begtime,int2str(endtime),'speech');
  %fprintf(fidout,'%d %s %s\n',begtime,int2str(endtime),model_ids{spk});
  %fprintf(fidout,'%s\n','.');
end
end
fclose(lbl);
%fclose(fidout);