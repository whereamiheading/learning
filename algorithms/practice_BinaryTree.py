class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, var):
        if var is None:
            return
        print var.info + "   &&&&"
        self._preorder(var.lchild)
        self._preorder(var.rchild)


    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,var):
        if var is None:
            return

        self._inorder(var.lchild)
        print var.info + '****'
        self._inorder(var.rchild)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, var):
        if var is None:
            return

        self._postorder(var.lchild)
        self._postorder(var.rchild)
        print var.info + '%%%%'



    def create_tree(self):
        self.root = Node('P')
        self.root.lchild = Node('Q')
        self.root.rchild = Node('R')
        self.root.lchild.lchild = Node('A')
        self.root.lchild.rchild = Node('B')
        self.root.rchild.lchild = Node('Y')
        self.root.rchild.rchild = Node('Z')


bt = BinaryTree()
bt.create_tree()
print 'pre-order seq: '
bt.preorder()


print 'in-order seq: '
bt.inorder()

print 'postorder seq: '
bt.postorder()
