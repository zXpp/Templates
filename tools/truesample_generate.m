nspk=21;
sample_each=30;
truelabels=cell(nspk*sample_each,1);

for i=1:nspk
    
    for j=1:sample_each
        truelabels{j+(i-1)*sample_each}=i;
    end
end
truelabels_fina=cat(1,truelabels{:});
dlmwrite('/home/zzpp220/DATA/TRAIN/lists/truelabels_630.txt',truelabels_fina);