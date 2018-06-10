from collections import deque
class Node:
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def create_tree(self):
		self.root = Node('A')
		self.root.lchild = Node('B')
		self.root.rchild = Node('C')
		self.root.lchild.lchild = Node('P')
		self.root.lchild.rchild = Node('Q')
		self.root.rchild.lchild = Node('R')
		self.root.rchild.rchild = Node('S')

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

	def _inorder(self,p):
		if p is None:
			return

		self._inorder(p.lchild)
		print p.data
		self._inorder(p.rchild)

	def postorder(self):
		self._postorder(self.root)

	def _postorder(self, p):
		if p is None:
			return
		self._postorder(p.lchild)
		self._postorder(p.rchild)
		print p.data

	def level_order(self):
		queue = deque()
		queue.append(self.root)

		while len(queue) != 0:
			p = queue.popleft()
			print p.data
			if p.lchild is not None:
				queue.append(p.lchild)
			if p.rchild is not None:
				queue.append(p.rchild)

	def height(self):
		return self._height(self.root)

	def _height(self, p):
		if p is None:
			return 0

		hL = self._height(p.lchild)
		hR = self._height(p.rchild)

		if hL >hR:
			return 1 + hL
		else:
			return 1 + hR


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

print 'Height of the tree is ' + str(bt.height())


