# -*- coding: utf-8 -*-
import math

#the function to calculate entropy--(joint-entropy/conditional-entropy/mutual-information) you should use the probabilities as the parameters
def entropy(*c):
    result=-1;
    if(len(c)>0):
        result=0;
    for x in c:
        result+=(-x)*math.log(x,2)
    return result;
if __name__=="__main__":
    a=entropy(6/17,6/17,5/17)#H(A)
    b=entropy(8/17,5/17,4/17)#H(B)
    ab=entropy(1/17,1/17,5/17,4/17,1/17,2/17,3/17)#H(A,B)
    Iab=a+b-ab#I(A,B)
    print("H(A): ",a)
    print("H(B): ",b)
    print("H(A,B): ",ab)
    print("I(A,B)(MI): ",Iab)#
    print("NMI_v1(): ",2*Iab/(a+b))#NMI
    print("NMI_v2: ",Iab/(math.sqrt(a*b)))

