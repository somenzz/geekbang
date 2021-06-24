# 基于orderedDict实现
from collections import OrderedDict
class LRUCache():
    '''
    function:利用collection.OrdereDict数据类型实现最近最少使用的算法
    OrdereDict有个特殊的方法popitem(Last=False)时则实现队列，弹出最先插入的元素
    而当Last=True则实现堆栈方法，弹出的是最近插入的那个元素。
    实现了两个方法：get(key)取出键中对应的值，若没有返回None
    set(key,value)更具LRU特性添加元素
    '''

    def __init__(self, size=5):
        self.size = size
        self.cache = OrderedDict()  # 有序字典

    def get(self, key):
        if key in self.cache.keys():
            # 因为在访问的同时还要记录访问的次数（顺序）
            value = self.cache.pop(key)
            # 保证最近访问的永远在list的最后面
            self.cache[key] = value
            return value
        else:
            return None

    def put(self, key, value):
        if key in self.cache.keys():
            self.cache.pop(key)
            self.cache[key] = value
        elif self.size == len(self.cache):
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value

    def print(self):
        for x in self.cache:
            print(self.cache.get(x), end='<-')

        print()


if __name__ == '__main__':


    cache = LRUCache(3)
    cache.put(1,'Python七号1')
    print('put 1 Python七号1')
    cache.put(2, 'Python七号2')
    print('put 2 Python七号2')
    cache.put(3, 'Python七号3')
    print('put 3 Python七号3')
    cache.print()
    print('put 4 Python七号4')
    cache.put(4, 'Python七号4')
    cache.print()
    print('get 3')
    print(cache.get(3))
    cache.print()