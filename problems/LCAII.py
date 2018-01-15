'''
Given two nodes in a binary tree (with parent pointer available), find their lowest common ancestor.

Assumptions

There is parent pointer for the nodes in the binary tree

The given two nodes are not guaranteed to be in the binary tree

Examples

        5

      /   \

     9     12

   /  \      \

  2    3      14

The lowest common ancestor of 2 and 14 is 5

The lowest common ancestor of 2 and 9 is 9

The lowest common ancestor of 2 and 8 is null (8 is not in the tree)

'''
class BinaryTree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None



BTroot = BinaryTree(1)
BTrootl = BinaryTree(2)
BTrootr = BinaryTree(3)
BTrootll = BinaryTree(4)
BTrootlr = BinaryTree(5)
BTrootrl = BinaryTree(6)
BTrootrr = BinaryTree(7)
BTroot.left = BTrootl
BTroot.right = BTrootr
BTrootr.left = BTrootrl
BTrootr.parent = BTroot
BTrootl.parent = BTroot
BTrootr.right = BTrootrr
BTrootl.left = BTrootll
BTrootl.right = BTrootlr
BTrootrr.parent = BTrootr
BTrootrl.parent = BTrootr
BTrootlr.parent = BTrootl
BTrootll.parent = BTrootl

def lca(root, p, q):
	q = [root]
	level = 0
	pLoc = (None, 0)
	qLoc = (None, 0)
	while q:
		curSize = len(q)
		for i in range(curSize):
			curr = q.pop(0)
			if curr == p:
				pLoc = (curr, level)
			elif curr == q:
				qLoc = (curr, level)

			if curr.left:
				q.append(curr.left)
			if curr.right:
				q.append(curr.right)
		level += 1
















