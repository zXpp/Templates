mydir='/home/zzpp220/DATA/TRAIN/GMSV2268/';
desdir='/home/zzpp220/DATA/TRAIN/HTK_GMSV2268/';
filelist=dir([mydir,'*.gmsv']);
 matnum=length(filelist);
 for q=1:matnum,
    filename=filelist(q).name;%TBL0101-MIXA1.ev_is.180.seg
    findchar=strfind(filename,'.gmsv');%�����ַ��λ��
  %begpos=length(mydir);
     tmpname=filename(1:findchar-1);%TBL0101-MIXA1
     newname=strcat(desdir,tmpname,'_htk.gmsv');
     fid2=fopen([newname],'wb');
     totalname=strcat(mydir,filelist(q).name);
     rawdata=load(totalname);
     rawdata=rawdata';
     htkwrite(newname,rawdata,100000,70);
 end