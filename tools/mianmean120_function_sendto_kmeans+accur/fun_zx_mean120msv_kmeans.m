function fun_zx_mean120msv_kmeans(rootdir,aa,flag,label_prefix,true_labelsdir,brandnamedir)

    %% GET the mean of the sample to send to kmeans as the center data matrix
    %mydir='/home/zzpp220/DATA/TEST/2520/evy_gmsv/';
     %rootdir='F:\tmp\';
     %aa={'gmm13_0dB';'gmm13_10dB';'gmm13_20dB';'gmm13_30dB'};%'MeiZu_M2-None']
	 %label_prefix: cell %数组。存储每个mFCC目录久中除相同前       缀之外的剩余部分。如MFCC_whitetest_20dB、MFCC_whitetest_10dB中
	 %为{whitetest_20dB、whitetest_10dB},由aa决定共同前缀
     idsum=0;filenum2=0;
     listdir='H:\lists';
    if strcmp(true_labelsdir,'') && strcmp(brandnamedir,'')
        if strcmp(flag,'total') ||strcmp(flag,'single')
            disp('use default listfile:\n');
            disp([fullfile(listdir,'true_labels.lst'),'or true_labels-sigbrand.lst']);
        end 
    end
    for z=1:size(aa,1);
     x=aa{z,:};%''MFCC_whitetest_0dB'
         %rootdir='/home/zzpp220/Documents/mobile/DATA/TRAIN/';
    %findchar=strfind(x,'_WAV');
    g=strcat('gmm13_',label_prefix{z});%'gmm13-256_whitetest_0dB'
    filedir=fullfile(rootdir,strcat(g,filesep));%'208_500_500_39_21.gmm/');
    if strcmp(flag,'total')
        true_labels=load(fullfile(listdir,'true_labels.lst'));
        fid = fopen(fullfile(listdir,'brandname.list'), 'rt');
    elseif strcmp(flag,'single')
        true_labels=load(fullfile(listdir,'true_labels-sigbrand.lst'));
        fid = fopen(fullfile(listdir,'brandname-single.list'), 'r');
    elseif strcmp(flag,'other')
        true_labels=load(true_labelsdir);
        fid=fopen(brandnamedir,'r');
    end

     C = textscan(fid, '%s %s');
    fclose(fid);
        %[C,IA,IC] = unique(A,'stable') returns the values of C in the same order that they appear in A
    model_ids = unique(C{1}, 'stable');
    nspks = length(model_ids);%all clusters counts
    gmmtot=dir([filedir,'*.gmm']);gmmnum=length(gmmtot);% all gmm file counts

    label=strcat(label_prefix{z},x,'_13-256_kmeans');
    %codebook=8;%if use vq 

    %tot2520=fopen(strcat(rootdir,label,'tot_cat.txt'),'wb');
    %each_mode=fopen(strcat(rootdir,label,'_centercat.txt'),'wb');

    total=cell(gmmnum,1);%%%%need change 2520
    mean_center=cell(nspks,1);
    for j= 1 : nspks
                model_index=strcat('*',model_ids{j},'*.gmm'); %model_index=strcat(model_ids{j},'*_txt.gmsv');    
                filelist=dir([filedir,model_index]);
                filenum=length(filelist);
                sum=0;
                samplenum=filenum;%%%change follow your need
                idsum=idsum+filenum2;
                for k=1:filenum
                    a=filelist(k).name;findchar=strfind(a,'.gmm');
                    tmpname=a(1:findchar-1); 
                    totalname=strcat(filedir,filelist(k).name);
        %%
                     %%if use zx_main01_MFCC.m to get the spkr gmms
                    [~,M,~,~,~] = load_mixture_model_diagb(totalname); %M IS N*D
                     tmp=M';
                     tmp=tmp(:);
                     tmp=tmp';
                 %% if use gmm excrated by Miscrosoft adapt_gmm then use this 
                 %tmp=load(totalname); 
                 %%
                %{ %% use the cut the frame contain 0 method to vq 

            %      [d]=READHTK(totalname);
            %         [z,x]=size(d);
            %         MFCC_zerocut=[];
            %         for row =1:z
            %             rowline=d(row,:);
            %             count_zero=size(find(rowline==0),2);%%find and count the frame who has 0 elements
            %             if count_zero==0
            %                 MFCC_zerocut=[MFCC_zerocut;rowline];% put the no 0 frame into new matrix
            %             end
            %         end
            %         v=MFCC_zerocut';
            %          code{k} = vqlbg(v, codebook); % Train VQ codebook
            %         tmp=code{k}(:)';}%
                %%

                    sum=sum+tmp;
                    total{k+idsum}=tmp;
                   % dlmwrite(txtname,tmp);
                %% save the mean gmsv of each speaker.
                 %txtname=strcat('/home/zzpp220/DATA/bn/gmsv_208.1024.1024.13.21-13/',tmpname,'_iv_gmsv.txt'); 
               %long_fid = fopen(txtname,'wb');
               % total_precise_array(long_fid,tmp);
                %fclose(long_fid);
                end
                filenum2=filenum;
                avg=sum/samplenum;
                mean_center{j}=avg;

    end

    cat_total=cat(1,total{:});
    cat_mean=cat(1,mean_center{:});

        %%
    %total_precise_array(tot2520,cat_total);
    %total_precise_array(each_mode,cat_mean);
        %%
        %% send to kmeans
        %%send to kmeans
         %a=load('cat_total.mat'); b=load('cat_mean.mat');%
    [cluster_labels,newname]=sendto_kmeans(rootdir,cat_total,cat_mean,label,nspks);
        %[cluster_labels,newname]=sendto_kmeans(rootdir,a.cat_total,b.cat_mean,label);
        %%
        %%send to accuracy&&nmi


    send_to_accury(true_labels,cluster_labels,label,rootdir);
%     fclose(tot2520);
%     fclose(each_mode);
        %%
    end
end
