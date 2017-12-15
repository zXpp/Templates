%%mfcc2mlf2lab
%.
mydir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/audio/train/fea/';
label={'wind';'Rivers';'Rain';'Male';'Female';'gunshots';'drums';'birds';'bass';'babies';'applause'};
train=fopen(strcat('/media/zzpp220/Data/Linux_Documents/Mobile/ILP/audio/train/','train.mlf'),'wb');
fprintf(train,'%s\n','#!MLF!#');
 for dd=1:length(label)
type_tmp=label(dd,1);
type=type_tmp{1,1}
filelist=dir([mydir,'*',type,'*.fea']);
filenum=length(filelist);
% fidout=fopen(strcat(type,'.mlf'),'wb');  %��һ���ļ�����д 
% fprintf(fidout,'%s\n','#!MLF!#');
for k=1:filenum
 % filename=[mydir,filelist(k).name];
% filename=filelist(k).name;
 filename1=[mydir,filelist(k).name];
  [D,FP,DT,TC,T]=READHTK(filename1)
  findchar=strfind(filename1,'.fea');%�����ַ��λ��
  begpos=length(mydir);
  tmpname=filename1(begpos+1:findchar-1);
  newname=strcat(tmpname,'.lab"');
  fprintf(train,'"*/%s\n',newname);
  
  %fprintf(fidout,'"*/%s\n',newname);
  [row col] = size(D);  %ȡ�������������к���
  begtime=0;
  endtime=row*FP*10000000; 
  
  %fid=fopen([tmpname '.lab'],'wt');
  %fprintf(fid,'%d %s %s\n',begtime,int2str(endtime),type);% lab�ļ�
  
%   fprintf(fidout,'%d %s %s\n',begtime,int2str(endtime),type);%mlf�ļ�
%   fprintf(fidout,'%s\n','.');
     fprintf(train,'%d %s %s\n',begtime,int2str(endtime),type);%mlf�ļ�
     fprintf(train,'%s\n','.');
    

end
%fclose(fidout);
%fclose(fid);
     
 end
 fclose(train);

