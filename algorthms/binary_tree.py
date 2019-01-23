# encoding=utf-8

class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)


class Tree(object):
    def __init__(self):
        # 根节点定义为 root 永不删除，做为哨兵使用。
        self.root = Node('root')

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

    def get_parent(self, item):
        '''
        找到 Item 的父节点
        '''
        if self.root.item == item:
            return None  # 根节点没有父节点
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item:
                return pop_node
            if pop_node.right and pop_node.right.item == item:
                return pop_node
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, item):
        '''
        从二叉树中删除一个元素
        先获取 待删除节点 item 的父节点
        如果父节点不为空，
            判断 item 的左右子树
            如果左子树为空，那么判断 item 是父节点的左孩子，还是右孩子，如果是左孩子，将父节点的左指针指向 item 的右子树，反之将父节点的右指针指向 item 的右子树
            如果右子树为空，那么判断 item 是父节点的左孩子，还是右孩子，如果是左孩子，将父节点的左指针指向 item 的左子树，反之将父节点的右指针指向 item 的左子树
            如果左右子树均不为空，寻找右子树中的最左叶子节点 x ，将 x 替代要删除的节点。
        删除成功，返回 True
        删除失败, 返回 False

        '''
        if self.root is None:  # 如果根为空，就什么也不做
            return False

        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

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

    def preorder(self, root):  # 先序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorder(self, root):  # 中序序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self, root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result

if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    print('层序遍历:', t.traverse())
    print('先序遍历:', t.preorder(t.root))
    print('中序遍历:', t.inorder(t.root))
    print('后序遍历:', t.postorder(t.root))

    for i in range(10):
        print(i, " 的父亲", t.get_parent(i))

    for i in range(0, 15, 3):
        print(f"删除 {i}", '成功' if t.delete(i) else '失败')
        print('层序遍历:', t.traverse())
        print('先序遍历:', t.preorder(t.root))
        print('中序遍历:', t.inorder(t.root))
        print('后序遍历:', t.postorder(t.root))
