#!/usr/bin/python
# This script is to extract lines in MLF file according to one SCP file, and then
# write these lines into another MLF file
#
import os,sys
fn1 = 'TBL0101-MIXA1'
fn2 = 'TBL0206-MIXA1'
fn3 = 'TBL0301-MIXA1'
fn4 = 'TBL0401-MIXA1'
fn5 = 'TBL0501-MIXA1'
fn6 = 'TBL0601-MIXA1'
fn7 = 'TBL0701-MIXA1'
fn8 = 'TBL0801-MIXA1'
fn9 = 'TBL0901-MIXA1'
fn10 = 'TBL1001-MIXA1'
fn11 = 'TBL1101-MIXA1'
fn12 = 'TBL1201-MIXA1'
mlf2 = open('/share/spandh.ami1/usr/yanxiong/tnet.tbl-tbl.sad.fbank/cv.mlf.temp','wa')
mlf2.write('#!MLF!#\n') # write the first line of mlf file
mlf1 = open('/share/spandh.ami1/usr/yanxiong/data/tbl.full.fbank.new/tbl.all.files.merged.segments.mlf','r')
while True:
    line1 = mlf1.readline()
    if not line1:
        break
    ex1 = fn1 in line1  or fn2 in line1  or fn3 in line1  or fn4 in line1  or fn5 in line1  or fn6 in line1
    ex2 = fn7 in line1 or fn8 in line1 or fn9 in line1 or fn10 in line1 or fn11 in line1 or fn12 in line1
    if ex1 or ex2:
        mlf2.write(line1)
        line2 = mlf1.readline()
        mlf2.write(line2)
        line3 = mlf1.readline()
        mlf2.write(line3)
mlf1.close
mlf2.close            
