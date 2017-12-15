
function [cluster_labels,name]=sendto_kmeans(rootdir,a,b,label,clusters)
%rootdir='/media/zzpp220/Document&&Data/Linux_Documents/9.6/624.500.13.21/';
%rootdir='/home/zzpp220/DATA/TRAIN/vq/';
%mfccdir='/home/zzpp220/Documents/mobile/DATA/TRAIN/MFCC39/';

%/home/zzpp220/Documents/mobile/zouling/MSR Identity Toolkit v1.0/MSR Identity Toolkit v1.0/From Microsoft web/code/sendto_kmeans.m

% totpath=strcat(rootdir,'624.500.13.21tot_cat.txt');
% meanpath=strcat(rootdir,'624.500.13.21_centercat.txt');
% a= load(totpath);
% b=load(meanpath);
%for i=1:1000
    cluster_labels = k_means(a,b,clusters);
  %  name=strcat('630\630_meancen_cluster',num2str(i),'.txt');
    name=strcat(rootdir,label,'_cluster.txt'); 
  f=fopen(name,'wb');
    dlmwrite(name,cluster_labels);
    fclose(f);
%end 