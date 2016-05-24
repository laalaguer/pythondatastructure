class DoublyLinkedList(object):
	# A doubly linked list, has head and tail, and can go from head to tail.
	# and also vic-versa
	class Node(object):
		__slots__ = ['before','after','element']
		def __init__(self, before, after, element):
			self.before = before
			self.after = after
			self.element = element

	def __init__(self):
		self.size = 0
		self.head = self.Node(None,None,None)
		self.tail = self.Node(None,None,None)
		self.head.after = self.tail
		self.tail.before = self.head

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def _insert_between(self, element, node1, node2):
		node = self.Node(None,None,element)
		node.after = node2
		node.before = node1
		node1.after = node
		node2.before = node
		self.size += 1
		return node

	def _delete_node(self, node):
		# I assume you never make the mistake of deleting head/tail node
		node.before.after = node.after
		node.after.before = node.before
		element = node.element
		node.element = node.before = node.after = None
		self.size -= 1
		return element

	def __iter__(self):
		return self.generator()

	def generator(self):
		start = self.head.after
		while start is not self.tail:
			yield start # return all the node
			start = start.after

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return str([ each.element for each in self ]) # will call the __iter__

m_list = DoublyLinkedList()
a = m_list._insert_between('a',m_list.head,m_list.tail)
b = m_list._insert_between('b',a , m_list.tail)
c = m_list._insert_between('c',b , m_list.tail)
print m_list
m_list._delete_node(b)
print m_list


class LinkedDeque(DoublyLinkedList):
	# double ends in, double ends out
	def peak_first(self):
		''' read the first element, if empty then throw error'''
		if self.is_empty():
			raise Exception('queue empty')
		return self.head.after.element

	def peak_last(self):
		''' read the last element, if empty then throw error '''
		if self.is_empty():
			raise Exception('queue empty')
		return self.tail.before.element

	def insert_first(self, element):
		self._insert_between(element,self.head,self.head.after)

	def insert_last(self, element):
		self._insert_between(element,self.tail.before,self.tail)

	def delete_first(self):
		''' read the first element, remove it, return its value'''
		if self.is_empty():
			raise Exception('queue empty')
		return self._delete_node(self.head.after)

	def delete_last(self):
		''' read the last element, remove it, return its value'''
		if self.is_empty():
			raise Exception('queue empty')
		return self._delete_node(self.tail.before)

m_queue = LinkedDeque()
m_queue.insert_first('1')
m_queue.insert_first('2')
print m_queue
m_queue.insert_last('3')
m_queue.insert_last('4')
print m_queue
m_queue.delete_first()
m_queue.delete_last()
print m_queue