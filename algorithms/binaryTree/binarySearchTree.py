class TreeEmptyError(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, x):
        self._insert(self, root, x)

    def _insert(self, p ,x ):
        if p is None:
            p = Node(x)
        elif x < p.data:
            p.lchild = self._insert(self, p.lchild, x)
        elif x >p.data:
            p.rchild = self._insert(self, p.rchild, x)
        else:
            print str(x) +' is already present in the tree'

        return p


    def search(self, x):
        return self._search(self.root,x ) is not None

    def _search(self, p,x):
        if p is None:
            return None
        if x < p.data:
            return self._search(p.lchild, x)
        if x > p.data:
            return self._search(p.rchild, x)
        return p

    def search1(self, x):
        p =self.root
        while p is not None:
            if x < p.data:
                p = p.lchild
            elif x > p.data:
                p = p.rchild
            else:
                return true
        return false


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

    def min2(self):
        return self._min(self.root).data

    def _min(self, p):
        if p.lchild is None:
            return p.data
        return self._min(p.lchild)

    def max2(self):
        return self._max(self.root).data

    def _max(self, p):
        if p.rchild is None:
            return p.data
        return self._max(p.rchild)

    def insert1(self, x):
        p = self.root
        par = None

        while p is not None:
            par = p
            if x < p.data:
                p = p.lchild
            elif x >p.data:
                p = p.rchild
            else:
                print 'key present '
                return
        temp = Node(x)
        if par == None:
            self.root = par
        elif x < par.data:
            par.lchild = temp
        else:
            par.rchild = temp

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p,x ):
        if p is None:
            p = Node(x)
        elif x < p.data:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.data:
            p.rchild = self._insert(p.rchild, x)
        else:
            print 'key already present'
        return p

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print p.data
        self._inorder(p.rchild)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, p):
        if p is None:
            return
        print p.data
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print p.data


bst = BinarySearchTree()

while True:
    print "1: Display Tree"
    print "2: Search Iterative"
    print "3: Search Recursive"
    print "4: Insert a node Iterative"
    print "5: Insert a node recursive"
    print "6: Delete a node Iterative"
    print "7: Delete a node Recursive"
    print "8. Find min Iterative"
    print "9: Find min Recursive"
    print "10: Find max Iterative"
    print "11: Find max Recursive"
    print "12: PreOrder traversal"
    print "13: InOrder traversal"
    print "14: PostOrder traversal"
    print "15: Height of tree"
    print "16: quit"
    option = int(input("Enter an option: "))


    if option == 1:
        bst.display()
    elif option == 2:
        x = int(input("Enter key to be searched: "))
        if bst.search1(x):
            print "Key Found"
        else:
            print 'Key not found'


    elif option == 3:
        x = int(input("Enter key to be searched: "))
        if bst.search(x):
            print "Key Found"
        else:
            print 'Key not found'

    elif option == 4:
        element = int(input("Enter element to be inserted: "))
        bst.insert1(element)

    elif option == 5:
        element = int(input("Enter element to be inserted: "))
        bst.insert(element)

    elif option == 6:
        element = int(input("Enter element to be deleted : "))
        bst.delete1(element)

    elif option == 7:
        element = int(input("Enter element to be deleted : "))
        bst.delete(element)

    elif option == 8:
        print 'Min key is : ' + str(bst.min1())
    elif option == 9:
        print 'Min key is : ' + str(bst.min2())
    elif option == 10:
        print 'Max key is : ' + str(bst.max1())
    elif option == 11:
        print 'Max key is : ' + str(bst.max2())
    elif option == 12:
        bst.preorder()
    elif option == 13:
    	bst.inorder()
    elif option == 14:
    	bst.postorder()
    elif option == 15:
        print 'Height of tree is: '+ str(bst.height())
    elif option == 16:
        break
    else:
        print "Wrong choice"
