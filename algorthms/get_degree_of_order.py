# -*- coding: utf-8 -*-
# !/usr/local/bin/python
# Time: 2019/11/1 9:42:56
# Description:
# File Name: get_degree_of_order.py

yxd, nxd = 0, 0
yxd_pair ,nxd_pair = [],[]

def get_yxd_nxd(array):
    global yxd,nxd
    yxd, nxd = 0, 0
    mergSortCounting(array[:],0,len(array)-1) 
    print(f"原始数组{array} \n有序度为{yxd} : {yxd_pair}\n逆序度为{nxd} : {nxd_pair}")
    return yxd,nxd

def mergSortCounting(array,low,high):
    if low >= high:
        return
    middle = (low + high)//2
    mergSortCounting(array,low,middle)
    mergSortCounting(array,middle+1,high)
    merge(array,low,middle,high)


def merge(array,low,middle,high):
    global yxd,nxd,yxd_pair,nxd_pair
    array1 = array[low:middle+1]
    len_array1 = len(array1)
    array2 = array[middle+1:high+1]
    len_array2 = len(array2)
    i,i1,i2 = low,0,0

    while i1 < len_array1 and i2 < len_array2:
        if array1[i1] <= array2[i2]:
            array[i] = array1[i1]

            #在array2中找到比array1[i1]大的数据个数，并累加
            yxd += len_array2 - i2

            ##增加对有序对的记录，方便理解。
            for x in range(i2,len_array2):
                yxd_pair.append((array1[i1],array2[x]))
            
            i += 1
            i1 += 1

        else:
            array[i] = array2[i2]

            #在array1中找到比 array2[i2] 大的个数，并累加
            nxd += len_array1 - i1

            ##增加对逆序对的记录，方便理解。
            for x in range(i1,len_array1):
                nxd_pair.append((array1[x],array2[i2]))

            i += 1
            i2 += 1


    while i1 < len_array1:
        array[i] = array1[i1]
        i += 1
        i1 += 1
        
    while i2 < len_array2:
        array[i] = array2[i2]
        i += 1
        i2 += 1


if __name__ == "__main__":
    array_list = [2,4,3,1,5,6]
    get_yxd_nxd(array_list)
