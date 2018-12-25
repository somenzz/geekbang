#encoding=utf-8
#实现极客专栏 数据结构与算法之美 第13节 线性排序中的计数排序算法
def counting_sort(data_list):
    length = len(data_list)

    #定义桶
    bucket = [] 
    max = data_list[0]
    for d in data_list:
        if d > max:
            max = d
    #初始化
    for i in range(max+1):
        bucket.append(0)

    #计数
    for i in range(length):
        bucket[data_list[i]] = bucket[data_list[i]] + 1
    
    ##累加
    for i in range(1,max+1):
        bucket[i] = bucket[i]+bucket[i-1]

    #计数排序,定义结果数组并初始化
    result = []
    for i in range(length):
        result.append(0)

    #从尾至头查找分数在result的插入位置，如果从头到尾的话就不是稳定的排序算法。
    for i in range(length-1,-1,-1):
        result[bucket[data_list[i]]-1] = data_list[i]
        bucket[data_list[i]] = bucket[data_list[i]] -1

    #将结果复制到原来的数组中，达到修改传入数组的效果
    for i in range(length):
        data_list[i] = result[i]


if __name__ == "__main__":
    data_list = [2,5,3,0,2,3,0,3]
    print(data_list)
    counting_sort(data_list)
    print(data_list)
    


    

