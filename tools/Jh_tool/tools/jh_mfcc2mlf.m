%%由mfcc文件转化成mlf文件
%转换完成后检查有无空行，Linux下的文件格式可能需要转化为unix.
mydir='F:\mfcc\gunshot\';
filelist=dir([mydir,'*.mfcc']);
filenum=length(filelist);
fidout=fopen('gunshot.mlf','wb');  %打开一个文件，可写 
fprintf(fidout,'%s\n','#!MLF!#');
for k=1:filenum
  filename=[mydir,filelist(k).name];
  [D,FP,DT,TC,T]=READHTK(filename)
  findchar=strfind(filename,'.mfcc');%返回字符串的位置
  begpos=length(mydir);
  tmpname=filename(begpos+1:findchar-1);
  newname=strcat(tmpname,'.lab"');
  fprintf(fidout,'"*/%s\n',newname);
 
  [row col] = size(D);  %取得两个变量的行和列
  begtime=0;
  endtime=row*FP*10000000;
  fprintf(fidout,'%d %s %s\n',begtime,int2str(endtime),'Gunshot');
  fprintf(fidout,'%s\n','.');
end
fclose(fidout);