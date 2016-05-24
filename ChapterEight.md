## Tree
Tree is a big step forward, first time people think beyond "before and after" this kind of linear data structure.

## Parts
1. Root, 2. Parent - Children 3. Leaves, Siblings, internal nodes. 4. Ancestor(including itself), decendant, and subtree (all including it self) 5. edge - between two leaves.
6. Path - linked edge.

## Ordered Tree
the kids of a tree is ORDERED. Which means the it is like a book. all immediate kids are ordered as Chpt1, Chpt2,... and in each chapter the documents are arranged as $1.1, $1.2....

The familiy tree, if ordered by birthday, is an ordered tree.

## depth
how many ancestors p has, not counting itself.

## height
from bottom to top. how high is the tree (subtree), must be the heighest number in of all leaves. leaf height == 0

## binary tree
two kids or non kids - proper tree
decision tree - yes or no, go deep
left subtree, right subtree
+ - X /  can form a binary tree
binary tree has left, right and sibling to find the surrounding element

## proper binary tree
nodes internal + 1 = nodes external
n > h + 1 (height is counted from 0)
n > 2h + 1 (height is counted from 0)

## Linked binary tree
Use a (element,parent,left,right) to represent a node.
a position contains a node.
a tree contains positions, each position contains a backward pointer to tree

## Array based binary tree
[0] is the root, the location of child node based on the location of parent node.
[p] is the parent location, then [2p+1] is the left child position, [2p+2] is the right child position. grandparent location is [(p-1)//2]
Worst case: space and node number n: S = 2^n -1 (huge waste)

## Preorder, Postorder traversal
Preorder - visit root, visit kids.
Post order - visit kids, visit root.
If a book, with Chapter 1 ...n and 1.1, 1,2... etc,

Preorder - C1, 1.1,1.2, C2, 2.1,2.2...
Postorder - 1.1,1.2,C1, 2.1,2.2,C2...

Since it goes no-repeat to all elements, it is O(n)

## Breadth - first
Common, for playing games.(make decisions)
list = queue
queue.append(root)
while queue.size > 0:
	current = q.dequeue()
	visit current
	q.enqueue(current.children)

## inorder traversal - only for binary trees
Concept: visit kid left, visit root, visit kid right
Recursion Method:
inorder(p):
	if p.left:
		inorder(p.left)
	visit p
	if p.right:
		inorder(p.right)
This will make sure that, the left-most is visited first.


Stack based:
def inorder(p):
	stack = stack()

	def do_visit(p):
		print(p)
		yeild p # maybe we want to yeild???

	def go_to_far_left(p):
		# goes to the left most child of position p
		stack.push(p)
		while stack.peak() and stack.peak().left:
			stack.push(stack.peak().left)

	go_to_far_left(p) # push the first element and now goes left-most
	while stack is not empty:
		visit = stack.pop() # left most leaf/non-leaf if has right child
		do_visit(visit)
		if visit.is_not_leaf(): # has right kid
			visit = visit.right
			go_to_far_left(visit)
			# back to while loop
		else:
			visit = stack.pop() # left most leaf's parent
			do_visit(visit)
			visit = visit.right # left most leaf's right sibling
			go_to_far_left(visit)
			# back to while loop

# Step 3, now visit parent
visit = visit.right # left most leaf's sibling
if visit.is_not_leaf():
	stack.push(visit)
	# go back to while loop Step 1
else:
	print visit
	# go back to Step 3


## Binary Search Tree
left < root < right
So the smallest on the left most and biggest on the right most. Inorder travel will get from small --> biggest
* if we use ordered list, same effect, each time we get rid of half elements.

## Euler Tour
It is exact the in-order implementation, but
we do something before we push stuff into a stack. and after it pops out, we do something to it again. In general, pre,post and in order can all use this hook to perform

def preorder(p):
	_pre_visit_hook
	visit p
	_post_visit_hook
	for each in p.children:
		preorder(each)

## Express Tree
1. How to create string from a tree?
2. How to create a tree from a string?
3. How to calculate result by the string?
4. How to calculate by the tree?

1. in-order traversal
def make_string(p):
	final_string = []
	create_string(p,final_string)
	return ''.join(final_string)

def create_string(p,final_string=[]):
	if p.is_leaf():
		final_string.append(p.value) 
	else:
		final_string.append('(')
		if p.left:
			create_string(p.left,final_string)
		
		final_string.append(p.value)

		if p.right:
			create_string(p.right,final_string)

2. use stack
def create_tree(tokens):
	s = stack
	# ignore the left (
	for each in tokens:
		if each == '(':
			continue
		if each == 'number':
			stack.push(each)
			continue
		if each == 'operator':
			stack.push(each)
			continue
		if each == ')':
			nodes = stack.pop(3)
			t = make_tree(nodes[left], nodes[root], nodes[right])
			stack.push(t)
			continue
	# now shall have last element in stack, it is a tree
	return s.pop()

3. Calculate result by string tokens?
def calculate(tokens):
	s = stack
	for each in tokens:
		if each == '(':
			continue
		if each == 'number':
			stack.push(each)
			continue
		if each == 'operator':
			stack.push(each)
			continue
		if each == ')':
			nodes = stack.pop(3)
			t = nodes[left] nodes[operator] nodes[right]
			stack.push(t)
			continue
	# now shall have last element in stack, it is a tree
	return s.pop()

4. Calculate by tree? Post traversal
def calculate(tree):
	p = tree.root
	def posttravel(p):
		if p is leaf():
			return p
		else:
			previous = posttravel(p.left)
			next = posttravel(p.right)
			return previous (p) next
		
		return p
	return posttravel(p)