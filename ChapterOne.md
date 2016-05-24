# Chapter One

Since I am quite familiar with Python since 2.7, I go with some stuff that I didn`t notice.

##1.
Except `tuple` and `str` type, other basic objects in Python is also immutable.
For example: `int`, `float`, and `bool`

##2. 
The division operation like a/b will get you a float. But sometimes you use a//b to get only the integer part of it.

##3.
[5,7] and [5,6,7] can be compared by element till we find the first element difference

##4.
Exclusive OR is `^`. Bit operation is useful in the `set` concept when you have two sets and wanna compare those or opearte on those:
```
a = set([1,2,3]) # Init by a list
b = set([2,3,4]) # Init by a list
c = a | b        # (1,2,3,4)
d = a ^ b        # (1,4)
e = a & b        # (2,3)

##5.
If you init a set with a dict object, then the only thing left inside dict is the key, like this:
m = {}
m['a'] = 1
m['b'] = 2
set(m) # ('a','b')

I think to get the value set then it is like this
m = {}
m['a'] = 1
m['b'] = 2
set(m.values())

##6.
The `list` is mutable we know that, it can be changed any time. I found out that `+=` is like `.extend()`
and `b = b + [] ` will assign `b` to a new object. This is interesting.
a = [1,2]
b = a
b += [3,4] # a is [1,2,3,4] , b is [1,2,3,4]
b = b + [5,6] # a is [1,2,3,4] , b is [1,2,3,4,5,6]

##7.
`enumerate()` and loop count, and `range(len())` get loop count.
Well, pythonic idom is to do `for idx, item in enumerate(a_list)` to get the idx loop count

##8.
In Python function, the parameter that passed in can be changed in place, if it is mutable.
`def function(a_list):` then the `a_list` maybe changed inside the function body.

##9.
`yield` statement is a stopper, function yield and will stop here and then continue execution.
You can put a yield statement inside a `while` loop to generate fib() sequence