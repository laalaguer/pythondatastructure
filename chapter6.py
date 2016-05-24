class MyStack(object):
	def __init__(self):
		self._holder = [] # a list

	def pop(self):
		if len(self._holder):
			result = self._holder[-1]
			del self._holder[-1]
			return result
		else:
			return None

	def push(self, node):
		self._holder.append(node)

	def is_empty(self):
		return False if len(self._holder) else True

	def peek(self):
		if len(self._holder):
			return self._holder[-1]
		else:
			return None

	def __len__(self):
		return len(self._holder)

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return str(self._holder)

s = MyStack()
s.push(1)
s.push(2)
print s
s.pop()
s.pop()
print s
s.pop()
print s
s.push(3)
s.push(4)
s.push(1)
print s
print s.peek()
print s

def reverse_by_stack(data):
	s = MyStack()
	[s.push(each) for each in data] # N
	result = [ s.pop() for each in data] # N
	return result

a = [1,2,3,4,5,6]
print a
print reverse_by_stack(a)


# a queue implemented with a python list is inefficient, as when it pops at [0] position
# it will pop out and the try to move the whole list forward by 1, it is a disaster!
# And plus, we call the pop() much often.
# So it leaves to us that a linked list is a good idea. Which is suitable for this one-by-one situation.
# Also a circle of array is another good idea.

class MyQueue(object):
	''' one side in, other side out'''
	def __init__(self, capacity):
		self.capacity = capacity
		self.holder = [None] * capacity
		self.total = 0 # total elements
		self.head = 0 # point to the first element

	def enlarge(self):
		''' double the space of current structure '''
		self.holder.extend([None] * self.capacity)
		# if possible tail elements goes to the front, we copy it back to conjunction
		if self.head + self.total > self.capacity:
			source = self.holder[0:self.head+self.total-self.capacity]
			len_source = len(source)
			i = 0 + self.capacity
			for each in source:
				self.holder[i] = each
				i = i + 1
			# clean the source area
			j = 0
			for j in xrange(len_source):
				self.holder[j] = None

		self.capacity *= 2 # markup the capacity

	def enqueue(self, node):
		# if the list is full, ask for double space
		if self.total == self.capacity:
			self.enlarge()
			print 'enlarge x2'

		# get the item into list, now!
		self.holder[(self.head + self.total) % self.capacity] = node
		self.total += 1

	def dequeue(self):
		if self.total > 0:
			result = self.holder[self.head]
			self.holder[self.head] = None
			self.head += 1
			self.total -= 1
			return result
		else:
			return None

	def peakfront(self):
		if self.total > 0:
			return self.holder[self.head]
		else:
			return None

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return str(self.holder)

	def __len__(self):
		return len(self.holder)

q = MyQueue(5)
print 'q', q, 'actual', len(q)
for x in xrange(8):
	q.enqueue(x)
	print 'q', q, 'actual', len(q)

for x in xrange(2):
	q.dequeue()
	print 'q', q, 'actual', len(q)

for x in xrange(8,13):
	q.enqueue(x)
	print 'q', q, 'actual', len(q)

for x in xrange(13,16):
	q.enqueue(x)
	print 'q', q, 'actual', len(q)	
