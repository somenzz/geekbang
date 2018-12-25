#encoding=utf-8
import random

def quick_sort(data_list):
    length = len(data_list)
    quick_sort_c(data_list,0,length)

def quick_sort_c(data_list,begin,end):
    """
    可以递归的函数调用
    """
    if begin == end:
        return
    else:
        #获取分区数据partition_data最后的下标
        index = partition(data_list,begin,end)
        # print(data_list)
        quick_sort_c(data_list,begin,index)
        quick_sort_c(data_list,index+1,end)

def partition(data_list,begin,end):
    #选择最后一个元素作为分区键
    partition_key = data_list[end-1]

    #index为分区键的最终位置
    index= begin  
    for i in range(begin,end-1):
        if data_list[i] < partition_key: 
            data_list[i],data_list[index] = data_list[index],data_list[i] 
            index+=1
    
    data_list[index],data_list[end-1] = data_list[end-1],data_list[index] 
    return index


def find_top_k(data_list,K):
    length = len(data_list)
    begin = 0
    end = length
    index = partition(data_list,begin,end)
    while index != length - K:
        if index >length - K:
            index = partition(data_list,begin,index)
        else:
            index = partition(data_list,index+1,end)
    return data_list[index]



if __name__ == "__main__":
    # data_list = [random.randint(0,100) for i in range(10)]
    
    data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
    print(data_list)
    for i in [1,2,3,4,5]:
        print(f"第 {i} 大元素是 {find_top_k(data_list,i)}")
    # data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
    # print("原始数组:", data_list)
    # print("排序过程如下")
    # quick_sort(data_list)
    # print("最终结果:",data_list)

 
