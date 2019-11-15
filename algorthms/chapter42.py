#encoding=utf-8

def max_increase_list(nums:list) -> int:
    '''
    给定一组数据，返回最长递增子序列的长度
    '''
    
    length = len(nums)
    table = [[1]*length for _ in range(length)]
    
    for i in range(length):
        for j in range(i,length):
            # print(i,j)
            if nums[i] == nums[j]:
                table[i][j] = table[i-1][j]
            elif nums[i] < nums[j]: 
                table[i][j] = table[i][i]+1
            else : 
                table[i][j] = table[i][i]
    
    return table[length-1][length-1]

def max_increase_list2(nums:list) -> int:
    length= len(nums)
    lss_lengths = [0]*length
    lss_lengths[0] = 1
    #动态规划求解最长子序列
    for i in range(1,length):
    # 递推公式: lss_lengths[i] = max(condition: j < i && a[j] < a[i] value: lss_lengths[j] + 1)
        max = 1
        for j in range(0,i):
            if nums[i] > nums[j] and lss_lengths[j] >= max:
                max = lss_lengths[j] + 1
        lss_lengths[i] = max
    return lss_lengths[-1]



if __name__ == "__main__":
    print(max_increase_list2([0,2,9,3,6,5,1,7])) #5
    print(max_increase_list2([5,4,3,2,1])) #1
    print(max_increase_list2([1,2,3,4,5])) #5
    print(max_increase_list2([7,6,5,1,2,3,4,5]))#5
    print(max_increase_list2([7,1,6,2,3,5,4,5]))#5
    
