function [nSig, sig, noise] = addnoisemono(sig, noise, snr)
%将NoiseX-92噪声信号以信噪比snr添加到纯净信号sig中(sig和noise必须采样率相同，长度相同),单声道的方式
%输入： sig      - 纯净语音信号
%       noise    - 噪声信号
%       snr      - 信噪比(db)

%输出： nSig  - 带噪声的语音信号
%       sig   - 纯净语音信号
%       noise - 噪声信号


%计算纯净语音信号的强度(功率)
sigPower = sum(abs(sig(:)).^2)/length(sig(:));

%计算噪声信号的强度(功率)
noisePower = sum(abs(noise(:)).^2)/length(noise(:));

m = 10^(snr/10);

a = ( sigPower / (noisePower*m) )^0.5; %计算噪声信号的放大系数

noise = a*noise;                       %得到符合指定信噪比要求的噪声信号

nSig(:,1) = sig(:,1) + noise;          %以单声道的方式，不管输入是单声道还是双声道的方式




