%删除文件中的某些符合变量str中正则表达式的行，将剩余的内容存到tmpfile
%只需要按需改变 no.5 中的文件名和no.10中想要删除的行中的特有字符/数字/表示之类的正则表达式
%
tmpfile='tmp1.rttm';
fidin=fopen('train.lab','r'); % 打开原始数据文件（.list）
fidtmp=fopen(tmpfile,'w'); % 创建保存数据文件（不含说明文字）
 while ~feof(fidin) % 判断是否为文件末尾
  tline=fgetl(fidin); % 从文件读入一行文本（不含回车键）
  if ~isempty(tline) % 判断是否空行
    str = '*'; %正则表达式为：该行中是否包含除 - . E e 数字 和 空白字符 外的其他字符
    start = regexp(tline,str, 'once');
    if isempty(start)
      fprintf(fidtmp,'%s\n',tline);
    end
  end
 end
fclose(fidin);
fclose(fidtmp);
%data=textread(tmpfile);
% delete(tmpfile)