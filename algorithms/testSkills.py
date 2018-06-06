from collections import deque

class Node:
    def __init__(self, value):
        self.info = value
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
        self.recur_preorder(self.root)

    def recur_preorder(self, p):
        if p is None:
            return
        print p.info + ' @@@@@'
        self.recur_preorder(p.lchild)
        self.recur_preorder(p.rchild)

    def inorder(self):
        self.recur_inorder(self.root)

    def recur_inorder(self, p):
        if p is None:
            return
        self.recur_inorder(p.lchild)
        print p.info + ' ####'
        self.recur_inorder(p.rchild)

    def postorder(self):
        self.recur_postorder(self.root)

    def recur_postorder(self, p):
        if p is None:
            return

        self.recur_postorder(p.lchild)
        self.recur_postorder(p.rchild)
        print p.info + '  $$$$'

    def level_order(self):
        queue = deque()
        queue.append(self.root)

        while len(queue) != 0:
            p = queue.popleft()
            print p.info + ' %%%%'
            if p.lchild is not None:
                queue.append(p.lchild)
            if p.rchild is not None:
                queue.append(p.rchild)

bt = BinaryTree()
bt.create_tree()

print 'pre-order'
bt.preorder()

print 'in-order'
bt.inorder()

print 'postorder'
bt.postorder()

print 'level-order'
bt.level_order()
