function [nSig, sig, noise] = addnoisestereo(sig, noise, snr)
%将NoiseX-92噪声信号以信噪比snr添加到纯净信号sig中(sig和noise必须采样率相同，长度相同),根据输入的情况而定，若输入是单声道，输出也是单声道，若输入是双声道，输出也是双声道
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

colsig=size(sig,2);                    %获得信号的列数
if(colsig==1)                          %若为单声道
  nSig  = sig + noise;                 %叠加噪声
else                                   %若为双声道
  nSig(:,1) = sig(:,1) + noise;
  nSig(:,2) = sig(:,2) + noise;
end



