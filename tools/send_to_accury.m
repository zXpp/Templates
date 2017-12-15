true_labels=load('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/lists/true_labels.lst');
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_1260.txt');
%true_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_630.txt');

% destdir='/media/zzpp220/Document&&Data/Linux_Documents/9.8/sparse/39.256-corresponding/shiyan/feature//';
 destfile='624.500.13.21-spetc-sys-affi=0';
cluster_labels=load('624.500.13.21-spetc-sys-affi=0.txt');

score = accuracy(true_labels, cluster_labels);
%newname=strcat(destdir,'accur：',num2str(score),'%_',destfile);
newname=strcat('accur：',num2str(score),'%_',destfile);
fid=fopen(newname,'wb');
fclose(fid);

score_nmi=nmi(true_labels, cluster_labels);
newname2=strcat('nmi：',num2str(score_nmi*100),'%_',destfile);
fid2=fopen(newname2,'wb');
fclose(fid2);