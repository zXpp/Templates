function [nSig, sig, noise] = addnoisemono(sigwav, noisewav, s,outpath)
%将NoiseX-92噪声信号以信噪比snr添加到纯净信号sig中(sig和noise必须采样率相同，长度相同),单声道的方式
%输入： sigwav      - 纯净语音音频
%       noisewav    - 噪声音频
%       snr      - 信噪比(db)

%输出： nSig  - 带噪声的语音信号
%       sig   - 纯净语音信号
%       renoise - 符合指定信噪比要求的噪声信号

snr=s;
noise=audioread(noisewav);%读入特定噪声
sig=audioread(sigwav);
[sigpath,sigbase]=fileparts(sigwav);%[d,e,f]=fileparts(sigwav),如果只需要一个参数，可以不用数组形式
if nargin<4
    outpath=sigpath;
end

legth=min(length(sig(:)),length(noise(:)));

sig=sig(1:legth);noise=noise(1:legth);
%计算纯净语音信号的强度(功率)
sigPower = sum(abs(sig(:)).^2)/legth;

%计算噪声信号的强度(功率)
noisePower = sum(abs(noise(:)).^2)/legth;

m = 10^(snr/10);%信号与噪声的功率比

a = ( sigPower / (noisePower*m) )^0.5; %计算满足给定信噪比的噪声信号的放大系数

renoise = a*noise;                       %得到符合指定信噪比要求的噪声信号

nSig(:,1) = sig(:,1) + renoise;          %以单声道的方式（加性白噪声），不管输入是单声道还是双声道的方式
snrlabel=num2str(snr);
if snr<0
	snrlabel=strcat('0',snrlabel); %in case  of -10dB as option label
end
audioWithNoise=fullfile(outpath,strcat(snrlabel,'dB_',sigbase,'.wav'));
audiowrite(audioWithNoise,nSig,16000,'BitsPerSample',16);




