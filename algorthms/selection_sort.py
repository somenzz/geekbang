#encoding=utf-8

def selection_sort(data_list):
    count = 0 
    length = len(data_list)
    for i in range(length -1):
        print(data_list) #打印每一次选择后的结果
        min_index = i #存储最小值的下标，以便最后交换
        for j in range(i+1,length):
            count +=1
            if data_list[min_index] > data_list[j]:
                min_index = j
        if min_index != i: #说明需要交换，否则不需要自己自己交换 
            tmp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = tmp
    print(f"总循环次数为 {count}")
    return data_list

def selection_sort2(data_list):
    count = 0 
    length = len(data_list)
    for i in range(length -1):
        print(data_list) #打印每一次选择后的结果
        min_index = i #存储最小值的下标 
        max_index = length - i -1 #最大值的下标，以便最后交换

        for j in range(i+1,length - i -1):
            count +=1
            if data_list[min_index] > data_list[j]:
                min_index = j
            if data_list[max_index] < data_list[j]:
                max_index = j
            
            #退出条件
        if min_index +1 == max_index:
            break

        #前面的数据与最小值交换
        if min_index != i: #说明需要交换，否则不需要自己自己交换 
            tmp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = tmp

        #后面的数据与最大值交换
        if max_index != length - i -1: #说明需要交换，否则不需要自己与自己交换 
            tmp = data_list[length - i -1 ]
            data_list[length -i -1 ] = data_list[max_index]
            data_list[max_index] = tmp


    print(f"总循环次数为 {count}")
    return data_list


if __name__ == "__main__":
    unsort = [3,4,2,1,5,6,7,8]
    print("selection_sort 的结果",*selection_sort(unsort))
    unsort = [3,4,2,1,5,6,7,8]
    print("selection_sort2 的结果",*selection_sort2(unsort))