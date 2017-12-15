function send_to_accury(ref_labels,sys_labels,label,destdir)
%ref_labels=load('/home/zzpp220/DATA/TRAIN/lists/ref_labels.lst');
%ref_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_1260.txt');
%ref_labels=load('/home/zzpp220/DATA/TRAIN/lists/truelabels_630.txt');

% destdir='/media/zzpp220/Document&&Data/Linux_Documents/9.6/624.500.13.21/';
% destfile='624.500.13.21_cluster.txt';

%sys_labels=load(strcat(destdir,destfile));
if nargin < 4, destdir = strcat(pwd,'/'); end

score_acc = accuracy(ref_labels, sys_labels);
score_nmi=nmi(ref_labels, sys_labels);

%newname=strcat(destdir,'accur：',num2str(score_acc),'%_','nmi：',num2str(score_nmi*100),'%_',destfile);
newname=strcat(destdir,'accur:',num2str(score_acc),'%_','nmi:',num2str(score_nmi*100),'%_',label,'_clusterRes.txt');
disp([label]);
disp(['accur:',num2str(score_acc),'%_','nmi:',num2str(score_nmi*100),'%_']);
fid=fopen(newname,'wb');

fclose(fid);