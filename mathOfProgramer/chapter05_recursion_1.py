# -*- coding: utf-8 -*-
# !/usr/local/bin/python
# Time: 2018/12/19 16:56:31
# Description:
# File Name: chapter05_recursion_1.py

money = [1,2,5,10]

def kinds_of_reward(total_reward, result):
    '''
   假设有四种面额的钱币，1 元、2 元、5 元和 10 元，而您一共给我 10 元，
   那您可以奖赏我 1 张 10 元，或者 10 张 1 元，或者 5 张 1 元外加 1 张 5 元等等。
   如果考虑每次奖赏的金额和先后顺序，那么最终一共有多少种不同的奖赏方式呢？”
    '''
    if total_reward == 0:
        print(result)
    elif total_reward < 0:
        return
    else:
        for m in money:
            newresult = result.copy()
            newresult.append(m)
            kinds_of_reward(total_reward-m,newresult)

def kinds_of_decompose(num,result):
    '''
    一个整数可以被分解为多个整数的乘积，
    例如，6 可以分解为 2x3。
    请使用递归编程的方法，为给定的整数 n，找到所有可能的分解（1 在解中最多只能出现 1 次）。
    例如，输入 8，输出是可以是 1x8, 8x1, 2x4, 4x2, 1x2x2x2, 1x2x4, ……
    '''

    if num == 1:
        result.append(1)
        print(result)    
    else:
        for i in range(num,0,-1):
            newresult = result.copy()
            if num % i == 0:
                newresult.append(i)
                if i == 1:
                    newresult.append(num)
                    print(newresult)
                else:
                    kinds_of_decompose(num // i, newresult)

def kids_of_decompose2(num,result):
    '''
    一个整数可以被分解为多个整数的乘积，
    例如，6 可以分解为 2x3。
    请使用递归编程的方法，为给定的整数 n，找到所有可能的分解（1 在解中最多只能出现 1 次）。
    例如，输入 8，输出是可以是 1x8, 8x1, 2x4, 4x2, 1x2x2x2, 1x2x4, ……
    修复部分选项缺失的bug 
    '''

    if num == 1:
        if 1 not in result:
            result.append(1)
        print(result)
    else:
        for i in range(1,num+1):
            if 1 in result:
                if i == 1:
                    continue
            if num % i == 0:
                newresult = result.copy()
                newresult.append(i)
                decompose(num // i, newresult)


          
if __name__ == "__main__":
    kinds_of_reward(5,[])
# [1, 1, 1, 1, 1]
# [1, 1, 1, 2]
# [1, 1, 2, 1]
# [1, 2, 1, 1]
# [1, 2, 2]
# [2, 1, 1, 1]
# [2, 1, 2]
# [2, 2, 1]
# [5]   
    kinds_of_decompose(8,[])

# [8, 1]
# [4, 2, 1]
# [4, 1, 2]
# [2, 4, 1]
# [2, 2, 2, 1]
# [2, 2, 1, 2]
# [2, 1, 4]
# [1, 8]
    kinds_of_decompose2(8,[])
# [1, 2, 2, 2]
# [1, 2, 4]
# [1, 4, 2]
# [1, 8]
# [2, 1, 2, 2]
# [2, 1, 4]
# [2, 2, 1, 2]
# [2, 2, 2, 1]
# [2, 4, 1]
# [4, 1, 2]
# [4, 2, 1]
# [8, 1]


