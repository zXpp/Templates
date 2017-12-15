function [C,M,W,N,D] = load_mixture_model_diagb(filename);
% load both ascii and binary format models;
%
% C = Covariance matrices 
% M = Mean vectors
% W = Prior probs (mixing weights)
% N = Number of components
% D = Dimensionality

fid=fopen(filename);
N0=fread(fid,2,'int32');
if N0(2)<200;   % maybe binary format 
Data(N0(1),N0(2))=0;
for i=1:N0(1);
Data(i,:)=fread(fid,N0(2),'float');   
end
fclose(fid);
N = Data(1,1);
D = size(Data, 2);
W = Data(2:4:size(Data, 1), 1);
M = Data(3:4:size(Data, 1), :);
C = Data(5:4:size(Data, 1), :);

else   %
fclose(fid);
Data = load(filename);
N = Data(1,1);
D = size(Data, 2);
W = Data(2:4:size(Data, 1), 1);
M = Data(3:4:size(Data, 1), :);
C = Data(5:4:size(Data, 1), :);
end;
