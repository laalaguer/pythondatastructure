# --- A positional List, you can access with position if you know the node
# --- We are able to traversal on this list and add_before and add_after
# --- Also we are able to delete before and delete after
# --- For add, we can add element, for remove, we only remove node(the wrapper of element)
class PositionalDeque(object):
	class Node(object):
		__slots__ = ['element', 'predecessor','successor']
		def __init__(self, element):
			self.element = element
			self.predecessor = None
			self.successor = None

	def __init__(self):
		self.size = 0
		self.head = self.Node(None)
		self.tail = self.Node(None)
		self.head.successor = self.tail
		self.tail.predecessor = self.head

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size

	def first(self):
		''' return the first node '''
		if self.is_empty():
			raise Exception('List is empty')
		return self.head.successor

	def last(self):
		''' return the last node '''
		if self.is_empty():
			raise Exception('list is empty')
		return self.tail.predecessor

	def add_first(self, element):
		node = self.Node(element)
		node.successor = self.head.successor
		self.head.successor.predecessor = node
		node.predecessor = self.head
		self.head.successor = node
		self.size += 1

	def add_last(self, element):
		node = self.Node(element)
		node.successor = self.tail
		node.predecessor = self.tail.predecessor
		self.tail.predecessor.successor = node
		self.tail.predecessor = node
		self.size += 1
	
	def add_before(self, node, element):
		''' add before the node '''
		new = self.Node(element)
		new.predecessor = node.predecessor
		new.successor = node
		node.predecessor.successor = new
		node.predecessor = node
		self.size += 1

	def add_after(self, node, element):
		''' add after the node '''
		new = self.Node(element)
		node.successor.predecessor = new
		new.successor = node.successor
		new.predecessor = node
		node.successor = new
		self.size += 1

	def delete_fist(self):
		''' delete the node at the first node '''
		if self.is_empty():
			raise Exception('The list is Empty')
		return self.delete_after(self.head)

	def delete_last(self):
		''' delete the node at the last node '''
		if self.is_empty():
			raise Exception('The list is empty')
		return self.delete_before(self.tail)

	def delete_before(self, node):
		''' delete the one before the node '''
		self.size -= 1
		to_delete = node.predecessor
		to_delete.predecessor.successor = node
		node.predecessor = to_delete.predecessor
		to_delete.successor = None
		to_delete.predecessor = None
		return to_delete

	def delete_after(self, node):
		''' delete the one after the node '''
		self.size -= 1
		to_delete = node.successor
		to_delete.successor.predecessor = node
		node.successor = to_delete.successor
		to_delete.successor = None
		to_delete.predecessor = None
		return to_delete

	def __iter__(self):
		''' Will return the node one by one'''
		cur = self.head.successor
		while cur is not self.tail:
			yield cur
			cur = cur.successor

q = PositionalDeque()
q.add_first(1)
q.add_last(2)
print [each.element for each in q],len(q)
q.add_first(3)
print [each.element for each in q],len(q)
for each in q:
	if each.element == 3:
		q.add_before(each,2.9)
print [each.element for each in q],len(q)
for each in q:
	if each.element == 2:
		q.add_after(each,2.1)
print [each.element for each in q],len(q)
q.delete_fist()
print [each.element for each in q],len(q)
q.delete_last()
print [each.element for each in q],len(q)


class PriorityQueueBase(object):

	# --- item class ---
	class Item(object):
		# key is the priority, value is the actual value you want to store
		__slots__ = ['key','value']

		def __init__(self,key,value):
			self.key = key
			self.value = value

		def __lt__(self,other):
			return self.key < other.key

class PriorityQueueUnsorted(PriorityQueueBase):
	def __init__(self):
		self.holder = PositionalDeque()

	def is_empty(self):
		return self.holder.is_empty()

	def __len__(self):
		return len(self.holder)

	def add(self,key,value):
		self.holder.add_last(self.Item(key,value))

	def min(self):
		''' big O(n) '''
		if self.is_empty():
			raise Exception('Nothing inside the list')

		min_node = self.holder.first()
		for each in self.holder:
			# each will be the Node wraps around the Item
			if each.element.key < min_node.element.key:
				min_node = each

		return min_node.element.key, min_node.element.value

	def remove_min(self):
		''' big O(n) to find, remove O(1)'''
		if self.is_empty():
			raise Exception('Nothing inside the list')
		min_node = self.holder.first()
		for each in self.holder:
			# each will be the Node wraps around the Item
			if each.element.key < min_node.element.key:
				min_node = each

		result_node = self.holder.delete_before(min_node.successor)
		return result_node.element.key, result_node.element.value

	def __iter__(self):
		return self.holder.__iter__()

p = PriorityQueueUnsorted()
p.add(3,'a')
p.add(4,'b')
p.add(5,'c')
print [(each.element.key, each.element.value) for each in p]
print p.min()
print [(each.element.key, each.element.value) for each in p]
print p.remove_min()
print [(each.element.key, each.element.value) for each in p]


