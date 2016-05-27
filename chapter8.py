class Tree(object):
	''' Abstract class of a tree '''

	# ------- Abstract description of a position --------------
	class Position(object):
		''' a position in a tree, a node '''
		# --- abstract method ---
		def element(self):
			raise NotImplementedError('must implemented by sublclass')

		def __eq__(self, other):
			''' Return True if same location of position'''
			raise NotImplementedError('must implemented by sublclass')
		
		# --- Concret ---
		def __ne__(self, other):
			''' opposite of __eq__ '''
			return not (self.__eq__(other))

	# -------- Start the Tree implementation -----------
	def root(self):
		''' get back the root position, or None if empty tree'''
		raise NotImplementedError('must implemented by sublclass')

	def parent(self, p):
		''' return p's parent, or None if p is root '''
		raise NotImplementedError('must implemented by sublclass')

	def num_children(self,p):
		''' return the count of children that p has '''
		raise NotImplementedError('must implemented by sublclass')

	def children(self,p):
		''' get back an iteration of positions'''
		raise NotImplementedError('must implemented by sublclass')

	def __len__(self):
		''' return total numbers of positions inside the tree '''
		raise NotImplementedError('must implemented by sublclass')

	# -----------------------Concret methods inside this class ------------
	def is_root(self,p):
		'''check if position p is the root '''
		return self.root() == p

	def is_leaf(self,p):
		''' check if it is a leaf '''
		return self.num_children(p) == 0

	def is_empty(self):
		''' check if tree is empty '''
		return len(self) == 0

	def depth(self,p):
		''' return the number of ancenstors of p, not include itself'''
		# depth d, run time O(d), d < n, d worst case is n.
		if self.root() == p:
			return 0
		else:
			return 1 + self.depth(self, self.parent(p))

	def _height2(self,p):
		''' how heigh is the p position '''
		# Top down recursion will call on all the children element, ~n
		# return 0 is constant time
		# self.children(p) is related how many direct kids the p has, ~Cp
		# max() is like take 1 element if not big enough then throw it away.
		# eventually will go through all n, so is ~n
		# so each p will waste Cp on max() and C1+C2+C3... = n
		# so it will become O(n)
		if self.is_leaf(p):
			return 0
		else:
			p_children = self.children(p)
			max_child_height = max(self._height2(x) for x in p_children) 
			return 1 + max_child_height

	def height(self,p=None):
		''' return the height of subtree, if p == None, the entire tree '''
		if p is None:
			p = self.root()
		return self._height2(self,p)

class BinaryTree(Tree):
	''' ABS class for binary tree '''

	# --- Abstract ---
	def left(self,p):
		''' return a position representing a left child'''
		raise NotImplementedError('must implemented by sublclass')

	def right(self,p):
		''' return a right position as right child '''
		raise NotImplementedError('must implemented by sublclass')

    # --- Concret Method ---
	def sibling(self,p):
		''' return a borther of current position, can be None'''
		parent = self.parent(p)
		if parent:
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)
		else:
			return None

	def children(self,p):
		''' get iteration of children of p '''
		if self.left(p):
			yield self.left(p)
		if self.right(p):
			yield self.right(p)

class LinkedBinaryTree(BinaryTree):
	''' Concret class for linked binary class '''
	# Node points to parent, left kid, right kid and element
	# Four pointers.

	class _Node(object):
		__slots__ = ['element','parent','left','right']

		def __init__(self, element, parent=None,left=None,right=None):
			self.element = element
			self.parent = parent
			self.left = left
			self.right = right

	class Position(BinaryTree.Position):
		def __init__(self, container, node):
			self.container = container # reference to father tree object
			self.node = node

		# --- concret method ---
		def element(self):
			return self.node.element		

		def __eq__(self, other):
			''' Return True if same location of position'''
			if type(other) == type(self) and self.node == other.node

	# --- Linked Binary Tree ---
	# _root pointer, points to None or root
	# _size value, keep all values

	def _validate(self,p):
		''' tree validate that the position is valid '''
		if not isinstance(p, self.Position):
			raise TypeError('p must be a Position type')
		if p.container is not self:
			raise ValueError('p is not inside this tree')
		if p.node.parent is p.node:
			raise ValueError('p parent is itself, error!')

		return p.node

	def _make_position(self, node):
		''' if node is None, return None'''
		return self.Position(self, node) if node is not None else None
	
	def __init__(self):
		self.root = None # the pointer points to root element
		self.size = 0

	def __len__(self):
		return self.size

	def root(self):
		''' Get the root element '''
		return self._make_position(self.root) # if root is None, then return None

	def parent(self,p):
		''' return parent position of current position '''
		node = self._validate(p)
		return self._make_position(node.parent)

	def num_children(self,p):
		''' return the direct kids of node p '''
		node = self._validate(p)
		count = 0
		if node.left:
			count += 1
		if node.right:
			count += 1
		return count

	def left(self, p):
		''' Return left kid '''
		node = self._validate(p)
		return self._make_position(node.left)

	def right(self,p):
		node = self._validate(p)
		return self._make_position(node.right)

	def _add_root(self, e):
		if self.root is not None:
			raise Exception('root exists in tree')
		self.root = self._Node(e)
		self.size += 1
		return self._make_position(self.root)

	def _add_left(self,p,e):
		''' create a new left kid of position p.
		if p is invalid, or p has a left kid, then Exception'''
		node = self._validate(p)
		if node.left is not None:
			raise ValueError('p has a left kid')

		node.left = self._Node(e,node)
		self.size += 1
		return self._make_position(node.left)

	def _add_right(self,p,e):
		''' create a new left kid of position p.
		if p is invalid, or p has a left kid, then Exception'''
		node = self._validate(p)
		if node.right is not None:
			raise ValueError('p has a left kid')

		node.right = self._Node(e,node)
		self.size += 1
		return self._make_position(node.right)

	def _replace(self, p, e):
		''' swith the p position, its node's element as new element
			return the old element object
		'''
		node = self._validate(p)
		old = node.element
		node.element = e
		return old

	def _delete(self,p):
		''' delete position p, try to replace it with its kid,
		if it has two kids, then error '''
		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError('p has two kids')

		kid = node.left if node.left else node.right
		if kid: # maybe none
			kid.parent = node.parent # points to one level above

		if node is self.root:
			self.root = kid
		else:
			if node is node.parent.left:
				node.parent.left = kid
			else:
				node.parent.right = kid

		self.size -= 1
		# delete the node, let it parent point to itself
		node.parent = node
		return node.element