from __future__ import division
# activate n times depth, O(n) time
def factorial1(n):
	if n == 0:
		return 1
	else:
		return factorial1(n-1) * n


print factorial1(3)

# activate log(n) times depth
# this is a recursive call
# and always be a linear recursive call
def binarysearch(data,target,low,high):
	# search for target in data, from low to high
	if low > high:
		return False
	else:
		mid = (low+high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binarysearch(data, target,low,mid -1)
		else:
			return binarysearch(data, target, mid+1, high)

print binarysearch([1,2,3,4,5], 5, 0,4)

# linea recursion
# always recurse on the one side
# Compute x^n, so we have
# 0. non-recursion, x*x*x*x*x, O(n) time. O(1) space
# 1. x * x^(n-1) ..., O(n) depth (space), O(n) time.
# 2. x^(n/2) then multiply it, it feels good.
# log(n) depth, log(n) time
def my_power0(x, n):
	i = 0
	sum = 1
	while i < n: # 0 -> n-1
		sum *= x
		i += 1
	return sum

print my_power0(10,10)

def my_power1(x,n):
	if n == 0:
		return 1
	else:
		return x * my_power1(x, n-1)

print my_power1(10,10)

def my_power2(x,n):
	if n == 0:
		return 1

	k = n // 2
	partial = my_power2(x, k)
	result = partial * partial

	if n % 2 == 1: # odd
		return result * x
	else:
		return result

print my_power2(10,10)


def binary_search_non_recursive(data,target):
	# search target in data
	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low+high) // 2
		if target == data[mid]:
			return True
		elif target > data[mid]:
			# move to high ground
			low = mid + 1
		else:
			# move to low ground
			high = mid - 1
	
	return False

print binary_search_non_recursive([1,2,3,4,5], 5)

def recursive_reverse(data, start, stop):
	# reverse data sequence, return new data
	# depth: O(n/2) time: O(n/2)
	if start == stop:
		return data

	if start > stop:
		return data

	data[start], data[stop] = data[stop], data[start]
	start += 1
	stop -= 1
	return recursive_reverse(data,start,stop)

print recursive_reverse([1,2,3],0,2)

def non_recursive_reverse(data):
	# time n/2
	# space: original space
	start = 0
	stop = len(data) - 1
	while start < stop:
		data[start], data[stop] = data[stop], data[start]
		start += 1
		stop -= 1

	return data

print non_recursive_reverse([1,2,3])


### Excercises
# R-4.1
def find_max(data, start, stop):
	# find max value, return the value
	# depth and time 1, 2, 2*2 = 2^0+2^1 + 2^2 = n!
	if start == stop:
		return data[start]
	if start == stop - 1 :
		return data[start] if data[start] > data[stop] else data[stop]

	half = (start + stop) // 2
	sub_max1 = find_max(data,start,half)
	sub_max2 = find_max(data,half,stop)
	if sub_max1 >= sub_max2:
		return sub_max1
	else:
		return sub_max2

print find_max([10,100,20],0,2)

# R-4.7
import math
def str_to_int(data):
	''' calculate a number to int '''
	_length = len(data) # n elements
	i = 0
	result = 0
	for each in data:
		result += math.pow(10,_length-1-i) * int(each)
		i = i + 1
	return result

print str_to_int('523')

# C-4.9
def find_min_max(data, start, stop):
	# find max value, return the value
	# depth and time 1, 2, 2*2 = 2^0+2^1 + 2^2 = n!
	if start == stop:
		return data[start], data[start]
	if start == stop - 1:
		if data[start] > data[stop]:
			return data[stop], data[start]
		else:
			return data[start], data[stop]

	half = (start + stop) // 2
	sub_min1, sub_max1 = find_min_max(data,start,half)
	sub_min2, sub_max2 = find_min_max(data,half,stop)
	if sub_max1 >= sub_max2:
		if sub_min1 < sub_min2:
			return sub_min1, sub_max1
		else:
			return sub_min2, sub_max1
	else:
		if sub_min1 < sub_min2:
			return sub_min1, sub_max2
		else:
			return sub_min2, sub_max2

print find_min_max([10,100,20,23,1000],0,4)

