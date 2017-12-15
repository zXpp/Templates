rootdir='/home/zzpp220/DATA/TRAIN/result/kmeans-iv/iv-13-500/';
%mfccdir='/home/zzpp220/Documents/mobile/DATA/TRAIN/MFCC39/';
%zx_train(mfccdir);
%/home/zzpp220/Documents/mobile/zouling/MSR Identity Toolkit v1.0/MSR Identity Toolkit v1.0/From Microsoft web/code/sendto_kmeans.m

totpath=strcat(rootdir,'13.500.256.15-ivtot_cat.txt');
meanpath=strcat(rootdir,'13.500.256.15-iv_centercat.txt');
a= load(totpath);
b=load(meanpath);
%for i=1:1000
    cluster_labels = k_means(a,b,21);
  %  name=strcat('630\630_meancen_cluster',num2str(i),'.txt');
    name=strcat(rootdir,'13.500.256.15_cluster.txt'); 
  f=fopen(name,'wb');
    dlmwrite(name,cluster_labels);
    fclose(f);
%end 