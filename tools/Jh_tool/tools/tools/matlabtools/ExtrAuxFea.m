function [feature] = ExtrAuxFea(samples_enframe, fs)
% This function is to extract extral auxiliary features from input audio files
%% output parameters
% feature.ne : normalized energy
% feature.log_en_diff: log-energy difference represents the log of the ratio of short-time energy between  two 
%              channels, and is computed between a given target IHM channel and each of the non-target channels.
% feature.norm_log_en_diff: This normalization consists of subtracting the minimum frame log-energy
%                   of a channel from all log-energy values in the channel
% feature.kur: kurtosis
% feature.mean_norm_cross_corr: mean normalized cross correlation
% feature.max_norm_cross_corr: maximum normalized correlation
% feature.min_norm_cross_corr: minimum normalized correlation
% feature.zcr: zero crossing rate
%% input parameters
% FilePath: the path of input files
% NamePrefix: prefix of input file names
% FileType: the type of input files, e.g. sph, wav
%

if nargin < 1,
   error('Usage: [feature] = ExtrAuxFea(samples_enframe, fs)');
end;
%% Read audio files with the same prefix of file name
% [samples, filenames] = getaudios(FilePath, NamePrefix, FileType); % read all file with the same prefix of file name
% filenames(:, end - length(FileType) : end) = [];
% fs = samples(1).info.fs;
% fs = samples(1).fs
windowsize = floor(25 * fs / 1000); %window size is 400 when fs is 16000 (i.e. 25 ms)
overlap = floor(15 * fs / 1000); %window overlap is 15 ms, shift is 240 when fs is 16000 (i.e. 10 ms)
filenum = length(samples_enframe);
% %% Enframe each channel
% for i = 1 : filenum   
%     % enframe, each column is a frame
%     samples_enframe{i} = lyx_frame(samples(i).wave, windowsize,overlap,fs);% enframe
% end
% framenum = size(samples_enframe{1}, 2); % frame number
% clear samples;
%% Extract zero cross rate
zcr = zeros(framenum, filenum); % sum of all channel's zcr
for i = 1 : filenum
    for j = 1 : size(samples_enframe{i}, 2)
        x1 = samples_enframe{i};
        x = x1(:, j)'; % the j-th frame
        tmp = sum(0.5 * abs(sign(x(:, 2: windowsize)) - sign(x(:, 1 : windowsize - 1))));
        zcr(j, i) = tmp; % the j-th framne's zcr of the i-th channel
    end
end
%% Extract kurtosis
kur = zeros(framenum, filenum);
for i = 1 : filenum
    kur(:,i)  = kurtosis(samples_enframe{i})'; %a column is the kurtosis for one channel   
end

%% normaized energy
EnSum = zeros(framenum, 1); % sum of all channel's energy
energy = zeros(framenum, filenum); % raw energy
ne = zeros(framenum, filenum); % normalized energy
for i = 1 : filenum
    energy(:, i) = sum(samples_enframe{i} .* samples_enframe{i}); %sumarize on each column
    EnSum(:, 1) = EnSum(:, 1) + energy(:, i); % energy sum of all channels
end
for i = 1 : filenum     
    ne(:,i)  = energy(:, i) ./ EnSum; %a column is the normaized energy for one channel  
end
ne = log(ne); % Natural logarithm of normalized energy
clear EnSum;
%% log energy differences
log_en_diff = zeros(framenum, filenum); % 
for i = 1 : filenum 
    for j = 1 : filenum
        if i == j
            continue
        end
        log_en_diff(:,i) = log_en_diff(:,i) + energy(:, i) ./ energy(:, j); %a column is the energy for a channel         
    end
end
log_en_diff = log(log_en_diff); % Natural logarithm 
%% normalized log energy differences
norm_log_en_diff = zeros(framenum, filenum); % 
for i = 1 : filenum    
     norm_log_en_diff(:,i) = log(energy(:, i)) - log(min(energy, [], 2)); %a column is the energy for a channel 
end
%% cross-channel correlation
w = hamming(windowsize); % hamming window
mean_norm_cross_corr = zeros(framenum, filenum);
max_norm_cross_corr = zeros(framenum, filenum); 
min_norm_cross_corr = zeros(framenum, filenum);
for i = 1 : filenum
    m = 1;
    for j = 1 : filenum
        if i == j
            continue; % only computed Cij when i != j
        end 
        for k = 1 : framenum
            max_tmp(k) = max(xcorr(samples_enframe{i}(:,k) .* w, samples_enframe{j}(:,k)));% cross-channel correlation             
        end
        cross_corr(:, m) = max_tmp' ./ energy(:, i);%normalized cross-channel correlation            
        m = m + 1; % increase the number of column
    end
    min_norm_cross_corr(:,i) = min(cross_corr, [], 2);
    max_norm_cross_corr(:, i) = max(cross_corr, [], 2);
    mean_norm_cross_corr(:, i) = mean(cross_corr, 2);   
end
clear energy;
feature.ne = ne;
feature.log_en_diff = log_en_diff;
feature.norm_log_en_diff = norm_log_en_diff;
feature.kur = kur;
feature.mean_norm_cross_corr = mean_norm_cross_corr;
feature.max_norm_cross_corr = max_norm_cross_corr;
feature.min_norm_cross_corr = min_norm_cross_corr;
feature.zcr = zcr;
disp('Finished!');