# C-4.10
def find_base_2_log(n):
	''' log(a+b) = loga+logb 
		log(a) = log(a/2) + 1
	'''
	if n == 1:
		return 0
	return find_base_2_log(n//2) + 1

print find_base_2_log(32)

# C-4.11
def if_unique(data,start,stop):
	''' data is not ordered, find unique element '''
	if start == stop:
		return True

	if data[start] not in data[start+1:]:
		return (True and if_unique(data, start+1,stop))
	else:
		return False

print if_unique([1,2,3],0,2)

# C-4.12
def product_of_two(m,n):
	if n == 1:
		return m
	else:
		return m + product_of_two(m, n-1)

print product_of_two(3,2)

# C-4.14
def hanoi_problem(n, source, helper, target):
	''' move from source to target
	'''
	print 'n', n
	print 'source', source
	print 'helper', helper
	print 'target', target
	print '---'
	if n > 0:
		# step 1, move all n-1 to helper
		# step 2, move last n on source to target
		# steap 3, move all n-1 on helper to target
		hanoi_problem(n-1, source, target, helper)
		target.append(source.pop())
		hanoi_problem(n-1, helper, source, target)

hanoi_problem(3, [3,2,1],[],[])

# C-4.15
def subsets(data):
	if len(data) > 0:
		head = data[0]
		for each in subsets(data[1:]):
			yield [head] + each
			yield each
	else:
		yield []

for each in subsets([1,2,3]):
	print each

# C-4.16
def reverse_recursive(data, start, stop):
	if start > stop:
		return

	if start < stop:
		data[start] , data[stop] = data[stop], data[start]
		reverse_recursive(data, start+1, stop-1)
		return

a = [1,2,3,4,5,6]
reverse_recursive(a, 0, len(a)-1)
print a

# C-4.17
def if_palindrome(data, start, stop):
	if start > stop:
		return True

	if start < stop:
		return False if data[start] != data[stop] else True
		return if_palindrome(data, start+1,stop-1)

a = "carrac"
print if_palindrome(a,0,len(a)-1)

# c-4.19
def odd_first(data, start, stop):
	if start > stop:
		return
	else:
		head = data[start]
		if head % 2 == 0:
			data.remove(head)
			data.append(head)
			odd_first(data, start, stop-1)
		else:
			odd_first(data, start+1, stop)

a = [1,1,3,2,2,5,4,3,8]
odd_first(a,0,len(a)-1)
print a

# c-4.20
# O(n) - each time we eliminate one element, so O(n)
def before_k(data, start, stop, k):
	if start > stop:
		return
	else:
		head = data[start]
		if head > k:
			data.remove(head)
			data.append(head)
			before_k(data, start, stop-1, k)
		else:
			before_k(data, start+1, stop, k)

a = [8,7,6,5,4,3,5,5,5,8,1,2]
before_k(a,0,len(a)-1, 5)
print a

# c-4.21
def find_k_sum(data, start, stop, k):
	''' find if elements in data can sum up to k, data is ordered small to big '''
	if start >= stop:
		return False

	if data[stop] > k:
		find_k_sum(data, start, stop-1,k)

	if data[start] + data[stop] == k:
		return True
	elif data[start] + data[stop] < k:
		return find_k_sum(data, start+1, stop,k)
	else: # sum > k, maybe sum is lonly slightly bigger than the k
		return find_k_sum(data, start, stop-1,k)

a = [2,4,5,5,5,5,8]
print find_k_sum(a,0,len(a)-1,6)

# c-4.22
# non-repeat power by squaring
def power_me(x, n):
	if n == 0:
		return 1
	if n == 1:
		return x

	k = n // 2
	partial = power_me(x,k)
	if n % 2 == 1: # if n is odd
		return x * partial * partial
	else:
		return partial * partial

print power_me(2,5)

# define a non-recursive way
# the increment way
def power_me_non_rec(x,n):
	product = x
	k = 1
	while k*2 <= n:
		print 'k', k
		product *= product
		k = k * 2

	if k == n:
		return product
	else:
		return product * x

print power_me_non_rec(3,4)



def my_memory(func):
	already = {}
	def wrapped_func(number):
		if number in already:
			return already[number]
		else:
			result = func(number)
			already[number] = result
			return result

	return wrapped_func

# big O n changed to maybe O(1)
@my_memory
def check_prime(x):
	for idx in xrange(2,x//2):
		if x // idx == x / idx:
			return False
	return True

print check_prime(10)
print check_prime(3)
print check_prime(21)
print check_prime(47)
print check_prime(51)
print check_prime(100)