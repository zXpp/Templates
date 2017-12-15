% DP_boundary_alignment.m
%
% Determine closeness between two time alignments using dynamic programming
%
% Authors:  Van Zyl van Vuuren, Louis ten Bosch and Thomas Niesler
%           Stellenbosch University
%           Copyright (C) 2012-2013. All rights reserved.
% 
% This software is provided for research purposes only. Under this
% condition it may be distributed freely, both in full and in part,
% provided that this entire copyright notice is included at the
% start of any of its copies and any applications and derivations
% thereof.
%
% This software is supplied as-is. There is no warranty of any kind,
% either explicit or implied, regarding any aspect including, but not
% limited to: warranty of fitness of purpose, or merchantability, or 
% results obtained from use of this software.
%
% If you would like to acknowledge this software, please cite:
% van Vuuren, VZ; ten Bosch, L; Niesler, T.R. A Dynamic Programming
% Framework for Neural Network-Based Automatic Speech Segmentation.
% Proceedings of Interspeech, Lyon, France, 2013. 


function [overall_score, nmatches, nins, ndel, ins_indices, del_indices, match_indices] = DP_boundary_alignment(P1, P2)
%DP alignment between two arrays of boundary times 

% P1 and P2 are arrays with real numbers (interpreted as time instants)
% P1 is the hypothesised boundary time sequence
% P2 is considered the reference boundary time sequence
% overall_score = time alignment score between two sequences
% nmatches =  number of matches
% nins = number of insertions
% ndel = number of deletions
% ins_indices = indices of insertions in P1
% del_indices = indices of deletions in P2
% match_indices = indices of matches in P1


% Define global score matrix, keep pointers in matrix pointer
glob = inf*ones(length(P1), length(P2));
pointer = nan*ones(length(P1), length(P2));

glob(1, 1) = abs(P1(1)-P2(1));
pointer(1, 1) = 0;

for i=2:size(glob, 1) % Calculate first column's score
   if(P1(i)>=P2(1) && P1(i)<P2(2)) % If P1(i) boundary lies between two P2 bounds 
       loc_score = min(abs(P1(i)-P2(1)),abs(P2(2)-P1(i)));
   else
       loc_score = abs(P1(i)-P2(1));
   end
  glob(i, 1) = glob(i-1, 1) + loc_score;
  pointer(i, 1) = 2;
end;

for j=2:size(glob, 2) % Calculate first row's score
    if(P2(j)>=P1(1) && P2(j)<P1(2)) % If P2(i) boundary lies between two P1 bounds 
       loc_score = min(abs(P2(j)-P1(1)),abs(P1(2)-P2(j)));
   else
       loc_score = abs(P2(j)-P1(1));
   end
    glob(1, j) = glob(1, j-1) + loc_score;
    pointer(1, j) = 3;
end;

match_weight = 1.01; % Match penalty

for i=2:size(glob, 1)
    for j=2:size(glob, 2)
        % Match: Give match a slight penalty by heavier weight than an insertion or deletion
        %        This forces matches to be between closest possible boundaries
        match_score = abs(P1(i)-P2(j))*match_weight; 

        %Insertion: 
        if( j<length(P2))
            if(P1(i)>=P2(j) && P1(i)<P2(j+1)) %if P1(i) boundary lies between two P2 boundaries
                ins_score = min(abs(P1(i)-P2(j)),abs(P2(j+1)-P1(i)));
            else
                ins_score = abs(P1(i)-P2(j));
            end
        else
            ins_score = abs(P1(i)-P2(j));
        end
        
        %Deletion:
        if( i<length(P1))
            if(P2(j)>=P1(i) && P2(j)<P1(i+1)) %if P2(2) boundary lies between two P1 boundaries
                del_score = min(abs(P2(j)-P1(i)),abs(P1(i+1)-P2(j)));
            else
                del_score = abs(P2(j)-P1(i));
            end
        else
            del_score = abs(P2(j)-P1(i));
        end
        
        % The minimum of the three score paths survives 
        [minimum, where] = ...
            min([(glob(i-1, j-1)+match_score) (glob(i-1, j)+ins_score) (glob(i, j-1)+del_score)]);
        glob(i, j) = minimum;
        pointer(i, j) = where;
    end;
end;

ins_indices = [];
del_indices = [];
match_indices = [];

% Backtrace path.
PATH = [];
i=size(glob, 1); j=size(glob, 2);
PATH = [[i j]; PATH];
nins = 0; ndel = 0; nmatches = 0;
ptr = pointer(i, j);
match_score = 0;

while (ptr > 0)
    if (ptr == 2)
        ins_indices = [ins_indices i];
        i=i-1; nins = nins+1;
    end
    if (ptr == 1)
        match_indices = [match_indices i];
        temp = glob(i, j);
        i=i-1; j=j-1; nmatches = nmatches+1;
        match_score = match_score + temp - glob(i, j);
    end
    if (ptr == 3)
        del_indices = [del_indices j];
        j=j-1; ndel = ndel+1;
    end
    PATH = [[i j]; PATH];
    ptr = pointer(i, j);
end

nmatches = nmatches + 1; % Rememberthe first match at matrix(0,0)
overall_score = glob(end, end);
