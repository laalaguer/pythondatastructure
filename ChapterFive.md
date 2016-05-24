# list and its underlying structure
Python list is underlying an array. Which means the it will automaticically enlarge by double the space.
This gives a warning:
1. pythong list is a compact list, which is NOT a linked list.
2. The operation of append() is cheap, when it hits the current internal storage limit, it will double, which is expensive.
3. The operation of remove(element) and pop(index) is expensive. Because it will try to move the list elements together where you punched a hole.
4. Try to set the space in advance, the a = [] then do append() is bad idea.
5. If it is changed to a = [0] * 12 then it is better
6. String append() is also bad because it will create additional n-1 intermediate strings. use ''.join()

# Insert Sort
Work on a sequence list. Keep a tiny fraction of list ordered, go forward and take an item inside, then sort again, like bubble sorting. The outer loop goes O(n) and if worst, the innter loop goes as 1,2,3,...n which is n^2 worse.
Good with a list that is "almost" in order

# Initialize a three-dimensional matrix
data = [[0] * x for j in xrange(y)]