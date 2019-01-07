#encoding = utf-8

def count_dp(num):
    kinds = [2,3,7]
    ##循环使用tmp，降低内存占用
    tmp = [1,1,2,2,2,1,3]
    result = [[2],[3],[2,2],[2,3],[3,3],[7],[2,3,3]]
    if num <2:
        return
    elif 2 <= num <=8:
        return tmp[num-2],result[num-2]
    else:
        for i in range(9,num+1):
            values=[] #保留三个数据，取最小的那个
            for kind in kinds:
                values.append( (tmp[(i-2-kind)%7] + 1, (i-2-kind)%7 , kind) )
            min_value = min(values) ##默认按第一个值比较，取最小的
            #print(min_value)
            tmp_result = result[min_value[1]].copy()
            #print(tmp_result)
            tmp_result.append(min_value[2])
            #print(tmp_result)

            ##循环保存在临时数组中
            tmp[(i-2)%7] = min_value[0]
            result[(i-2)%7].clear()
            result[(i-2)%7] = tmp_result.copy()
        return tmp[(num-2)%7],result[(num-2)%7]


def count_recursion(num):
    kinds = [2,3,7]
    ##循环使用tmp，降低内存占用
    tmp = [1,1,2,2,2,1,3]
    if num <2:
        return
    elif 2 <= num <=8:
        return tmp[num-2]
    else:
        ##采用递归方式
        values=[] #保留三个数据，取最小的那个
        for kind in kinds:
            values.append(count_recursion(num - kind))
        min_value = min(values)+1 ##默认按第一个值比较，取最小的
        return min_value

if __name__ == "__main__":
    for i in [1,2,3,4,5,6,7,8,9,10,100]:
        print(i,'->',count_dp(i))

    for i in [1,2,3,4,5,6,7,8,9,15,20]:
        print(i,'->',count_recursion(i))

# 1 -> None
# 2 -> (1, [2])
# 3 -> (1, [3])
# 4 -> (2, [2, 2])
# 5 -> (2, [2, 3])
# 6 -> (2, [3, 3])
# 7 -> (1, [7])
# 8 -> (3, [2, 3, 3])
# 9 -> (2, [2, 7])
# 10 -> (2, [3, 7])
# 100 -> (15, [2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])

# 1 -> None
# 2 -> 1
# 3 -> 1
# 4 -> 2
# 5 -> 2
# 6 -> 2
# 7 -> 1
# 8 -> 3
# 9 -> 2
# 15 -> 4
# 20 -> 4