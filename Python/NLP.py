#encoding=utf-8
import os
import re

def count(file_path):
    text = ""
    with open(file_path,"r") as r:
        text = r.read()
    text = text.lower()
    result = re.findall("\w+",text)
    count_dict = {}
    for s in result:
        if s not in count_dict:
            count_dict[s]  = 0
        count_dict[s]+=1
    return sorted(count_dict.items(),key=lambda x:x[1],reverse=True)



if __name__ == "__main__":
    r = count(r"E:\github\geekbang\Python\test.txt")
    for i in r:
        print(i)


    
    
