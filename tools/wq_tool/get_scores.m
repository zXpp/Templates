% load reference
fid = fopen('temp.ref', 'r');
in = textscan(fid, '%s');
fclose(fid);
ref = str2double(in{:});

% load system
fid = fopen('temp.sys', 'r');
in = textscan(fid, '%s');
fclose(fid);
sys = str2double(in{:});

% score
addpath('/home/sisterqin/score/');
[overall_score, nmatches, nins, ndel, ins_indices, del_indices, match_indices] = DP_boundary_alignment(sys,ref);
disp(['overall_score = ', num2str(overall_score)])
disp(['nmatches = ', num2str(nmatches)])
disp(['nins = ', num2str(nins)])
disp(['ndel = ', num2str(ndel)])
