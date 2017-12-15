function total_precise_array(fid,matrix);
[m,n]=size(matrix);
if m==1
    for j= 1: n
    fprintf(fid,'%18.16f\t',matrix(j));
    end
else
    for i=1:m
        for j= 1: n
            fprintf(fid,'%18.16f\t',matrix(i,j));
        end
        fprintf(fid,'\n');
    end
end