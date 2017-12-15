%% This script is combine the k-means and send-to-accuracy 
%%
data=load('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-dnn/208.500.500.26.21-26-256/No-Change-dn-26_2520cat.txt');
set_clusters=[21];%[23,17,16,20,19,15,22];
true_labels=load('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/lists/true_labels.lst');
for i =1:length(set_clusters)
 num_clusters=set_clusters(i);   
destdir=strcat('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-dnn/208.500.500.26.21-26-256/shuf_clustercenter_test/',int2str(num_clusters),'/');
centers=load(strcat(destdir,'shuf-208-500-500-26-21-26-256cen',int2str(num_clusters),'.txt'));
%centers=load('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-dnn/208.500.500.26.21-26-256/dn-26_centercat.txt');
label=strcat('shuf-208-500-500-26-21-26-256-',int2str(num_clusters));
cluster_labels = k_means(data, centers, num_clusters);


send_to_accury(destdir,true_labels,cluster_labels,label)

dlmwrite(strcat(destdir,'/',label,'-clu.txt'),cluster_labels);
end