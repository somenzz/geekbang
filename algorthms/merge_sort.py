#encoding=utf-8
import random

def merge_sort(data_list):
    '''
    归并排序程序入口
    '''
    length = len(data_list)
    merge_sort_c(data_list,0,length)

def merge_sort_c(data_list,p,q):
    '''
    递归调用
    '''
    #退出条件
    if p+1>=q:
        return 
    else:
        r = (p+q)//2 
        merge_sort_c(data_list,p,r)
        merge_sort_c(data_list,r,q)
        merge2(data_list,p,r,q)  #将data_list[p:r] 与 data_list[r:q] 按顺序归并到 data_list 相应位置

def merge(data_list,p,r,q):
    '''
    归并函数
    例如 data_list[p:q] = [...,1,4,2,3,...]
    data_list[p:r] = [1,4]
    data_list[r:q] = [2,3]
    tmp = [1,2,3,4]
    归并后 data_list[p:q] = [...,1,2,3,4,...]     
    '''
    tmp = []    
    i = p
    j = r 
    while i < r and j < q:
        if data_list[i] <= data_list[j]:
            tmp.append(data_list[i])
            i+=1
        else:
            tmp.append(data_list[j])
            j+=1

    while i < r :
        tmp.append(data_list[i])
        i+=1

    while j < q:
        tmp.append(data_list[j])
        j+=1
    
    #将 tmp 数据复制到 data_list
    for tmp_index,index in enumerate(range(p,q)):
        data_list[index] = tmp[tmp_index]
    
    
def merge2(data_list,p,r,q):
    '''
    利用哨兵的归并函数
    例如 data_list[p:q] = [...,1,4,2,3,...]
    part_left = [1,4]
    part_right = [2,3]
    归并后 data_list[p:q] = [...,1,2,3,4,...]     
    '''
    part_left = [data_list[index] for index in range(p,r)]
    part_right = [data_list[index] for index in range(r,q)]
    #对左边部分或右边部分增加哨兵，哨兵为待排序数据的最大值如99999
    max_value = 99999
    part_left.append(max_value)
    part_right.append(max_value)
    i = 0
    j = 0
    k = p
    # while i != r-p: # 也可以这样写，看自己喜好
    while part_left[i] != max_value:
        if part_left[i] <= part_right[j]:
            data_list[k] = part_left[i]
            i += 1
        else:
            data_list[k] = part_right[j]
            j += 1
        k +=1 #依次从左边部分和右边部分按顺序抽取数据    

if __name__ == "__main__":
    data_list = [random.randint(0,100) for i in range(10)]
    # data_list = [4,2,1,3,5,6,7,8]
    print(data_list)
    # merge(data_list,data_list[0:4],data_list[4:8])
    merge_sort(data_list)
    print(data_list)

