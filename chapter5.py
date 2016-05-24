import sys
data = []
for each in xrange(20):
	length = len(data)
	size = sys.getsizeof(data)
	print 'length %d , memory size: %d' %(length, size)
	data.append(None)

# length 0 , memory size: 72
# length 1 , memory size: 104
# length 2 , memory size: 104
# length 3 , memory size: 104
# length 4 , memory size: 104
# length 5 , memory size: 136
# length 6 , memory size: 136
# length 7 , memory size: 136
# length 8 , memory size: 136
# length 9 , memory size: 200
# length 10 , memory size: 200
# length 11 , memory size: 200
# length 12 , memory size: 200
# length 13 , memory size: 200
# length 14 , memory size: 200
# length 15 , memory size: 200
# length 16 , memory size: 200
# length 17 , memory size: 272
# length 18 , memory size: 272
# length 19 , memory size: 272

class GameEntry(object):
	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return '{0} : {1}'.format(self._name, self._score)

class HighBoard(object):
	def __init__(self, capacity):
		self._n = 0
		self._capacity = capacity
		self._holder = []

	def __getitem__(self, index):
		return self.holder[indexs]

	def search_position(self, target):
		start = 0
		stop = self._n - 1
		if self._n == 0:
			return 0
		if target < self._holder[stop].get_score(): # smaller than smallest
			return stop + 1
		if target > self._holder[start].get_score(): # bigger than biggest
			return start
		
		while start <= stop:
			if start + 1 == stop:
				return stop # only between two elements, we push the stop element back

			mid = (start+stop)//2
			if self._holder[mid].get_score() == target:
				return mid
			elif self._holder[mid].get_score() < target:
				stop = mid
			else:
				start = mid
		return stop

	def insert(self, entry):
		''' entry has name and score value '''
		qualify = self._n < self._capacity or self._holder[self._n-1].get_score() < entry.get_score()
		if qualify:
			if self._n < self._capacity:
				pass
			else:
				self._holder.pop()
				self._n -= 1

			position = self.search_position(entry.get_score())
			print 'position', position
			self._holder.insert(position,entry)
			self._n += 1

	def __str__(self):
		result = [str(each) for each in self._holder]
		return '\n'.join(result)

def insert_sort(data):
	''' portion of data is sorted, so insert the new element till it is sorted
		we want an ascending order.
	'''
	start = 1
	stop = len(data) -1
	while start <= stop: # discuss later
		# 1. sort the small list from [0:start]
		current = start
		while data[current] < data[current-1] and current > 1:
			data[current-1], data[current] = data[current], data[current-1] # swap
			current = current-1 # move backward a slot
		# 2. pushing start pivot forward till we meet the stop pivot
		start += 1


a = [1,2,3,4,5,6,1]
insert_sort(a)
print a

# initialize the matirx of 3x3
a = data = [[0] * 3 for j in xrange(3)]
print a
a[0][0] = 1
print a