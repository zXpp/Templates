%{ 

This is a demo on how to use the Identity Toolbox for GMM-UBM based speaker
recognition. A relatively small scale task has been designed using speech
material from the TIMIT corpus. There are a total of 630 (192 female and
438 male) speakers in TIMIT, from which we have selected 530 speakers for
background model training and the remaining 100 (30 female and 70 male)
speakers are used for tests. There are 10 short sentences per speaker in
TIMIT. For background model training we use all sentences from all 530
speakers (i.e., 5300 speech recordings in total). For speaker specific
model training we use 9 out of 10 sentences per speaker and keep the
remaining 1 sentence for tests. Verification trials consist of all possible
model-test combinations, making a total of 10,000 trials (100 target vs
9900 impostor trials).

Assuming that audio recordings are already converted 
into cepstral features, there are 4 steps involved:
 
 1. training a UBM from background data
 2. MAP adapting speaker models from the UBM using enrollment data
 3. scoring verification trials
 4. computing the performance measures (e.g., EER)

Note: given the relatively small size of the task, we can load all the data 
and models into memory. This, however, may not be practical for large scale 
tasks (or on machines with a limited memory). In such cases, the parameters 
should be saved to the disk.

Omid Sadjadi <s.omid.sadjadi@gmail.com>
Microsoft Research, Conversational Systems Research Center

%}

clc
clear

%% Step0: Opening MATLAB pool
nworkers = 1;
nworkers = min(nworkers, feature('NumCores'));
% isopen = parpool('local')>0;
% if ~isopen, parpool(nworkers); end

%% Step1: Training the UBM
dataList = '/home/zzpp220/DATA/TRAIN/lists/ubm_test.lst';
nmix = 512;
final_niter = 10;
ds_factor = 1;
ubmFilename='/home/zzpp220/DATA/TEST/ubm_test.gmm';
%ubm = gmm_em(dataList, nmix, final_niter, ds_factor, nworkers,ubmFilename);

%% Step2: Adapting the speaker models from UBM
fea_dir = '/home/zzpp220/DATA/TEST/MFCC/';
fea_ext = '.mfcc';
%fea_ext = '';
fid = fopen('/home/zzpp220/DATA/TRAIN/lists/test_speaker_model_maps.lst', 'rt');
C = textscan(fid, '%s %s');
fclose(fid);
%[C,IA,IC] = unique(A,'stable') returns the values of C in the same order that they appear in A
model_ids = unique(C{1}, 'stable');%
model_files = C{2};
nspks = length(model_ids);
map_tau = 10.0;
config = 'mwv';
gmm_models = cell(nspks, 1); 
 ubm=load('ubm_test.mat');%%% !!! tiaoshishi yong d bianliang
for spk = 1 : nspks,
    ids = find(ismember(C{1}, model_ids{spk}));
    spk_files = model_files(ids);
    spk_files = cellfun(@(x) fullfile(fea_dir, [x, fea_ext]),...  %# Prepend path to files
                       spk_files, 'UniformOutput', false);
    %a=[model_ids{spk}];
    gmm_models{spk} = mapAdapt(spk_files, ubm, map_tau, config,[model_ids{spk}]);
end

% %% Step3: Scoring the verification trials
% fea_dir = '../features/';
% fea_ext = '.htk';
% trial_list = '../lists/trials.lst';
% fid = fopen(trial_list, 'rt');
% C = textscan(fid, '%s %s %s');
% fclose(fid);
% [model_ids, ~, Kmodel] = unique(C{1}, 'stable'); % check if the order is the same as above!
% [test_files, ~, Ktest] = unique(C{2}, 'stable');
% test_files = cellfun(@(x) fullfile(fea_dir, [x, fea_ext]),...  %# Prepend path to files
%                        test_files, 'UniformOutput', false);
% trials = [Kmodel, Ktest];
% scores = score_gmm_trials(gmm_models, test_files, trials, ubm);
% 
% %% Step4: Computing the EER and plotting the DET curve
% labels = C{3};
% eer = compute_eer(scores, labels, true);