## Copyright (C) 2014 Yan-Xiong Li
## 
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Octave; see the file COPYING.  If not, see
## <http://www.gnu.org/licenses/>.

## mergehtkfiles

## Author: Yan-Xiong Li <yanxiong@snarl.minigrid.dcs.shef.ac.uk>
## Created: 2014-03-28

function [ ret ] = mergehtkfiles(corpus)
if corpus == 'rt07'
    filepath = '/share/spandh.ami1/usr/yanxiong/data/rt07/auxfea/';  
if corpus == 'ami'
   filepath = '/share/spandh.ami1/usr/yanxiong/data/ami/auxfea/';
else corpus != 'rt07' && corpus != "ami"
   error('plese the name of corpus!');
end
[ d0, HTKCode ] = htkread('/share/spandh.ami1/usr/yanxiong/data/ami/fbank/complete/AMI-S3012D_m5048.fbk');I
[ d1, HTKCode ] = htkread(strcat(filepath, 'AMI-S3012D_m5048.ne'));
[ d2, HTKCode ] = htkread(strcat(filepath, 'AMI-S3012D_m5048.kur'));
%[ d3, HTKCode ] = htkread(strcat(filepath, 'AMI-S3012D_m5048.max_xcor'));
%[ d4, HTKCode ] = htkread(strcat(filepath, 'AMI-S3012D_m5048.mean_xcor'));
size(d0)
size(d1)
size(d2)
%size(d3)
%size(d4)
fprintf('d0 is: %f, d1 is: %f, d2 is: %f, d3 is: %f', d0, d1, d2, d3);
data = [d1 d2];
%data = [d1 d2 d3 d4];
Filename = strcat(filepath, 'CMU-0E07000-CM00x-R7.auxfeat');
htkwrite( data, Filename, HTKCode );

disp('finished!');

endfunction
