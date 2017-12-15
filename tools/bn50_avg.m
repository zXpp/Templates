function bn50_avg(bn50_dir,scp_dir,suffix,forhead,outsuffix)

%clear all
%% This script is to change the bn feature file by frame to by seg. the argv is ex,chain66.bn && chain66.scp.
%bn50_dir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain_v2.0_concate/bn_fea/';
%forhead='chain';
%suffix='.bn';
model_index=strcat(forhead,'*',suffix);    
bnfilelist=dir([bn50_dir,model_index]);
filenum=length(bnfilelist);
%scp_dir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain_v2.0_concate/chain_scp/';

for k=1:filenum

totalname=strcat(bn50_dir,bnfilelist(k).name); 
bn_matrix=READHTK(totalname);
a=bnfilelist(k).name;findchar=strfind(a,suffix);
tmpname=a(1:findchar-1);
scp_file=strcat(scp_dir,tmpname,'.scp');
seg_fea=[];
[start,End] = importfile(scp_file);
start(1)=1;
for i=1:size(start,1)
    begin_index=int32(start(i));end_index=int32(End(i));
    bn_matrix_tmp=bn_matrix((begin_index:end_index),:);
    mean_matrix=[i-1 mean(bn_matrix_tmp)];%0 1.8449 2.8258 0.34835
   %mean=mean(bn_matrix(1:369,:));
   
    seg_fea=[seg_fea;mean_matrix];
end

dlmwrite(strcat(bn50_dir,tmpname,outsuffix),seg_fea,' ');
    
end

