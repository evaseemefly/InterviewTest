# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/5/3 15:01'

def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(1,len(arr)):
            # 后面的大于前面的
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]

    return arr

arr=[1,3,2,4,9,6]
for temp in arr:
    print(temp)
print("---------")
arr_sort=bubble_sort(arr)
for temp in arr_sort:
    print(temp)
my_p= lambda :(print(temp) for temp in arr)
my_p()
