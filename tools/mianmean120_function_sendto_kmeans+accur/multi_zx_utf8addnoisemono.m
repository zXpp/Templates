function multi_zx_utf8addnoisemono(sigpath, noisewav,label, snr,outdir)
%将NoiseX-92噪声信号以信噪比snr添加到纯净信号sig中(sig和noise必须采样率相同，长度相同),单声道的方式
%输入： sigpath      - 纯净语音音频/存放语音音频的目录
%       noisewav    - 噪声音频
%       snr      - 数组信噪比(db)[0,10,20,30] 
%       subarroutdir-输出加噪声文件的目录集合，为数组形式

%输出： nSig  - 带噪声的语音信号
%       sig   - 纯净语音信号
%       renoise - 符合指定信噪比要求的噪声信号
if nargin<5
    outdir=fileparts(sigpath);
    if nargin<4
        snr=[0,10,20,30];
        outdir=fileparts(sigpath);
    end
end

if isdir(sigpath)%w为该目录下的全部wav文件加噪声
        siglist=dir([sigpath,strcat(filesep,'*.wav')]);
        signum=length(siglist);
else
    zx_utf8addnoisemono(sigpath,noisewav,snr(s));    
end
for s=1:length(snr)
    %suboutdir=outdir(s);
    suboutdir=fullfile(outdir,strcat('WAV_',label,num2str(snr(s)),'dB'));
    if isdir(suboutdir)
        disp([suboutdir,'already exitsts!']);
    else
        mkdir(suboutdir);
    end
            for k=1:signum
             
              zx_utf8addnoisemono(fullfile(sigpath,siglist(k).name),noisewav,snr(s),suboutdir);      
            end
    disp(['add noise ',num2str(snr(s)),'db for ',num2str(signum),'sucessfully!'])
end




