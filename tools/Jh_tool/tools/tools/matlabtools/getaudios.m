function samples = getaudios(dirName,wavename_prefix, filetype)
%��dirNameĿ¼������WAV�����ļ������������ȡ������������������samples��
%���룺dirName:            Ŀ¼���?
%      wavename_prefix: �����з��ļ�����ļ���ǰ׺�ַ�����Ҫ��filler1,filler2�����з���
%                       wavename_prefixӦΪ'filler'
%�����samples:         ������

%wave = getInfo(dirName, '.wav'); %���dirNameĿ¼������WAV�ļ��������Ϣ��·�����?
wave = getInfo(dirName, filetype); %Added by Yanxiong, 2014.3.28

t = 0;
while(~isempty(wave))
    
    count = 0;
	c     = [];
	
	%���������ͬ������WAV�ļ���Ϣ(��'��ʵ1.wav'��'��ʵ2.wav'����ͬ����)
	name  = getName(wave(1).name,wavename_prefix,filetype);	
	count = 1;	
	c(1)  = 1;	
	for i = 2:length(wave)    
  	    if(strcmp(getName(wave(i).name,wavename_prefix,filetype),name))
    	    count = count+1;
            c(count) = i;
   	    end   
	end

    %���������ͬ������WAV�ļ�����Ƶ��ݣ�������sample��
	sample.name = name;
	for i = 1:length(c)
        if strcmp(filetype,'wav')
            [w, fs, wmode, fidx] = readwav(wave(c(i)).path); % changed by Yanxiong, 2014.3.28
        elseif strcmp(filetype, 'sph')
            [w, fs, ffx] = readsph(wave(c(i)).path); % changed by Yanxiong, 2014.3.28
        end        
		sample.wave{i}  = w;		
    end
    sample.n    = length(c);
    info.fs     = fs;
    if strcmp(filetype,'wav')
        info.wmode    = wmode;
        info.fidx    = fidx;
        sample.info = info;        
    elseif strcmp(filetype, 'sph')
        info.ffx    = ffx;        
 	    sample.info = info;	
    end
 	
 	%���÷����������������?
 	t = t+1;
 	samples(t) = sample;
  
    %ɾ���Ѿ���ȡ��ϵķ����ļ����?
	wave(c) = []; 
	
end

function name = getName(waveName,wavename_prefix,filetype)
%��ȡ�ļ���ǰ׺Ϊwavename_prefix���ļ���
%���?waveName = '��ʵ5.wav'(����ʵ������ʵĵ�?�η���),��getName(waveName,wavename_prefix)�õ�name = ����ʵ�� 

k = strfind(waveName, wavename_prefix);
if(isempty(k))
    if strcmp(filetype, 'wav')
        k = strfind(waveName, '.wav'); %added by Yanxiong, 2014.3.28
    elseif strcmp(filetype, 'sph')
        k = strfind(waveName, '.sph'); %added by Yanxiong, 2014.3.28
    end
end
waveName(k+length(wavename_prefix): end) = [];%���ļ���ǰ׺�Ժ���ַ����ε�?
name = waveName;
