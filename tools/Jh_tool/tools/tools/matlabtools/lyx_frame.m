%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%程序信息%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%--1.功能描述：对输入的语音信号进行分帧处理

%--2.输入参数： x:           Nx1 speech signal vector, typically an utterance in the time domain(输入信号矢量)
%Note: x is zero-padded to be of length m*l
%               windowsize:  Number of points to consider in each window of speech(窗长)
%               overlap:     Number of samples between two frames(两帧之间重叠的点数)
%               fs:          sampling frequency(取样频率)

%%--3.输出参数：y:           mxl matrix, where each column is a frame of x (l frames in x)

%%--4.编程信息：编程时间： 2006-11-4； 编程人员：李艳雄

%%--5.参考文献或网站
%   

%%--6.程序思想： 根据输入参数（即帧长，帧移，取样频率）对信号进行加窗（汉明窗）分帧

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%程序内容%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function y =lyx_frame(x,windowsize,overlap,fs)
if size(x,1)>1 & size(x,2)>1
   error('x is not Nx1 vector!');
   return
end;
if nargin<4,
   fs = 11025; % If fs isn't global, set to 11025 KHz
end;
if nargin<3,
   frameRate = windowsize/2;
end;
if nargin<2,
   if fs==22050,
      windowsize = 512; % 23.22 ms at 22.05KHz
   elseif fs==11025,
      windowsize = 256; % 23.22 ms at 11.025 KHz
   elseif fs==8000,
      windowsize = 128; % 16 ms at 8KHz
  else
      windowsize = 256;
   end;
end;
if size(x,2)>1,
   x = x'; % Convert to coulmn vector
end;
N=length(x);%length of speech signal
p=windowsize-overlap; % Increment by p samples between frames
m=windowsize;%size of per frame
l = ceil((N-m+p)/p); % Number of frames in y
x = [x;zeros(m+(l-1)*p-N,1)]; % Zero-pad to fit in m*l matrix
y = zeros(m,l); % Declare space for y
for c=1:l
   y(:,c)=x(1+(c-1)*p:(c-1)*p+m).*hamming(m);%x is multiplied by hamming(m) and divided into l parts,the result is y
end;