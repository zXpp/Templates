#!~/anaconda3/bin python3
# -*- coding: utf-8 -*-

"""
 @author:zzpp220
 @file:s1_addnoise.py
 Create on 12:04:21 Dec 10,2017 
 """
import librosa
import librosa.feature as feature
import IPython.display as ipdis

# 输入参数
sigwav = "/media/zzpp220/Data/Linux_Documents/Mobile/zx_mobile_test/noise/babble116.wav"
noisewav = "/media/zzpp220/Data/Linux_Documents/Mobile/zx_mobile_test/noise/WhiteNoise16.wav"
snr = 10  # db

# 加载信号、噪声，使之有共同长度
sig, sr = librosa.load(sigwav, sr=None, mono=None)
noise, _ = librosa.load(noisewav, sr=None, mono=None)
legth = min(len(sig), len(noise))
sig, noise = sig[:legth], noise[:legth]
# import IPython.display
ipdis.Audio(sig, rate=sr, autoplay=True)
# librosa.samples_to_frames(sig,)

# 计算计算信号、噪声的功率
import numpy as np

sigPower, noisePower = np.sum(sig ** 2) / legth, np.sum(noise ** 2) / legth
m = 10 ** (snr / 10.0)  # 信号与噪声的功率比
a = (sigPower / (noisePower * m)) ** 0.5  # 计算满足给定信噪比的噪声信号的放大系数
renoise = a * noise  # 得到符合指定信噪比要求的噪声信号

# 得到加躁后的语音
nSig = sig[:] + renoise  # 以单声道的方式（加性白噪声），不管输入是单声道还是双声道的方式
# 对加躁信号提取mfcc特征
n_mfcc = 13
n_mels = 24  # number of Mel bands to generate
n_fft = 2048  # int(sr/40)
win_length = int(0.025 * sr)  # 0.025*16000
hop_length = int(0.01 * sr) + 1  # 0.010 * 16000=10ms
window = 'hamming'
fmin = 20
fmax = 4000
D = np.abs(librosa.stft(sig, window=window, n_fft=n_fft, win_length=win_length, hop_length=hop_length)) ** 2
S = feature.melspectrogram(S=D, y=sig, n_mels=n_mels)
feats = feature.mfcc(S=librosa.power_to_db(S), n_mfcc=n_mfcc).T
print(feats.shape)
print(feats)


# M=feature.mfcc(nSig,sr,S=None, n_mfcc=13,hop_length=,htk=True,n_mels=24)
# print(M)


def make_mfcc_feats(uttList, input_file_list, output_feat_list, nj=1, sampling_frequency=16000, filter_bank_size=24,
                    window_size=0.025, shift=0.01, ceps_number=20, save_param=["cep"]):
    extractor = sidekit.FeaturesExtractor(audio_filename_structure=None,
                                          feature_filename_structure=None,
                                          sampling_frequency=sampling_frequency,
                                          filter_bank='log',
                                          filter_bank_size=filter_bank_size,
                                          window_size=window_size,
                                          shift=shift,
                                          ceps_number=ceps_number,
                                          pre_emphasis=0.97,
                                          save_param=save_param,
                                          )
    channel_list = np.zeros(len(uttList), dtype='int')
    extractor.save_list(show_list=uttList, channel_list=channel_list, audio_file_list=input_file_list,
                        feature_file_list=output_feat_list, num_thread=nj)
