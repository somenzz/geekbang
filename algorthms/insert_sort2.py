#encoding=utf-8
import time

def insert_sort(data_list):
    '''
    无优化版
    '''
    count=0 #统计循环次数
    length = len(data_list)
    for i in range(1,length ): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
        tmp = data_list[i] #待插入的数据
        j = i 
        while j > 0: #从已排序区间查找插入位置
            count +=1
            if tmp < data_list[j-1]:
                data_list[j] = data_list[j-1]  #元素向后移动，腾出插入位置
            else:
                break
            j -= 1
        data_list[j] = tmp #插入操作
        print(data_list)
    print(f"总循环次数为 {count}")
    return data_list

def insert_sort2(data_list):
    '''
    使用二分查找函数确定待插入元素在有序区间的插入位置
    '''
    count=0 #统计循环次数
    length = len(data_list)
    for i in range(1,length ): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
        wait_insert_data = data_list[i] ##等待插入元素
        move_index = i 
        insert_index,count1 = binary_search(data_list[0:i],wait_insert_data) #寻找插入位置
        count+=count1 #统计循环次数需要加上二分查找的循环次数
        while move_index > insert_index: #移动元素，直到待插入位置处
            count+=1
            data_list[move_index] = data_list[move_index - 1]
            move_index -= 1
        data_list[insert_index] = wait_insert_data #插入操作
        print(data_list)

    print(f"总循环次数为 {count}")
    return data_list


def binary_search(data_list,data):    
    """
    输入:有序列表，和待查找的数据data
    输出：data 应该在该有序列表的插入位置
    count 变量纯粹是为了统计循环次数而使用的，实际应用时可去除。
    """
    count = 0
    length = len(data_list)
    low = 0
    high = length-1
    ##如果给定元素大于等于最后一个元素，则插入最后元素位置的后面
    ##如果小于第一个元素，则插入位置0 
    if data >= data_list [length -1]: return length,0
    elif data < data_list [0]: return 0,0
    insert_index = 0 
    while low < high-1:
        count +=1
        mid = (low + high)//2 #python中的除法结果默认为浮点数取整数部分时使用 //
        if data_list[mid] > data:
            high = mid
            insert_index = high
        else:
            low = mid
            insert_index = low+1  #如果值相同或者值大于mid的值，那么插入位置位于其后面
    return insert_index,count
        

def shell_sort(data_list):
    '''
    思想：分治策略
    希尔排序是一种分组直接插入排序方法，其原理是：先将整个序列分割成若干小的子序列，
    再分别对子序列进行直接插入排序，使得原来序列成为基本有序。
    这样通过对较小的序列进行插入排序，然后对基本有序的数列进行插入排序，能够提高插入排序算法的效率.
    '''
    length = len(data_list)
    space  = length//2
    while space > 0:
        for i in range(space,length ): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
            tmp = data_list[i] #待插入的数据
            index = i 
            for j in range(i-space,-1,-space): #从已排序区间查找插入位置
                if tmp < data_list[j]:
                    data_list[j+space] = data_list[j]  #元素向后移动，腾出插入位置
                    index = j #最后的j即为插入的位置
                else:
                    break
            data_list[index] = tmp #插入操作
            print(data_list)
        space = space // 2
    return data_list

def shell_sort2(data_list):
    '''
    思想：分治策略
    希尔排序是一种分组直接插入排序方法，其原理是：先将整个序列分割成若干小的子序列，
    再分别对子序列进行直接插入排序，使得原来序列成为基本有序。
    这样通过对较小的序列进行插入排序，然后对基本有序的数列进行插入排序，能够提高插入排序算法的效率.
    '''
    length = len(data_list)
    space  = length//2
    while space > 0:
        i = space
        while i < length: #默认第一个位置的元素是已排序区间，因此下标从 1 开始
            tmp = data_list[i] #待插入的数据
            j = i
            while j >= space and data_list[j - space] > tmp: #从已排序区间查找插入位置
                data_list[j] = data_list[j-space]  #元素向后移动，腾出插入位置                    
                j -= space
            data_list[j] = tmp #插入操作
            print(data_list)
            i +=1
        space = space // 2
    return data_list


        
if __name__ == "__main__":
    unsort = [1,3,4,2,1,5,6,7,8,4]
    print(*insert_sort(unsort)) 
    unsort = [1,3,4,2,1,5,6,7,8,4]
    # unsort = [1,2,3,4,5,6,7,8]
    print(*insert_sort2(unsort)) 
    # unsort = [9,8,7,6,5,4,3,2,1]
    # print(*shell_sort(unsort)) 
    # unsort = [9,8,7,6,5,4,3,2,1]
    # print(*shell_sort2(unsort)) 
