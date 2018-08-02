class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class binarySearchTree():
    def __init__(self):
        self.root  = None

    def search(self,x):
        p = self.root
        while p is not None:
            if x < p.data:
                p = p.lchild
            elif x>p.data:
                p = p.rchild
            else:
                return True
        return False

    def min1(self):
        if self.isEmpty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p.data

    def max1(self):
        if self.isEmpty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.data

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x<p.data:
            p.lchild = self._insert(p.lchild , x)
        elif x>p.data:
            p.rchild = self._insert(p.rchild, x)
        else:
            print  str(x) +'already exists'
        return p

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print p.data
        self._inorder(p.rchild)

#recursive to merge two sortd linked list 
    def merge_lists(h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if (h1.value < h2.value):
            h1.next = merge_lists(h1.next, h2)
            return h1
        else:
            h2.next = merge_lists(h2.next, h1)
            return h2

b = binarySearchTree()
lst = [2,1,1, 4]
for i in lst:
    b.insert(i)

print 'inorder starts now'
b.inorder()
print b.search(4)
