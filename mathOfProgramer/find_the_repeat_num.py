#encoding=utf-8


def find_repeat_num(data_list):
    '''
    桶排序的思想
    '''
    length = len(data_list)
    bucket = []
    for i in range(max(data_list)):
        bucket.append(0)

    for i in range(length):
        if bucket[data_list[i]-1] == 1:
            return data_list[i]
        else:
            bucket[data_list[i]-1] = 1
    return None


def find_repeat_num2(data_list):
    '''
    1 到 n 连续
    1 2 3 4 5 3
    '''
    length = len(data_list)
    sum = data_list[0] 
    for i in range(1,length):
        sum = sum ^ data_list[i] 
    
    sum2 = 0
    for i in range(1,max(data_list)+1):
        sum2 = sum2 ^ i

    return sum ^ sum2
        

    
if __name__ == "__main__":
    data_list = [1,2,3,5,8,3]
    data_list2 = [1,2,3,4,5,6,4]
    repeat_num = find_repeat_num(data_list)    
    repeat_num2 = find_repeat_num2(data_list2)    
    print(repeat_num)
    print(repeat_num2)

    

