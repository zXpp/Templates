# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:14:13 2016
#
@author: zzpp220
"""
import sys  
#
  
#
def merge(nums, first, middle, last):  
    ''''' merge '''  
    # 切片边界,左闭右开并且是了0为开始  
    lnums = nums[first:middle+1]  
    rnums = nums[middle+1:last+1]  
    lnums.append(sys.maxint)  
    rnums.append(sys.maxint)  
    l = 0  
    r = 0  
    for i in range(first, last+1):  
        if lnums[l] < rnums[r]:  
            nums[i] = lnums[l]  
            l+=1  
        else:  
            nums[i] = rnums[r]  
            r+=1  
#
def merge_sort(nums, first, last):  
    ''''' merge sort
    merge_sort函数中传递的是下标，不是元素个数
    '''  
#
    if first < last:  
        middle = (first + last)/2
        merge_sort(nums, first, middle)  
        merge_sort(nums, middle+1, last)  
        merge(nums, first, middle,last)  
#
        
def insert_sort(a):  
    ''''' 插入排序
有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，
但要求插入后此数据序列仍然有序。刚开始 一个元素显然有序，然后插入一
个元素到适当位置，然后再插入第三个元素，依次类推
    '''  
    a_len = len(a)  
    for i in range(a_len):
        key = a[i]
        j = i - 1
        while j > 0 and a[j] > key:  
            a[j+1] = a[j]  
            j-=1  
        a[j+1] = key  
    return a      
        
if __name__ == '__main__':  
 
    nums = [10,8,4,-1,2,6,7,3]  
    print 'nums is:', nums  
   # merge_sort(nums, 0, 7)
    print 'merge sort:', nums
    insert_sort(nums)
    print 'insert sort:', nums