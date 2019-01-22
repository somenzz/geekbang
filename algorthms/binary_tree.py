#encoding=utf-8

class Node(object):
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.item)


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self,item):
        '''
        找到 Item 的父节点
        '''
        if self.root.item == item:
            return None #根节点没有父节点
        tmp = [self.root]
        while tmp :
            pop_node = tmp.pop(0)
            if pop_node.left.item == item or pop_node.right.item == item: 
                return pop_node
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None




    def delete(self,item):
        '''
        从树中删除一个元素，如果 item 的右节点为空，则将 item 的左节点提升至当前位置
        如果 item 的左节点为空，则将 item 的右节点提升至当前位置
        否则
        '''
        if self.root is None:
            return
        
    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res

    def preorder(self,root):  # 先序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorder(self,root):  # 中序序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self,root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result

t = Tree()
for i in range(10):
    t.add(i)
print('层序遍历:',t.traverse())
print('先序遍历:',t.preorder(t.root))
print('中序遍历:',t.inorder(t.root))
print('后序遍历:',t.postorder(t.root))

for i in range(1,10,2):
    print(i," 的父亲",t.get_parent(i))