# python 通过位运算将整数转为二进制
#encoding=utf-8
def int2binary(num):
    result=[]
    while num!=0:
        result.append(num & 1)
        num = num >> 1
    result.reverse()
    return result

print(*int2binary(10))
#输出 1010