class PriorityQueueSorted(PriorityQueueBase):
	def __init__(self):
		self.holder = PositionalDeque()

	def is_empty(self):
		return self.holder.is_empty()

	def __len__(self):
		return len(self.holder)

	def add(self,key,value):
		''' big O(n) '''
		if self.is_empty():
			self.holder.add_last(self.Item(key,value))
		else:
			max_node = self.holder.last()
			if key >= max_node.element.key:
				self.holder.add_last(self.Item(key,value))
			else:
				for target_node in self.holder:
					if target_node.element.key > key:
						continue
					else:
						self.holder.add_before(target_node, self.Item(key,value))

	def min(self):
		''' O(1) '''
		return self.holder.first().element.key,self.holder.first().element.value

	def remove_min(self):
		''' O(1) '''
		return self.holder.delete_first()

	def __iter__(self):
		return self.holder.__iter__()

p = PriorityQueueUnsorted()
p.add(3,'a')
p.add(4,'b')
p.add(5,'c')
print [(each.element.key, each.element.value) for each in p]
print p.min()
print [(each.element.key, each.element.value) for each in p]
print p.remove_min()
print [(each.element.key, each.element.value) for each in p]

# --- item class ---
class Item(object):
	# key is the priority, value is the actual value you want to store
	__slots__ = ['key','value']

	def __init__(self,key,value):
		self.key = key
		self.value = value

	def __cmp__(self,other):
		if self.key < other.key:
			return -1
		elif self.key == other.key:
			return 0
		else:
			return 1

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return '( %s, %s )' % (self.key,self.value)

class ArrayBinaryTreeHeap(object):
	def __init__(self):
		self.size = 0
		self.holder = [] # a list

	def _insert_last(self, element):
		self.holder.append(element)
		self.size += 1

	def _adjust_bubble_up(self, position):
		# adjust from the position, by bubbling up
		if position == 0:
			return
		else:
			# parent position x, then child left position 2x+1, child right = 2x+2
			# so child position x, if left, then (x-1)/2 is parent, if right, (x-2)/2 is parent
			parent_location = (position-2)/2 if position % 2 == 0 else (position-1)/2
			if self.holder[parent_location] > self.holder[position]:
				self.holder[parent_location], self.holder[position] = self.holder[position],self.holder[parent_location]
				self._adjust_bubble_up(parent_location)
			else:
				return

	def add(self,key,value):
		item = Item(key,value)
		self._insert_last(item)
		self._adjust_bubble_up(self.size-1)

	def min(self):
		''' peak at the minimun value '''
		return self.holder[0].key, self.holder[0].value

	def _adjust_bubble_down(self, position):
		possible_left_child = position * 2 + 1
		possible_right_child = position * 2 + 2
		if possible_right_child > self.size -1 and possible_left_child > self.size -1 : # no right kid and left kid
			return
		elif possible_right_child > self.size-1: # no right kid, but has left kid
			if self.holder[position] > self.holder[possible_left_child]:
				self.holder[position], self.holder[possible_left_child] = self.holder[possible_left_child], self.holder[position]
				self._adjust_bubble_down(possible_left_child)
			else:
				return
		else: # has left kid and has right kid
			# we change the parent with the most smallest kid
			if self.holder[possible_left_child] < self.holder[possible_right_child]:
				# change the left kid
				if self.holder[position] > self.holder[possible_left_child]:
					self.holder[position], self.holder[possible_left_child] = self.holder[possible_left_child], self.holder[position]
					self._adjust_bubble_down(possible_left_child)
				else:
					return
			else:
				# change the right kid
				if self.holder[position] > self.holder[possible_right_child]:
					self.holder[position], self.holder[possible_right_child] = self.holder[possible_right_child], self.holder[position]
					self._adjust_bubble_down(possible_right_child)
				else:
					return

	def remove_min(self):
		''' remove the min, and exchange the last element to root. then bubble down'''
		result = self.holder[0].key, self.holder[0].value
		self.holder[0] = self.holder[self.size-1] # now the last element goest to the front
		self.holder.pop() # remove the last element
		self.size -= 1 # decrease the size
		self._adjust_bubble_down(0) # start to sort the tree
		return result

	def __iter__(self):
		for each in self.holder:
			yield each

h = ArrayBinaryTreeHeap()
h.add(4,'c')
h.add(5,'a')
h.add(6,'z')
h.add(15,'k')
h.add(9,'f')
h.add(7,'q')
h.add(20,'b')
print [each for each in h]
h.add(16,'x')
h.add(25,'j')
h.add(14,'e')
h.add(12,'h')
h.add(11,'s')
h.add(13,'w')
print [each for each in h]
print 'min', h.min()
print 'remove_min', h.remove_min()
print [each for each in h]
