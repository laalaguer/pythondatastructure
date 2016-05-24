from __future__ import division

def prefix_average1(data):
	''' calculate the average of sequence
		also return the calculated sequence
	'''
	_length = len(data)
	a = [0] * _length
	for i in xrange(_length):
		a[i] = sum(data[:i+1]) / (i+1) # this is like O(N^2)

	return a

def prefix_average2(data):
	''' Now we want to get rid of over-and-over
	calculation of sum() by cache the result
	'''
	# we store a sum cache
	_length = len(data)
	a = [0] * _length
	total = 0 # store the calculated sum
	for i in xrange(_length): # O(n) calculation
		total += data[i]
		a[i] = total / (i+1)

	return a

# Three-way Disjointness
# This N^3
def disjoint1(a,b,c): # three sequence
	for each in a:
		for every in b:
			for item in c:
				if each == every and each == item:
					return False
	return True

# Worst case, a == b sequence,
# c loop called N times, each c loop is N times
# So it is O(N^2)
def disjoint2(a,b,c):
	for each in a:
		for every in b:
			if each == every:
				for item in c:
					if each == item:
						return False
	return True

# check if a list has duplicat elements
# N^2
def distinct1(a):
	_length = len(a)
	for i in xrange(_length):
		for j in xrange(i+1,_length):
			if a[i] == a[j]:
				return False

	return True
	
# Improve by sorting. Sorting is a tool.
# sorting is O(nlogn)
# the rest is O(n)
# so it is O(nlogn)
def distinct2(a):
	new_a = sorted(a) # small to big.
	for i in xrange(len(new_a)-1):
		if new_a[i] == new_a[i+1]:
			return False
	return True