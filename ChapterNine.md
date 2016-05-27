# Priority Queue
each node has a k,v value pair. k is the value of priority, value is the actual element.

# Insert and Find
This is similar to the 'find a value' or 'find min' or 'find max' in the basic array.
If you have a unsorted list, then find will take O(n) time
If you have a sorted list, then find min, max only takes O(1) time

However, to use the sorted list, you need O(n) time to insert since you need to compare and insert.
BUT... You can compare and insert by log(n) time, if the list is sorted and is in an array.
BUT... If it is a list, then you have to overcome the drawback that it doesn't have a positional access.
Then you are stuck with the O(n) time.

    	Unsorted List 	Sorted list 	Sorted array 					Sorted, Circular array
add 	O(1)			O(n)			log(n)+O(n) to move others		log(n) + O(n) to move others
rm_min	O(n)			O(1)			O(1) + O(n) to move others		O(1)
min 	O(n)			O(1)			O(1) + O(n) to move others		O(1)
Find 	O(n)			O(n) worst		O(logn)							O(logn)

# Heap based Priority Queue
add O(logn)--> for each insertion, remove O(logn), min O(1)
The Heap is not the heap we are talking about. Its a pyramid-like binary tree.
On the top it is the min() value. We add element by adding it to the last available position,
then bubble it up if it is greater than it's parent/grandparent. If we realize the structure and has a complete/full tree like structure, then log(n) time we are able to insert it. To remvoe the min(), it takes O(1) time. We find the last tree element on the right-down corner and then replace the vacancy left by the root element. Then bubble it till it has the right place.

In terms of space comsuming, the tree is always nearly-full so the space is not wasted too much if you implement by array.
If you implement by Linked node style, then the insert action will need you to remember the last possible insertng position.
As well as your array style implementation, you need to keep track on the last available slot.

So, we need a binary tree that can store Item(k,v) as element as position.

# Heap based min-ordered tree
min() -> O(1)
remove_min() -> O(logn)
insert() -> O(logn)
find(value) -> not possibly efficient. O(n)