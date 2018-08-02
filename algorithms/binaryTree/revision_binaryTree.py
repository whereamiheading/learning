####   For every Node K, left child is at 2K, right child is at 2k+1. if 2k>n, then there is no left child for k-th element. If 2k+1>n, then no right child for element at k-th node .
###    Parent of any k-th node is at k//2  
####
####

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def create_tree(self):
        self.root = Node('P')
        self.root.lchild = Node('Q')
        self.root.rchild = Node('R')
        self.root.lchild.lchild = Node('A')
        self.root.lchild.rchild = Node('B')
        self.root.rchild.lchild = Node('C')
        self.root.rchild.rchild = Node('D')

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, p):
        if p is None:
            return

        print p.data
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, p):
        if p is None:
            return

        self._inorder(p.lchild)
        print p.data
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self,p):
        if p is None:
            return

        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print p.data

    def levelorder(self):
        queue = deque()
        queue.append(self.root)

        while len(queue)!=0:
            p = queue.popleft()
            print p.data
            if p.lchild is not None:
                queue.append(p.lchild)
            if p.rchild is not None:
                queue.append(p.rchild)


    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return 0

        hL = self._height(p.lchild)
        hR = self._height(p.rchild)

        if hL > hR:
            return 1+hL
        else:
            return 1+hR




bt = BinaryTree()
bt.create_tree()

print 'Pre-order'
bt.preorder()

print 'In-order'
bt.inorder()

print 'Post-order'
bt.postorder()

print 'Level-order'
bt.levelorder()

print 'Height of the tree is: ' + str(bt.height())
