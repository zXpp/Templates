
function score = accuracy(ref_labels, sys_labels),
%ACCURACY Compute clustering accuracy using the true and cluster labels and
%   return the value in 'score'.
%
%   Input  : ref_labels    : N-by-1 vector containing true labels
%            sys_labels : N-by-1 vector containing cluster labels
%
%   Output : score          : clustering accuracy
%
%   Author : Wen-Yen Chen (wychen@alumni.cs.ucsb.edu)
%			 Chih-Jen Lin (cjlin@csie.ntu.edu.tw)

% Compute the confusion matrix 'cmat', where
%   col index is for true label (CAT),
%   row index is for cluster label (CLS).
n = length(ref_labels);
cat = spconvert([(1:n)',ref_labels,ones(n,1)]);% merge matrix by cols ,cat:n*3
cls = spconvert([(1:n)',sys_labels,ones(n,1)]);
cls = cls';
cmat = full(cls * cat);

%
% Calculate accuracy
%
[match, cost] = hungarian(-cmat);
score = 100*(-cost/n);
