#encoding=utf-8
import random


class phone_num(object):

    num = ""

    def __init__(self,num=""):
        self.num = num
    
    def get_bit(self,bit):
        return int(self.num[bit-1:bit])
    
    def __str__(self):
        return self.num
    
    def __repr__(self):
        return self.num
    
def radix_sort(data_list):
    radix = 11
    ##借助稳定排序算法从尾至头排序 radix 次
    for i in range(radix,0,-1):
        counting_sort(data_list,i)


#改写的计数排序，方便基数排序调用,radix 指示是待排序数据的哪一位
def counting_sort(data_list,radix):
    length = len(data_list)
    #定义桶
    bucket = [] 
    max = data_list[0].get_bit(radix)
    for i in range(length):
        if data_list[i].get_bit(radix) > max:
            max = data_list[i].get_bit(radix)
    
    #初始化
    for i in range(max+1):
        bucket.append(0)

    #计数
    for i in range(length):
        bucket[data_list[i].get_bit(radix)] = bucket[data_list[i].get_bit(radix)] + 1
    
    ##累加
    for i in range(1,max+1):
        bucket[i] = bucket[i]+bucket[i-1]

    #计数排序,定义结果数组并初始化
    result = []
    for i in range(length):
        result.append(0)

    #从尾至头查找分数在result的插入位置，如果从头到尾的话就不是稳定的排序算法。
    for i in range(length-1,-1,-1):
        result[bucket[data_list[i].get_bit(radix)]-1] = data_list[i]
        bucket[data_list[i].get_bit(radix)] = bucket[data_list[i].get_bit(radix)] -1

    #将结果复制到原来的数组中，达到修改传入数组的效果
    for i in range(length):
        data_list[i] = result[i]

def create_phone_num():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    randomPre = random.choice(prelist)
    Number = "".join(random.choice("0123456789") for i in range(8))
    phoneNum = randomPre +Number
    return phoneNum

if __name__ == "__main__":
    data_list = [phone_num(create_phone_num()) for _ in range(10)]
    print("排序前")
    for i in data_list:
        print(i)

    radix_sort(data_list)

    print("排序后")
    for i in data_list:
        print(i)
    
   


