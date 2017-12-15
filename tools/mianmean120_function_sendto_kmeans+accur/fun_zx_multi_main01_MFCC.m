function fun_zx_multi_main01_MFCC(srcpath,flag,subfeadirpre,trulab,bandlab)
% this function is to train the models and testing results;
% training model
% model 1 feature;
%srcpath: pardir of <path to feature(mfcc) files>
%flag: for zxmobile-dataset,all type(19)=total,all brand(7)=sigle
%subfeadirpre :要使用的多个特征子目录的名称的共同前缀

%clear all;
%fclose all;

%addpath C:\SRE04\MH_GMM\MFCC;
%cd C:\SRE04\MH_GMM\MFCC;

% training UBM
%load C:\SRE04\MH_GMM\MFCC\MFCC % load feature file
%{}%'120-159','160-199','200-,'240-279','280-319','320-359','360-399','400-439','440-479','480-519','520-559','560-599','600-639','640-679','80-119'
    %srcpath='F:\zx_mobile-test\samptest-factory\';
    a={};
    
	fprintf(' srcpath: %s\n flag: %s\n subfeadirpre: %s\n trulab: %s \n bandlab: %s \n',srcpath,flag,subfeadirpre,trulab,bandlab);

    submfccdir=dir(fullfile(srcpath,strcat(subfeadirpre,'*')));
	%disp(submfccdir)
    assert(~isempty(submfccdir), strcat('ERROR:empty subdir in the given srcpath ',srcpath));

    for i=1:size(submfccdir,1)
		subname=submfccdir(i).name;
		if submfccdir(i).isdir && strmatch(subfeadirpre,subname)
			
			a{i}=subname;
		end
    end
    %a={'MFCC13_WAV_Factory0dB';'MFCC13_WAV_Factory10dB';'MFCC13_WAV_Factory20dB';'MFCC13_WAV_Factory30dB'};
    gmmcell=cell(length(a),1);
    %flag='single';%
    %flag='total';
	uniquelabcell={};
	%assert (~isempty(length(a)),strcat('ERROR:no subdir with ',subfeadirpre,'in the given srcpath ',srcpath));
    for y=1:size(a,1)
		x=a{y,:};
		tmplabel=strcat(x,''); %  _MFCC13 
		mydir=fullfile(srcpath,tmplabel,filesep);%wavdir 最后一个目录一定要加反斜杠，不然22行的*.mfcc会出错,存放mfcc的目录
		findchar=strfind(tmplabel,subfeadirpre);
		uniquelab=tmplabel(findchar+length(subfeadirpre):length(tmplabel));
		uniquelabcell{y}=uniquelab;
		addsuffix=strcat('gmm13_',uniquelab);
		gmmcell{y}=addsuffix;
		destdir=fullfile(srcpath,addsuffix,filesep);
		if isdir(destdir)
			disp([destdir,'exists!']);
		else
			mkdir(destdir);
		end
		%{  %}  

		%mydir='I:\L_MFCC_13\MFCC_13\';
		 filelist=dir([mydir,'*.mfcc']);%,'*.mfcc'
		 filenum=length(filelist);


		%%

		 MFCC=cell(filenum,1);
		 MFCC_file=cell(filenum,1);%record the bn-fea order of the MFCC cell.
		for q=1:filenum,
			filename=filelist(q).name;
			total=strcat(mydir,filename);
			MFCC_file{q}=filename;
			%d=load(total);read txt mfcc-file
			[d,~,~]=htkread(total); %[d,fp,dt,tc,t]=READHTK(total);
			MFCC{q}=d;
		end

		%%
		fprintf('\n\nMFCCload success ...\n\n');
		%   MFCC=load('MFCC1024_26.mat');
		%   MFCC=MFCC.MFCC;
		%%
		% MFCC data must be in N by M dimension N is number of length frame 
		% M is vector dimension.   e.g  100000 by 30

		%%
		%%jiang mfcc cong shude biancheng heng de
		%{%}
		Cep={};
		 k = 0; % total number of segments (models)
		 for i=1:size(MFCC, 1)
			 for j = 1 : size(MFCC, 2)
				 if ~isempty(MFCC{i, j});
					 k = k + 1;
					if size(MFCC{i, j},2)>42;    
						Cep{k} = MFCC{i, j}';
					else
						Cep{k} = MFCC{i, j}; 				
					end 
					fprintf('MFCC size is: [%d, %d] \n', size(MFCC));	
				end
			 end
		 end 

		%%
		%{
		 Cep=load('Cep-tot.mat');
		 Cep=Cep.Cep; 
		 %}   
		%%
		gaussian=256;
		ubmname=strcat('adnos',tmplabel);

		%{%}
		zx_train_UBM(Cep,gaussian,ubmname);  % feature in cell structure  adn 32 is nuimber of GMM 'UBM01'  model name;
		clear MFCC;


		% save all 
		% % load all

		% adapt training model
		%%
		%MFCC_filelist=load('MFCC_file-tot.mat');MFCC_filelist=MFCC_filelist.MFCC_file;


		MFCC_filelist=MFCC_file;%MFCC_filelist.MFCC_file
		%%
			for i = 1 : length(Cep);
			   % gmmname=['model', num2str(i)];%model1
				filename=MFCC_filelist{i};
				findchar=strfind(filename,'.mfcc');
				if ~isempty(filename)
					gmmname=filename(1:findchar-1);%different with python,都是闭区间
					%tic;
					zx_adap_UBM(Cep(i), gaussian,gmmname, ubmname);  % feature in cell structure  adn 32 is nuimber of GMM 'model i'  model name;
					%disp(['This time extract an bn-gmm-fea of a sample use : ',num2str(toc),'s']);
				end
				if exist(strcat(gmmname,'.gmm'),'file')
					 movefile(strcat(gmmname,'.gmm'),destdir);
				else
					assert(~exist(strcat(gmmname,'.gmm')),disp([strcat(gmmname,'.gmm'),' does not exist']));
				end


			end
		clear Cep;
    end
    disp(['now send to mean-120 kmeans','......']);
    if strcmp(flag,'other')
        true_labels_dir=trulab;
        brandnamedir=bandlab;
    else
        true_labels_dir='';
        brandnamedir='';
    end
    disp(['now use kmeans-clustering:','fun_zx_mean120msv_kmeans']);
    fun_zx_mean120msv_kmeans(srcpath,a,flag,uniquelabcell,true_labels_dir,brandnamedir);
end
