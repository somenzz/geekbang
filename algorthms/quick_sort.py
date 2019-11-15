#encoding=utf-8
import random

def quick_sort(data_list):
    length = len(data_list)
    quick_sort_c(data_list,0,length-1)

def quick_sort_c(data_list,begin,end):
    """
    可以递归的函数调用
    """
    if begin >= end:
        return
    else:
        #获取分区数据partition_data最后的下标
        index = partition(data_list,begin,end)
        print(data_list)
        quick_sort_c(data_list,begin,index-1)
        quick_sort_c(data_list,index+1,end)

def partition(data_list,begin,end):
    #选择最后一个元素作为分区键
    partition_key = data_list[end]

    #index为分区键的最终位置
    #比partition_key小的放左边，比partition_key 大的放右边
    index = begin 
    for i in range(begin,end):
        if data_list[i] < partition_key: 
            data_list[i],data_list[index] = data_list[index],data_list[i] 
            index+=1

    data_list[index],data_list[end] = data_list[end],data_list[index] 
    return index


def find_top_k(data_list,K):
    length = len(data_list)
    begin = 0
    end = length-1
    index = partition(data_list,begin,end)
    while index != length - K:
        if index >length - K:
            end = index-1
            index = partition(data_list,begin,index-1)
        else:
            begin = index+1
            index = partition(data_list,index+1,end)
    return data_list[index]



if __name__ == "__main__":
    # data_list = [random.randint(0,100) for i in range(100)]
    
    data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
    print(data_list)

    # print(find_top_k(data_list,7))
    for i in range(1,11):
        print(f"第 {i} 大元素是 {find_top_k(data_list,i)}")
    # data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
    # print("原始数组:", data_list)
    # print("排序过程如下")
    # quick_sort(data_list)
    # print("最终结果:",data_list)

 
