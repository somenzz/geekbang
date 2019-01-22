#encoding = utf-8

class TrieNode(object):
    def __init__(self, data):
        self.data = data
        self.children = [None for i in range(26)]
        self.isWordEnd = False

global root 
root = TrieNode('')


def insert(key):
    newnode = root
    for s in key:
        index = ord(s) - ord('a')
        if newnode.children[index] is None:
            newnode.children[index] = TrieNode(s)
        newnode = newnode.children[index]

    newnode.isWordEnd = True

def search(key):
    searchNode = root
    for s in key:
        index = ord(s) - ord('a')
        if searchNode.children[index] is None:
            return False
        searchNode = searchNode.children[index]
    if searchNode is None:
        return False
    elif searchNode.isWordEnd:
        return True
    else:
        return False

def d_print(node):
    if node.children is None:
        return
    else:
        print(node.data)
        for i in range(26):
            d_print(node.children[i])

if __name__ == "__main__":
    keys = ['my','name','mine','zheng','zhen']
    search_keys = ['my','name','mine','zheng','zheggn']
    for key in keys:
        insert(key)

    # d_print(root) 
    
    for key in search_keys:
        print(key,search(key))
        

    


