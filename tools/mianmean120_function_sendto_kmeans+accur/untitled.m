%% Convert the feafile from Htk to txt format ,and put them into a cell.cell{i} mean a sample fea,
%% in N *D fea-matrix.and then send to spectralclustering .

tic;%tic1
t1=clock;

%mydir='/home/zzpp220/DATA/TEST/2520/evy_gmsv/';
 rootdir='/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TEST/Mobile_Timit/';
 %rootdir='/home/zzpp220/Documents/mobile/DATA/TRAIN/';
  filedir=strcat(rootdir,'MFCC-13/');
  
%/home/zzpp220/Documents/mobile/MFCC/MFCC/mean120msv.m
fid = fopen('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/lists/model_all.lst', 'rt');
C = textscan(fid, '%s %s');
fclose(fid);
%[C,IA,IC] = unique(A,'stable') returns the values of C in the same order that they appear in A
model_ids = unique(C{1}, 'stable');
nspks = length(model_ids);

label='13-MFCC-12*21-fea';
%diary(strcat(label,'spectclu.log'));diary on;
%tot2520=fopen(strcat(rootdir,label,'tot_cat.txt'),'wb');
%each_mode=fopen(strcat(rootdir,label,'_centercat.txt'),'wb');

total=cell(252,1);%%%%need change
%mean_center=cell(nspks,1);
tic;%tic2
%------------------------------------------------------------------------------------------------
for j= 1 : nspks
    model_index=strcat(model_ids{j},'*1.mfcc'); %model_index=strcat(model_ids{j},'*_txt.gmsv');    
    filelist=dir([filedir,model_index]);
    filenum=length(filelist);
    sum=0;
    samplenum=filenum;%%%change follow your need
    for k=1:filenum
        a=filelist(k).name;findchar=strfind(a,'.mfcc');
        tmpname=a(1:findchar-1); 
        totalname=strcat(filedir,filelist(k).name);
        [D]=READHTK(totalname);
        total{k+samplenum*(j-1)}=D;
    end
end
%计算到上一次遇到tic的时间，
disp(['load fea-file use time：',num2str(toc),'s']);
%-----------------------------------------------------------------------------------------------
%total=load('208.500.500.13.21-total.mat')
%total=total.total
Max_Class_Num=25;Min_Class_Num=20;
%计算到上一次遇到tic的时间，
tic;%tic3
disp('And:');
[IDX, k, EigValues, Eig_Gaps] = lyx_Jordan_Weiss(total,label, Max_Class_Num, Min_Class_Num);
disp(['spectral Clustering use time：',num2str(toc),'s']);

disp(['etime total time：',num2str(etime(clock,t1)),'s']);
disp('===============END=======================')

true_label=load('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/lists/true_labels252.lst');
send_to_accury(true_label,IDX,label);
dlmwrite(strcat(label,'-clu.txt'),IDX);
%diary off;