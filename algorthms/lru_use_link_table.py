


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class LRU:

    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.head = Node('head') #哨兵
        self.tail = Node('tail') #尾部哨兵

        self.head.next = self.tail
        self.tail.before = self.head

        self.cache = {}

    def __remove(self,node, delete = False):
        """
        删除双向链表的某一个 node  before - node - next
        """
        before = node.before
        next = node.next
        before.next = next
        next.before = before
        if delete:
            del node



    def __append_first(self,node):
        """
        插入  head node ......
        """

        node.next = self.head.next
        self.head.next.before = node
        self.head.next = node
        node.before = self.head



    def put(self,key,value):
        if key in self.cache:
            #缓存命中，删除当前节点，插入链表头部
            self.__remove(self.cache[key], delete = True)
        elif len(self.cache) >= self.max_size:
            self.__remove(self.tail.before, delete = True)

        new_node = Node(value)
        self.__append_first(new_node)
        self.cache[key] = new_node

    def get(self,key):
        if key in self.cache:
            node = self.cache[key]
            self.__remove(node,delete=False)
            self.__append_first(node)
            return node.data
        else:
            return None

    def print(self):
        node = cache.head
        while node:
            if node.next == None:
                print(node.data)
            else:
                print(node.data,end=' -> ')
            node = node.next


if __name__ == '__main__':

    cache = LRU(3)
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
    print(cache.get(5))
    cache.print()


